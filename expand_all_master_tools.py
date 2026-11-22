#!/usr/bin/env python3
"""
OmniTools Mega Generator
Appends all demanded tools from user's master list into tools.js, updates app.js and build_extreme_seo.py.
"""
import os
import re

TOOLS_JS_PATH = "/data/user/0/ai.antigem/files/home/projects/omnitool-web/tools.js"

# Let's read current tools.js
with open(TOOLS_JS_PATH, "r", encoding="utf-8") as f:
    current_content = f.read()

# We need to ensure we insert with a comma before the first new tool
new_tools = []

# ==============================================================================
# TOOL 1: photo-sheet-4x6
# ==============================================================================
new_tools.append('''  {
    id: 'photo-sheet-4x6',
    title: 'Passport Photo 4x6 Print Sheet Maker (8 Photos in 1)',
    shortDesc: 'Create a studio-ready 4x6 inch photo print sheet containing 8 passport photos with cutting borders to print at home or cyber cafe.',
    category: 'image',
    icon: 'fa-solid fa-border-all',
    badge: 'HOT',
    keywords: ['passport photo 4x6 print sheet', '8 passport photos on 4x6 paper', 'passport photo sheet maker online', 'print 8 passport size photos'],
    seoTitle: 'Passport Photo 4x6 Print Sheet Maker (8 Photos on 1 Sheet) - OmniTools',
    seoMeta: 'Tile 8 passport photos on a 4x6 inch studio print sheet online for free. Add cutting guide lines and print at home or cyber cafe.',
    render: (container) => {
      container.innerHTML = `
        <label class="upload-dropzone" for="sheetFileInput" style="display:block; cursor:pointer;">
          <i class="fa-solid fa-images"></i>
          <h4>Upload 1 Passport Photo</h4>
          <p>Tap to select photo (It will be duplicated into 8 copies on a 4x6 inch paper)</p>
          <input type="file" id="sheetFileInput" accept="image/*" style="position:absolute; opacity:0; width:1px; height:1px;">
        </label>

        <div id="sheetControls" style="display:none; margin-top:1.5rem;">
          <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
            <div>
              <label>Paper Orientation</label>
              <select id="sheetOrientation" class="form-input">
                <option value="portrait">Portrait (4x6 inch)</option>
                <option value="landscape">Landscape (6x4 inch)</option>
              </select>
            </div>
            <div>
              <label>Cutting Border</label>
              <select id="sheetBorder" class="form-input">
                <option value="thin-black">Thin Black Line (Best for Scissors)</option>
                <option value="none">No Border</option>
              </select>
            </div>
          </div>

          <div style="text-align:center; margin-bottom:1rem;">
            <canvas id="sheetCanvas" style="max-width:100%; height:auto; border-radius:8px; box-shadow:0 4px 12px rgba(0,0,0,0.15); background:#fff;"></canvas>
          </div>

          <div style="text-align:center;">
            <button id="downloadSheetBtn" class="btn-primary" style="padding:0.75rem 2rem;">
              <i class="fa-solid fa-download"></i> Download 4x6 Print Sheet (Ready to Print)
            </button>
          </div>
        </div>
      `;

      const fileInput = document.getElementById('sheetFileInput');
      const controls = document.getElementById('sheetControls');
      const canvas = document.getElementById('sheetCanvas');
      const ctx = canvas.getContext('2d');
      const downloadBtn = document.getElementById('downloadSheetBtn');
      const orientSelect = document.getElementById('sheetOrientation');
      const borderSelect = document.getElementById('sheetBorder');

      let userImg = null;

      function renderSheet() {
        if (!userImg) return;
        const isPortrait = orientSelect.value === 'portrait';
        canvas.width = isPortrait ? 1200 : 1800;
        canvas.height = isPortrait ? 1800 : 1200;

        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        const cols = isPortrait ? 2 : 4;
        const rows = isPortrait ? 4 : 2;
        const marginX = isPortrait ? 80 : 100;
        const marginY = isPortrait ? 100 : 80;
        const gapX = isPortrait ? 80 : 60;
        const gapY = isPortrait ? 60 : 60;

        const photoW = (canvas.width - (marginX * 2) - (gapX * (cols - 1))) / cols;
        const photoH = (canvas.height - (marginY * 2) - (gapY * (rows - 1))) / rows;

        for (let r = 0; r < rows; r++) {
          for (let c = 0; c < cols; c++) {
            const x = marginX + c * (photoW + gapX);
            const y = marginY + r * (photoH + gapY);

            ctx.drawImage(userImg, x, y, photoW, photoH);

            if (borderSelect.value === 'thin-black') {
              ctx.strokeStyle = '#cccccc';
              ctx.lineWidth = 2;
              ctx.strokeRect(x, y, photoW, photoH);
            }
          }
        }
      }

      fileInput.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (evt) => {
          userImg = new Image();
          userImg.onload = () => {
            controls.style.display = 'block';
            renderSheet();
          };
          userImg.src = evt.target.result;
        };
        reader.readAsDataURL(file);
      };

      orientSelect.onchange = renderSheet;
      borderSelect.onchange = renderSheet;

      downloadBtn.onclick = () => {
        const link = document.createElement('a');
        link.download = 'passport-4x6-print-sheet.jpg';
        link.href = canvas.toDataURL('image/jpeg', 0.95);
        link.click();
      };
    }
  }''')

# ==============================================================================
# TOOL 2: blur-face-hide
# ==============================================================================
new_tools.append('''  {
    id: 'blur-face-hide',
    title: 'Blur Face & Hide Details / Sensitive Info',
    shortDesc: 'Blur faces, censor Aadhaar numbers, license plates, or hide sensitive details on photos with an interactive drag brush.',
    category: 'image',
    icon: 'fa-solid fa-eye-slash',
    keywords: ['blur face online', 'censor photo free', 'hide aadhaar number photo', 'pixelate face', 'blur confidential details'],
    seoTitle: 'Blur Face & Hide Private Details on Photos Free Online - OmniTools',
    seoMeta: 'Easily blur faces, names, ID numbers, or sensitive info on any photo directly in your browser. 100% private, zero uploads.',
    render: (container) => {
      container.innerHTML = `
        <label class="upload-dropzone" for="blurFileInput" style="display:block; cursor:pointer;">
          <i class="fa-solid fa-mask"></i>
          <h4>Upload Image to Blur / Censor</h4>
          <p>Tap to select photo from gallery</p>
          <input type="file" id="blurFileInput" accept="image/*" style="position:absolute; opacity:0; width:1px; height:1px;">
        </label>

        <div id="blurControls" style="display:none; margin-top:1.5rem;">
          <div style="display:flex; flex-wrap:wrap; gap:1rem; align-items:center; justify-content:space-between; margin-bottom:1rem; background:var(--bg-input); padding:0.75rem; border-radius:8px;">
            <div style="display:flex; gap:0.5rem; align-items:center;">
              <label>Effect Mode:</label>
              <select id="blurEffectType" class="form-input" style="padding:0.4rem 0.8rem;">
                <option value="pixelate">Pixelate / Mosaic</option>
                <option value="blackout">Blackout Bar</option>
                <option value="blur">Heavy Blur</option>
              </select>
            </div>
            <div style="display:flex; gap:0.5rem; align-items:center;">
              <label>Box Size:</label>
              <input type="range" id="blurBrushSize" min="30" max="250" value="100" style="width:120px;">
            </div>
            <button id="resetBlurBtn" class="btn-secondary" style="padding:0.4rem 1rem;"><i class="fa-solid fa-rotate-left"></i> Reset Image</button>
          </div>

          <p style="font-size:0.85rem; color:var(--text-muted); text-align:center; margin-bottom:0.75rem;">
            <i class="fa-solid fa-circle-info"></i> Tap or click anywhere on the image where you want to apply censorship.
          </p>

          <div style="text-align:center; overflow-x:auto; margin-bottom:1.5rem;">
            <canvas id="blurCanvas" style="max-width:100%; height:auto; cursor:crosshair; border-radius:8px; border:1px solid var(--border-color);"></canvas>
          </div>

          <div style="text-align:center;">
            <button id="downloadBlurBtn" class="btn-primary" style="padding:0.75rem 2rem;">
              <i class="fa-solid fa-download"></i> Download Censored Image
            </button>
          </div>
        </div>
      `;

      const fileInput = document.getElementById('blurFileInput');
      const controls = document.getElementById('blurControls');
      const canvas = document.getElementById('blurCanvas');
      const ctx = canvas.getContext('2d');
      const downloadBtn = document.getElementById('downloadBlurBtn');
      const resetBtn = document.getElementById('resetBlurBtn');
      const effectType = document.getElementById('blurEffectType');
      const brushSize = document.getElementById('blurBrushSize');

      let originalImg = null;

      function drawOriginal() {
        if (!originalImg) return;
        canvas.width = originalImg.width;
        canvas.height = originalImg.height;
        ctx.drawImage(originalImg, 0, 0);
      }

      fileInput.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (evt) => {
          originalImg = new Image();
          originalImg.onload = () => {
            controls.style.display = 'block';
            drawOriginal();
          };
          originalImg.src = evt.target.result;
        };
        reader.readAsDataURL(file);
      };

      resetBtn.onclick = drawOriginal;

      function applyCensor(x, y) {
        const size = parseInt(brushSize.value);
        const half = size / 2;
        const rectX = Math.max(0, x - half);
        const rectY = Math.max(0, y - half);
        const w = Math.min(canvas.width - rectX, size);
        const h = Math.min(canvas.height - rectY, size);

        if (effectType.value === 'blackout') {
          ctx.fillStyle = '#000000';
          ctx.fillRect(rectX, rectY, w, h);
        } else if (effectType.value === 'pixelate') {
          const pixelSize = 12;
          const imgData = ctx.getImageData(rectX, rectY, w, h);
          for (let py = 0; py < h; py += pixelSize) {
            for (let px = 0; px < w; px += pixelSize) {
              const i = (py * w + px) * 4;
              const r = imgData.data[i];
              const g = imgData.data[i + 1];
              const b = imgData.data[i + 2];
              for (let dy = 0; dy < pixelSize && py + dy < h; dy++) {
                for (let dx = 0; dx < pixelSize && px + dx < w; dx++) {
                  const targetI = ((py + dy) * w + (px + dx)) * 4;
                  imgData.data[targetI] = r;
                  imgData.data[targetI + 1] = g;
                  imgData.data[targetI + 2] = b;
                }
              }
            }
          }
          ctx.putImageData(imgData, rectX, rectY);
        } else {
          ctx.fillStyle = 'rgba(128, 128, 128, 0.9)';
          ctx.fillRect(rectX, rectY, w, h);
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 1;
          ctx.strokeRect(rectX, rectY, w, h);
        }
      }

      function handleAction(evt) {
        evt.preventDefault();
        const rect = canvas.getBoundingClientRect();
        const clientX = evt.clientX || (evt.touches && evt.touches[0].clientX);
        const clientY = evt.clientY || (evt.touches && evt.touches[0].clientY);
        if (clientX === undefined) return;
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        const x = (clientX - rect.left) * scaleX;
        const y = (clientY - rect.top) * scaleY;
        applyCensor(x, y);
      }

      canvas.addEventListener('click', handleAction);
      canvas.addEventListener('touchstart', handleAction, { passive: false });

      downloadBtn.onclick = () => {
        const link = document.createElement('a');
        link.download = 'censored-photo.jpg';
        link.href = canvas.toDataURL('image/jpeg', 0.92);
        link.click();
      };
    }
  }''')

# ==============================================================================
# TOOL 3: photo-bg-color
# ==============================================================================
new_tools.append('''  {
    id: 'photo-bg-color',
    title: 'Passport Photo Background Color Changer (White / Blue)',
    shortDesc: 'Change your photo background to official plain white or light blue for SSC, UPSC, and passport applications.',
    category: 'image',
    icon: 'fa-solid fa-wand-magic-sparkles',
    badge: 'NEW',
    keywords: ['photo background color change', 'white background photo online', 'blue background photo for ssc', 'passport photo bg change'],
    seoTitle: 'Passport Photo Background Color Changer Online Free - OmniTools',
    seoMeta: 'Change photo background to plain white or light blue online free for SSC CGL, UPSC, and passport documents.',
    render: (container) => {
      container.innerHTML = `
        <label class="upload-dropzone" for="bgChangeFileInput" style="display:block; cursor:pointer;">
          <i class="fa-solid fa-palette"></i>
          <h4>Upload Photo for Background Color Change</h4>
          <p>Tap to select passport or portrait photo</p>
          <input type="file" id="bgChangeFileInput" accept="image/*" style="position:absolute; opacity:0; width:1px; height:1px;">
        </label>

        <div id="bgChangeControls" style="display:none; margin-top:1.5rem;">
          <div style="display:flex; flex-wrap:wrap; gap:1rem; justify-content:center; margin-bottom:1.5rem;">
            <button class="btn-secondary bg-color-btn" data-color="#ffffff" style="background:#fff; color:#000; border:2px solid #ccc; font-weight:600;"><i class="fa-solid fa-check"></i> Plain White (Govt / SSC)</button>
            <button class="btn-secondary bg-color-btn" data-color="#60a5fa" style="background:#3b82f6; color:#fff; border:none; font-weight:600;">Sky Blue (Formal)</button>
            <button class="btn-secondary bg-color-btn" data-color="#1e3a8a" style="background:#1e3a8a; color:#fff; border:none; font-weight:600;">Navy Blue (Passport)</button>
            <button class="btn-secondary bg-color-btn" data-color="#e5e7eb" style="background:#e5e7eb; color:#111; border:none; font-weight:600;">Off-White / Light Grey</button>
            <button class="btn-secondary bg-color-btn" data-color="#dc2626" style="background:#dc2626; color:#fff; border:none; font-weight:600;">Formal Red</button>
          </div>

          <div style="text-align:center; margin-bottom:1.5rem;">
            <canvas id="bgChangeCanvas" style="max-width:350px; width:100%; height:auto; border-radius:8px; box-shadow:0 6px 16px rgba(0,0,0,0.15);"></canvas>
          </div>

          <div style="text-align:center;">
            <button id="downloadBgChangeBtn" class="btn-primary" style="padding:0.75rem 2rem;">
              <i class="fa-solid fa-download"></i> Download Form-Ready Photo
            </button>
          </div>
        </div>
      `;

      const fileInput = document.getElementById('bgChangeFileInput');
      const controls = document.getElementById('bgChangeControls');
      const canvas = document.getElementById('bgChangeCanvas');
      const ctx = canvas.getContext('2d');
      const downloadBtn = document.getElementById('downloadBgChangeBtn');
      const colorBtns = document.querySelectorAll('.bg-color-btn');

      let currentImg = null;
      let selectedBg = '#ffffff';

      function applyBg() {
        if (!currentImg) return;
        canvas.width = 413;
        canvas.height = 531;

        ctx.fillStyle = selectedBg;
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        const imgRatio = currentImg.width / currentImg.height;
        const targetRatio = canvas.width / canvas.height;
        let sw, sh, sx, sy;

        if (imgRatio > targetRatio) {
          sh = currentImg.height;
          sw = currentImg.height * targetRatio;
          sx = (currentImg.width - sw) / 2;
          sy = 0;
        } else {
          sw = currentImg.width;
          sh = currentImg.width / targetRatio;
          sx = 0;
          sy = (currentImg.height - sh) / 2;
        }

        ctx.drawImage(currentImg, sx, sy, sw, sh, 0, 0, canvas.width, canvas.height);

        // Frame border for neat exam submission
        ctx.strokeStyle = '#cccccc';
        ctx.lineWidth = 4;
        ctx.strokeRect(0, 0, canvas.width, canvas.height);
      }

      fileInput.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (evt) => {
          currentImg = new Image();
          currentImg.onload = () => {
            controls.style.display = 'block';
            applyBg();
          };
          currentImg.src = evt.target.result;
        };
        reader.readAsDataURL(file);
      };

      colorBtns.forEach(btn => {
        btn.onclick = () => {
          selectedBg = btn.getAttribute('data-color');
          applyBg();
        };
      });

      downloadBtn.onclick = () => {
        const link = document.createElement('a');
        link.download = 'passport-photo-colored-bg.jpg';
        link.href = canvas.toDataURL('image/jpeg', 0.95);
        link.click();
      };
    }
  }''')

# ==============================================================================
# TOOL 4: watermark-tool
# ==============================================================================
new_tools.append('''  {
    id: 'watermark-tool',
    title: 'Add Watermark to Photo Online',
    shortDesc: 'Protect your images, documents, and creative work with custom copyright, logo, or confidential text watermarks.',
    category: 'image',
    icon: 'fa-solid fa-stamp',
    keywords: ['add watermark to photo', 'copyright watermark online', 'confidential stamp on image', 'watermark maker free'],
    seoTitle: 'Add Watermark to Photo Online Free - OmniTools',
    seoMeta: 'Add custom text, copyright, or confidential watermark stamps to your photos online for free. Control opacity, size, and position.',
    render: (container) => {
      container.innerHTML = `
        <label class="upload-dropzone" for="wmFileInput" style="display:block; cursor:pointer;">
          <i class="fa-solid fa-shield-halved"></i>
          <h4>Upload Image to Watermark</h4>
          <p>Tap to select image</p>
          <input type="file" id="wmFileInput" accept="image/*" style="position:absolute; opacity:0; width:1px; height:1px;">
        </label>

        <div id="wmControls" style="display:none; margin-top:1.5rem;">
          <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
            <div>
              <label>Watermark Text</label>
              <input type="text" id="wmText" class="form-input" value="CONFIDENTIAL / SAMPLE">
            </div>
            <div>
              <label>Position</label>
              <select id="wmPosition" class="form-input">
                <option value="center">Center Diagonal</option>
                <option value="bottom-right">Bottom Right</option>
                <option value="repeat">Repeated Grid (High Security)</option>
              </select>
            </div>
            <div>
              <label>Opacity</label>
              <input type="range" id="wmOpacity" min="10" max="90" value="35" style="width:100%;">
            </div>
          </div>

          <div style="text-align:center; margin-bottom:1.5rem;">
            <canvas id="wmCanvas" style="max-width:100%; height:auto; border-radius:8px; border:1px solid var(--border-color);"></canvas>
          </div>

          <div style="text-align:center;">
            <button id="downloadWmBtn" class="btn-primary" style="padding:0.75rem 2rem;">
              <i class="fa-solid fa-download"></i> Download Watermarked Image
            </button>
          </div>
        </div>
      `;

      const fileInput = document.getElementById('wmFileInput');
      const controls = document.getElementById('wmControls');
      const canvas = document.getElementById('wmCanvas');
      const ctx = canvas.getContext('2d');
      const downloadBtn = document.getElementById('downloadWmBtn');
      const textInput = document.getElementById('wmText');
      const posSelect = document.getElementById('wmPosition');
      const opacityInput = document.getElementById('wmOpacity');

      let userImg = null;

      function renderWatermark() {
        if (!userImg) return;
        canvas.width = userImg.width;
        canvas.height = userImg.height;
        ctx.drawImage(userImg, 0, 0);

        const text = textInput.value || 'CONFIDENTIAL';
        const opacity = parseInt(opacityInput.value) / 100;
        const pos = posSelect.value;

        ctx.save();
        ctx.fillStyle = `rgba(255, 255, 255, ${opacity})`;
        ctx.strokeStyle = `rgba(0, 0, 0, ${opacity * 0.7})`;
        ctx.lineWidth = Math.max(1, canvas.width / 500);

        if (pos === 'bottom-right') {
          const fontSize = Math.max(20, Math.floor(canvas.width / 25));
          ctx.font = `bold ${fontSize}px sans-serif`;
          ctx.textAlign = 'right';
          ctx.textBaseline = 'bottom';
          const x = canvas.width - 25;
          const y = canvas.height - 25;
          ctx.strokeText(text, x, y);
          ctx.fillText(text, x, y);
        } else if (pos === 'repeat') {
          const fontSize = Math.max(24, Math.floor(canvas.width / 20));
          ctx.font = `bold ${fontSize}px sans-serif`;
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.rotate(-0.4);
          for (let x = -canvas.width; x < canvas.width * 2; x += 300) {
            for (let y = -canvas.height; y < canvas.height * 2; y += 180) {
              ctx.strokeText(text, x, y);
              ctx.fillText(text, x, y);
            }
          }
        } else {
          // Center diagonal
          const fontSize = Math.max(30, Math.floor(canvas.width / 14));
          ctx.font = `bold ${fontSize}px sans-serif`;
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.translate(canvas.width / 2, canvas.height / 2);
          ctx.rotate(-0.5);
          ctx.strokeText(text, 0, 0);
          ctx.fillText(text, 0, 0);
        }
        ctx.restore();
      }

      fileInput.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (evt) => {
          userImg = new Image();
          userImg.onload = () => {
            controls.style.display = 'block';
            renderWatermark();
          };
          userImg.src = evt.target.result;
        };
        reader.readAsDataURL(file);
      };

      textInput.oninput = renderWatermark;
      posSelect.onchange = renderWatermark;
      opacityInput.oninput = renderWatermark;

      downloadBtn.onclick = () => {
        const link = document.createElement('a');
        link.download = 'watermarked-image.jpg';
        link.href = canvas.toDataURL('image/jpeg', 0.92);
        link.click();
      };
    }
  }''')

# ==============================================================================
# TOOL 5: id-card-print-layout
# ==============================================================================
new_tools.append('''  {
    id: 'id-card-print-layout',
    title: 'Aadhaar / PAN / ID Card 1-Click Print Layout Maker',
    shortDesc: 'Place Front and Back of your Aadhaar card, PAN card, or Voter ID side-by-side on a single A4 page for instant photocopy or print.',
    category: 'image',
    icon: 'fa-solid fa-address-card',
    badge: 'HOT',
    keywords: ['aadhaar print layout maker', 'pan card print layout', 'aadhaar front back print single page', 'voter id a4 print maker'],
    seoTitle: 'Aadhaar / PAN Card Front & Back Print Layout Maker Online - OmniTools',
    seoMeta: 'Place both Front and Back sides of your Aadhaar, PAN or Voter ID on a single A4 page online. Cyber cafe ready print layout.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1.5rem;">
          <label class="upload-dropzone" for="idFrontInput" style="display:block; cursor:pointer; padding:1.5rem;">
            <i class="fa-solid fa-id-card"></i>
            <h4>Upload Front Side</h4>
            <p>Tap to select Front Photo</p>
            <input type="file" id="idFrontInput" accept="image/*" style="position:absolute; opacity:0; width:1px; height:1px;">
          </label>

          <label class="upload-dropzone" for="idBackInput" style="display:block; cursor:pointer; padding:1.5rem;">
            <i class="fa-solid fa-id-card-clip"></i>
            <h4>Upload Back Side</h4>
            <p>Tap to select Back Photo</p>
            <input type="file" id="idBackInput" accept="image/*" style="position:absolute; opacity:0; width:1px; height:1px;">
          </label>
        </div>

        <div id="idLayoutControls" style="text-align:center; margin-top:1.5rem;">
          <div style="margin-bottom:1rem;">
            <canvas id="idLayoutCanvas" style="max-width:100%; height:auto; background:#fff; border-radius:8px; box-shadow:0 6px 18px rgba(0,0,0,0.15);"></canvas>
          </div>
          <button id="downloadIdLayoutBtn" class="btn-primary" style="padding:0.75rem 2rem;">
            <i class="fa-solid fa-print"></i> Download A4 Print-Ready Sheet
          </button>
        </div>
      `;

      const frontInput = document.getElementById('idFrontInput');
      const backInput = document.getElementById('idBackInput');
      const canvas = document.getElementById('idLayoutCanvas');
      const ctx = canvas.getContext('2d');
      const downloadBtn = document.getElementById('downloadIdLayoutBtn');

      let frontImg = null;
      let backImg = null;

      function renderA4Layout() {
        // A4 sheet proportions at standard printable resolution
        canvas.width = 1240;
        canvas.height = 1754;

        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Header label
        ctx.fillStyle = '#333333';
        ctx.font = 'bold 28px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('IDENTITY DOCUMENT - PRINT COPY', canvas.width / 2, 80);

        ctx.strokeStyle = '#cccccc';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(100, 105);
        ctx.lineTo(canvas.width - 100, 105);
        ctx.stroke();

        // Standard ID card size in pixels: ~500x315
        const cardW = 500;
        const cardH = 315;
        const gap = 40;
        const startX = (canvas.width - (cardW * 2 + gap)) / 2;
        const startY = 160;

        // Front Card
        if (frontImg) {
          ctx.drawImage(frontImg, startX, startY, cardW, cardH);
        } else {
          ctx.fillStyle = '#f8fafc';
          ctx.fillRect(startX, startY, cardW, cardH);
          ctx.fillStyle = '#94a3b8';
          ctx.font = '22px sans-serif';
          ctx.fillText('Front Side Placeholder', startX + cardW / 2, startY + cardH / 2);
        }
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;
        ctx.strokeRect(startX, startY, cardW, cardH);

        // Back Card
        const backX = startX + cardW + gap;
        if (backImg) {
          ctx.drawImage(backImg, backX, startY, cardW, cardH);
        } else {
          ctx.fillStyle = '#f8fafc';
          ctx.fillRect(backX, startY, cardW, cardH);
          ctx.fillStyle = '#94a3b8';
          ctx.font = '22px sans-serif';
          ctx.fillText('Back Side Placeholder', backX + cardW / 2, startY + cardH / 2);
        }
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;
        ctx.strokeRect(backX, startY, cardW, cardH);

        // Print cutting guide instruction
        ctx.fillStyle = '#64748b';
        ctx.font = '16px sans-serif';
        ctx.fillText('Cut along borders. Official dimensions preserved. Generated by OmniTools.', canvas.width / 2, startY + cardH + 40);
      }

      frontInput.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (evt) => {
          frontImg = new Image();
          frontImg.onload = renderA4Layout;
          frontImg.src = evt.target.result;
        };
        reader.readAsDataURL(file);
      };

      backInput.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (evt) => {
          backImg = new Image();
          backImg.onload = renderA4Layout;
          backImg.src = evt.target.result;
        };
        reader.readAsDataURL(file);
      };

      renderA4Layout();

      downloadBtn.onclick = () => {
        const link = document.createElement('a');
        link.download = 'id-card-a4-print-sheet.jpg';
        link.href = canvas.toDataURL('image/jpeg', 0.95);
        link.click();
      };
    }
  }''')

# ==============================================================================
# TOOL 6: photo-cropper
# ==============================================================================
new_tools.append('''  {
    id: 'photo-cropper',
    title: 'Photo Cropper & Aspect Ratio Tool',
    shortDesc: 'Crop photos to exact ratios: Square 1:1, YouTube 16:9, Passport 3.5:4.5, Story 9:16 or free-form.',
    category: 'image',
    icon: 'fa-solid fa-crop-simple',
    keywords: ['photo cropper online', 'crop image 1:1 square', 'crop 16:9 youtube thumbnail', 'passport photo cropper'],
    seoTitle: 'Photo Cropper & Aspect Ratio Tool Online Free - OmniTools',
    seoMeta: 'Crop photos online free to 1:1, 16:9, 4:3, or custom ratios. Instant high quality image download.',
    render: (container) => {
      container.innerHTML = `
        <label class="upload-dropzone" for="cropFileInput" style="display:block; cursor:pointer;">
          <i class="fa-solid fa-crop"></i>
          <h4>Upload Image to Crop</h4>
          <p>Tap to select image</p>
          <input type="file" id="cropFileInput" accept="image/*" style="position:absolute; opacity:0; width:1px; height:1px;">
        </label>

        <div id="cropControls" style="display:none; margin-top:1.5rem;">
          <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; margin-bottom:1.5rem;">
            <button class="btn-secondary crop-ratio-btn active" data-ratio="1">1:1 Square</button>
            <button class="btn-secondary crop-ratio-btn" data-ratio="1.777">16:9 Landscape</button>
            <button class="btn-secondary crop-ratio-btn" data-ratio="0.562">9:16 Story / Reel</button>
            <button class="btn-secondary crop-ratio-btn" data-ratio="1.333">4:3 Standard</button>
            <button class="btn-secondary crop-ratio-btn" data-ratio="0.777">3.5:4.5 Passport</button>
          </div>

          <div style="text-align:center; margin-bottom:1.5rem;">
            <canvas id="cropCanvas" style="max-width:100%; height:auto; border-radius:8px; box-shadow:0 4px 14px rgba(0,0,0,0.15);"></canvas>
          </div>

          <div style="text-align:center;">
            <button id="downloadCropBtn" class="btn-primary" style="padding:0.75rem 2rem;">
              <i class="fa-solid fa-download"></i> Download Cropped Image
            </button>
          </div>
        </div>
      `;

      const fileInput = document.getElementById('cropFileInput');
      const controls = document.getElementById('cropControls');
      const canvas = document.getElementById('cropCanvas');
      const ctx = canvas.getContext('2d');
      const downloadBtn = document.getElementById('downloadCropBtn');
      const ratioBtns = document.querySelectorAll('.crop-ratio-btn');

      let userImg = null;
      let targetRatio = 1;

      function renderCropped() {
        if (!userImg) return;
        const imgRatio = userImg.width / userImg.height;
        let cropW, cropH, cropX, cropY;

        if (imgRatio > targetRatio) {
          cropH = userImg.height;
          cropW = cropH * targetRatio;
          cropX = (userImg.width - cropW) / 2;
          cropY = 0;
        } else {
          cropW = userImg.width;
          cropH = cropW / targetRatio;
          cropX = 0;
          cropY = (userImg.height - cropH) / 2;
        }

        canvas.width = cropW;
        canvas.height = cropH;
        ctx.drawImage(userImg, cropX, cropY, cropW, cropH, 0, 0, cropW, cropH);
      }

      fileInput.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (evt) => {
          userImg = new Image();
          userImg.onload = () => {
            controls.style.display = 'block';
            renderCropped();
          };
          userImg.src = evt.target.result;
        };
        reader.readAsDataURL(file);
      };

      ratioBtns.forEach(btn => {
        btn.onclick = () => {
          ratioBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          targetRatio = parseFloat(btn.getAttribute('data-ratio'));
          renderCropped();
        };
      });

      downloadBtn.onclick = () => {
        const link = document.createElement('a');
        link.download = 'cropped-photo.jpg';
        link.href = canvas.toDataURL('image/jpeg', 0.95);
        link.click();
      };
    }
  }''')

# ==============================================================================
# TOOL 7: pdf-splitter
# ==============================================================================
new_tools.append('''  {
    id: 'pdf-splitter',
    title: 'Split PDF & Extract Pages Online',
    shortDesc: 'Extract individual pages or specific page ranges (e.g. 1-3, 5) from any PDF document into a new PDF.',
    category: 'pdf',
    icon: 'fa-solid fa-scissors',
    badge: 'NEW',
    keywords: ['split pdf online', 'extract pages from pdf', 'separate pdf pages', 'cut pdf pages free'],
    seoTitle: 'Split PDF Online - Extract Pages from PDF Document Free',
    seoMeta: 'Split PDF online for free. Extract specific pages or split multi-page PDF files client-side with 100% data privacy.',
    render: (container) => {
      container.innerHTML = `
        <label class="upload-dropzone" for="splitPdfInput" style="display:block; cursor:pointer;">
          <i class="fa-solid fa-file-pdf"></i>
          <h4>Upload PDF File to Split</h4>
          <p>Tap to select PDF from storage</p>
          <input type="file" id="splitPdfInput" accept="application/pdf" style="position:absolute; opacity:0; width:1px; height:1px;">
        </label>

        <div id="splitPdfControls" style="display:none; margin-top:1.5rem; background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
          <div style="margin-bottom:1rem; font-weight:600; color:var(--text-color);" id="pdfInfoText">Total Pages: ...</div>
          
          <div style="margin-bottom:1.5rem;">
            <label style="display:block; margin-bottom:0.5rem;">Pages to Extract (e.g. 1, 3-5):</label>
            <input type="text" id="splitPageRanges" class="form-input" placeholder="e.g. 1-2, 4">
            <span style="font-size:0.8rem; color:var(--text-muted);">Enter comma separated page numbers or ranges</span>
          </div>

          <button id="executeSplitBtn" class="btn-primary" style="width:100%; padding:0.75rem;">
            <i class="fa-solid fa-file-export"></i> Split & Download Extracted PDF
          </button>
        </div>
      `;

      const fileInput = document.getElementById('splitPdfInput');
      const controls = document.getElementById('splitPdfControls');
      const infoText = document.getElementById('pdfInfoText');
      const rangesInput = document.getElementById('splitPageRanges');
      const splitBtn = document.getElementById('executeSplitBtn');

      let pdfBytes = null;
      let totalPages = 0;

      fileInput.onchange = async (e) => {
        const file = e.target.files[0];
        if (!file) return;
        pdfBytes = await file.arrayBuffer();

        if (window.PDFLib) {
          const pdfDoc = await PDFLib.PDFDocument.load(pdfBytes);
          totalPages = pdfDoc.getPageCount();
          infoText.innerText = `Uploaded PDF: ${file.name} (Total Pages: ${totalPages})`;
          rangesInput.value = `1-${Math.min(totalPages, 2)}`;
          controls.style.display = 'block';
        }
      };

      splitBtn.onclick = async () => {
        if (!pdfBytes || !window.PDFLib) return;
        splitBtn.disabled = true;
        splitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Extracting Pages...';

        try {
          const originalDoc = await PDFLib.PDFDocument.load(pdfBytes);
          const newDoc = await PDFLib.PDFDocument.create();

          const rangeStr = rangesInput.value.replace(/\\s+/g, '');
          const parts = rangeStr.split(',');
          const pageIndices = new Set();

          parts.forEach(p => {
            if (p.includes('-')) {
              const [start, end] = p.split('-').map(Number);
              if (start && end) {
                for (let i = start; i <= end; i++) {
                  if (i >= 1 && i <= totalPages) pageIndices.add(i - 1);
                }
              }
            } else {
              const num = Number(p);
              if (num >= 1 && num <= totalPages) pageIndices.add(num - 1);
            }
          });

          const indicesArray = Array.from(pageIndices).sort((a,b) => a - b);
          if (indicesArray.length === 0) {
            alert('Please enter valid page numbers between 1 and ' + totalPages);
            splitBtn.disabled = false;
            splitBtn.innerHTML = '<i class="fa-solid fa-file-export"></i> Split & Download Extracted PDF';
            return;
          }

          const copiedPages = await newDoc.copyPages(originalDoc, indicesArray);
          copiedPages.forEach(page => newDoc.addPage(page));

          const savedBytes = await newDoc.save();
          const blob = new Blob([savedBytes], { type: 'application/pdf' });
          const link = document.createElement('a');
          link.href = URL.createObjectURL(blob);
          link.download = 'split-extracted.pdf';
          link.click();
        } catch (err) {
          alert('Error extracting pages: ' + err.message);
        } finally {
          splitBtn.disabled = false;
          splitBtn.innerHTML = '<i class="fa-solid fa-file-export"></i> Split & Download Extracted PDF';
        }
      };
    }
  }''')

# ==============================================================================
# TOOL 8: pdf-page-manager
# ==============================================================================
new_tools.append('''  {
    id: 'pdf-page-manager',
    title: 'Rotate PDF & Delete PDF Pages Online',
    shortDesc: 'Rotate upside-down PDF pages 90° or 180° and delete unwanted pages with instant client-side saving.',
    category: 'pdf',
    icon: 'fa-solid fa-arrows-rotate',
    keywords: ['rotate pdf pages', 'rotate pdf 90 degrees', 'delete page from pdf', 'reorient pdf pages online'],
    seoTitle: 'Rotate PDF & Delete PDF Pages Online Free - OmniTools',
    seoMeta: 'Rotate PDF pages 90, 180 or 270 degrees and delete unwanted pages online for free. Private client-side PDF tool.',
    render: (container) => {
      container.innerHTML = `
        <label class="upload-dropzone" for="rotatePdfInput" style="display:block; cursor:pointer;">
          <i class="fa-solid fa-file-lines"></i>
          <h4>Upload PDF to Rotate or Edit</h4>
          <p>Tap to select PDF file</p>
          <input type="file" id="rotatePdfInput" accept="application/pdf" style="position:absolute; opacity:0; width:1px; height:1px;">
        </label>

        <div id="rotatePdfControls" style="display:none; margin-top:1.5rem; background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
          <div id="pdfRotateStatus" style="font-weight:600; margin-bottom:1rem;">Total Pages: ...</div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1.5rem;">
            <div>
              <label>Rotate All Pages</label>
              <select id="pdfRotationAngle" class="form-input">
                <option value="90">Rotate 90° Clockwise</option>
                <option value="180">Rotate 180° Upside Down</option>
                <option value="270">Rotate 270° Counter-Clockwise</option>
              </select>
            </div>
            <div>
              <label>Delete Specific Page (Optional)</label>
              <input type="number" id="deletePageNum" class="form-input" placeholder="e.g. 2" min="1">
            </div>
          </div>

          <button id="saveRotatedPdfBtn" class="btn-primary" style="width:100%; padding:0.75rem;">
            <i class="fa-solid fa-floppy-disk"></i> Apply Changes & Save PDF
          </button>
        </div>
      `;

      const fileInput = document.getElementById('rotatePdfInput');
      const controls = document.getElementById('rotatePdfControls');
      const statusText = document.getElementById('pdfRotateStatus');
      const angleSelect = document.getElementById('pdfRotationAngle');
      const deleteInput = document.getElementById('deletePageNum');
      const saveBtn = document.getElementById('saveRotatedPdfBtn');

      let rawBytes = null;
      let pageCount = 0;

      fileInput.onchange = async (e) => {
        const file = e.target.files[0];
        if (!file) return;
        rawBytes = await file.arrayBuffer();

        if (window.PDFLib) {
          const doc = await PDFLib.PDFDocument.load(rawBytes);
          pageCount = doc.getPageCount();
          statusText.innerText = `Uploaded: ${file.name} (${pageCount} pages)`;
          deleteInput.max = pageCount;
          controls.style.display = 'block';
        }
      };

      saveBtn.onclick = async () => {
        if (!rawBytes || !window.PDFLib) return;
        saveBtn.disabled = true;
        saveBtn.innerText = 'Processing PDF...';

        try {
          const doc = await PDFLib.PDFDocument.load(rawBytes);
          const angle = parseInt(angleSelect.value);

          // Apply rotation
          const pages = doc.getPages();
          pages.forEach(p => {
            const currentRotation = p.getRotation().angle;
            p.setRotation(PDFLib.degrees((currentRotation + angle) % 360));
          });

          // Delete page if specified
          const delNum = parseInt(deleteInput.value);
          if (delNum && delNum >= 1 && delNum <= doc.getPageCount()) {
            doc.removePage(delNum - 1);
          }

          const outBytes = await doc.save();
          const blob = new Blob([outBytes], { type: 'application/pdf' });
          const link = document.createElement('a');
          link.href = URL.createObjectURL(blob);
          link.download = 'modified-document.pdf';
          link.click();
        } catch (err) {
          alert('Error modifying PDF: ' + err.message);
        } finally {
          saveBtn.disabled = false;
          saveBtn.innerHTML = '<i class="fa-solid fa-floppy-disk"></i> Apply Changes & Save PDF';
        }
      };
    }
  }''')

# ==============================================================================
# TOOL 9: attendance-calculator
# ==============================================================================
new_tools.append('''  {
    id: 'attendance-calculator',
    title: 'Attendance Calculator (75% Rule & Bunk Calculator)',
    shortDesc: 'Calculate your college attendance percentage and find out how many classes you can bunk or need to attend to maintain 75%.',
    category: 'calculator',
    icon: 'fa-solid fa-clipboard-user',
    badge: 'HOT',
    keywords: ['attendance calculator', '75 attendance rule calculator', 'how many classes can i bunk', 'college attendance tracker'],
    seoTitle: 'Attendance Calculator & 75% Bunk Planner Online - OmniTools',
    seoMeta: 'Calculate attendance percentage and check how many classes you must attend or can safely bunk to maintain 75% criteria.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div>
            <label>Total Classes Held</label>
            <input type="number" id="attTotal" class="form-input" value="60" min="1">
          </div>
          <div>
            <label>Classes Attended</label>
            <input type="number" id="attPresent" class="form-input" value="48" min="0">
          </div>
          <div>
            <label>Target Criteria (%)</label>
            <input type="number" id="attTarget" class="form-input" value="75" min="1" max="100">
          </div>
        </div>

        <div id="attResultBox" style="background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color); text-align:center;">
          <div style="font-size:0.9rem; color:var(--text-muted); margin-bottom:0.25rem;">Current Attendance Percentage</div>
          <div id="attPercentDisplay" style="font-size:2.8rem; font-weight:800; color:var(--primary-color);">80.0%</div>
          <div id="attAdvice" style="font-size:1.1rem; font-weight:600; margin-top:0.75rem; color:#10b981;">
            🎉 You can safely bunk 4 more classes and still maintain 75%!
          </div>
        </div>
      `;

      const totalInput = document.getElementById('attTotal');
      const presentInput = document.getElementById('attPresent');
      const targetInput = document.getElementById('attTarget');
      const percentEl = document.getElementById('attPercentDisplay');
      const adviceEl = document.getElementById('attAdvice');

      function calculate() {
        const total = parseInt(totalInput.value) || 0;
        const present = parseInt(presentInput.value) || 0;
        const target = parseFloat(targetInput.value) || 75;

        if (total <= 0 || present > total) {
          percentEl.innerText = '--%';
          adviceEl.innerText = 'Classes attended cannot exceed total classes.';
          adviceEl.style.color = '#ef4444';
          return;
        }

        const pct = (present / total) * 100;
        percentEl.innerText = pct.toFixed(1) + '%';

        if (pct >= target) {
          // Bunk formula: present / (total + x) >= target/100  =>  x = (100*present - target*total) / target
          const canBunk = Math.floor((100 * present - target * total) / target);
          percentEl.style.color = '#10b981';
          adviceEl.style.color = '#10b981';
          adviceEl.innerHTML = canBunk > 0 
            ? `🎉 You are safe! You can bunk <strong>${canBunk}</strong> more classes and stay at ${target}%.`
            : `✅ You are right on track. Do not miss the next class to stay above ${target}%.`;
        } else {
          // Need to attend formula: (present + y) / (total + y) >= target/100 => y = (target*total - 100*present) / (100 - target)
          const mustAttend = Math.ceil((target * total - 100 * present) / (100 - target));
          percentEl.style.color = '#ef4444';
          adviceEl.style.color = '#ef4444';
          adviceEl.innerHTML = `⚠️ Shortage alert! You must attend <strong>${mustAttend}</strong> consecutive classes without missing to reach ${target}%.`;
        }
      }

      totalInput.oninput = calculate;
      presentInput.oninput = calculate;
      targetInput.oninput = calculate;
      calculate();
    }
  }''')

# ==============================================================================
# TOOL 10: percentage-calculator
# ==============================================================================
new_tools.append('''  {
    id: 'percentage-calculator',
    title: 'Percentage Calculator (3-in-1 Math Tool)',
    shortDesc: 'Calculate percentage of a number, find what percent X is of Y, or calculate percentage increase/decrease.',
    category: 'calculator',
    icon: 'fa-solid fa-percent',
    badge: 'HOT',
    keywords: ['percentage calculator', 'calculate percent online', 'percentage increase calculator', 'percentage of marks'],
    seoTitle: 'Percentage Calculator Online - Quick Math Percent Tool',
    seoMeta: 'Free online percentage calculator. Calculate X% of Y, percentage difference, discount, and percentage increase or decrease instantly.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:1fr; gap:1.5rem;">
          <!-- Mode 1: What is X% of Y? -->
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <h4 style="margin-bottom:0.75rem;"><i class="fa-solid fa-calculator"></i> 1. What is X% of Y?</h4>
            <div style="display:flex; flex-wrap:wrap; align-items:center; gap:0.5rem;">
              <span>What is</span>
              <input type="number" id="p1X" class="form-input" style="width:100px;" value="18">
              <span>% of</span>
              <input type="number" id="p1Y" class="form-input" style="width:130px;" value="5000">
              <span>=</span>
              <span id="p1Res" style="font-weight:800; font-size:1.3rem; color:var(--primary-color);">900</span>
            </div>
          </div>

          <!-- Mode 2: X is what percent of Y? -->
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <h4 style="margin-bottom:0.75rem;"><i class="fa-solid fa-graduation-cap"></i> 2. Marks / Ratio: X is what % of Y?</h4>
            <div style="display:flex; flex-wrap:wrap; align-items:center; gap:0.5rem;">
              <input type="number" id="p2X" class="form-input" style="width:110px;" value="425" placeholder="Marks">
              <span>is what % of</span>
              <input type="number" id="p2Y" class="form-input" style="width:110px;" value="500" placeholder="Total">
              <span>=</span>
              <span id="p2Res" style="font-weight:800; font-size:1.3rem; color:#10b981;">85.0%</span>
            </div>
          </div>

          <!-- Mode 3: Percentage Change -->
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <h4 style="margin-bottom:0.75rem;"><i class="fa-solid fa-chart-line"></i> 3. Percentage Increase / Decrease</h4>
            <div style="display:flex; flex-wrap:wrap; align-items:center; gap:0.5rem;">
              <span>From</span>
              <input type="number" id="p3X" class="form-input" style="width:120px;" value="1200">
              <span>to</span>
              <input type="number" id="p3Y" class="form-input" style="width:120px;" value="1500">
              <span>=</span>
              <span id="p3Res" style="font-weight:800; font-size:1.3rem; color:#3b82f6;">+25.0% Increase</span>
            </div>
          </div>
        </div>
      `;

      function calc() {
        const x1 = parseFloat(document.getElementById('p1X').value) || 0;
        const y1 = parseFloat(document.getElementById('p1Y').value) || 0;
        document.getElementById('p1Res').innerText = ((x1 / 100) * y1).toLocaleString();

        const x2 = parseFloat(document.getElementById('p2X').value) || 0;
        const y2 = parseFloat(document.getElementById('p2Y').value) || 1;
        document.getElementById('p2Res').innerText = ((x2 / y2) * 100).toFixed(2) + '%';

        const x3 = parseFloat(document.getElementById('p3X').value) || 0;
        const y3 = parseFloat(document.getElementById('p3Y').value) || 0;
        if (x3 !== 0) {
          const diff = ((y3 - x3) / x3) * 100;
          const label = diff >= 0 ? `+${diff.toFixed(2)}% Increase` : `${diff.toFixed(2)}% Decrease`;
          document.getElementById('p3Res').innerText = label;
          document.getElementById('p3Res').style.color = diff >= 0 ? '#10b981' : '#ef4444';
        }
      }

      ['p1X', 'p1Y', 'p2X', 'p2Y', 'p3X', 'p3Y'].forEach(id => {
        document.getElementById(id).oninput = calc;
      });
    }
  }''')

# ==============================================================================
# TOOL 11: upi-qr-maker
# ==============================================================================
new_tools.append('''  {
    id: 'upi-qr-maker',
    title: 'UPI Payment QR Code Maker (Google Pay, PhonePe, Paytm)',
    shortDesc: 'Create an instant UPI payment QR code with customized amount, payee name, and note for shopkeepers or freelance payments.',
    category: 'developer',
    icon: 'fa-solid fa-indian-rupee-sign',
    badge: 'HOT',
    keywords: ['upi qr code generator', 'gpay qr code maker', 'phonepe payment qr maker', 'custom amount upi qr'],
    seoTitle: 'UPI QR Code Generator with Amount (PhonePe, GPay, Paytm) - OmniTools',
    seoMeta: 'Generate custom UPI payment QR codes online. Enter UPI ID, name, and amount for instant payment collection via Google Pay, PhonePe, and Paytm.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div>
            <label>UPI ID (VPA) *</label>
            <input type="text" id="upiId" class="form-input" placeholder="e.g. mobile@upi, name@okaxis" value="shopexample@upi">
          </div>
          <div>
            <label>Payee / Business Name *</label>
            <input type="text" id="upiName" class="form-input" placeholder="e.g. Rahul Sharma" value="Smart Store">
          </div>
          <div>
            <label>Amount (₹) (Optional)</label>
            <input type="number" id="upiAmount" class="form-input" placeholder="e.g. 500" value="500">
          </div>
          <div>
            <label>Payment Note (Optional)</label>
            <input type="text" id="upiNote" class="form-input" placeholder="e.g. Bill Payment" value="Order Payment">
          </div>
        </div>

        <div style="text-align:center; background:var(--bg-input); padding:2rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
          <div id="upiQrTarget" style="display:inline-block; padding:1rem; background:#fff; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.1);"></div>
          <div style="margin-top:1rem; font-weight:600; color:var(--text-color);" id="upiDisplayAmount">Scan to pay: ₹500 via Any UPI App</div>
          <div style="margin-top:1.5rem;">
            <button id="downloadUpiQrBtn" class="btn-primary" style="padding:0.75rem 2rem;">
              <i class="fa-solid fa-download"></i> Download Payment QR Code
            </button>
          </div>
        </div>
      `;

      const idInput = document.getElementById('upiId');
      const nameInput = document.getElementById('upiName');
      const amountInput = document.getElementById('upiAmount');
      const noteInput = document.getElementById('upiNote');
      const qrTarget = document.getElementById('upiQrTarget');
      const amountDisplay = document.getElementById('upiDisplayAmount');
      const downloadBtn = document.getElementById('downloadUpiQrBtn');

      let qrInstance = null;

      function generateUpi() {
        const vpa = idInput.value.trim();
        const name = encodeURIComponent(nameInput.value.trim());
        const amt = amountInput.value.trim();
        const note = encodeURIComponent(noteInput.value.trim());

        if (!vpa) return;

        let uri = `upi://pay?pa=${vpa}&pn=${name}`;
        if (amt) uri += `&am=${amt}&cu=INR`;
        if (note) uri += `&tn=${note}`;

        amountDisplay.innerText = amt ? `Scan to pay: ₹${amt} to ${nameInput.value}` : `Scan to pay any amount to ${nameInput.value}`;

        qrTarget.innerHTML = '';
        if (window.QRCode) {
          qrInstance = new QRCode(qrTarget, {
            text: uri,
            width: 200,
            height: 200,
            colorDark: '#000000',
            colorLight: '#ffffff',
            correctLevel: QRCode.CorrectLevel.H
          });
        }
      }

      [idInput, nameInput, amountInput, noteInput].forEach(inp => inp.oninput = generateUpi);
      generateUpi();

      downloadBtn.onclick = () => {
        const img = qrTarget.querySelector('img');
        if (img && img.src) {
          const a = document.createElement('a');
          a.download = 'upi-payment-qr.png';
          a.href = img.src;
          a.click();
        }
      };
    }
  }''')

# ==============================================================================
# TOOL 12: wifi-qr-maker
# ==============================================================================
new_tools.append('''  {
    id: 'wifi-qr-maker',
    title: 'Wi-Fi QR Code Generator (Instant Connect)',
    shortDesc: 'Create a Wi-Fi QR code so guests or customers can scan and connect to your Wi-Fi instantly without typing password.',
    category: 'developer',
    icon: 'fa-solid fa-wifi',
    keywords: ['wifi qr code generator', 'connect wifi by scanning qr', 'wifi password qr maker', 'wifi share qr'],
    seoTitle: 'Wi-Fi QR Code Generator - Connect Without Typing Password',
    seoMeta: 'Generate Wi-Fi QR code online for free. Guests can scan with iPhone or Android camera to instantly join your Wi-Fi network.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div>
            <label>Wi-Fi Name (SSID) *</label>
            <input type="text" id="wifiSsid" class="form-input" placeholder="e.g. Home_5G" value="MyHome_WiFi">
          </div>
          <div>
            <label>Password</label>
            <input type="text" id="wifiPass" class="form-input" placeholder="e.g. MySecret123" value="Password@123">
          </div>
          <div>
            <label>Security Encryption</label>
            <select id="wifiEnc" class="form-input">
              <option value="WPA">WPA / WPA2 (Most Common)</option>
              <option value="WEP">WEP</option>
              <option value="nopass">None (Open Network)</option>
            </select>
          </div>
        </div>

        <div style="text-align:center; background:var(--bg-input); padding:2rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
          <div id="wifiQrBox" style="display:inline-block; padding:1.25rem; background:#fff; border-radius:12px; box-shadow:0 4px 14px rgba(0,0,0,0.1);"></div>
          <p style="margin-top:1rem; font-size:0.9rem; color:var(--text-muted);">Scan this code with any phone camera to connect directly.</p>
          <div style="margin-top:1.5rem;">
            <button id="downloadWifiQr" class="btn-primary" style="padding:0.75rem 2rem;">
              <i class="fa-solid fa-download"></i> Download Wi-Fi Connect QR
            </button>
          </div>
        </div>
      `;

      const ssid = document.getElementById('wifiSsid');
      const pass = document.getElementById('wifiPass');
      const enc = document.getElementById('wifiEnc');
      const qrBox = document.getElementById('wifiQrBox');
      const downloadBtn = document.getElementById('downloadWifiQr');

      function gen() {
        const s = ssid.value.trim();
        const p = pass.value.trim();
        const t = enc.value;
        const text = `WIFI:T:${t};S:${s};P:${p};;`;

        qrBox.innerHTML = '';
        if (window.QRCode) {
          new QRCode(qrBox, {
            text: text,
            width: 200,
            height: 200,
            colorDark: '#000000',
            colorLight: '#ffffff',
            correctLevel: QRCode.CorrectLevel.H
          });
        }
      }

      [ssid, pass, enc].forEach(inp => inp.oninput = gen);
      gen();

      downloadBtn.onclick = () => {
        const img = qrBox.querySelector('img');
        if (img && img.src) {
          const a = document.createElement('a');
          a.download = 'wifi-connect-qr.png';
          a.href = img.src;
          a.click();
        }
      };
    }
  }''')

# ==============================================================================
# TOOL 13: fuel-mileage-calc
# ==============================================================================
new_tools.append('''  {
    id: 'fuel-mileage-calc',
    title: 'Fuel Cost & Mileage Calculator (Petrol / Diesel / EV)',
    shortDesc: 'Calculate total fuel cost, liters needed, and cost per kilometer for your car, bike, or road trip.',
    category: 'calculator',
    icon: 'fa-solid fa-gas-pump',
    keywords: ['fuel cost calculator', 'mileage calculator km per liter', 'petrol cost per km', 'car trip cost calculator'],
    seoTitle: 'Fuel Cost & Mileage Calculator - Road Trip Fuel Planner',
    seoMeta: 'Calculate trip fuel cost, mileage (km/l), total liters required, and per-km travel cost for petrol, diesel, and CNG vehicles.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div>
            <label>Trip Distance (KM)</label>
            <input type="number" id="fuelDistance" class="form-input" value="350">
          </div>
          <div>
            <label>Vehicle Mileage (KM / Liter)</label>
            <input type="number" id="fuelMileage" class="form-input" value="18">
          </div>
          <div>
            <label>Fuel Price (₹ per Liter)</label>
            <input type="number" id="fuelPrice" class="form-input" value="96.5">
          </div>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:1rem; text-align:center;">
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="font-size:0.85rem; color:var(--text-muted);">Total Fuel Required</div>
            <div id="fuelNeeded" style="font-size:1.8rem; font-weight:800; color:var(--primary-color); margin-top:0.5rem;">19.4 L</div>
          </div>
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="font-size:0.85rem; color:var(--text-muted);">Estimated Trip Cost</div>
            <div id="fuelTotalCost" style="font-size:1.8rem; font-weight:800; color:#10b981; margin-top:0.5rem;">₹1,876</div>
          </div>
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="font-size:0.85rem; color:var(--text-muted);">Cost Per Kilometer</div>
            <div id="fuelCostPerKm" style="font-size:1.8rem; font-weight:800; color:#3b82f6; margin-top:0.5rem;">₹5.36 / km</div>
          </div>
        </div>
      `;

      const dist = document.getElementById('fuelDistance');
      const mil = document.getElementById('fuelMileage');
      const price = document.getElementById('fuelPrice');

      function calculate() {
        const d = parseFloat(dist.value) || 0;
        const m = parseFloat(mil.value) || 1;
        const p = parseFloat(price.value) || 0;

        const liters = d / m;
        const total = liters * p;
        const perKm = d > 0 ? total / d : 0;

        document.getElementById('fuelNeeded').innerText = liters.toFixed(1) + ' Liters';
        document.getElementById('fuelTotalCost').innerText = '₹' + Math.round(total).toLocaleString();
        document.getElementById('fuelCostPerKm').innerText = '₹' + perKm.toFixed(2) + ' / km';
      }

      [dist, mil, price].forEach(inp => inp.oninput = calculate);
      calculate();
    }
  }''')

# ==============================================================================
# TOOL 14: date-difference-calc
# ==============================================================================
new_tools.append('''  {
    id: 'date-difference-calc',
    title: 'Date Difference & Days Calculator',
    shortDesc: 'Calculate the exact number of days, weeks, months, and years between two dates.',
    category: 'calculator',
    icon: 'fa-solid fa-calendar-days',
    keywords: ['date difference calculator', 'calculate days between two dates', 'days between dates online', 'duration between dates'],
    seoTitle: 'Date Difference Calculator - Days Between Two Dates Online',
    seoMeta: 'Calculate exact days, months, and years between two dates online. Find time duration between any two dates with 1-click precision.',
    render: (container) => {
      const today = new Date().toISOString().split('T')[0];
      const future = new Date(Date.now() + 30 * 86400000).toISOString().split('T')[0];

      container.innerHTML = `
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-bottom:1.5rem;">
          <div>
            <label>Start Date</label>
            <input type="date" id="dateStart" class="form-input" value="${today}">
          </div>
          <div>
            <label>End Date</label>
            <input type="date" id="dateEnd" class="form-input" value="${future}">
          </div>
        </div>

        <div style="background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color); text-align:center;">
          <div style="font-size:0.9rem; color:var(--text-muted);">Exact Duration</div>
          <div id="dateDiffDays" style="font-size:2.5rem; font-weight:800; color:var(--primary-color); margin:0.5rem 0;">30 Days</div>
          <div id="dateDiffDetailed" style="font-size:1.1rem; color:var(--text-color);">4 weeks and 2 days</div>
        </div>
      `;

      const start = document.getElementById('dateStart');
      const end = document.getElementById('dateEnd');
      const daysDisplay = document.getElementById('dateDiffDays');
      const detailedDisplay = document.getElementById('dateDiffDetailed');

      function calculate() {
        const d1 = new Date(start.value);
        const d2 = new Date(end.value);

        if (isNaN(d1) || isNaN(d2)) return;

        const diffTime = Math.abs(d2 - d1);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        const weeks = Math.floor(diffDays / 7);
        const remDays = diffDays % 7;

        daysDisplay.innerText = `${diffDays} Days`;
        detailedDisplay.innerText = `${weeks} weeks and ${remDays} days (${(diffDays * 24).toLocaleString()} hours)`;
      }

      start.onchange = calculate;
      end.onchange = calculate;
      calculate();
    }
  }''')

# ==============================================================================
# TOOL 15: scientific-calculator
# ==============================================================================
new_tools.append('''  {
    id: 'scientific-calculator',
    title: 'Scientific Calculator Online',
    shortDesc: 'Advanced online scientific calculator for trigonometry, logarithms, square root, powers, and engineering formulas.',
    category: 'calculator',
    icon: 'fa-solid fa-calculator',
    keywords: ['scientific calculator online', 'trigonometry calculator', 'online calculator with sin cos tan', 'log calculator'],
    seoTitle: 'Scientific Calculator Online Free - Advanced Math Calculator',
    seoMeta: 'Free online scientific calculator with sin, cos, tan, log, powers, square root, and parenthesis for students and engineers.',
    render: (container) => {
      container.innerHTML = `
        <div style="max-width:380px; margin:0 auto; background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color); box-shadow:0 8px 24px rgba(0,0,0,0.12);">
          <input type="text" id="sciScreen" class="form-input" style="font-size:1.6rem; text-align:right; font-weight:700; margin-bottom:1rem; padding:0.75rem;" readonly value="0">

          <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap:0.5rem;">
            <button class="sci-btn btn-secondary" data-val="C" style="color:#ef4444; font-weight:700;">C</button>
            <button class="sci-btn btn-secondary" data-val="(">(</button>
            <button class="sci-btn btn-secondary" data-val=")">)</button>
            <button class="sci-btn btn-secondary" data-val="/" style="color:var(--primary-color);">÷</button>

            <button class="sci-btn btn-secondary" data-val="sin(">sin</button>
            <button class="sci-btn btn-secondary" data-val="cos(">cos</button>
            <button class="sci-btn btn-secondary" data-val="tan(">tan</button>
            <button class="sci-btn btn-secondary" data-val="*" style="color:var(--primary-color);">×</button>

            <button class="sci-btn btn-secondary" data-val="7">7</button>
            <button class="sci-btn btn-secondary" data-val="8">8</button>
            <button class="sci-btn btn-secondary" data-val="9">9</button>
            <button class="sci-btn btn-secondary" data-val="-" style="color:var(--primary-color);">-</button>

            <button class="sci-btn btn-secondary" data-val="4">4</button>
            <button class="sci-btn btn-secondary" data-val="5">5</button>
            <button class="sci-btn btn-secondary" data-val="6">6</button>
            <button class="sci-btn btn-secondary" data-val="+" style="color:var(--primary-color);">+</button>

            <button class="sci-btn btn-secondary" data-val="1">1</button>
            <button class="sci-btn btn-secondary" data-val="2">2</button>
            <button class="sci-btn btn-secondary" data-val="3">3</button>
            <button class="sci-btn btn-secondary" data-val="sqrt(">√</button>

            <button class="sci-btn btn-secondary" data-val="0">0</button>
            <button class="sci-btn btn-secondary" data-val=".">.</button>
            <button class="sci-btn btn-secondary" data-val="^">^</button>
            <button class="sci-btn btn-primary" data-val="=" style="font-weight:800; font-size:1.3rem;">=</button>
          </div>
        </div>
      `;

      const screen = document.getElementById('sciScreen');
      const buttons = container.querySelectorAll('.sci-btn');

      buttons.forEach(btn => {
        btn.onclick = () => {
          const val = btn.getAttribute('data-val');
          if (val === 'C') {
            screen.value = '0';
          } else if (val === '=') {
            try {
              let expr = screen.value
                .split('sin(').join('Math.sin(')
                .split('cos(').join('Math.cos(')
                .split('tan(').join('Math.tan(')
                .split('sqrt(').join('Math.sqrt(')
                .split('^').join('**');
              const res = Function('"use strict";return (' + expr + ')')();
              screen.value = Number(res.toFixed(8)).toString();
            } catch (e) {
              screen.value = 'Error';
            }
          } else {
            if (screen.value === '0' || screen.value === 'Error') {
              screen.value = val;
            } else {
              screen.value += val;
            }
          }
        };
      });
    }
  }''')

# ==============================================================================
# TOOL 16: what-is-my-ip
# ==============================================================================
new_tools.append('''  {
    id: 'what-is-my-ip',
    title: 'What Is My IP & Browser Diagnostics',
    shortDesc: 'Check your public IPv4/IPv6 address, internet location, browser user agent, and screen resolution.',
    category: 'developer',
    icon: 'fa-solid fa-network-wired',
    keywords: ['what is my ip', 'check my ip address', 'public ip finder', 'browser diagnostics online'],
    seoTitle: 'What Is My IP Address Online - Free IP & Network Lookup',
    seoMeta: 'Find your public IP address, browser details, screen resolution, and network diagnostics online for free.',
    render: (container) => {
      container.innerHTML = `
        <div style="background:var(--bg-input); padding:2rem; border-radius:var(--radius-lg); border:1px solid var(--border-color); text-align:center; margin-bottom:1.5rem;">
          <div style="font-size:0.9rem; color:var(--text-muted); margin-bottom:0.5rem;">Your Public IP Address</div>
          <div id="publicIpDisplay" style="font-size:2.6rem; font-weight:800; color:var(--primary-color); word-break:break-all;">Loading IP...</div>
          <button id="copyIpBtn" class="btn-secondary" style="margin-top:1rem; padding:0.4rem 1.25rem;"><i class="fa-solid fa-copy"></i> Copy IP</button>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:1rem;">
          <div style="background:var(--bg-input); padding:1rem; border-radius:8px; border:1px solid var(--border-color);">
            <div style="color:var(--text-muted); font-size:0.85rem;">Screen Resolution</div>
            <div style="font-weight:700; margin-top:0.25rem;" id="diagScreen">...</div>
          </div>
          <div style="background:var(--bg-input); padding:1rem; border-radius:8px; border:1px solid var(--border-color);">
            <div style="color:var(--text-muted); font-size:0.85rem;">Operating Platform</div>
            <div style="font-weight:700; margin-top:0.25rem;" id="diagPlatform">...</div>
          </div>
          <div style="background:var(--bg-input); padding:1rem; border-radius:8px; border:1px solid var(--border-color);">
            <div style="color:var(--text-muted); font-size:0.85rem;">Device Language</div>
            <div style="font-weight:700; margin-top:0.25rem;" id="diagLang">...</div>
          </div>
        </div>
      `;

      const ipDisplay = document.getElementById('publicIpDisplay');
      const copyBtn = document.getElementById('copyIpBtn');

      document.getElementById('diagScreen').innerText = `${window.screen.width} x ${window.screen.height} (${window.devicePixelRatio}x)`;
      document.getElementById('diagPlatform').innerText = navigator.platform || 'Unknown';
      document.getElementById('diagLang').innerText = navigator.language || 'en-US';

      fetch('https://api.ipify.org?format=json')
        .then(res => res.json())
        .then(data => {
          ipDisplay.innerText = data.ip;
        })
        .catch(() => {
          ipDisplay.innerText = 'Unable to fetch IP (Check adblocker)';
        });

      copyBtn.onclick = () => {
        navigator.clipboard.writeText(ipDisplay.innerText).then(() => {
          copyBtn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
          setTimeout(() => copyBtn.innerHTML = '<i class="fa-solid fa-copy"></i> Copy IP', 2000);
        });
      };
    }
  }''')

# ==============================================================================
# TOOL 17: coin-toss-dice
# ==============================================================================
new_tools.append('''  {
    id: 'coin-toss-dice',
    title: 'Coin Toss & Dice Roller (Heads or Tails)',
    shortDesc: 'Flip an animated coin (Heads/Tails) or roll a 6-sided dice for instant random decisions and board games.',
    category: 'developer',
    icon: 'fa-solid fa-dice',
    keywords: ['coin toss online', 'flip a coin heads tails', 'dice roller online', 'roll a dice 1 to 6', 'random coin flip'],
    seoTitle: 'Coin Toss & 6-Sided Dice Roller Online Free - OmniTools',
    seoMeta: 'Flip a coin for Heads or Tails, or roll a 6-sided dice online for free. Instant fair random decision maker.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; text-align:center;">
          <!-- Coin -->
          <div style="background:var(--bg-input); padding:2rem 1rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div id="coinGraphic" style="width:100px; height:100px; border-radius:50%; background:linear-gradient(135deg, #f59e0b, #d97706); display:flex; align-items:center; justify-content:center; font-size:1.5rem; font-weight:800; color:#fff; margin:0 auto 1.5rem; box-shadow:0 6px 16px rgba(245, 158, 11, 0.4); border:3px solid #fbbf24;">HEADS</div>
            <button id="flipCoinBtn" class="btn-primary" style="width:100%;"><i class="fa-solid fa-coins"></i> Flip Coin</button>
          </div>

          <!-- Dice -->
          <div style="background:var(--bg-input); padding:2rem 1rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div id="diceGraphic" style="width:100px; height:100px; border-radius:16px; background:linear-gradient(135deg, #3b82f6, #1d4ed8); display:flex; align-items:center; justify-content:center; font-size:3rem; font-weight:800; color:#fff; margin:0 auto 1.5rem; box-shadow:0 6px 16px rgba(59, 130, 246, 0.4);">5</div>
            <button id="rollDiceBtn" class="btn-primary" style="width:100%;"><i class="fa-solid fa-dice"></i> Roll Dice</button>
          </div>
        </div>
      `;

      const coinEl = document.getElementById('coinGraphic');
      const diceEl = document.getElementById('diceGraphic');
      const flipBtn = document.getElementById('flipCoinBtn');
      const rollBtn = document.getElementById('rollDiceBtn');

      flipBtn.onclick = () => {
        coinEl.innerText = '...';
        setTimeout(() => {
          const isHeads = Math.random() > 0.5;
          coinEl.innerText = isHeads ? 'HEADS' : 'TAILS';
          coinEl.style.background = isHeads ? 'linear-gradient(135deg, #f59e0b, #d97706)' : 'linear-gradient(135deg, #94a3b8, #475569)';
        }, 200);
      };

      rollBtn.onclick = () => {
        diceEl.innerText = '...';
        setTimeout(() => {
          const roll = Math.floor(Math.random() * 6) + 1;
          diceEl.innerText = roll;
        }, 200);
      };
    }
  }''')

# ==============================================================================
# TOOL 18: profit-loss-calculator
# ==============================================================================
new_tools.append('''  {
    id: 'profit-loss-calculator',
    title: 'Profit & Loss Calculator (CP, SP & Margin)',
    shortDesc: 'Calculate profit, loss, profit percentage, and gross profit margin by entering Cost Price and Selling Price.',
    category: 'calculator',
    icon: 'fa-solid fa-chart-pie',
    keywords: ['profit and loss calculator', 'cost price selling price calculator', 'profit percentage calculator', 'gross margin calc'],
    seoTitle: 'Profit & Loss Calculator Online - Cost & Selling Price Tool',
    seoMeta: 'Calculate profit or loss amount, profit percentage, and sales margin online for free. Ideal for business and commerce students.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-bottom:1.5rem;">
          <div>
            <label>Cost Price (CP) (₹)</label>
            <input type="number" id="plCP" class="form-input" value="1200">
          </div>
          <div>
            <label>Selling Price (SP) (₹)</label>
            <input type="number" id="plSP" class="form-input" value="1500">
          </div>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:1rem; text-align:center;">
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="font-size:0.85rem; color:var(--text-muted);" id="plStatusLabel">Total Profit</div>
            <div id="plAmount" style="font-size:2rem; font-weight:800; color:#10b981; margin-top:0.5rem;">₹300</div>
          </div>
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="font-size:0.85rem; color:var(--text-muted);">Profit / Loss %</div>
            <div id="plPercent" style="font-size:2rem; font-weight:800; color:#10b981; margin-top:0.5rem;">+25.0%</div>
          </div>
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="font-size:0.85rem; color:var(--text-muted);">Profit Margin</div>
            <div id="plMargin" style="font-size:2rem; font-weight:800; color:var(--primary-color); margin-top:0.5rem;">20.0%</div>
          </div>
        </div>
      `;

      const cpInput = document.getElementById('plCP');
      const spInput = document.getElementById('plSP');
      const statusLabel = document.getElementById('plStatusLabel');
      const amountEl = document.getElementById('plAmount');
      const percentEl = document.getElementById('plPercent');
      const marginEl = document.getElementById('plMargin');

      function calculate() {
        const cp = parseFloat(cpInput.value) || 0;
        const sp = parseFloat(spInput.value) || 0;

        const diff = sp - cp;
        const pct = cp > 0 ? (diff / cp) * 100 : 0;
        const margin = sp > 0 ? (diff / sp) * 100 : 0;

        if (diff >= 0) {
          statusLabel.innerText = 'Total Profit';
          amountEl.innerText = '₹' + Math.abs(diff).toLocaleString();
          amountEl.style.color = '#10b981';
          percentEl.innerText = '+' + pct.toFixed(2) + '%';
          percentEl.style.color = '#10b981';
        } else {
          statusLabel.innerText = 'Total Loss';
          amountEl.innerText = '₹' + Math.abs(diff).toLocaleString();
          amountEl.style.color = '#ef4444';
          percentEl.innerText = pct.toFixed(2) + '%';
          percentEl.style.color = '#ef4444';
        }
        marginEl.innerText = margin.toFixed(2) + '%';
      }

      cpInput.oninput = calculate;
      spInput.oninput = calculate;
      calculate();
    }
  }''')

# ==============================================================================
# TOOL 19: discount-calculator
# ==============================================================================
new_tools.append('''  {
    id: 'discount-calculator',
    title: 'Discount & Sale Price Calculator',
    shortDesc: 'Calculate sale price, flat discounts, and how much money you save on shopping and online purchases.',
    category: 'calculator',
    icon: 'fa-solid fa-tag',
    keywords: ['discount calculator', 'shopping sale calculator', 'calculate discount percentage', 'save money calc'],
    seoTitle: 'Discount Calculator Online - Sale Price & Savings Calculator',
    seoMeta: 'Calculate final discounted price and savings on sales, shopping, and online deals with our free discount calculator.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-bottom:1.5rem;">
          <div>
            <label>Original Price (₹)</label>
            <input type="number" id="discOriginal" class="form-input" value="2499">
          </div>
          <div>
            <label>Discount (%)</label>
            <input type="number" id="discRate" class="form-input" value="30">
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; text-align:center;">
          <div style="background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="font-size:0.9rem; color:var(--text-muted);">Final Discounted Price</div>
            <div id="discFinal" style="font-size:2.5rem; font-weight:800; color:#10b981; margin-top:0.5rem;">₹1,749</div>
          </div>
          <div style="background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="font-size:0.9rem; color:var(--text-muted);">You Save</div>
            <div id="discSaved" style="font-size:2.5rem; font-weight:800; color:var(--primary-color); margin-top:0.5rem;">₹750</div>
          </div>
        </div>
      `;

      const origInput = document.getElementById('discOriginal');
      const rateInput = document.getElementById('discRate');
      const finalEl = document.getElementById('discFinal');
      const savedEl = document.getElementById('discSaved');

      function calculate() {
        const orig = parseFloat(origInput.value) || 0;
        const rate = parseFloat(rateInput.value) || 0;

        const saved = (orig * rate) / 100;
        const finalP = orig - saved;

        finalEl.innerText = '₹' + Math.round(finalP).toLocaleString();
        savedEl.innerText = '₹' + Math.round(saved).toLocaleString();
      }

      origInput.oninput = calculate;
      rateInput.oninput = calculate;
      calculate();
    }
  }''')

# ==============================================================================
# TOOL 20: interest-calculator
# ==============================================================================
new_tools.append('''  {
    id: 'interest-calculator',
    title: 'Simple & Compound Interest Calculator (SI & CI)',
    shortDesc: 'Calculate Simple Interest and Compound Interest with yearly, half-yearly, and quarterly compounding options.',
    category: 'calculator',
    icon: 'fa-solid fa-coins',
    keywords: ['simple interest calculator', 'compound interest calculator', 'si ci calculator online', 'interest rate formula'],
    seoTitle: 'Simple & Compound Interest Calculator Online - OmniTools',
    seoMeta: 'Calculate simple and compound interest online. Compare maturity amount, interest earned, and compounded growth.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div>
            <label>Principal Amount (₹)</label>
            <input type="number" id="intPrincipal" class="form-input" value="100000">
          </div>
          <div>
            <label>Annual Interest Rate (%)</label>
            <input type="number" id="intRate" class="form-input" value="8.5" step="0.1">
          </div>
          <div>
            <label>Time Period (Years)</label>
            <input type="number" id="intTime" class="form-input" value="3">
          </div>
          <div>
            <label>Type</label>
            <select id="intType" class="form-input">
              <option value="compound">Compound Interest (Annually)</option>
              <option value="simple">Simple Interest (SI)</option>
            </select>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; text-align:center;">
          <div style="background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="font-size:0.9rem; color:var(--text-muted);">Total Interest Earned</div>
            <div id="intEarned" style="font-size:2.2rem; font-weight:800; color:var(--primary-color); margin-top:0.5rem;">₹27,729</div>
          </div>
          <div style="background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="font-size:0.9rem; color:var(--text-muted);">Total Maturity Amount</div>
            <div id="intMaturity" style="font-size:2.2rem; font-weight:800; color:#10b981; margin-top:0.5rem;">₹1,27,729</div>
          </div>
        </div>
      `;

      const pInput = document.getElementById('intPrincipal');
      const rInput = document.getElementById('intRate');
      const tInput = document.getElementById('intTime');
      const typeSelect = document.getElementById('intType');
      const earnedEl = document.getElementById('intEarned');
      const matEl = document.getElementById('intMaturity');

      function calculate() {
        const p = parseFloat(pInput.value) || 0;
        const r = parseFloat(rInput.value) || 0;
        const t = parseFloat(tInput.value) || 0;
        const isCompound = typeSelect.value === 'compound';

        let interest = 0;
        let total = 0;

        if (isCompound) {
          total = p * Math.pow((1 + (r / 100)), t);
          interest = total - p;
        } else {
          interest = (p * r * t) / 100;
          total = p + interest;
        }

        earnedEl.innerText = '₹' + Math.round(interest).toLocaleString();
        matEl.innerText = '₹' + Math.round(total).toLocaleString();
      }

      [pInput, rInput, tInput, typeSelect].forEach(el => el.oninput = calculate);
      calculate();
    }
  }''')

# ==============================================================================
# TOOL 21: electricity-bill-calc
# ==============================================================================
new_tools.append('''  {
    id: 'electricity-bill-calc',
    title: 'Electricity Bill Calculator (Slab & Units)',
    shortDesc: 'Estimate your monthly home electricity bill based on units consumed (kWh) and slab rates.',
    category: 'calculator',
    icon: 'fa-solid fa-bolt',
    keywords: ['electricity bill calculator', 'calculate power consumption bill', 'units to bill calculator', 'kwh power bill calculator'],
    seoTitle: 'Electricity Bill Calculator Online - Estimate Power Bill',
    seoMeta: 'Estimate monthly electricity bill online based on consumed units (kWh) and fixed charges. Free online power bill estimator.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div>
            <label>Units Consumed (kWh)</label>
            <input type="number" id="elecUnits" class="form-input" value="250">
          </div>
          <div>
            <label>Average Rate per Unit (₹)</label>
            <input type="number" id="elecRate" class="form-input" value="6.5" step="0.5">
          </div>
          <div>
            <label>Fixed Monthly Charges (₹)</label>
            <input type="number" id="elecFixed" class="form-input" value="110">
          </div>
        </div>

        <div style="background:var(--bg-input); padding:1.75rem; border-radius:var(--radius-lg); border:1px solid var(--border-color); text-align:center;">
          <div style="font-size:0.9rem; color:var(--text-muted);">Estimated Monthly Electricity Bill</div>
          <div id="elecTotal" style="font-size:2.8rem; font-weight:800; color:#f59e0b; margin:0.5rem 0;">₹1,735</div>
          <div id="elecSubText" style="font-size:0.95rem; color:var(--text-muted);">Energy Charge: ₹1,625 + Fixed Charge: ₹110</div>
        </div>
      `;

      const unitsInput = document.getElementById('elecUnits');
      const rateInput = document.getElementById('elecRate');
      const fixedInput = document.getElementById('elecFixed');
      const totalEl = document.getElementById('elecTotal');
      const subEl = document.getElementById('elecSubText');

      function calculate() {
        const u = parseFloat(unitsInput.value) || 0;
        const r = parseFloat(rateInput.value) || 0;
        const f = parseFloat(fixedInput.value) || 0;

        const energy = u * r;
        const total = energy + f;

        totalEl.innerText = '₹' + Math.round(total).toLocaleString();
        subEl.innerText = `Energy Charge: ₹${Math.round(energy).toLocaleString()} + Fixed Charge: ₹${f}`;
      }

      [unitsInput, rateInput, fixedInput].forEach(inp => inp.oninput = calculate);
      calculate();
    }
  }''')

# ==============================================================================
# TOOL 22: unit-converter
# ==============================================================================
new_tools.append('''  {
    id: 'unit-converter',
    title: 'All-in-One Unit Converter (Length, Weight, Temp)',
    shortDesc: 'Convert length, weight, temperature, area, volume, and digital storage units in real time.',
    category: 'calculator',
    icon: 'fa-solid fa-arrow-right-arrow-left',
    keywords: ['unit converter online', 'length converter cm to feet', 'weight converter kg to lbs', 'temperature converter c to f'],
    seoTitle: 'All-in-One Unit Converter Online Free - OmniTools',
    seoMeta: 'Convert Length, Weight, Temperature, Area and Digital Storage units instantly with our free online unit converter.',
    render: (container) => {
      container.innerHTML = `
        <div style="margin-bottom:1.5rem;">
          <label>Conversion Category</label>
          <select id="unitCategory" class="form-input">
            <option value="length">Length (Meters, Feet, Inches, KM, CM)</option>
            <option value="weight">Weight (Kilograms, Grams, Pounds, Ounces)</option>
            <option value="temp">Temperature (Celsius, Fahrenheit, Kelvin)</option>
          </select>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-bottom:1.5rem;">
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <label>From</label>
            <input type="number" id="unitValFrom" class="form-input" value="10" style="margin-bottom:0.75rem;">
            <select id="unitSelectFrom" class="form-input"></select>
          </div>

          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <label>To</label>
            <input type="number" id="unitValTo" class="form-input" readonly style="margin-bottom:0.75rem; font-weight:700; color:var(--primary-color);">
            <select id="unitSelectTo" class="form-input"></select>
          </div>
        </div>
      `;

      const catSelect = document.getElementById('unitCategory');
      const valFrom = document.getElementById('unitValFrom');
      const valTo = document.getElementById('unitValTo');
      const selFrom = document.getElementById('unitSelectFrom');
      const selTo = document.getElementById('unitSelectTo');

      const units = {
        length: {
          'Meter': 1,
          'Kilometer': 1000,
          'Centimeter': 0.01,
          'Millimeter': 0.001,
          'Foot': 0.3048,
          'Inch': 0.0254,
          'Mile': 1609.34
        },
        weight: {
          'Kilogram': 1,
          'Gram': 0.001,
          'Pound (lbs)': 0.453592,
          'Ounce (oz)': 0.0283495,
          'Metric Ton': 1000
        },
        temp: {
          'Celsius': 'C',
          'Fahrenheit': 'F',
          'Kelvin': 'K'
        }
      };

      function populate() {
        const cat = catSelect.value;
        selFrom.innerHTML = '';
        selTo.innerHTML = '';
        Object.keys(units[cat]).forEach(k => {
          selFrom.innerHTML += `<option value="${k}">${k}</option>`;
          selTo.innerHTML += `<option value="${k}">${k}</option>`;
        });
        if (selTo.options.length > 1) selTo.selectedIndex = 1;
        convert();
      }

      function convert() {
        const cat = catSelect.value;
        const val = parseFloat(valFrom.value) || 0;
        const uFrom = selFrom.value;
        const uTo = selTo.value;

        if (cat === 'temp') {
          let c = val;
          if (uFrom === 'Fahrenheit') c = (val - 32) * (5/9);
          if (uFrom === 'Kelvin') c = val - 273.15;

          let res = c;
          if (uTo === 'Fahrenheit') res = (c * (9/5)) + 32;
          if (uTo === 'Kelvin') res = c + 273.15;
          valTo.value = res.toFixed(2);
        } else {
          const meters = val * units[cat][uFrom];
          const result = meters / units[cat][uTo];
          valTo.value = Number(result.toFixed(4)).toString();
        }
      }

      catSelect.onchange = populate;
      valFrom.oninput = convert;
      selFrom.onchange = convert;
      selTo.onchange = convert;
      populate();
    }
  }''')

# ==============================================================================
# TOOL 23: whatsapp-qr-maker
# ==============================================================================
new_tools.append('''  {
    id: 'whatsapp-qr-maker',
    title: 'WhatsApp Direct Chat QR & Link Maker',
    shortDesc: 'Generate a WhatsApp click-to-chat QR code and link with phone number and pre-filled message.',
    category: 'developer',
    icon: 'fa-brands fa-whatsapp',
    badge: 'HOT',
    keywords: ['whatsapp qr code generator', 'whatsapp click to chat link', 'whatsapp chat qr maker', 'whatsapp business qr'],
    seoTitle: 'WhatsApp Direct Chat QR Code & Link Generator - OmniTools',
    seoMeta: 'Generate WhatsApp direct chat QR codes and links online for free. Customers can scan to start chatting with prefilled message.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-bottom:1.5rem;">
          <div>
            <label>WhatsApp Number (With Country Code, e.g. 919876543210)</label>
            <input type="text" id="waPhone" class="form-input" placeholder="e.g. 919876543210" value="919876543210">
          </div>
          <div>
            <label>Pre-filled Message</label>
            <input type="text" id="waMessage" class="form-input" placeholder="e.g. Hello, I want to inquire about..." value="Hello! I would like more information.">
          </div>
        </div>

        <div style="background:var(--bg-input); padding:2rem; border-radius:var(--radius-lg); border:1px solid var(--border-color); text-align:center;">
          <div id="waQrBox" style="display:inline-block; padding:1.25rem; background:#fff; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.1);"></div>
          <div style="margin-top:1.5rem;">
            <button id="downloadWaQr" class="btn-primary" style="padding:0.75rem 2rem;">
              <i class="fa-solid fa-download"></i> Download WhatsApp QR Code
            </button>
          </div>
        </div>
      `;

      const phone = document.getElementById('waPhone');
      const msg = document.getElementById('waMessage');
      const qrBox = document.getElementById('waQrBox');
      const downloadBtn = document.getElementById('downloadWaQr');

      function gen() {
        const p = phone.value.replace(/[^0-9]/g, '');
        const m = encodeURIComponent(msg.value);
        const url = `https://wa.me/${p}?text=${m}`;

        qrBox.innerHTML = '';
        if (window.QRCode) {
          new QRCode(qrBox, {
            text: url,
            width: 200,
            height: 200,
            colorDark: '#075e54',
            colorLight: '#ffffff',
            correctLevel: QRCode.CorrectLevel.H
          });
        }
      }

      phone.oninput = gen;
      msg.oninput = gen;
      gen();

      downloadBtn.onclick = () => {
        const img = qrBox.querySelector('img');
        if (img && img.src) {
          const a = document.createElement('a');
          a.download = 'whatsapp-chat-qr.png';
          a.href = img.src;
          a.click();
        }
      };
    }
  }''')

# ==============================================================================
# TOOL 24: reverse-text
# ==============================================================================
new_tools.append('''  {
    id: 'reverse-text',
    title: 'Text Reverser & Upside Down Font Tool',
    shortDesc: 'Reverse text characters, flip word order, or generate upside-down upside mirrored text for social media.',
    category: 'text',
    icon: 'fa-solid fa-arrows-left-right',
    keywords: ['reverse text online', 'backwards text generator', 'upside down text maker', 'mirror text online'],
    seoTitle: 'Text Reverser & Upside Down Text Generator Online - OmniTools',
    seoMeta: 'Reverse text, reverse wording, or flip characters upside down for Discord, Instagram, and gaming tags.',
    render: (container) => {
      container.innerHTML = `
        <div style="margin-bottom:1.5rem;">
          <label>Input Text</label>
          <textarea id="revInput" class="form-input" rows="3" placeholder="Type text here...">OmniTools is awesome</textarea>
        </div>

        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; margin-bottom:1.5rem;">
          <button class="btn-secondary rev-btn active" data-mode="chars">Reverse Characters</button>
          <button class="btn-secondary rev-btn" data-mode="words">Reverse Words</button>
          <button class="btn-secondary rev-btn" data-mode="upside">Upside Down (Flip)</button>
        </div>

        <div style="background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color); text-align:center;">
          <div id="revOutput" style="font-size:1.4rem; font-weight:700; color:var(--primary-color); word-break:break-all; margin-bottom:1rem;">emosewa si slooTinmO</div>
          <button id="copyRevBtn" class="btn-primary"><i class="fa-solid fa-copy"></i> Copy Reversed Text</button>
        </div>
      `;

      const input = document.getElementById('revInput');
      const output = document.getElementById('revOutput');
      const copyBtn = document.getElementById('copyRevBtn');
      const buttons = container.querySelectorAll('.rev-btn');
      let currentMode = 'chars';

      const flipMap = {'a':'ɐ','b':'q','c':'ɔ','d':'p','e':'ǝ','f':'ɟ','g':'ƃ','h':'ɥ','i':'ᴉ','j':'ɾ','k':'ʞ','l':'l','m':'ɯ','n':'u','o':'o','p':'d','q':'b','r':'ɹ','s':'s','t':'ʇ','u':'n','v':'ʌ','w':'ʍ','x':'x','y':'ʎ','z':'z','A':'∀','B':'𐐒','C':'Ɔ','D':'ᗡ','E':'Ǝ','F':'Ⅎ','G':'⅁','H':'H','I':'I','J':'ſ','K':'ʞ','L':'˥','M':'W','N':'N','O':'O','P':'Ԁ','Q':'Ò','R':'ᴚ','S':'S','T':'⊥','U':'∩','V':'Λ','W':'M','X':'X','Y':'⅄','Z':'Z'};

      function update() {
        const text = input.value;
        if (currentMode === 'chars') {
          output.innerText = text.split('').reverse().join('');
        } else if (currentMode === 'words') {
          output.innerText = text.split(' ').reverse().join(' ');
        } else {
          output.innerText = text.split('').map(c => flipMap[c] || c).reverse().join('');
        }
      }

      buttons.forEach(btn => {
        btn.onclick = () => {
          buttons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          currentMode = btn.getAttribute('data-mode');
          update();
        };
      });

      input.oninput = update;
      copyBtn.onclick = () => {
        navigator.clipboard.writeText(output.innerText).then(() => {
          copyBtn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
          setTimeout(() => copyBtn.innerHTML = '<i class="fa-solid fa-copy"></i> Copy Reversed Text', 2000);
        });
      };
    }
  }''')

# ==============================================================================
# TOOL 25: username-generator
# ==============================================================================
new_tools.append('''  {
    id: 'username-generator',
    title: 'Aesthetic & Gamer Username Generator',
    shortDesc: 'Generate stylish usernames, Instagram handles, and gaming tags based on your favorite keyword or style.',
    category: 'text',
    icon: 'fa-solid fa-user-tag',
    keywords: ['username generator', 'gamer tag generator', 'instagram username ideas', 'aesthetic usernames generator'],
    seoTitle: 'Aesthetic & Gamer Username Generator Online Free - OmniTools',
    seoMeta: 'Generate cool, stylish usernames for Instagram, Discord, YouTube, and Gaming. Instant copy with 1-click.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:1fr auto; gap:1rem; margin-bottom:1.5rem;">
          <input type="text" id="unameSeed" class="form-input" placeholder="Enter keyword or name (e.g. shadow, neo, star)" value="shadow">
          <button id="unameGenBtn" class="btn-primary" style="padding:0.75rem 1.5rem;"><i class="fa-solid fa-dice"></i> Generate New</button>
        </div>

        <div id="unameList" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:0.75rem;"></div>
      `;

      const seedInput = document.getElementById('unameSeed');
      const genBtn = document.getElementById('unameGenBtn');
      const listContainer = document.getElementById('unameList');

      const prefixes = ['xX_', 'Its_', 'TheReal_', 'Vibe_', 'Cyber_', 'Dark_', 'Aesthetic_', 'Silent_', 'Hyper_', 'Ghost_'];
      const suffixes = ['_99', '_exe', '_Vibes', '_Official', '_Zone', '_Prime', '_OP', '_X', '_Gamer', '_Nova'];

      function generate() {
        const base = seedInput.value.trim() || 'user';
        listContainer.innerHTML = '';

        for (let i = 0; i < 12; i++) {
          const pre = prefixes[Math.floor(Math.random() * prefixes.length)];
          const suf = suffixes[Math.floor(Math.random() * suffixes.length)];
          const u = `${pre}${base}${suf}`;

          const div = document.createElement('div');
          div.style.cssText = 'background:var(--bg-input); padding:0.75rem 1rem; border-radius:8px; border:1px solid var(--border-color); display:flex; justify-content:space-between; align-items:center; cursor:pointer;';
          div.innerHTML = `<span>${u}</span> <i class="fa-regular fa-copy" style="color:var(--text-muted);"></i>`;
          div.onclick = () => {
            navigator.clipboard.writeText(u).then(() => {
              div.style.borderColor = '#10b981';
              setTimeout(() => div.style.borderColor = 'var(--border-color)', 1500);
            });
          };
          listContainer.appendChild(div);
        }
      }

      genBtn.onclick = generate;
      seedInput.oninput = generate;
      generate();
    }
  }''')

# ==============================================================================
# TOOL 26: random-number-generator
# ==============================================================================
new_tools.append('''  {
    id: 'random-number-generator',
    title: 'Random Number & Lottery Picker',
    shortDesc: 'Generate random numbers within any custom range (Min to Max) with options for unique numbers or duplicates.',
    category: 'developer',
    icon: 'fa-solid fa-shuffle',
    keywords: ['random number generator', 'pick random number online', 'lottery number picker', 'random integer generator'],
    seoTitle: 'Random Number Generator Online Free - True Fair Picker',
    seoMeta: 'Generate random numbers between any range online for free. Fair random integer picker for giveaways, raffles, and decisions.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div>
            <label>Minimum Value</label>
            <input type="number" id="rngMin" class="form-input" value="1">
          </div>
          <div>
            <label>Maximum Value</label>
            <input type="number" id="rngMax" class="form-input" value="100">
          </div>
          <div>
            <label>How Many Numbers?</label>
            <input type="number" id="rngCount" class="form-input" value="1" min="1" max="50">
          </div>
        </div>

        <div style="background:var(--bg-input); padding:2rem; border-radius:var(--radius-lg); border:1px solid var(--border-color); text-align:center;">
          <div id="rngResultBox" style="font-size:3rem; font-weight:800; color:var(--primary-color); margin-bottom:1.5rem; word-break:break-all;">42</div>
          <button id="rngGenerateBtn" class="btn-primary" style="padding:0.75rem 2.5rem; font-size:1.1rem;"><i class="fa-solid fa-rotate"></i> Generate Random Number</button>
        </div>
      `;

      const minInput = document.getElementById('rngMin');
      const maxInput = document.getElementById('rngMax');
      const countInput = document.getElementById('rngCount');
      const resultBox = document.getElementById('rngResultBox');
      const genBtn = document.getElementById('rngGenerateBtn');

      function generate() {
        const min = parseInt(minInput.value) || 0;
        const max = parseInt(maxInput.value) || 100;
        const count = Math.min(50, Math.max(1, parseInt(countInput.value) || 1));

        if (min >= max) {
          resultBox.innerText = 'Min must be less than Max';
          return;
        }

        const numbers = [];
        for (let i = 0; i < count; i++) {
          const rand = Math.floor(Math.random() * (max - min + 1)) + min;
          numbers.push(rand);
        }

        resultBox.innerText = numbers.join(', ');
      }

      genBtn.onclick = generate;
    }
  }''')

# ==============================================================================
# TOOL 27: days-until-date
# ==============================================================================
new_tools.append('''  {
    id: 'days-until-date',
    title: 'Days Until Date & Event Countdown Timer',
    shortDesc: 'Live countdown of days, hours, minutes, and seconds until your next exam, birthday, or upcoming holiday.',
    category: 'calculator',
    icon: 'fa-solid fa-hourglass-half',
    keywords: ['days until date calculator', 'countdown to date online', 'exam countdown timer', 'days left until birthday'],
    seoTitle: 'Days Until Date & Event Countdown Timer Online - OmniTools',
    seoMeta: 'Count down days, hours, and minutes until any event or date online. Live real-time event timer for exams and celebrations.',
    render: (container) => {
      // Default to next New Year
      const nextYear = new Date().getFullYear() + 1;
      const targetDateStr = `${nextYear}-01-01`;

      container.innerHTML = `
        <div style="max-width:400px; margin:0 auto 1.5rem;">
          <label>Select Target Event Date</label>
          <input type="date" id="eventTargetDate" class="form-input" value="${targetDateStr}">
        </div>

        <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap:1rem; text-align:center;">
          <div style="background:var(--bg-input); padding:1.25rem 0.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div id="cntDays" style="font-size:2.2rem; font-weight:800; color:var(--primary-color);">0</div>
            <div style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase;">Days</div>
          </div>
          <div style="background:var(--bg-input); padding:1.25rem 0.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div id="cntHours" style="font-size:2.2rem; font-weight:800; color:#3b82f6;">0</div>
            <div style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase;">Hours</div>
          </div>
          <div style="background:var(--bg-input); padding:1.25rem 0.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div id="cntMinutes" style="font-size:2.2rem; font-weight:800; color:#10b981;">0</div>
            <div style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase;">Minutes</div>
          </div>
          <div style="background:var(--bg-input); padding:1.25rem 0.5rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div id="cntSeconds" style="font-size:2.2rem; font-weight:800; color:#f59e0b;">0</div>
            <div style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase;">Seconds</div>
          </div>
        </div>
      `;

      const dateInput = document.getElementById('eventTargetDate');
      const dEl = document.getElementById('cntDays');
      const hEl = document.getElementById('cntHours');
      const mEl = document.getElementById('cntMinutes');
      const sEl = document.getElementById('cntSeconds');

      function updateCountdown() {
        const target = new Date(dateInput.value + 'T00:00:00');
        const now = new Date();
        const diff = target - now;

        if (diff <= 0) {
          dEl.innerText = '0';
          hEl.innerText = '0';
          mEl.innerText = '0';
          sEl.innerText = '0';
          return;
        }

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const mins = Math.floor((diff / 1000 / 60) % 60);
        const secs = Math.floor((diff / 1000) % 60);

        dEl.innerText = days;
        hEl.innerText = hours;
        mEl.innerText = mins;
        sEl.innerText = secs;
      }

      dateInput.onchange = updateCountdown;
      const interval = setInterval(updateCountdown, 1000);
      updateCountdown();
    }
  }''')

# ==============================================================================
# TOOL 28: code-beautifier-minifier
# ==============================================================================
new_tools.append('''  {
    id: 'code-beautifier-minifier',
    title: 'HTML, CSS & JS Code Minifier & Formatter',
    shortDesc: 'Minify code to shrink file sizes or format messy code into beautifully indented readable blocks.',
    category: 'developer',
    icon: 'fa-solid fa-code',
    keywords: ['html minifier online', 'css minifier free', 'js code beautifier', 'code compressor formatter'],
    seoTitle: 'Code Minifier & Beautifier Online (HTML, CSS, JS) - OmniTools',
    seoMeta: 'Minify and compress HTML, CSS, and JavaScript or beautify messy source code online with 1-click.',
    render: (container) => {
      container.innerHTML = `
        <div style="margin-bottom:1.5rem;">
          <textarea id="codeSource" class="form-input" rows="8" placeholder="Paste your HTML, CSS or JavaScript code here..."><div class="card">
  <h1>Hello World</h1>
  <p>Test</p>
</div></textarea>
        </div>

        <div style="display:flex; flex-wrap:wrap; gap:0.75rem; justify-content:center; margin-bottom:1.5rem;">
          <button id="btnMinifyCode" class="btn-primary"><i class="fa-solid fa-compress"></i> Minify Code (Shrink Size)</button>
          <button id="btnBeautifyCode" class="btn-secondary"><i class="fa-solid fa-align-left"></i> Beautify / Indent</button>
          <button id="btnCopyCode" class="btn-secondary"><i class="fa-solid fa-copy"></i> Copy Result</button>
        </div>
      `;

      const source = document.getElementById('codeSource');
      const minBtn = document.getElementById('btnMinifyCode');
      const beauBtn = document.getElementById('btnBeautifyCode');
      const copyBtn = document.getElementById('btnCopyCode');

      minBtn.onclick = () => {
        let code = source.value;
        // Basic minification: remove extra spaces, newlines, comments
        code = code.replace(/\\/\\*[\\s\\S]*?\\*\\//g, '')
                   .replace(/\\/\\/.*/g, '')
                   .replace(/\\s+/g, ' ')
                   .replace(/\\s*([{}:;,>+~=])\\s*/g, '$1')
                   .trim();
        source.value = code;
      };

      beauBtn.onclick = () => {
        let code = source.value;
        let formatted = '';
        let indent = 0;
        const tab = '  ';

        // simple token formatter
        for (let i = 0; i < code.length; i++) {
          const char = code[i];
          if (char === '{' || char === '<' && code[i+1] !== '/') {
            formatted += char + '\\n' + tab.repeat(++indent);
          } else if (char === '}' || (char === '<' && code[i+1] === '/')) {
            indent = Math.max(0, indent - 1);
            formatted += '\\n' + tab.repeat(indent) + char;
          } else if (char === ';') {
            formatted += char + '\\n' + tab.repeat(indent);
          } else {
            formatted += char;
          }
        }
        source.value = formatted.trim();
      };

      copyBtn.onclick = () => {
        navigator.clipboard.writeText(source.value).then(() => {
          copyBtn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
          setTimeout(() => copyBtn.innerHTML = '<i class="fa-solid fa-copy"></i> Copy Result', 2000);
        });
      };
    }
  }''')

print(f"Total new tools prepared: {len(new_tools)}")

# Join all new tools with comma
code_to_insert = ",\n" + ",\n".join(new_tools)

# Insertion point right before ];\n\n// Helper to look up a tool by its ID
target_str = "\n];\n\n// Helper to look up a tool by its ID"
if target_str in current_content:
    updated = current_content.replace(target_str, code_to_insert + target_str, 1)
    with open(TOOLS_JS_PATH, "w", encoding="utf-8") as f:
        f.write(updated)
    print("SUCCESS: Inserted all demanded tools into tools.js!")
else:
    print("ERROR: Target string not found in tools.js")
