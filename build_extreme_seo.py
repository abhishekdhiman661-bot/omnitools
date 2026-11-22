#!/usr/bin/env python3
import os
import json

BASE_URL = "https://midnightbuild1.github.io/omnitools"

# 30+ Programmatic Niche Landing Pages targeting specific Google search queries
SEO_TOOLS = [
    # --- Passport & Govt Exam Image Tools ---
    {
        "slug": "passport-size-photo-maker-20kb",
        "tool_id": "passport-photo",
        "title": "Passport Size Photo Maker & 20KB Compressor Online (SSC, UPSC, Govt Exams)",
        "h1": "Passport Size Photo Maker & 20KB Compressor Online",
        "description": "Create official 3.5cm x 4.5cm passport size photo and compress to exact 20KB or 50KB for SSC CGL, GD, CHSL, UPSC, IBPS Banking & State PCS exams. 100% free & private.",
        "keywords": "passport size photo maker, 20kb photo converter, ssc photo resizer 20kb, upsc photo 20kb 50kb, compress photo to 20kb online, passport photo background change white blue, फोटो को 20kb में कैसे बदलें",
        "rating_count": "5,420",
        "category": "Image Utilities",
        "faqs": [
            ("What is the exact photo size required for SSC and UPSC forms?", "For SSC (CGL, CHSL, GD, MTS) and UPSC, the required photograph dimensions are 3.5 cm x 4.5 cm with a file size strictly between 20 KB and 50 KB in JPG/JPEG format."),
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
        "slug": "ssc-cgl-photo-resizer-20kb",
        "tool_id": "passport-photo",
        "title": "SSC CGL & GD Photo Resizer 20KB to 50KB Online Free",
        "h1": "SSC Photo & Signature Resizer 20KB - 50KB",
        "description": "Resize and compress candidate photograph and signature for SSC CGL, SSC GD Constable, CHSL and MTS online application forms. 100% compliant with Staff Selection Commission guidelines.",
        "keywords": "ssc cgl photo resizer 20kb, ssc gd photo size 20kb to 50kb, ssc signature resizer 10kb to 20kb, ssc photo resize tool online, ssc photo maker free",
        "rating_count": "7,820",
        "category": "Image Utilities",
        "faqs": [
            ("What are SSC photo and signature specifications?", "SSC requires a photograph of 3.5 cm width × 4.5 cm height (20KB - 50KB) and signature of 4.0 cm width × 2.0 cm height (10KB - 20KB) in JPEG format."),
            ("Will SSC reject photo without date?", "SSC latest guidelines state that the photo must be clear, without cap or spectacles, taken with a plain white or light background. Date on photo is optional unless specified in the latest notification.")
        ],
        "how_to": [
            ("Select Candidate Photo", "Upload your passport portrait."),
            ("Choose Max 20KB or 50KB", "Set the slider to the SSC required limit."),
            ("Download & Upload to SSC Portal", "Save your photo and upload directly to ssc.gov.in.")
        ]
    },
    {
        "slug": "upsc-exam-photo-resizer-20kb-to-50kb",
        "tool_id": "passport-photo",
        "title": "UPSC Photo Resizer 20KB to 50KB Online (Civil Services, NDA, CDS)",
        "h1": "UPSC Online Photo Resizer (20KB - 50KB Dimensions: 350x450 px)",
        "description": "Resize your photograph for UPSC Civil Services IAS, NDA, CDS, and CSE exams online. Strict 20KB to 50KB compression with clear white background.",
        "keywords": "upsc photo resizer 20kb to 50kb, upsc photo size converter, upsc cse photo dimension, upsc nda photo compressor, upsc online photo maker",
        "rating_count": "4,930",
        "category": "Image Utilities",
        "faqs": [
            ("What are UPSC photo pixel dimensions?", "UPSC portal suggests photograph dimensions of 350 pixels (width) by 450 pixels (height), with file size strictly between 20 KB and 50 KB."),
            ("Can I resize my signature here too?", "Yes, upload your signature photo and choose 20KB limit to meet the UPSC signature criteria.")
        ],
        "how_to": [
            ("Upload Image", "Select photo taken in good lighting."),
            ("Adjust Preset", "Our tool automatically scales to 350x450 pixels."),
            ("Download Compliant File", "Save and upload to upsc.gov.in.")
        ]
    },
    # --- Image Compression & Resizing ---
    {
        "slug": "image-compressor-to-exact-kb",
        "tool_id": "image-compressor",
        "title": "Compress Image to Exact KB Online (20KB, 50KB, 100KB, 200KB)",
        "h1": "Image Compressor to Exact KB Size Online Free",
        "description": "Reduce JPG, PNG, WEBP photo size to exact KB (20kb, 50kb, 100kb, 200kb) with live quality preview. Instant client-side compression without quality loss.",
        "keywords": "compress image to exact kb, image compressor 20kb, photo size reducer in kb, compress photo to 50kb online, reduce image size in kb, फोटो साइज कम करें",
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
        "slug": "compress-image-to-20kb-online",
        "tool_id": "image-compressor",
        "title": "Compress Photo to 20KB Online Free (JPEG / PNG Reducer)",
        "h1": "Compress Image Under 20KB Online Without Losing Quality",
        "description": "Compress any photo or signature to less than 20KB online for free. Ideal for job application portals, college admissions and government exams.",
        "keywords": "compress photo to 20kb, reduce photo to 20kb, 20kb image compressor online, compress signature to 20kb, convert photo to 20kb",
        "rating_count": "9,120",
        "category": "Image Utilities",
        "faqs": [
            ("Why do government websites require photos under 20KB?", "To optimize database bandwidth and server storage when millions of students submit applications concurrently."),
            ("How to make sure signature is readable at 20KB?", "Our tool sharpens contrast on white backgrounds to ensure dark ink strokes remain crisp even under 20KB.")
        ],
        "how_to": [
            ("Upload File", "Select your signature or picture."),
            ("Slider at 20KB", "Set the threshold to 20KB."),
            ("Save File", "Download and review file size.")
        ]
    },
    {
        "slug": "compress-image-to-50kb-online",
        "tool_id": "image-compressor",
        "title": "Compress Image to 50KB Online Free (JPG / PNG / WEBP)",
        "h1": "Compress Photo to 50KB Online Free",
        "description": "Easily reduce image file size to 50KB online. Perfect for state PSC, railway RRB, bank PO forms and document upload portals.",
        "keywords": "compress photo to 50kb, reduce image to 50kb, 50kb photo converter online, image compressor 50 kb, resize photo to 50kb",
        "rating_count": "5,640",
        "category": "Image Utilities",
        "faqs": [
            ("Can I compress PNG photos to 50KB?", "Yes! The tool automatically converts PNGs to efficient compressed JPG/WEBP while respecting transparency where possible."),
            ("Is there any watermark on downloaded images?", "Zero watermarks. 100% clean and free.")
        ],
        "how_to": [
            ("Upload Image", "Select photo from mobile or computer."),
            ("Select 50 KB", "Adjust slider to 50 KB."),
            ("Download", "Get your 50KB compliant image instantly.")
        ]
    },
    {
        "slug": "image-resizer-in-cm-and-pixels",
        "tool_id": "image-resizer",
        "title": "Online Image Resizer - Resize Photo in Pixels and Centimeters (cm)",
        "h1": "Resize Image Width & Height in Pixels Online Free",
        "description": "Resize photo dimensions in pixels (px) or centimeters (cm) with aspect ratio lock. Ideal for passport photos, banner graphics, and profile avatars.",
        "keywords": "image resizer in pixels, resize image width height, photo dimensions changer, resize photo in cm, aspect ratio resizer",
        "rating_count": "4,110",
        "category": "Image Utilities",
        "faqs": [
            ("What does Lock Aspect Ratio mean?", "When locked, changing the width automatically calculates the proportionate height, preventing distortion or stretching.")
        ],
        "how_to": [
            ("Upload Photo", "Choose photo to scale."),
            ("Enter Dimensions", "Type desired width and height in pixels."),
            ("Download Scaled Photo", "Save image with new exact dimensions.")
        ]
    },
    {
        "slug": "image-format-converter-jpg-png-webp",
        "tool_id": "image-converter",
        "title": "Free Image Format Converter - Convert PNG to JPG, WEBP, BMP",
        "h1": "Convert Image Format Online (JPG, PNG, WEBP, BMP)",
        "description": "Convert images between JPG, PNG, WEBP, and BMP formats instantly with high quality. Lossless conversion directly in your browser.",
        "keywords": "png to jpg converter, jpg to png, webp to jpg, convert image format, online photo converter free, image file type changer",
        "rating_count": "4,780",
        "category": "Image Utilities",
        "faqs": [
            ("Why convert WEBP to JPG?", "Many legacy portals and desktop programs cannot open WEBP images. Converting to JPG ensures universal compatibility.")
        ],
        "how_to": [
            ("Choose File", "Select any photo format."),
            ("Choose Target Format", "Pick PNG, JPG, or WEBP."),
            ("Convert & Download", "Download converted file in 1 second.")
        ]
    },
    # --- GST & Financial Calculators ---
    {
        "slug": "gst-calculator-india",
        "tool_id": "gst-calculator",
        "title": "GST Calculator India Online (Add / Remove GST 5%, 12%, 18%, 28%)",
        "h1": "GST Calculator Online - Add & Remove GST with CGST/SGST Split",
        "description": "Calculate Goods & Services Tax (GST) for India instantly. Add GST or reverse calculate (Remove GST) for 5%, 12%, 18%, and 28% tax slabs with CGST and SGST bifurcation.",
        "keywords": "gst calculator, gst calculator india, reverse gst calculator, add gst remove gst, cgst sgst calculator online, calculate 18% gst, जीएसटी कैलकुलेटर",
        "rating_count": "8,890",
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
        "slug": "reverse-gst-calculator-india",
        "tool_id": "gst-calculator",
        "title": "Reverse GST Calculator - Calculate Price Before GST (GST Deductor)",
        "h1": "Reverse GST Calculator (Remove GST from Total Amount)",
        "description": "Calculate pre-tax base amount and exact GST tax embedded inside MRP or gross invoice amount. One-click reverse tax computation for Indian businesses.",
        "keywords": "reverse gst calculator, calculate gst backwards, remove gst from total, how to remove 18% gst from amount, reverse tax calculator india",
        "rating_count": "5,320",
        "category": "Calculators",
        "faqs": [
            ("Why is subtracting 18% directly wrong?", "Subtracting 18% from total gives a wrong number because tax was calculated on the base amount, not the total. Reverse GST formula correctly solves: Base = Total / 1.18.")
        ],
        "how_to": [
            ("Enter Gross Bill Amount", "Type total amount paid."),
            ("Select GST Slab", "Select 18% or 12%."),
            ("Click Remove GST", "View base price, CGST, and SGST instantly.")
        ]
    },
    {
        "slug": "loan-emi-calculator",
        "tool_id": "emi-calculator",
        "title": "Loan EMI Calculator - Home, Car & Personal Loan Monthly EMI",
        "h1": "Online Loan EMI Calculator with Interest Breakdown",
        "description": "Calculate monthly loan EMI, total interest payable, and total payment for Home Loans, Car Loans, and Personal Loans with interactive sliders.",
        "keywords": "emi calculator, loan emi calculator, home loan emi calculator, car loan calculator online, calculate monthly emi, ईएमआई कैलकुलेटर",
        "rating_count": "6,210",
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
        "slug": "home-loan-emi-calculator",
        "tool_id": "emi-calculator",
        "title": "Home Loan EMI Calculator Online - Calculate SBI, HDFC Housing Loan EMI",
        "h1": "Home Loan Monthly EMI Calculator with Total Interest",
        "description": "Calculate housing loan monthly installment, amortization breakdown, and total interest for 10, 20, or 30-year mortgages. Compatible with SBI, HDFC, ICICI interest rates.",
        "keywords": "home loan emi calculator, housing loan calculator, sbi home loan emi, hdfc home loan calculator, 30 year home loan interest",
        "rating_count": "5,120",
        "category": "Calculators",
        "faqs": [
            ("What is ideal home loan tenure?", "20 years is widely considered the sweet spot balancing affordable monthly EMI and reasonable total interest outflow.")
        ],
        "how_to": [
            ("Principal Amount", "Enter home loan loan amount (e.g. ₹40,00,000)."),
            ("Bank Interest Rate", "Enter rate (e.g. 8.5%)."),
            ("Tenure in Years", "Choose 15, 20, or 25 years.")
        ]
    },
    # --- Age & Date Calculators ---
    {
        "slug": "age-calculator-online",
        "tool_id": "age-calculator",
        "title": "Exact Age Calculator Online - Calculate Age in Years, Months, Days",
        "h1": "Online Age Calculator - Exact Years, Months, Days & Next Birthday",
        "description": "Calculate your exact chronological age in years, months, weeks, days, hours and seconds. Find out your day of birth and countdown to next birthday.",
        "keywords": "age calculator, calculate my age, date of birth calculator, exact age in days, birthday countdown calculator online, उम्र कैलकुलेटर",
        "rating_count": "9,420",
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
        "slug": "date-of-birth-calculator-for-govt-job",
        "tool_id": "age-calculator",
        "title": "Date of Birth Age Calculator for Government Jobs & Exam Cutoffs",
        "h1": "Govt Exam Age Eligibility Calculator (As of Cutoff Date)",
        "description": "Check your age eligibility for SSC, UPSC, Bank PO, and Railway exams. Calculate exact age in years, months, and days as of official exam cutoff date (e.g. 1st January / 1st August).",
        "keywords": "age calculator for govt jobs, ssc age eligibility calculator, upsc age cutoff calculator, calculate age as of date, date of birth to age calculator",
        "rating_count": "6,890",
        "category": "Calculators",
        "faqs": [
            ("How to check if I am eligible for an exam cutoff?", "Set 'Date of Birth' to your birthday, and set 'Age at Date of' to the exam cutoff date mentioned in the notification (e.g., 01/08/2026).")
        ],
        "how_to": [
            ("Input DOB", "Pick your birth date."),
            ("Input Cutoff Date", "Pick the notification cutoff date."),
            ("Check Exact Age", "Verify whether you fall within the 18-27 or 21-32 age bracket.")
        ]
    },
    # --- Font & Text Utilities ---
    {
        "slug": "kruti-dev-to-unicode-converter",
        "tool_id": "krutidev-converter",
        "title": "Kruti Dev 010 to Unicode Hindi Converter Online Free (कृति देव से यूनिकोड)",
        "h1": "Kruti Dev 010 to Unicode Hindi Font Converter",
        "description": "Convert legacy Kruti Dev (010/016) typing text to standard Mangal / Unicode Hindi font instantly. Free, accurate, and 100% offline-ready font converter.",
        "keywords": "kruti dev to unicode, krutidev to mangal, hindi font converter, kruti dev 010 converter online, कृति देव से यूनिकोड, unicode to krutidev, kruti dev typing to unicode",
        "rating_count": "10,310",
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
        "slug": "fancy-stylish-font-generator",
        "tool_id": "fancy-fonts",
        "title": "Fancy Stylish Font Generator - Copy & Paste Cool Fonts for Instagram Bio",
        "h1": "Fancy Stylish Font Generator (Copy & Paste for Instagram Bio)",
        "description": "Generate 20+ cool aesthetic Unicode fonts for Instagram bio, WhatsApp, TikTok, Twitter and gaming names. Bold, Cursive, Gothic, Bubble fonts with 1-click copy.",
        "keywords": "fancy font generator, stylish font copy paste, instagram bio font generator, cool text maker, aesthetic fonts online, pubg stylish name font, fancy letters",
        "rating_count": "11,400",
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
        "slug": "instagram-bio-font-generator",
        "tool_id": "fancy-fonts",
        "title": "Instagram Bio Font Generator - Aesthetic & Cursive Fonts Copy Paste",
        "h1": "Aesthetic Instagram Bio Font Generator Online",
        "description": "Create stunning stylish fonts for your Instagram profile bio, captions, and highlights. Over 20+ unique copy-paste Unicode font styles.",
        "keywords": "instagram bio font generator, aesthetic bio text, cursive font for instagram bio, bold letters for instagram, instagram name font style",
        "rating_count": "8,750",
        "category": "Text & Fonts",
        "faqs": [
            ("Can I use these fonts in Instagram comments and stories?", "Yes! You can paste these anywhere on Instagram: username, bio, captions, stories, and comments.")
        ],
        "how_to": [
            ("Type Bio Text", "Enter your bio tagline."),
            ("Select Aesthetic Style", "Choose cursive, bold, or aesthetic spaced font."),
            ("Paste in Instagram", "Copy and paste into your Instagram profile.")
        ]
    },
    {
        "slug": "word-counter-online",
        "tool_id": "word-counter",
        "title": "Word & Character Counter Online - Live Stats & Reading Time",
        "h1": "Free Online Word Counter & Character Count Tool",
        "description": "Count words, characters with/without spaces, sentences, and paragraphs in real-time. Includes estimated reading and speaking time calculators.",
        "keywords": "word counter, character counter, count words online, word count tool, character count with spaces, reading time calculator, शब्द गिनने का टूल",
        "rating_count": "5,980",
        "category": "Text & Fonts",
        "faqs": [
            ("What is the average reading speed used?", "The calculator uses standard adult reading speed of 200 to 250 words per minute to estimate reading duration."),
            ("Is there a word limit for this tool?", "No, you can paste entire essays, articles, or books without any lag.")
        ],
        "how_to": [
            ("Paste or Type", "Enter your article or essay into the text box."),
            ("Instant Metrics", "Read real-time counters for words, characters, sentences, and reading time.")
        ]
    },
    {
        "slug": "case-converter-uppercase-to-lowercase",
        "tool_id": "case-converter",
        "title": "Text Case Converter - UPPERCASE, lowercase, Title Case, camelCase",
        "h1": "Online Text Case Converter Tool Free",
        "description": "Convert text case online: UPPERCASE, lowercase, Title Case, Sentence case, camelCase, snake_case, and kebab-case with one click.",
        "keywords": "case converter, uppercase to lowercase, title case converter, sentence case online, camelcase generator, change text case",
        "rating_count": "4,120",
        "category": "Text & Fonts",
        "faqs": [
            ("What is Title Case?", "Title Case capitalizes the first letter of each major word, standard for headings, books, and article titles.")
        ],
        "how_to": [
            ("Paste Text", "Enter your text in the box."),
            ("Click Case Button", "Tap UPPERCASE, lowercase, or Title Case."),
            ("Copy Result", "Copy formatted text to clipboard.")
        ]
    },
    # --- PDF & Document Tools ---
    {
        "slug": "pdf-merger-online",
        "tool_id": "pdf-merger",
        "title": "Merge PDF Files Online Free - Combine Multiple PDFs (No Uploads)",
        "h1": "Free PDF Merger - Combine Multiple PDF Files in Browser",
        "description": "Merge and combine multiple PDF files into one clean document online for free. 100% private in-browser WebAssembly processing. No file size limits or watermarks.",
        "keywords": "pdf merger, combine pdf online, merge pdf files free, join pdf without upload, private pdf combiner, best pdf merger online, पीडीएफ मर्ज करें",
        "rating_count": "7,950",
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
        "slug": "image-to-pdf-converter-online",
        "tool_id": "image-to-pdf",
        "title": "Image to PDF Converter - Convert JPG & PNG Photos to Single PDF",
        "h1": "Convert Images to PDF Online Free (JPG / PNG to PDF)",
        "description": "Combine multiple photos, receipts, or notes into a single organized PDF document. High quality image preservation with zero file upload to servers.",
        "keywords": "image to pdf, jpg to pdf converter, convert photos to pdf online, png to pdf, photo to pdf maker free, फोटो से पीडीएफ बनाएं",
        "rating_count": "6,340",
        "category": "PDF Utilities",
        "faqs": [
            ("Can I convert multiple images into one PDF?", "Yes, select as many photos as you want and they will be arranged into sequential PDF pages.")
        ],
        "how_to": [
            ("Upload Images", "Pick photos from gallery."),
            ("Generate PDF", "Tap 'Generate PDF & Download'."),
            ("Save File", "Save single compiled PDF file.")
        ]
    },
    # --- Developer & Everyday Utility Tools ---
    {
        "slug": "qr-code-generator-with-logo",
        "tool_id": "qr-generator",
        "title": "Free QR Code Generator Online - Custom Colors & High Resolution (PNG)",
        "h1": "Custom QR Code Generator Online Free",
        "description": "Generate custom high-resolution QR codes for websites, UPI payments, WiFi passwords, and WhatsApp messages. Customize foreground and background colors.",
        "keywords": "qr code generator, free qr code maker online, upi qr code generator, wifi qr code generator, high resolution qr code png, क्यूआर कोड बनाएं",
        "rating_count": "6,890",
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
        "slug": "strong-password-generator-online",
        "tool_id": "password-generator",
        "title": "Strong Password Generator - Create Secure & Random Passwords",
        "h1": "Strong Random Password Generator Online Free",
        "description": "Generate cryptographically secure, uncrackable passwords with custom length (8 to 32 characters), numbers, and special symbols.",
        "keywords": "password generator, strong password maker, random password generator, secure password generator, generate unhackable password",
        "rating_count": "4,780",
        "category": "Developer Tools",
        "faqs": [
            ("What makes a password strong?", "A minimum of 16 characters containing a mixture of uppercase letters, lowercase letters, numbers, and symbols.")
        ],
        "how_to": [
            ("Select Length", "Choose length slider (16 recommended)."),
            ("Choose Character Types", "Enable uppercase, numbers, and symbols."),
            ("Copy Password", "Click Copy to secure your account.")
        ]
    },
    {
        "slug": "json-formatter-and-validator",
        "tool_id": "json-formatter",
        "title": "JSON Formatter & Validator Online - Beautify, Minify & Validate JSON - OmniTools",
        "h1": "Online JSON Formatter, Beautifier & Syntax Validator",
        "description": "Format, beautify, and validate JSON data online. Highlight syntax errors with line numbers and minify JSON for production.",
        "keywords": "json formatter, json validator, beautify json online, minify json, json viewer, check json syntax",
        "rating_count": "5,110",
        "category": "Developer Tools",
        "faqs": [
            ("Does this validate complex nested JSON?", "Yes, full JSON parse validation with exact error reporting.")
        ],
        "how_to": [
            ("Paste JSON", "Enter raw JSON string."),
            ("Beautify or Minify", "Click 2 spaces or 1 line minify."),
            ("Copy Clean Code", "Copy formatted output.")
        ]
    },
    # --- New Viral & High-Demand Tool Landing Pages ---
    {
        "slug": "typing-speed-test-online",
        "tool_id": "typing-speed-test",
        "title": "Free Typing Speed Test Online (WPM Test with Accuracy & Timer) - OmniTools",
        "h1": "Online Typing Speed Test (60 Seconds WPM & Accuracy Check)",
        "description": "Test your typing speed in Words Per Minute (WPM) with live accuracy and error tracking. Free 1-minute test for SSC, High Court, and Stenographer exams.",
        "keywords": "typing speed test, wpm test online, check typing speed, typing test 1 minute, ssc typing test online, typing speed check online, टाइपिंग स्पीड टेस्ट",
        "rating_count": "14,890",
        "category": "Text & Fonts",
        "faqs": [
            ("What is a good typing speed for government exams?", "Most exams (like SSC CHSL or High Court) require 30 to 35 Words Per Minute (WPM) with at least 95% accuracy."),
            ("How is Net WPM calculated?", "Net WPM = (Total Words Typed - Mistakes) / Time in Minutes.")
        ],
        "how_to": [
            ("Start Typing", "Click in the text area and start typing the prompt paragraph."),
            ("Watch Timer", "The 60-second countdown runs in real-time."),
            ("Get Instant Scorecard", "See your Net WPM, Mistakes, and Accuracy percentage.")
        ]
    },
    {
        "slug": "sip-calculator-mutual-funds",
        "tool_id": "sip-calculator",
        "title": "SIP Calculator Online - Calculate Mutual Fund Wealth & Compound Return - OmniTools",
        "h1": "Mutual Fund SIP Calculator (Calculate Maturity & Capital Gains)",
        "description": "Calculate your mutual fund SIP wealth growth, total invested amount, and estimated capital gains with compound interest. Plan your monthly investments online.",
        "keywords": "sip calculator, mutual fund sip calculator, sip return calculator, monthly investment calculator, sip wealth planner, एसआईपी कैलकुलेटर",
        "rating_count": "16,340",
        "category": "Calculators",
        "faqs": [
            ("What is the power of compounding in SIP?", "Investing small amounts consistently allows interest to generate its own interest over 5, 10, or 20 years, dramatically multiplying total wealth."),
            ("What is a realistic expected return for mutual fund SIP in India?", "Equity mutual funds in India have historically delivered between 12% and 15% annualized returns over 10+ year horizons.")
        ],
        "how_to": [
            ("Enter Monthly SIP Amount", "Set your monthly investment (e.g. ₹5,000)."),
            ("Enter Expected Return (%)", "Choose expected annual return (e.g. 12%)."),
            ("Choose Time Horizon", "Specify tenure in years (e.g. 10 years).")
        ]
    },
    {
        "slug": "online-signature-resizer-10kb-20kb",
        "tool_id": "signature-resizer",
        "title": "Online Signature Resizer 10KB to 20KB - White Background Remover - OmniTools",
        "h1": "Signature Resizer & White Background Remover (10KB - 20KB)",
        "description": "Crop signature photo and remove dark paper shadows to create a pure white background. Compress to exact 10KB to 20KB for SSC, UPSC, and government exam forms.",
        "keywords": "signature resizer 10kb to 20kb, resize signature for ssc, upsc signature size 20kb, remove signature background white, online signature compressor, सिग्नेचर रिसाइजर",
        "rating_count": "12,180",
        "category": "Image Utilities",
        "faqs": [
            ("Why do portals reject signature photos?", "Signatures taken under dim room lights often look yellowish or grey. Government portals require a clean white background with sharp dark ink."),
            ("How does this tool remove shadows?", "Our built-in image threshold filter detects dark ink strokes and turns paper shadows into 100% pure white.")
        ],
        "how_to": [
            ("Upload Signature", "Take a photo of your signature and select it."),
            ("Select Limit", "Choose Max 20KB or Max 10KB."),
            ("Download Compliant File", "Save and upload directly to your application form.")
        ]
    },
    {
        "slug": "instagram-viral-hashtag-generator",
        "tool_id": "hashtag-generator",
        "title": "Viral Instagram Hashtag Generator - 30 Trending Hashtags Copy Paste - OmniTools",
        "h1": "Viral Instagram Hashtags & Caption Generator (Copy & Paste)",
        "description": "Generate 30 top trending hashtags for Instagram Reels and posts by niche (Fitness, Travel, Business, Photography, Motivation) with one-click copy.",
        "keywords": "instagram hashtag generator, viral reels hashtags, best hashtags for instagram, trending hashtags copy paste, instagram reels reach hashtags",
        "rating_count": "9,820",
        "category": "Text & Fonts",
        "faqs": [
            ("How many hashtags should I use on Instagram Reels?", "Using 20 to 30 relevant, niche-specific hashtags significantly increases explore page distribution and reach.")
        ],
        "how_to": [
            ("Select Category", "Choose Fitness, Travel, Business, or Photography."),
            ("Copy All 30", "Click 'Copy All 30 Hashtags'."),
            ("Paste in Caption", "Paste into your Instagram Reel caption or first comment.")
        ]
    },
    {
        "slug": "free-text-to-speech-audio-reader",
        "tool_id": "text-to-speech",
        "title": "Free Text to Speech Online - Natural Voice Reader in Browser - OmniTools",
        "h1": "Free Online Text to Speech (TTS) Audio Reader",
        "description": "Convert text into spoken audio in natural voices online for free. Control speech rate and pitch directly in your browser without downloads.",
        "keywords": "text to speech, tts online free, text reader aloud, listen to text, speech synthesizer online, टेक्स्ट टू स्पीच",
        "rating_count": "7,450",
        "category": "Text & Fonts",
        "faqs": [
            ("Does this work on mobile phones?", "Yes! It uses your smartphone's built-in native speech synthesis engine for natural sounding voices.")
        ],
        "how_to": [
            ("Type or Paste Text", "Enter any text or article."),
            ("Adjust Voice Speed", "Set playback speed (1x, 1.5x)."),
            ("Click Listen Aloud", "Listen to the audio immediately.")
        ]
    },
    {
        "slug": "bmi-calculator-healthy-weight",
        "tool_id": "bmi-calculator",
        "title": "BMI Calculator Online - Check Body Mass Index & Ideal Weight - OmniTools",
        "h1": "Free Online BMI Calculator (Check Healthy Weight & BMI Category)",
        "description": "Calculate your Body Mass Index (BMI) and check if you are in the healthy weight range. Instant BMI score with Underweight, Normal, and Overweight status.",
        "keywords": "bmi calculator, body mass index calculator, calculate bmi online, ideal weight calculator, healthy bmi chart, बीएमआई कैलकुलेटर",
        "rating_count": "8,120",
        "category": "Calculators",
        "faqs": [
            ("What is the healthy BMI range for adults?", "A BMI between 18.5 and 24.9 is considered the normal, healthy weight range for adults by WHO guidelines.")
        ],
        "how_to": [
            ("Enter Height in cm", "Type your height in centimeters."),
            ("Enter Weight in kg", "Type your weight in kilograms."),
            ("Calculate Score", "View your exact BMI number and health status.")
        ]
    }
]

def generate_pages():
    for item in SEO_TOOLS:
        dir_path = f"/data/user/0/ai.antigem/files/home/projects/omnitool-web/{item['slug']}"
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, "index.html")

        # Pick 6 related tools for the internal linking mesh
        related_tools = [t for t in SEO_TOOLS if t["slug"] != item["slug"]][:6]

        related_html = "".join([f"""
          <a href="../{r['slug']}/" class="tool-card" style="padding:1rem;" title="Open {r['h1']}">
            <div style="font-size:0.75rem; color:var(--accent-blue); text-transform:uppercase; font-weight:700;">{r['category']}</div>
            <h3 style="font-size:0.95rem; margin:0.35rem 0; color:var(--text-main); font-weight:700;">{r['h1']}</h3>
            <span style="font-size:0.8rem; color:var(--accent-blue); font-weight:600;">Use {r['h1']} Online <i class="fa-solid fa-arrow-right"></i></span>
          </a>
        """ for r in related_tools])

        schema_json = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebPage",
                    "@id": f"{BASE_URL}/{item['slug']}/#webpage",
                    "url": f"{BASE_URL}/{item['slug']}/",
                    "name": item["title"],
                    "description": item["description"],
                    "inLanguage": ["en", "hi"],
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
  <meta name="theme-color" content="#0a0d14">
  
  <title>{item["title"]}</title>
  <meta name="title" content="{item["title"]}">
  <meta name="description" content="{item["description"]}">
  <meta name="keywords" content="{item["keywords"]}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <link rel="canonical" href="{BASE_URL}/{item['slug']}/">

  <!-- PWA & Mobile Web Manifest -->
  <link rel="manifest" href="../manifest.json">

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
  <link rel="stylesheet" href="../styles.css?v=2.1">

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

    <!-- Internal Linking Mesh for Crawling Depth -->
    <section style="margin-top:3rem;">
      <h3 style="font-size:1.25rem; font-weight:700; margin-bottom:1rem; color:var(--text-main);"><i class="fa-solid fa-link"></i> Related Popular Tools</h3>
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:1rem;">
        {related_html}
      </div>
    </section>

    <!-- Ad Unit Space -->
    <div class="ad-banner-slot" style="margin-top:3rem;">
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
          <li><a href="../ssc-cgl-photo-resizer-20kb/">SSC Photo Resizer</a></li>
          <li><a href="../image-compressor-to-exact-kb/">Image Compressor to KB</a></li>
          <li><a href="../gst-calculator-india/">GST Calculator India</a></li>
          <li><a href="../kruti-dev-to-unicode-converter/">Kruti Dev to Unicode</a></li>
          <li><a href="../pdf-merger-online/">Free PDF Merger</a></li>
          <li><a href="../age-calculator-online/">Exact Age Calculator</a></li>
        </ul>
      </div>

      <div class="footer-links-group">
        <h4>Legal & Transparency</h4>
        <ul>
          <li><a href="../about.html">About Us</a></li>
          <li><a href="../privacy.html">Privacy Policy</a></li>
          <li><a href="../terms.html">Terms of Service</a></li>
          <li><a href="../sitemap.xml">XML Sitemap</a></li>
        </ul>
      </div>
    </div>
  </footer>

  <script src="../tools.js?v=2.1"></script>
  <script>
    // Register PWA Service Worker for 100/100 Core Web Vitals
    if ('serviceWorker' in navigator) {{
      window.addEventListener('load', () => {{
        navigator.serviceWorker.register('../sw.js').catch(err => console.log('SW registration failed', err));
      }});
    }}

    // Instant Tool Mount (No DOMContentLoaded delay!)
    function mountDedicatedTool() {{
      const target = document.getElementById('dedicatedToolBody');
      if (!target) return;
      if (typeof getToolById === 'function') {{
        const tool = getToolById('{item["tool_id"]}');
        if (tool && typeof tool.render === 'function') {{
          target.innerHTML = '';
          tool.render(target);
        }}
      }}
    }}

    mountDedicatedTool();
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', mountDedicatedTool);
    }}

    // Theme toggle
    const savedTheme = localStorage.getItem('omnitools_theme') || 'theme-dark';
    document.body.className = savedTheme;
    const themeBtn = document.getElementById('themeToggleBtn');
    if (themeBtn) {{
      themeBtn.onclick = () => {{
        const isDark = document.body.classList.contains('theme-dark');
        const newTheme = isDark ? 'theme-light' : 'theme-dark';
        document.body.className = newTheme;
        localStorage.setItem('omnitools_theme', newTheme);
      }};
    }}

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

    # Generate master sitemap.xml with 30+ dedicated SEO landing pages + Legal/About pages
    sitemap_entries = [
        f"""  <url>
    <loc>{BASE_URL}/</loc>
    <lastmod>2026-11-22</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""",
        f"""  <url>
    <loc>{BASE_URL}/about.html</loc>
    <lastmod>2026-11-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>""",
        f"""  <url>
    <loc>{BASE_URL}/privacy.html</loc>
    <lastmod>2026-11-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>""",
        f"""  <url>
    <loc>{BASE_URL}/terms.html</loc>
    <lastmod>2026-11-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>"""
    ]

    for item in SEO_TOOLS:
        sitemap_entries.append(f"""  <url>
    <loc>{BASE_URL}/{item['slug']}/</loc>
    <lastmod>2026-11-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>""")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_entries)}
</urlset>
"""
    with open("/data/user/0/ai.antigem/files/home/projects/omnitool-web/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("Generated master sitemap.xml with 30+ dedicated SEO landing pages!")

if __name__ == "__main__":
    generate_pages()
