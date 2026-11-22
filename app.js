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

  toolsGrid.innerHTML = filtered.map(tool => `
    <a href="#${tool.id}" class="tool-card" onclick="openTool('${tool.id}'); return false;">
      <div>
        <div class="tool-card-top">
          <div class="tool-icon-wrapper">
            <i class="${tool.icon}"></i>
          </div>
          <div>
            ${tool.badge ? `<span class="tool-category-tag tool-badge-hot">${tool.badge}</span>` : `<span class="tool-category-tag">${tool.category}</span>`}
          </div>
        </div>
        <h3 class="tool-card-title">${tool.title}</h3>
        <p class="tool-card-description">${tool.shortDesc}</p>
      </div>
      <div class="tool-card-footer">
        <span>Use Tool Free</span>
        <i class="fa-solid fa-arrow-right"></i>
      </div>
    </a>
  `).join('');
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

// Initialize on Load
window.addEventListener('DOMContentLoaded', () => {
  initTheme();
  renderCatalog();
  handleHashRoute();
});

window.addEventListener('hashchange', handleHashRoute);
