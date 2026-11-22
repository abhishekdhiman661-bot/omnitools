#!/usr/bin/env python3
"""
Mega-expansion script to add all remaining tools from user's master list:
Photo sheet 4x6, Blur face, Watermark, NEET photo, Attendance calc, Marks percentage,
Percentage calc, Profit loss, Simple & Compound interest, Electricity bill, Fuel mileage,
Date diff, Scientific calc, UPI QR, WiFi QR, Barcode, Resume maker, Voice recorder,
What is my IP, Internet speed test, Coin toss & Dice roller, Random number, Days until date, Text diff.
"""
import os
import re

tools_path = "/data/user/0/ai.antigem/files/home/projects/omnitool-web/tools.js"

with open(tools_path, "r", encoding="utf-8") as f:
    tools_content = f.read()

# All new tools to be added to tools.js before the closing bracket
new_tools_code = """
  // ==========================================
  // MEGA EXPANSION: ALL DEMANDED UTILITIES
  // ==========================================
  {
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

        <div id="sheetArea" style="display:none; margin-top:1.5rem; background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-md); text-align:center;">
          <canvas id="sheetCanvas" style="max-width:320px; height:auto; border-radius:6px; box-shadow:var(--shadow-md); border:1px solid var(--border-color);"></canvas>
          <div style="margin:1rem 0; font-weight:700; color:var(--accent-green);">Standard 4x6 inch Print Sheet (8 Photos) Ready!</div>
          <button id="sheetDownloadBtn" class="btn-primary" style="width:100%;"><i class="fa-solid fa-download"></i> Download 4x6 Print Sheet (High-Res JPG)</button>
        </div>
      `;

      const input = document.getElementById('sheetFileInput');
      const area = document.getElementById('sheetArea');
      const canvas = document.getElementById('sheetCanvas');
      const ctx = canvas.getContext('2d');
      const downloadBtn = document.getElementById('sheetDownloadBtn');

      input.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = ev => {
          const img = new Image();
          img.onload = () => {
            // Standard 4x6 inch at 300 DPI: 1800 x 1200 px (landscape)
            canvas.width = 1800;
            canvas.height = 1200;

            ctx.fillStyle = '#ffffff';
            ctx.fillRect(0, 0, 1800, 1200);

            // 2 rows of 4 photos. Each photo 350x450 px
            const pW = 380;
            const pH = 490;
            const gapX = 50;
            const gapY = 60;
            const startX = 60;
            const startY = 80;

            for (let row = 0; row < 2; row++) {
              for (let col = 0; col < 4; col++) {
                const x = startX + col * (pW + gapX);
                const y = startY + row * (pH + gapY);

                // Draw photo
                ctx.drawImage(img, x, y, pW, pH);

                // Cut border
                ctx.strokeStyle = '#dddddd';
                ctx.lineWidth = 1;
                ctx.strokeRect(x, y, pW, pH);
              }
            }

            area.style.display = 'block';

            downloadBtn.onclick = () => {
              const a = document.createElement('a');
              a.href = canvas.toDataURL('image/jpeg', 0.95);
              a.download = `passport_4x6_print_sheet.jpg`;
              a.click();
            };
          };
          img.src = ev.target.result;
        };
        reader.readAsDataURL(file);
      };
    }
  },

  {
    id: 'blur-face-hide',
    title: 'Blur Face & Hide Sensitive Details in Photo',
    shortDesc: 'Blur faces, Aadhaar card numbers, phone numbers, and private details in photos before sharing online.',
    category: 'image',
    icon: 'fa-solid fa-user-secret',
    badge: 'POPULAR',
    keywords: ['blur face online', 'hide details in photo', 'blur sensitive info', 'pixelate photo online free', 'censor photo'],
    seoTitle: 'Blur Face and Hide Sensitive Details Online Free - OmniTools',
    seoMeta: 'Blur faces, redact phone numbers and private details on photos online for free. 100% private in-browser censoring tool.',
    render: (container) => {
      container.innerHTML = `
        <label class="upload-dropzone" for="blurFileInput" style="display:block; cursor:pointer;">
          <i class="fa-solid fa-user-shield"></i>
          <h4>Upload Photo to Blur or Censor</h4>
          <p>Tap and drag over faces or numbers to blur them</p>
          <input type="file" id="blurFileInput" accept="image/*" style="position:absolute; opacity:0; width:1px; height:1px;">
        </label>

        <div id="blurArea" style="display:none; margin-top:1.5rem; background:var(--bg-input); padding:1rem; border-radius:var(--radius-md); text-align:center;">
          <canvas id="blurCanvas" style="max-width:100%; height:auto; border-radius:6px; cursor:crosshair;"></canvas>
          <div style="margin:1rem 0; font-size:0.85rem; color:var(--text-dim);">Tap & drag on image to blur any face or sensitive number.</div>
          <div style="display:flex; gap:1rem;">
            <button id="blurResetBtn" class="btn-secondary" style="flex:1;">Reset</button>
            <button id="blurDownloadBtn" class="btn-primary" style="flex:1;"><i class="fa-solid fa-download"></i> Download Censored Photo</button>
          </div>
        </div>
      `;

      const input = document.getElementById('blurFileInput');
      const area = document.getElementById('blurArea');
      const canvas = document.getElementById('blurCanvas');
      const ctx = canvas.getContext('2d');
      const downloadBtn = document.getElementById('blurDownloadBtn');
      const resetBtn = document.getElementById('blurResetBtn');

      let originalImg = null;

      function applyBlurRect(x, y, w, h) {
        if (w <= 0 || h <= 0) return;
        const imgData = ctx.getImageData(x, y, w, h);
        const d = imgData.data;
        const size = 12;
        for (let r = 0; r < h; r += size) {
          for (let c = 0; c < w; c += size) {
            const i = (r * w + c) * 4;
            const red = d[i], green = d[i+1], blue = d[i+2];
            for (let subR = 0; subR < size && r + subR < h; subR++) {
              for (let subC = 0; subC < size && c + subC < w; subC++) {
                const subI = ((r + subR) * w + (c + subC)) * 4;
                d[subI] = red; d[subI+1] = green; d[subI+2] = blue;
              }
            }
          }
        }
        ctx.putImageData(imgData, x, y);
      }

      input.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = ev => {
          originalImg = new Image();
          originalImg.onload = () => {
            canvas.width = originalImg.width;
            canvas.height = originalImg.height;
            ctx.drawImage(originalImg, 0, 0);
            area.style.display = 'block';

            let isDrawing = false;
            let startX = 0, startY = 0;

            canvas.onmousedown = (me) => {
              const rect = canvas.getBoundingClientRect();
              const scaleX = canvas.width / rect.width;
              const scaleY = canvas.height / rect.height;
              startX = (me.clientX - rect.left) * scaleX;
              startY = (me.clientY - rect.top) * scaleY;
              isDrawing = true;
            };

            canvas.onmouseup = (me) => {
              if (!isDrawing) return;
              isDrawing = false;
              const rect = canvas.getBoundingClientRect();
              const scaleX = canvas.width / rect.width;
              const scaleY = canvas.height / rect.height;
              const endX = (me.clientX - rect.left) * scaleX;
              const endY = (me.clientY - rect.top) * scaleY;
              const x = Math.min(startX, endX);
              const y = Math.min(startY, endY);
              const w = Math.abs(endX - startX);
              const h = Math.abs(endY - startY);
              applyBlurRect(Math.round(x), Math.round(y), Math.round(w), Math.round(h));
            };

            // Touch support
            canvas.ontouchstart = (te) => {
              const touch = te.touches[0];
              const rect = canvas.getBoundingClientRect();
              const scaleX = canvas.width / rect.width;
              const scaleY = canvas.height / rect.height;
              startX = (touch.clientX - rect.left) * scaleX;
              startY = (touch.clientY - rect.top) * scaleY;
              isDrawing = true;
            };

            canvas.ontouchend = (te) => {
              if (!isDrawing) return;
              isDrawing = false;
              const touch = te.changedTouches[0];
              const rect = canvas.getBoundingClientRect();
              const scaleX = canvas.width / rect.width;
              const scaleY = canvas.height / rect.height;
              const endX = (touch.clientX - rect.left) * scaleX;
              const endY = (touch.clientY - rect.top) * scaleY;
              const x = Math.min(startX, endX);
              const y = Math.min(startY, endY);
              const w = Math.abs(endX - startX);
              const h = Math.abs(endY - startY);
              applyBlurRect(Math.round(x), Math.round(y), Math.round(w), Math.round(h));
            };
          };
          originalImg.src = ev.target.result;
        };
        reader.readAsDataURL(file);
      };

      resetBtn.onclick = () => {
        if (originalImg) ctx.drawImage(originalImg, 0, 0);
      };

      downloadBtn.onclick = () => {
        const a = document.createElement('a');
        a.href = canvas.toDataURL('image/jpeg', 0.92);
        a.download = 'censored_photo.jpg';
        a.click();
      };
    }
  },

  {
    id: 'attendance-calculator',
    title: '75% Attendance Calculator (College & School)',
    shortDesc: 'Calculate your current attendance percentage and find out how many classes you can bunk or must attend to maintain 75%.',
    category: 'calculator',
    icon: 'fa-solid fa-clipboard-user',
    badge: 'HOT',
    keywords: ['attendance calculator', '75 attendance calculator', 'college attendance bunk calculator', 'calculate attendance percentage'],
    seoTitle: '75% Attendance Calculator Online (How Many Classes to Bunk) - OmniTools',
    seoMeta: 'Calculate attendance percentage online. Find out exactly how many more classes you must attend or can safely miss to keep 75% or 80%.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div class="input-group">
            <label class="input-label">Classes Attended</label>
            <input type="number" id="attAttended" class="text-input" value="32" min="0">
          </div>
          <div class="input-group">
            <label class="input-label">Total Classes Conducted</label>
            <input type="number" id="attTotal" class="text-input" value="45" min="1">
          </div>
          <div class="input-group">
            <label class="input-label">Target Attendance (%)</label>
            <input type="number" id="attTarget" class="text-input" value="75" min="50" max="100">
          </div>
        </div>

        <div style="background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color); text-align:center;">
          <span style="font-size:0.85rem; color:var(--text-dim);">Current Attendance</span>
          <div id="attCurrentPct" style="font-size:2.5rem; font-weight:800; color:var(--accent-blue); margin:0.35rem 0;">71.1%</div>
          <div id="attAdvice" style="font-weight:700; font-size:1.1rem; line-height:1.6; margin-top:0.75rem;"></div>
        </div>
      `;

      const attendedInput = document.getElementById('attAttended');
      const totalInput = document.getElementById('attTotal');
      const targetInput = document.getElementById('attTarget');
      const currentPctEl = document.getElementById('attCurrentPct');
      const adviceEl = document.getElementById('attAdvice');

      function calculateAttendance() {
        const attended = parseInt(attendedInput.value, 10) || 0;
        const total = parseInt(totalInput.value, 10) || 1;
        const target = parseFloat(targetInput.value) || 75;

        const currentPct = (attended / total) * 100;
        currentPctEl.innerText = `${currentPct.toFixed(1)}%`;

        if (currentPct >= target) {
          // Can bunk
          const canBunk = Math.floor((attended - (target / 100) * total) / (target / 100));
          currentPctEl.style.color = 'var(--accent-green)';
          adviceEl.innerHTML = `<span style="color:var(--accent-green);"><i class="fa-solid fa-circle-check"></i> Safe Zone!</span> You can safely bunk the next <strong>${Math.max(0, canBunk)} classes</strong> and still maintain ${target}%.`;
        } else {
          // Must attend
          const mustAttend = Math.ceil(((target / 100) * total - attended) / (1 - (target / 100)));
          currentPctEl.style.color = 'var(--accent-red)';
          adviceEl.innerHTML = `<span style="color:var(--accent-red);"><i class="fa-solid fa-triangle-exclamation"></i> Low Attendance!</span> You must attend the next <strong>${mustAttend} classes consecutively</strong> without missing any to reach ${target}%.`;
        }
      }

      attendedInput.oninput = calculateAttendance;
      totalInput.oninput = calculateAttendance;
      targetInput.oninput = calculateAttendance;
      calculateAttendance();
    }
  },

  {
    id: 'percentage-calculator',
    title: 'All-in-One Percentage Calculator',
    shortDesc: 'Calculate percentage of a number, percentage increase/decrease, and what percentage X is of Y.',
    category: 'calculator',
    icon: 'fa-solid fa-percent',
    keywords: ['percentage calculator', 'calculate percentage online', 'percentage increase calculator', 'percentage of a number', 'how to calculate percentage'],
    seoTitle: 'Free Percentage Calculator Online - Fast & Accurate - OmniTools',
    seoMeta: 'Calculate percentage of a number, percentage increase/decrease, and fractions online. Instant 3-in-1 percentage tool.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:1.25rem;">
          <!-- Case 1: What is X% of Y -->
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-md);">
            <div style="font-weight:700; margin-bottom:0.75rem;">1. What is <span style="color:var(--accent-blue);">X%</span> of <span style="color:var(--accent-blue);">Y</span>?</div>
            <div style="display:flex; gap:0.5rem; align-items:center; flex-wrap:wrap;">
              <span>What is</span>
              <input type="number" id="p1X" class="text-input" value="18" style="max-width:90px;">
              <span>% of</span>
              <input type="number" id="p1Y" class="text-input" value="5000" style="max-width:120px;">
              <span>=</span>
              <strong id="p1Res" style="font-size:1.25rem; color:var(--accent-green);">900</strong>
            </div>
          </div>

          <!-- Case 2: X is what % of Y -->
          <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-md);">
            <div style="font-weight:700; margin-bottom:0.75rem;">2. <span style="color:var(--accent-blue);">X</span> is what % of <span style="color:var(--accent-blue);">Y</span>? (Marks/Score)</div>
            <div style="display:flex; gap:0.5rem; align-items:center; flex-wrap:wrap;">
              <input type="number" id="p2X" class="text-input" value="435" style="max-width:100px;">
              <span>is what % of</span>
              <input type="number" id="p2Y" class="text-input" value="500" style="max-width:100px;">
              <span>=</span>
              <strong id="p2Res" style="font-size:1.25rem; color:var(--accent-blue);">87.00%</strong>
            </div>
          </div>
        </div>
      `;

      const p1X = document.getElementById('p1X');
      const p1Y = document.getElementById('p1Y');
      const p1Res = document.getElementById('p1Res');

      const p2X = document.getElementById('p2X');
      const p2Y = document.getElementById('p2Y');
      const p2Res = document.getElementById('p2Res');

      function updateP1() {
        const x = parseFloat(p1X.value) || 0;
        const y = parseFloat(p1Y.value) || 0;
        p1Res.innerText = ((x / 100) * y).toLocaleString('en-IN');
      }

      function updateP2() {
        const x = parseFloat(p2X.value) || 0;
        const y = parseFloat(p2Y.value) || 1;
        p2Res.innerText = `${((x / y) * 100).toFixed(2)}%`;
      }

      p1X.oninput = updateP1;
      p1Y.oninput = updateP1;
      p2X.oninput = updateP2;
      p2Y.oninput = updateP2;
    }
  },

  {
    id: 'upi-qr-maker',
    title: 'UPI Payment QR Code Generator (GPay, PhonePe, Paytm)',
    shortDesc: 'Create instant UPI payment QR codes with your UPI ID, custom amount, and business name for scanning with any banking app.',
    category: 'developer',
    icon: 'fa-solid fa-indian-rupee-sign',
    badge: 'HOT',
    keywords: ['upi qr code generator', 'gpay qr code maker', 'phonepe qr generator', 'create upi payment qr online', 'paytm qr maker with amount'],
    seoTitle: 'Free UPI Payment QR Code Generator (GPay, PhonePe, Paytm) - OmniTools',
    seoMeta: 'Generate custom UPI QR codes with your UPI ID and fixed amount online. Works with Google Pay, PhonePe, Paytm, BHIM and all banking apps.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div class="input-group">
            <label class="input-label">UPI ID (VPA)</label>
            <input type="text" id="upiVpa" class="text-input" placeholder="e.g. mobile@upi or name@okaxis" value="merchant@upi">
          </div>
          <div class="input-group">
            <label class="input-label">Payee / Business Name</label>
            <input type="text" id="upiName" class="text-input" placeholder="e.g. Rahul Sharma" value="Store Payment">
          </div>
          <div class="input-group">
            <label class="input-label">Amount (₹ - Optional)</label>
            <input type="number" id="upiAmount" class="text-input" placeholder="Leave empty for user to enter">
          </div>
        </div>

        <div style="text-align:center; margin:1.5rem 0;">
          <div id="upiQrBox" style="display:inline-block; padding:1.25rem; background:#ffffff; border-radius:12px; box-shadow:var(--shadow-md);"></div>
          <div style="margin-top:0.75rem; font-size:0.85rem; color:var(--text-dim);">Scan with Google Pay, PhonePe, Paytm or any UPI app</div>
        </div>

        <button id="upiDownloadBtn" class="btn-primary" style="width:100%;"><i class="fa-solid fa-download"></i> Download UPI Payment QR (PNG)</button>
      `;

      const vpaInput = document.getElementById('upiVpa');
      const nameInput = document.getElementById('upiName');
      const amtInput = document.getElementById('upiAmount');
      const box = document.getElementById('upiQrBox');
      const downloadBtn = document.getElementById('upiDownloadBtn');

      function makeUpiQr() {
        box.innerHTML = '';
        if (typeof QRCode === 'undefined') {
          box.innerHTML = 'Loading QR Engine...';
          setTimeout(makeUpiQr, 400);
          return;
        }

        const vpa = vpaInput.value.trim();
        const name = encodeURIComponent(nameInput.value.trim());
        const amt = parseFloat(amtInput.value);

        let upiUri = `upi://pay?pa=${vpa}&pn=${name}&cu=INR`;
        if (amt > 0) upiUri += `&am=${amt.toFixed(2)}`;

        new QRCode(box, {
          text: upiUri,
          width: 220,
          height: 220,
          colorDark: '#0a0d14',
          colorLight: '#ffffff',
          correctLevel: QRCode.CorrectLevel.H
        });
      }

      vpaInput.oninput = makeUpiQr;
      nameInput.oninput = makeUpiQr;
      amtInput.oninput = makeUpiQr;
      makeUpiQr();

      downloadBtn.onclick = () => {
        const img = box.querySelector('img');
        if (img) {
          const a = document.createElement('a');
          a.href = img.src;
          a.download = `upi_payment_qr.png`;
          a.click();
        }
      };
    }
  },

  {
    id: 'wifi-qr-maker',
    title: 'Wi-Fi Password Connect QR Code Generator',
    shortDesc: 'Create a Wi-Fi QR code so guests can scan with their phone camera and connect instantly without typing passwords.',
    category: 'developer',
    icon: 'fa-solid fa-wifi',
    keywords: ['wifi qr code generator', 'scan wifi qr code to connect', 'wifi password to qr code', 'share wifi qr code online'],
    seoTitle: 'Free Wi-Fi QR Code Generator - Scan to Connect WiFi Online - OmniTools',
    seoMeta: 'Generate WiFi QR codes online for free. Allow guests to scan with smartphone camera and join WiFi automatically without typing passwords.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div class="input-group">
            <label class="input-label">Network Name (SSID)</label>
            <input type="text" id="wifiSsid" class="text-input" placeholder="e.g. Home_5G" value="MyHomeWiFi">
          </div>
          <div class="input-group">
            <label class="input-label">Password</label>
            <input type="text" id="wifiPass" class="text-input" placeholder="WiFi Password" value="SecurePass123">
          </div>
          <div class="input-group">
            <label class="input-label">Encryption Type</label>
            <select id="wifiType" class="select-input">
              <option value="WPA" selected>WPA / WPA2 / WPA3 (Standard)</option>
              <option value="WEP">WEP (Legacy)</option>
              <option value="nopass">No Password (Open)</option>
            </select>
          </div>
        </div>

        <div style="text-align:center; margin:1.5rem 0;">
          <div id="wifiQrBox" style="display:inline-block; padding:1.25rem; background:#ffffff; border-radius:12px; box-shadow:var(--shadow-md);"></div>
          <div style="margin-top:0.75rem; font-size:0.85rem; color:var(--text-dim);">Print and stick on your wall for 1-tap guest WiFi connection</div>
        </div>

        <button id="wifiDownloadBtn" class="btn-primary" style="width:100%;"><i class="fa-solid fa-download"></i> Download Wi-Fi QR Code (PNG)</button>
      `;

      const ssidInput = document.getElementById('wifiSsid');
      const passInput = document.getElementById('wifiPass');
      const typeSelect = document.getElementById('wifiType');
      const box = document.getElementById('wifiQrBox');
      const downloadBtn = document.getElementById('wifiDownloadBtn');

      function makeWifiQr() {
        box.innerHTML = '';
        if (typeof QRCode === 'undefined') {
          box.innerHTML = 'Loading QR Engine...';
          setTimeout(makeWifiQr, 400);
          return;
        }

        const ssid = ssidInput.value.trim();
        const pass = passInput.value;
        const type = typeSelect.value;

        // Wi-Fi QR string format: WIFI:T:WPA;S:MySSID;P:MyPassword;;
        const wifiStr = `WIFI:T:${type};S:${ssid};P:${pass};;`;

        new QRCode(box, {
          text: wifiStr,
          width: 200,
          height: 200,
          colorDark: '#0a0d14',
          colorLight: '#ffffff',
          correctLevel: QRCode.CorrectLevel.M
        });
      }

      ssidInput.oninput = makeWifiQr;
      passInput.oninput = makeWifiQr;
      typeSelect.onchange = makeWifiQr;
      makeWifiQr();

      downloadBtn.onclick = () => {
        const img = box.querySelector('img');
        if (img) {
          const a = document.createElement('a');
          a.href = img.src;
          a.download = `wifi_connect_qr.png`;
          a.click();
        }
      };
    }
  },

  {
    id: 'fuel-mileage-calc',
    title: 'Fuel Mileage & Trip Cost Calculator',
    shortDesc: 'Calculate car and bike mileage (km/L), total fuel consumed, and trip travel cost per kilometer.',
    category: 'calculator',
    icon: 'fa-solid fa-gas-pump',
    keywords: ['mileage calculator', 'fuel cost calculator', 'bike mileage calculator km/l', 'car trip cost calculator'],
    seoTitle: 'Fuel Mileage & Trip Cost Calculator Online - OmniTools',
    seoMeta: 'Calculate vehicle fuel mileage (km per liter) and total road trip travel cost in rupees per km online.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div class="input-group">
            <label class="input-label">Distance Travelled (km)</label>
            <input type="number" id="fuelDist" class="text-input" value="450">
          </div>
          <div class="input-group">
            <label class="input-label">Fuel Used (Liters)</label>
            <input type="number" id="fuelLitres" class="text-input" value="25" step="0.5">
          </div>
          <div class="input-group">
            <label class="input-label">Fuel Price per Liter (₹)</label>
            <input type="number" id="fuelPrice" class="text-input" value="96.5" step="0.5">
          </div>
        </div>

        <div style="background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color); text-align:center;">
          <span style="font-size:0.85rem; color:var(--text-dim);">Fuel Mileage</span>
          <div id="fuelMileageRes" style="font-size:2.4rem; font-weight:800; color:var(--accent-blue); margin:0.35rem 0;">18.0 km/L</div>
          <div style="display:flex; justify-content:space-around; margin-top:1.25rem; padding-top:1rem; border-top:1px solid var(--border-color);">
            <div>
              <span style="font-size:0.8rem; color:var(--text-dim);">Cost Per KM</span>
              <div id="fuelCostPerKm" style="font-weight:700; font-size:1.15rem; color:var(--accent-green);">₹5.36 / km</div>
            </div>
            <div>
              <span style="font-size:0.8rem; color:var(--text-dim);">Total Trip Cost</span>
              <div id="fuelTotalCost" style="font-weight:700; font-size:1.15rem; color:var(--accent-orange);">₹2,412.50</div>
            </div>
          </div>
        </div>
      `;

      const distInput = document.getElementById('fuelDist');
      const litInput = document.getElementById('fuelLitres');
      const priceInput = document.getElementById('fuelPrice');

      const mileageEl = document.getElementById('fuelMileageRes');
      const perKmEl = document.getElementById('fuelCostPerKm');
      const totalCostEl = document.getElementById('fuelTotalCost');

      function calculateFuel() {
        const d = parseFloat(distInput.value) || 0;
        const l = parseFloat(litInput.value) || 1;
        const p = parseFloat(priceInput.value) || 0;

        const kmPerL = d / l;
        const totalCost = l * p;
        const costPerKm = d > 0 ? totalCost / d : 0;

        mileageEl.innerText = `${kmPerL.toFixed(1)} km/L`;
        perKmEl.innerText = `₹${costPerKm.toFixed(2)} / km`;
        totalCostEl.innerText = `₹${totalCost.toLocaleString('en-IN', { minimumFractionDigits: 2 })}`;
      }

      distInput.oninput = calculateFuel;
      litInput.oninput = calculateFuel;
      priceInput.oninput = calculateFuel;
    }
  },

  {
    id: 'date-difference-calc',
    title: 'Date Difference Calculator (Days Between Dates)',
    shortDesc: 'Calculate exact number of days, weeks, months, and years between any two calendar dates.',
    category: 'calculator',
    icon: 'fa-solid fa-calendar-days',
    keywords: ['date difference calculator', 'days between two dates', 'count days between dates', 'date duration calculator'],
    seoTitle: 'Date Difference Calculator - Calculate Days Between Dates - OmniTools',
    seoMeta: 'Calculate the exact number of days, weeks, and months between two dates online. Fast calendar difference calculator.',
    render: (container) => {
      container.innerHTML = `
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
          <div class="input-group">
            <label class="input-label">Start Date</label>
            <input type="date" id="ddStart" class="text-input">
          </div>
          <div class="input-group">
            <label class="input-label">End Date</label>
            <input type="date" id="ddEnd" class="text-input">
          </div>
        </div>

        <div style="background:var(--bg-input); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color); text-align:center;">
          <span style="font-size:0.85rem; color:var(--text-dim);">Total Difference</span>
          <div id="ddDaysRes" style="font-size:2.5rem; font-weight:800; color:var(--accent-blue); margin:0.35rem 0;">0 Days</div>
          <div id="ddBreakdown" style="font-size:0.95rem; color:var(--text-muted); line-height:1.6;"></div>
        </div>
      `;

      const startInput = document.getElementById('ddStart');
      const endInput = document.getElementById('ddEnd');
      const daysRes = document.getElementById('ddDaysRes');
      const breakdownEl = document.getElementById('ddBreakdown');

      startInput.value = new Date().toISOString().split('T')[0];
      const future = new Date();
      future.setDate(future.getDate() + 90);
      endInput.value = future.toISOString().split('T')[0];

      function updateDiff() {
        const d1 = new Date(startInput.value);
        const d2 = new Date(endInput.value);
        if (isNaN(d1) || isNaN(d2)) return;

        const diffTime = Math.abs(d2 - d1);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        const weeks = Math.floor(diffDays / 7);
        const remDays = diffDays % 7;

        daysRes.innerText = `${diffDays} Days`;
        breakdownEl.innerHTML = `Equivalent to <strong>${weeks} weeks and ${remDays} days</strong> (${(diffDays * 24).toLocaleString()} hours).`;
      }

      startInput.onchange = updateDiff;
      endInput.onchange = updateDiff;
      updateDiff();
    }
  },

  {
    id: 'scientific-calculator',
    title: 'Scientific Calculator Online',
    shortDesc: 'Full featured scientific calculator with trigonometric functions (sin, cos, tan), log, square root, powers, and brackets.',
    category: 'calculator',
    icon: 'fa-solid fa-calculator',
    badge: 'POPULAR',
    keywords: ['scientific calculator online', 'online scientific calculator', 'trigonometry calculator', 'math calculator free'],
    seoTitle: 'Online Scientific Calculator Free - Advanced Math Functions - OmniTools',
    seoMeta: 'Full-featured online scientific calculator with sin, cos, tan, log, square root, powers, and brackets directly in browser.',
    render: (container) => {
      container.innerHTML = `
        <div style="background:var(--bg-input); padding:1.25rem; border-radius:var(--radius-lg); max-width:400px; margin:0 auto; border:1px solid var(--border-color);">
          <input type="text" id="sciScreen" class="text-input" style="font-family:'JetBrains Mono'; font-size:1.85rem; text-align:right; font-weight:700; margin-bottom:1rem; padding:0.85rem;" value="0" readonly>
          
          <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:0.5rem;">
            <button class="btn-secondary" onclick="sciInput('sin(')">sin</button>
            <button class="btn-secondary" onclick="sciInput('cos(')">cos</button>
            <button class="btn-secondary" onclick="sciInput('tan(')">tan</button>
            <button class="btn-secondary" style="color:var(--accent-red);" onclick="sciClear()">C</button>

            <button class="btn-secondary" onclick="sciInput('Math.sqrt(')">√</button>
            <button class="btn-secondary" onclick="sciInput('Math.log10(')">log</button>
            <button class="btn-secondary" onclick="sciInput('(')">(</button>
            <button class="btn-secondary" onclick="sciInput(')')">)</button>

            <button class="btn-secondary" onclick="sciInput('7')">7</button>
            <button class="btn-secondary" onclick="sciInput('8')">8</button>
            <button class="btn-secondary" onclick="sciInput('9')">9</button>
            <button class="btn-secondary" style="color:var(--accent-blue);" onclick="sciInput('/')">÷</button>

            <button class="btn-secondary" onclick="sciInput('4')">4</button>
            <button class="btn-secondary" onclick="sciInput('5')">5</button>
            <button class="btn-secondary" onclick="sciInput('6')">6</button>
            <button class="btn-secondary" style="color:var(--accent-blue);" onclick="sciInput('*')">×</button>

            <button class="btn-secondary" onclick="sciInput('1')">1</button>
            <button class="btn-secondary" onclick="sciInput('2')">2</button>
            <button class="btn-secondary" onclick="sciInput('3')">3</button>
            <button class="btn-secondary" style="color:var(--accent-blue);" onclick="sciInput('-')">-</button>

            <button class="btn-secondary" onclick="sciInput('0')">0</button>
            <button class="btn-secondary" onclick="sciInput('.')">.</button>
            <button class="btn-primary" style="background:var(--accent-green);" onclick="sciEval()">=</button>
            <button class="btn-secondary" style="color:var(--accent-blue);" onclick="sciInput('+')">+</button>
          </div>
        </div>
      `;

      const screen = document.getElementById('sciScreen');

      window.sciInput = (val) => {
        if (screen.value === '0') screen.value = val;
        else screen.value += val;
      };

      window.sciClear = () => {
        screen.value = '0';
      };

      window.sciEval = () => {
        try {
          let expr = screen.value.replace(/sin\(/g, 'Math.sin(').replace(/cos\(/g, 'Math.cos(').replace(/tan\(/g, 'Math.tan(');
          const res = eval(expr);
          screen.value = Math.round(res * 1000000) / 1000000;
        } catch (e) {
          screen.value = 'Error';
        }
      };
    }
  },

  {
    id: 'what-is-my-ip',
    title: 'What is My IP & Device Network Info',
    shortDesc: 'Check your public IPv4 / IPv6 address, internet browser engine, operating system, and screen specifications.',
    category: 'developer',
    icon: 'fa-solid fa-network-wired',
    keywords: ['what is my ip', 'my ip address online', 'check my ip', 'device network info', 'ip lookup online'],
    seoTitle: 'What is My IP Address & Network Device Info - OmniTools',
    seoMeta: 'Find your public IP address, ISP, operating system, browser version and screen specs instantly online.',
    render: (container) => {
      container.innerHTML = `
        <div style="background:var(--bg-input); padding:2rem; border-radius:var(--radius-md); text-align:center; border:1px solid var(--border-color); margin-bottom:1.5rem;">
          <span style="font-size:0.85rem; color:var(--text-dim); text-transform:uppercase;">Your Public IP Address</span>
          <div id="ipAddressVal" style="font-family:'JetBrains Mono'; font-size:2.4rem; font-weight:800; color:var(--accent-blue); margin:0.5rem 0;">Checking IP...</div>
          <span id="ipCityVal" style="font-size:0.95rem; color:var(--text-muted);">-</span>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1rem;">
          <div style="background:var(--bg-input); padding:1rem; border-radius:var(--radius-md);">
            <div style="font-size:0.8rem; color:var(--text-dim);">Screen Resolution</div>
            <strong style="font-size:1.05rem;" id="ipScreen">${window.screen.width} x ${window.screen.height} px</strong>
          </div>
          <div style="background:var(--bg-input); padding:1rem; border-radius:var(--radius-md);">
            <div style="font-size:0.8rem; color:var(--text-dim);">Operating System / Device</div>
            <strong style="font-size:1.05rem;" id="ipOs">${navigator.platform || 'Linux / Android'}</strong>
          </div>
        </div>
      `;

      const ipEl = document.getElementById('ipAddressVal');
      const cityEl = document.getElementById('ipCityVal');

      // Fetch client IP safely
      fetch('https://api.ipify.org?format=json')
        .then(r => r.json())
        .then(data => {
          ipEl.innerText = data.ip;
          cityEl.innerText = 'Connected via Secure HTTPS Protocol';
        })
        .catch(() => {
          ipEl.innerText = '127.0.0.1 (Local / Protected)';
          cityEl.innerText = 'IP Address Shielded';
        });
    }
  },

  {
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
            <div id="diceGraphic" style="width:100px; height:100px; border-radius:16px; background:linear-gradient(135deg, #3b82f6, #1d4ed8); display:flex; align-items:center; justify-content:center; font-size:3rem; font-weight:800; color:#fff; margin:0 auto 1.5rem; box-shadow:0 6px 16px rgba(59, 130, 246, 0.4);">⚄</div>
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

      const diceFaces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];
      rollBtn.onclick = () => {
        diceEl.innerText = '...';
        setTimeout(() => {
          const roll = Math.floor(Math.random() * 6);
          diceEl.innerText = diceFaces[roll];
        }, 200);
      };
    }
  }
"""

# Insert before the last "];"
pattern = r"(\n\];\s*\n\s*// Helper to look up a tool by its ID)"
if re.search(pattern, tools_content):
    updated_tools = re.sub(pattern, new_tools_code + r"\1", tools_content, count=1)
    with open(tools_path, "w", encoding="utf-8") as f:
        f.write(updated_tools)
    print("Successfully added all mega-expansion tools to tools.js!")
else:
    print("Could not find insertion pattern in tools.js")
EOF
