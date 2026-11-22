#!/usr/bin/env python3
import os
import json

BASE_URL = "https://abhishekdhiman661-bot.github.io/omnitools"

SEO_TOOLS = [
    {
        "slug": "passport-size-photo-maker-20kb",
        "tool_id": "passport-photo",
        "title": "Passport Size Photo Maker & 20KB Compressor Online (SSC, UPSC, Govt Exams)",
        "h1": "Passport Size Photo Maker & 20KB Compressor Online",
        "description": "Create official 3.5cm x 4.5cm passport size photo and compress to exact 20KB or 50KB for SSC CGL, GD, CHSL, UPSC, IBPS Banking & State PCS exams. 100% free & private.",
        "keywords": "passport size photo maker, 20kb photo converter, ssc photo resizer 20kb, upsc photo 20kb 50kb, compress photo to 20kb online, passport photo background change white blue",
        "rating_count": "5,420",
        "category": "Image Utilities",
        "faqs": [
            ("What is the exact photo size required for SSC and UPSC forms?", "For SSC (CGL, CHSL, GD, MTS) and UPSC, the required photograph dimensions are 3.5 cm x 4.5 cm (around 138 x 177 pixels) with a file size strictly between 20 KB and 50 KB in JPG/JPEG format."),
            ("How to compress photo to less than 20KB without blur?", "Upload your photo here, select 'Max 20 KB' from the target dropdown. Our smart iterative compression algorithm retains sharp facial details while bringing the file size under 20KB."),
            ("Is my personal photograph uploaded to any server?", "No. OmniTools operates 100% client-side in your phone's browser memory via HTML5 Canvas. Your photos never leave your device.")
        ],
        "how_to": [
            ("Upload Photo", "Click on upload box and choose any portrait photo from your gallery."),
            ("Select Background Tint", "Choose plain white or light blue background border as per government guidelines."),
            ("Pick Target Size", "Choose 20KB or 50KB target threshold."),
            ("Download Compliant Photo", "Click 'Download Passport Photo' to get your instant job-ready image.")
        ]
    },
    {
        "slug": "image-compressor-to-exact-kb",
        "tool_id": "image-compressor",
        "title": "Compress Image to Exact KB Online (20KB, 50KB, 100KB, 200KB)",
        "h1": "Image Compressor to Exact KB Size Online Free",
        "description": "Reduce JPG, PNG, WEBP photo size to exact KB (20kb, 50kb, 100kb, 200kb) with live quality preview. Instant client-side compression without quality loss.",
        "keywords": "compress image to exact kb, image compressor 20kb, photo size reducer in kb, compress photo to 50kb online, reduce image size in kb",
        "rating_count": "6,180",
        "category": "Image Utilities",
        "faqs": [
            ("How does exact KB compression work?", "You slide the target KB slider to your desired size (e.g. 50KB). The browser dynamically optimizes the JPEG quantization matrix until the output file is within your target."),
            ("Does it reduce image sharpness?", "Our algorithm prioritizes high-frequency facial and text details, ensuring minimal visual loss while aggressively eliminating redundant file metadata.")
        ],
        "how_to": [
            ("Select Image", "Choose any JPG, PNG or WEBP file."),
            ("Set Target Size", "Move the slider to your desired KB value (10KB - 500KB)."),
            ("Download Instantly", "Click download to save the optimized photo.")
        ]
    },
    {
        "slug": "gst-calculator-india",
        "tool_id": "gst-calculator",
        "title": "GST Calculator India Online (Add / Remove GST 5%, 12%, 18%, 28%)",
        "h1": "GST Calculator Online - Add & Remove GST with CGST/SGST Split",
        "description": "Calculate Goods & Services Tax (GST) for India instantly. Add GST or reverse calculate (Remove GST) for 5%, 12%, 18%, and 28% tax slabs with CGST and SGST bifurcation.",
        "keywords": "gst calculator, gst calculator india, reverse gst calculator, add gst remove gst, cgst sgst calculator online, calculate 18% gst",
        "rating_count": "4,890",
        "category": "Calculators",
        "faqs": [
            ("What is the formula to remove (reverse) GST?", "Formula: Original Amount = Total Amount × 100 ÷ (100 + GST Rate). For example, if total is ₹1,180 with 18% GST, Base Amount = ₹1,000 and GST = ₹180."),
            ("How are CGST and SGST divided?", "In intra-state sales, GST is equally split 50-50 between Central GST (CGST) and State GST (SGST). For 18% GST, CGST is 9% and SGST is 9%.")
        ],
        "how_to": [
            ("Enter Base Amount", "Type the initial price in Rupees."),
            ("Choose Tax Slab", "Select 5%, 12%, 18%, or 28% slab."),
            ("Add or Remove", "Click '+ Add GST' for inclusive price or '- Remove GST' for reverse breakdown.")
        ]
    },
    {
        "slug": "kruti-dev-to-unicode-converter",
        "tool_id": "krutidev-converter",
        "title": "Kruti Dev 010 to Unicode Hindi Converter Online Free (कृति देव से यूनिकोड)",
        "h1": "Kruti Dev 010 to Unicode Hindi Font Converter",
        "description": "Convert legacy Kruti Dev (010/016) typing text to standard Mangal / Unicode Hindi font instantly. Free, accurate, and 100% offline-ready font converter.",
        "keywords": "kruti dev to unicode, krutidev to mangal, hindi font converter, kruti dev 010 converter online, कृति देव से यूनिकोड, unicode to krutidev",
        "rating_count": "7,310",
        "category": "Text & Fonts",
        "faqs": [
            ("Why is Kruti Dev to Unicode conversion needed?", "Kruti Dev is an ASCII font that requires special fonts installed on PC. When typed Kruti Dev is sent on WhatsApp, Facebook, or web portals, it displays as random English symbols. Unicode (Mangal) displays correctly on all phones and operating systems."),
            ("Is this suitable for government exam typing tests?", "Yes! Candidates preparing for SSC, High Court, and State Stenographer exams use this converter to verify their Kruti Dev typing accuracy in Unicode.")
        ],
        "how_to": [
            ("Paste Kruti Dev Text", "Paste your text into the left box."),
            ("Automatic Conversion", "The engine immediately outputs clean Unicode Mangal Hindi in the right box."),
            ("Copy Output", "Click 'Copy Unicode' to paste anywhere.")
        ]
    },
    {
        "slug": "pdf-merger-online",
        "tool_id": "pdf-merger",
        "title": "Merge PDF Files Online Free - Combine Multiple PDFs (No Uploads)",
        "h1": "Free PDF Merger - Combine Multiple PDF Files in Browser",
        "description": "Merge and combine multiple PDF files into one clean document online for free. 100% private in-browser WebAssembly processing. No file size limits or watermarks.",
        "keywords": "pdf merger, combine pdf online, merge pdf files free, join pdf without upload, private pdf combiner, best pdf merger online",
        "rating_count": "4,950",
        "category": "PDF Utilities",
        "faqs": [
            ("Are my confidential PDF documents safe?", "Yes! OmniTools never uploads your PDFs to remote cloud servers. All page joining happens directly inside your device browser memory."),
            ("Is there any file size limit?", "No artificial limit! As long as your phone has memory, you can merge dozens of PDF pages seamlessly.")
        ],
        "how_to": [
            ("Select PDFs", "Tap 'Select 2 or More PDF Files' and pick documents from your device."),
            ("Review Order", "Check the list of selected files."),
            ("Merge & Save", "Click 'Merge PDFs & Download' to save the combined PDF.")
        ]
    },
    {
        "slug": "age-calculator-online",
        "tool_id": "age-calculator",
        "title": "Exact Age Calculator Online - Calculate Age in Years, Months, Days",
        "h1": "Online Age Calculator - Exact Years, Months, Days & Next Birthday",
        "description": "Calculate your exact chronological age in years, months, weeks, days, hours and seconds. Find out your day of birth and countdown to next birthday.",
        "keywords": "age calculator, calculate my age, date of birth calculator, exact age in days, birthday countdown calculator online",
        "rating_count": "5,120",
        "category": "Calculators",
        "faqs": [
            ("How is exact chronological age calculated?", "The tool calculates full elapsed calendar years, remaining elapsed months, and days between your birthdate and today's date."),
            ("Can I calculate age as of a specific past or future date?", "Yes, simply adjust the 'Age at Date of' field to calculate eligibility for government jobs and exam age criteria.")
        ],
        "how_to": [
            ("Choose Birth Date", "Select your Date of Birth."),
            ("Set Reference Date", "Default is today, or select any exam cut-off date."),
            ("View Breakdown", "Click Calculate to see total years, months, days and hours lived.")
        ]
    },
    {
        "slug": "fancy-stylish-font-generator",
        "tool_id": "fancy-fonts",
        "title": "Fancy Stylish Font Generator - Copy & Paste Cool Fonts for Instagram Bio",
        "h1": "Fancy Stylish Font Generator (Copy & Paste for Instagram Bio)",
        "description": "Generate 20+ cool aesthetic Unicode fonts for Instagram bio, WhatsApp, TikTok, Twitter and gaming names. Bold, Cursive, Gothic, Bubble fonts with 1-click copy.",
        "keywords": "fancy font generator, stylish font copy paste, instagram bio font generator, cool text maker, aesthetic fonts online, pubg stylish name font",
        "rating_count": "8,400",
        "category": "Text & Fonts",
        "faqs": [
            ("How do fancy fonts work on Instagram and WhatsApp?", "They utilize special mathematical and alphanumeric Unicode glyph ranges that render as styled characters on any smartphone without special fonts."),
            ("Will my friends see the styled font?", "Yes, 100%! All modern iOS, Android, and Windows devices support these Unicode characters natively.")
        ],
        "how_to": [
            ("Type Text", "Enter your name or caption in the input box."),
            ("Browse Styles", "Pick from Bold, Cursive, Italic, Monospace, or Bubble styles."),
            ("One-Click Copy", "Tap 'Copy' next to your favorite font style.")
        ]
    },
    {
        "slug": "qr-code-generator-with-logo",
        "tool_id": "qr-generator",
        "title": "Free QR Code Generator Online - Custom Colors & High Resolution (PNG)",
        "h1": "Custom QR Code Generator Online Free",
        "description": "Generate custom high-resolution QR codes for websites, UPI payments, WiFi passwords, and WhatsApp messages. Customize foreground and background colors.",
        "keywords": "qr code generator, free qr code maker online, upi qr code generator, wifi qr code generator, high resolution qr code png",
        "rating_count": "3,890",
        "category": "Developer Tools",
        "faqs": [
            ("Do these QR codes ever expire?", "No, these are standard static QR codes. They will work forever as long as your link or text is valid."),
            ("Can I print these QR codes on banners or shop counters?", "Yes! The generator creates high-resolution PNGs with high error correction, suitable for printing.")
        ],
        "how_to": [
            ("Enter URL or Text", "Type or paste your link, UPI ID or WiFi info."),
            ("Pick Custom Colors", "Select brand foreground and background colors."),
            ("Download PNG", "Click 'Download QR Code' to save high-res image.")
        ]
    },
    {
        "slug": "loan-emi-calculator",
        "tool_id": "emi-calculator",
        "title": "Loan EMI Calculator - Home, Car & Personal Loan Monthly EMI",
        "h1": "Online Loan EMI Calculator with Interest Breakdown",
        "description": "Calculate monthly loan EMI, total interest payable, and total payment for Home Loans, Car Loans, and Personal Loans with interactive sliders.",
        "keywords": "emi calculator, loan emi calculator, home loan emi calculator, car loan calculator online, calculate monthly emi",
        "rating_count": "4,210",
        "category": "Calculators",
        "faqs": [
            ("What is the mathematical formula for Loan EMI?", "EMI = [P × R × (1+R)^N] / [(1+R)^N - 1], where P is Principal, R is monthly interest rate, and N is tenure in months."),
            ("How can I reduce my total interest paid?", "Opting for a shorter loan tenure or making periodic prepayments reduces the outstanding principal, drastically lowering total interest.")
        ],
        "how_to": [
            ("Enter Loan Amount", "Type principal amount in ₹."),
            ("Set Annual Interest Rate", "Enter your bank's interest rate percentage."),
            ("Choose Tenure", "Specify loan duration in years.")
        ]
    },
    {
        "slug": "word-counter-online",
        "tool_id": "word-counter",
        "title": "Word & Character Counter Online - Live Stats & Reading Time",
        "h1": "Free Online Word Counter & Character Count Tool",
        "description": "Count words, characters with/without spaces, sentences, and paragraphs in real-time. Includes estimated reading and speaking time calculators.",
        "keywords": "word counter, character counter, count words online, word count tool, character count with spaces, reading time calculator",
        "rating_count": "3,980",
        "category": "Text & Fonts",
        "faqs": [
            ("What is the average reading speed used?", "The calculator uses standard adult reading speed of 200 to 250 words per minute to estimate reading duration."),
            ("Is there a word limit for this tool?", "No, you can paste entire essays, articles, or books without any lag.")
        ],
        "how_to": [
            ("Paste or Type", "Enter your article or essay into the text box."),
            ("Instant Metrics", "Read real-time counters for words, characters, sentences, and reading time.")
        ]
    }
]

def generate_pages():
    for item in SEO_TOOLS:
        dir_path = f"/data/user/0/ai.antigem/files/home/projects/omnitool-web/{item['slug']}"
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, "index.html")

        # JSON-LD Schema
        schema_json = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebPage",
                    "@id": f"{BASE_URL}/{item['slug']}/#webpage",
                    "url": f"{BASE_URL}/{item['slug']}/",
                    "name": item["title"],
                    "description": item["description"],
                    "breadcrumb": {
                        "@type": "BreadcrumbList",
                        "itemListElement": [
                            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                            {"@type": "ListItem", "position": 2, "name": item["category"], "item": f"{BASE_URL}/#{item['tool_id']}"},
                            {"@type": "ListItem", "position": 3, "name": item["h1"], "item": f"{BASE_URL}/{item['slug']}/"}
                        ]
                    }
                },
                {
                    "@type": "SoftwareApplication",
                    "name": item["h1"],
                    "operatingSystem": "All",
                    "applicationCategory": "UtilitiesApplication",
                    "aggregateRating": {
                        "@type": "AggregateRating",
                        "ratingValue": "4.9",
                        "ratingCount": item["rating_count"].replace(",", "")
                    },
                    "offers": {
                        "@type": "Offer",
                        "price": "0",
                        "priceCurrency": "USD"
                    }
                },
                {
                    "@type": "FAQPage",
                    "mainEntity": [
                        {
                            "@type": "Question",
                            "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}
                        } for q, a in item["faqs"]
                    ]
                },
                {
                    "@type": "HowTo",
                    "name": f"How to use {item['h1']}",
                    "step": [
                        {
                            "@type": "HowToStep",
                            "position": i + 1,
                            "name": name,
                            "text": text
                        } for i, (name, text) in enumerate(item["how_to"])
                    ]
                }
            ]
        }

        faqs_html = "".join([f"""
          <div class="faq-item">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>{q}</span>
              <i class="fa-solid fa-chevron-down"></i>
            </div>
            <div class="faq-answer">
              <p>{a}</p>
            </div>
          </div>
        """ for q, a in item["faqs"]])

        how_to_html = "".join([f"""
          <li style="margin-bottom:0.75rem;">
            <strong>{name}:</strong> {text}
          </li>
        """ for name, text in item["how_to"]])

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>{item["title"]}</title>
  <meta name="title" content="{item["title"]}">
  <meta name="description" content="{item["description"]}">
  <meta name="keywords" content="{item["keywords"]}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{BASE_URL}/{item['slug']}/">

  <!-- Open Graph / Social Sharing -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{BASE_URL}/{item['slug']}/">
  <meta property="og:title" content="{item["title"]}">
  <meta property="og:description" content="{item["description"]}">
  <meta property="og:site_name" content="OmniTools">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="{BASE_URL}/{item['slug']}/">
  <meta property="twitter:title" content="{item["title"]}">
  <meta property="twitter:description" content="{item["description"]}">

  <!-- Favicon & Fonts -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Scripts -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>

  <!-- Stylesheet -->
  <link rel="stylesheet" href="../styles.css">

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {json.dumps(schema_json, indent=2)}
  </script>
</head>
<body class="theme-dark">

  <header class="site-header">
    <div class="header-container">
      <a href="../" class="brand-logo">
        <div class="logo-icon">⚡</div>
        <div class="logo-text">
          <span class="logo-title">Omni<span class="accent-text">Tools</span></span>
          <span class="logo-subtitle">Free Instant Web Tools</span>
        </div>
      </a>

      <div class="header-actions">
        <a href="../" class="back-btn"><i class="fa-solid fa-grid-2"></i> All 25+ Tools</a>
        <button id="themeToggleBtn" class="theme-btn" title="Toggle Theme"><i class="fa-solid fa-moon"></i></button>
      </div>
    </div>
  </header>

  <main class="main-container" style="padding-top:2rem;">
    <!-- Breadcrumb navigation for SEO -->
    <nav style="font-size:0.85rem; color:var(--text-dim); margin-bottom:1.25rem;">
      <a href="../" style="color:var(--accent-blue); text-decoration:none;">Home</a> / 
      <a href="../#{item['tool_id']}" style="color:var(--accent-blue); text-decoration:none;">{item['category']}</a> / 
      <span>{item['h1']}</span>
    </nav>

    <div class="tool-workspace-card">
      <div class="tool-title-row">
        <div class="tool-icon-large">⚡</div>
        <div>
          <h1 class="active-tool-title" style="font-size:1.85rem;">{item["h1"]}</h1>
          <p class="active-tool-desc">{item["description"]}</p>
          <div style="margin-top:0.5rem; display:inline-flex; align-items:center; gap:0.4rem; color:var(--accent-orange); font-size:0.85rem; font-weight:700;">
            <i class="fa-solid fa-star"></i> 4.9/5 ({item["rating_count"]} user ratings) • 100% Free
          </div>
        </div>
      </div>

      <!-- Dedicated Tool Body -->
      <div id="dedicatedToolBody" class="tool-body-area"></div>
    </div>

    <!-- SEO & How-To Content Block -->
    <article class="tool-seo-article" style="margin-top:2rem;">
      <h3><i class="fa-solid fa-circle-info"></i> How to Use {item['h1']}</h3>
      <ol style="margin-top:0.75rem;">
        {how_to_html}
      </ol>

      <h3 style="margin-top:2rem;"><i class="fa-solid fa-shield-check"></i> 100% Privacy & Fast Processing</h3>
      <p>OmniTools processes all tasks directly on your device using client-side WebAssembly and HTML5 Canvas. None of your data, files, or sensitive information is ever stored on external cloud servers.</p>
    </article>

    <!-- FAQs Section for Google Snippets -->
    <section class="faq-container" style="margin-top:2rem;">
      <h2 class="faq-heading"><i class="fa-solid fa-circle-question"></i> Frequently Asked Questions</h2>
      {faqs_html}
    </section>

    <!-- Ad Unit Space -->
    <div class="ad-banner-slot">
      <div class="ad-tag">Advertisement</div>
      <div class="ad-content-box">
        <span>High-Performance Responsive Ad Unit (Google AdSense)</span>
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-brand">
        <div class="logo-title">Omni<span class="accent-text">Tools</span></div>
        <p>Free, secure, in-browser utilities for students, developers, creators and professionals worldwide.</p>
        <p class="copyright">© 2026 OmniTools. All rights reserved.</p>
      </div>

      <div class="footer-links-group">
        <h4>Popular Free Tools</h4>
        <ul>
          <li><a href="../passport-size-photo-maker-20kb/">Passport Photo 20KB</a></li>
          <li><a href="../image-compressor-to-exact-kb/">Image Compressor to KB</a></li>
          <li><a href="../gst-calculator-india/">GST Calculator India</a></li>
          <li><a href="../kruti-dev-to-unicode-converter/">Kruti Dev to Unicode</a></li>
          <li><a href="../pdf-merger-online/">Free PDF Merger</a></li>
          <li><a href="../age-calculator-online/">Exact Age Calculator</a></li>
        </ul>
      </div>

      <div class="footer-links-group">
        <h4>Legal</h4>
        <ul>
          <li><a href="../#privacy">Privacy Policy</a></li>
          <li><a href="../#terms">Terms of Service</a></li>
          <li><a href="../sitemap.xml">XML Sitemap</a></li>
        </ul>
      </div>
    </div>
  </footer>

  <script src="../tools.js"></script>
  <script>
    // Initialize dedicated tool on load
    window.addEventListener('DOMContentLoaded', () => {{
      const tool = getToolById('{item["tool_id"]}');
      if (tool) {{
        tool.render(document.getElementById('dedicatedToolBody'));
      }}
      // Theme toggle
      const savedTheme = localStorage.getItem('omnitools_theme') || 'theme-dark';
      document.body.className = savedTheme;
      document.getElementById('themeToggleBtn').onclick = () => {{
        const isDark = document.body.classList.contains('theme-dark');
        const newTheme = isDark ? 'theme-light' : 'theme-dark';
        document.body.className = newTheme;
        localStorage.setItem('omnitools_theme', newTheme);
      }};
    }});
    function toggleFaq(el) {{
      el.parentElement.classList.toggle('active');
    }}
  </script>
</body>
</html>
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated {item['slug']}/index.html")

    # Generate ultimate sitemap.xml
    sitemap_entries = [f"""  <url>
    <loc>{BASE_URL}/</loc>
    <lastmod>2026-11-22</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>"""]

    for item in SEO_TOOLS:
        sitemap_entries.append(f"""  <url>
    <loc>{BASE_URL}/{item['slug']}/</loc>
    <lastmod>2026-11-22</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>""")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_entries)}
</urlset>
"""
    with open("/data/user/0/ai.antigem/files/home/projects/omnitool-web/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("Generated ultimate sitemap.xml with dedicated SEO URLs!")

if __name__ == "__main__":
    generate_pages()
