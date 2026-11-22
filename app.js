/**
 * OmniTools - Core Application Controller
 * Handles live search, category filtering, hash routing, theme toggling, and SEO synchronization.
 */

// State variables
let currentCategory = 'all';
let currentSearchQuery = '';

// DOM Elements
const toolsGrid = document.getElementById('toolsGrid');
const noResultsState = document.getElementById('noResultsState');
const globalSearchInput = document.getElementById('globalSearchInput');
const clearSearchBtn = document.getElementById('clearSearchBtn');
const categoryPills = document.querySelectorAll('.pill');
const themeToggleBtn = document.getElementById('themeToggleBtn');
const toolsCountBadge = document.getElementById('toolsCountBadge');

// Active Tool View Elements
const activeToolContainer = document.getElementById('activeToolContainer');
const toolsCatalogSection = document.getElementById('toolsCatalogSection');
const activeToolTitle = document.getElementById('activeToolTitle');
const activeToolDesc = document.getElementById('activeToolDesc');
const activeToolIcon = document.getElementById('activeToolIcon');
const activeToolBody = document.getElementById('activeToolBody');
const activeToolSeoBlock = document.getElementById('activeToolSeoBlock');
const breadcrumbCategory = document.getElementById('breadcrumbCategory');
const breadcrumbToolName = document.getElementById('breadcrumbToolName');

// Theme Controller
function initTheme() {
  const savedTheme = localStorage.getItem('omnitools_theme') || 'theme-dark';
  document.body.className = savedTheme;
  updateThemeIcon(savedTheme);
}

function updateThemeIcon(theme) {
  const icon = themeToggleBtn.querySelector('i');
  if (theme === 'theme-light') {
    icon.className = 'fa-solid fa-sun';
  } else {
    icon.className = 'fa-solid fa-moon';
  }
}

themeToggleBtn.addEventListener('click', () => {
  const isDark = document.body.classList.contains('theme-dark');
  const newTheme = isDark ? 'theme-light' : 'theme-dark';
  document.body.className = newTheme;
  localStorage.setItem('omnitools_theme', newTheme);
  updateThemeIcon(newTheme);
});

const TOOL_PAGE_MAP = {
  'passport-photo': 'passport-size-photo-maker-20kb/',
  'image-compressor': 'image-compressor-to-exact-kb/',
  'image-resizer': 'image-resizer-in-cm-and-pixels/',
  'image-converter': 'image-format-converter-jpg-png-webp/',
  'gst-calculator': 'gst-calculator-india/',
  'emi-calculator': 'loan-emi-calculator/',
  'age-calculator': 'age-calculator-online/',
  'krutidev-converter': 'kruti-dev-to-unicode-converter/',
  'fancy-fonts': 'fancy-stylish-font-generator/',
  'word-counter': 'word-counter-online/',
  'case-converter': 'case-converter-uppercase-to-lowercase/',
  'pdf-merger': 'pdf-merger-online/',
  'image-to-pdf': 'image-to-pdf-converter-online/',
  'qr-generator': 'qr-code-generator-with-logo/',
  'password-generator': 'strong-password-generator-online/',
  'json-formatter': 'json-formatter-and-validator/',
  'typing-speed-test': 'typing-speed-test-online/',
  'sip-calculator': 'sip-calculator-mutual-funds/',
  'signature-resizer': 'online-signature-resizer-10kb-20kb/',
  'hashtag-generator': 'instagram-viral-hashtag-generator/',
  'text-to-speech': 'free-text-to-speech-audio-reader/',
  'bmi-calculator': 'bmi-calculator-healthy-weight/',
  'name-date-on-photo': 'add-name-and-date-on-photo-ssc/',
  'photo-signature-joiner': 'photo-and-signature-joiner-online/',
  'thumb-impression-resizer': 'thumb-impression-resizer-10kb-20kb/',
  'cgpa-to-percentage': 'cgpa-to-percentage-calculator-cbse/',
  'salary-calculator': 'in-hand-salary-calculator-india/',
  'speech-to-text': 'speech-to-text-online-voice-typing/',
  'invoice-generator': 'free-invoice-and-receipt-generator/',
  'stopwatch-timer': 'online-stopwatch-and-countdown-timer/',
  'photo-sheet-4x6': 'photo-sheet-4x6/',
  'blur-face-hide': 'blur-face-hide-details/',
  'photo-bg-color': 'photo-background-color-changer/',
  'watermark-tool': 'add-watermark-to-photo-online/',
  'id-card-print-layout': 'aadhaar-pan-card-a4-print-layout/',
  'photo-cropper': 'photo-cropper-and-aspect-ratio/',
  'pdf-splitter': 'split-pdf-extract-pages-online/',
  'pdf-page-manager': 'rotate-and-delete-pdf-pages/',
  'attendance-calculator': 'attendance-calculator-75-rule/',
  'percentage-calculator': 'percentage-calculator-online/',
  'upi-qr-maker': 'upi-qr-code-generator-with-amount/',
  'wifi-qr-maker': 'wifi-qr-code-generator/',
  'fuel-mileage-calc': 'fuel-mileage-and-cost-calculator/',
  'date-difference-calc': 'date-difference-calculator/',
  'scientific-calculator': 'scientific-calculator-online/',
  'what-is-my-ip': 'what-is-my-ip-address/',
  'coin-toss-dice': 'coin-toss-and-dice-roller/',
  'profit-loss-calculator': 'profit-and-loss-calculator/',
  'discount-calculator': 'discount-calculator-online/',
  'interest-calculator': 'simple-and-compound-interest-calculator/',
  'electricity-bill-calc': 'electricity-bill-calculator/',
  'unit-converter': 'all-in-one-unit-converter/',
  'whatsapp-qr-maker': 'whatsapp-chat-qr-code-generator/',
  'reverse-text': 'reverse-text-online/',
  'username-generator': 'aesthetic-gamer-username-generator/',
  'random-number-generator': 'random-number-generator-online/',
  'days-until-date': 'days-until-date-countdown/',
  'code-beautifier-minifier': 'code-minifier-and-beautifier/',
  'age-eligibility-calculator': 'sarkari-exam-age-eligibility-calculator/',
  'marks-calculator': 'student-marks-percentage-calculator/',
  'voice-recorder': 'online-voice-recorder/',
  'media-speed-changer': 'media-playback-speed-changer/',
  'internet-speed-test': 'internet-speed-test-online/',
  'resume-biodata-maker': 'simple-resume-and-biodata-maker/',
  'photo-collage-maker': 'photo-collage-maker-online/'
};

// Render Tools in Catalog Grid
function renderCatalog() {
  const query = currentSearchQuery.toLowerCase().trim();

  const filtered = TOOLS.filter(tool => {
    const matchCategory = currentCategory === 'all' || tool.category === currentCategory;
    const matchSearch = !query || 
      tool.title.toLowerCase().includes(query) || 
      tool.shortDesc.toLowerCase().includes(query) ||
      tool.keywords.some(k => k.toLowerCase().includes(query));
    return matchCategory && matchSearch;
  });

  toolsCountBadge.innerText = `${filtered.length} tools`;

  if (filtered.length === 0) {
    toolsGrid.innerHTML = '';
    noResultsState.style.display = 'block';
    return;
  }

  noResultsState.style.display = 'none';

  toolsGrid.innerHTML = filtered.map(tool => {
    const directUrl = TOOL_PAGE_MAP[tool.id] || `#${tool.id}`;
    const catClass = 'tag-' + (tool.category || 'developer');
    return `
      <a href="${directUrl}" class="tool-card">
        <div>
          <div class="tool-card-top">
            <div class="tool-icon-wrapper ${catClass}">
              <i class="${tool.icon}"></i>
            </div>
            <div style="display:flex; gap:0.4rem;">
              <span class="tool-category-tag ${catClass}">${tool.category}</span>
              ${tool.badge ? `<span class="tool-category-tag tool-badge-hot">${tool.badge}</span>` : ''}
            </div>
          </div>
          <h3 class="tool-card-title">${tool.title}</h3>
          <p class="tool-card-description">${tool.shortDesc}</p>
        </div>
        <div class="tool-card-footer">
          <span class="tool-action-btn-pill">Use Tool Free <i class="fa-solid fa-arrow-right"></i></span>
        </div>
      </a>
    `;
  }).join('');
}

// Open Active Tool
function openTool(toolId) {
  const tool = getToolById(toolId);
  if (!tool) return;

  window.location.hash = tool.id;

  activeToolTitle.innerText = tool.title;
  activeToolDesc.innerText = tool.shortDesc;
  activeToolIcon.innerHTML = `<i class="${tool.icon}"></i>`;
  breadcrumbCategory.innerText = tool.category.toUpperCase();
  breadcrumbToolName.innerText = tool.title;

  // Render Tool Form & Logic
  activeToolBody.innerHTML = '';
  tool.render(activeToolBody);

  // Render SEO Block
  if (tool.seoArticle) {
    activeToolSeoBlock.style.display = 'block';
    activeToolSeoBlock.innerHTML = tool.seoArticle;
  } else {
    activeToolSeoBlock.style.display = 'none';
  }

  // Update Page Title and Meta for Instant SEO
  document.title = `${tool.seoTitle || tool.title} | OmniTools`;

  // Hide catalog, show workspace
  toolsCatalogSection.style.display = 'none';
  activeToolContainer.style.display = 'block';

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Close Active Tool & Return to Catalog
function closeActiveTool() {
  window.location.hash = '';
  activeToolContainer.style.display = 'none';
  toolsCatalogSection.style.display = 'block';
  document.title = 'OmniTools - 25+ Free Online Tools for Image, PDF, Text & Daily Utilities';
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Handle Routing via Hash change
function handleHashRoute() {
  const hash = window.location.hash.replace('#', '').trim();
  if (hash) {
    const tool = getToolById(hash);
    if (tool) {
      openTool(tool.id);
      return;
    }
  }
  closeActiveTool();
}

// Search box interactions
globalSearchInput.addEventListener('input', (e) => {
  currentSearchQuery = e.target.value;
  clearSearchBtn.style.display = currentSearchQuery ? 'block' : 'none';
  renderCatalog();
});

clearSearchBtn.addEventListener('click', () => {
  globalSearchInput.value = '';
  currentSearchQuery = '';
  clearSearchBtn.style.display = 'none';
  renderCatalog();
});

// Category pills interaction
categoryPills.forEach(pill => {
  pill.addEventListener('click', () => {
    categoryPills.forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    currentCategory = pill.dataset.category;
    renderCatalog();
  });
});

function resetFilters() {
  currentCategory = 'all';
  currentSearchQuery = '';
  globalSearchInput.value = '';
  clearSearchBtn.style.display = 'none';
  categoryPills.forEach(p => p.classList.remove('active'));
  document.querySelector('.pill[data-category="all"]').classList.add('active');
  renderCatalog();
}

// FAQ Accordion
function toggleFaq(el) {
  const item = el.parentElement;
  item.classList.toggle('active');
}

// Immediate Execution
function initApp() {
  initTheme();
  renderCatalog();
  handleHashRoute();
}

initApp();
if (document.readyState === 'loading') {
  window.addEventListener('DOMContentLoaded', initApp);
}
window.addEventListener('hashchange', handleHashRoute);
