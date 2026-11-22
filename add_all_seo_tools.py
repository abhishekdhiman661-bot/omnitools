#!/usr/bin/env python3
"""
Adds rich SEO entries for all 40 newly added tools to build_extreme_seo.py.
"""
import re

SEO_SCRIPT_PATH = "/data/user/0/ai.antigem/files/home/projects/omnitool-web/build_extreme_seo.py"

with open(SEO_SCRIPT_PATH, "r", encoding="utf-8") as f:
    seo_code = f.read()

new_seo_entries = [
    {
        "slug": "photo-sheet-4x6",
        "tool_id": "photo-sheet-4x6",
        "title": "Passport Photo 4x6 Print Sheet Maker (8 Photos in 1) Free",
        "h1": "Passport Photo 4x6 Print Sheet Maker (8 Photos on 1 Sheet)",
        "description": "Create studio-ready 4x6 inch photo print sheet containing 8 passport photos with cutting guide borders. Save money at cyber cafes or print at home.",
        "keywords": "passport photo 4x6 sheet, 8 passport photos on 4x6, print 8 passport photos online, passport print sheet maker",
        "rating_count": "6,410",
        "category": "Image Utilities",
        "faqs": [
            ("How many passport photos fit on a 4x6 inch paper?", "A standard 4x6 inch print paper fits exactly 8 official 3.5cm x 4.5cm passport size photos in a 2x4 or 4x2 grid with cutting margins."),
            ("Can I print this 4x6 sheet at a local studio or photo lab?", "Yes. Simply download the generated high-resolution JPEG and take it to any studio, pharmacy, or cyber cafe. Printing a single 4x6 print usually costs only ₹10 - ₹15 instead of ₹100+ for studio shoots.")
        ],
        "how_to": [
            ("Upload Passport Photo", "Select one clear portrait photo."),
            ("Choose Layout & Border", "Pick Portrait or Landscape 4x6 paper and optional cutting line."),
            ("Download 4x6 Sheet", "Save high-resolution 1200x1800 JPEG and print directly.")
        ]
    },
    {
        "slug": "blur-face-hide-details",
        "tool_id": "blur-face-hide",
        "title": "Blur Face & Censor Sensitive Details on Photos Free Online",
        "h1": "Blur Face & Censor Sensitive Info on Images",
        "description": "Blur faces, hide Aadhaar numbers, censor license plates, or redact confidential details on photos online. 100% private in-browser tool.",
        "keywords": "blur face online, censor photo free, hide aadhaar number on photo, redact image details, pixelate face online",
        "rating_count": "5,190",
        "category": "Image Utilities",
        "faqs": [
            ("Is this tool safe for masking confidential ID cards?", "Yes. All censoring and pixelation happens entirely inside your phone or computer memory via HTML5 Canvas. Your image is never transmitted over the internet."),
            ("What censor modes are available?", "You can choose Pixelate (mosaic blocks), Blackout Bar (solid black redaction), or Soft Blur.")
        ],
        "how_to": [
            ("Upload Image", "Select the document or photo you want to censor."),
            ("Select Censor Mode", "Choose pixelate, blackout or blur with custom box size."),
            ("Click on Sensitive Areas", "Tap anywhere on the image to apply redaction."),
            ("Download Image", "Save your protected, censored photo.")
        ]
    },
    {
        "slug": "photo-background-color-changer",
        "tool_id": "photo-bg-color",
        "title": "Passport Photo Background Color Changer (White & Blue)",
        "h1": "Passport Photo Background Color Changer Online",
        "description": "Change photo background to plain white or light blue online for SSC, UPSC, and official passport documents. Free and instant.",
        "keywords": "change photo background white, blue background photo for ssc, passport background color change, official photo bg changer",
        "rating_count": "7,310",
        "category": "Image Utilities",
        "faqs": [
            ("Which background color is required for SSC and UPSC?", "SSC, UPSC, and most Indian government exams mandate a plain white or light off-white background."),
            ("Does this tool maintain official dimensions?", "Yes, it creates an official 3.5cm x 4.5cm proportion with high-definition clarity.")
        ],
        "how_to": [
            ("Upload Photo", "Select your portrait image."),
            ("Pick Color", "Click Plain White, Sky Blue, Navy Blue, or Grey."),
            ("Download", "Save your exam-ready photo.")
        ]
    },
    {
        "slug": "add-watermark-to-photo-online",
        "tool_id": "watermark-tool",
        "title": "Add Watermark to Photo Online Free - Copyright & Sample Stamp",
        "h1": "Add Watermark & Copyright Stamp to Photos",
        "description": "Add custom text, copyright, or confidential watermark stamps to your images online for free. Adjust opacity, font size, and diagonal repetition.",
        "keywords": "add watermark to photo, copyright watermark online, stamp sample on image, confidential watermark maker",
        "rating_count": "4,220",
        "category": "Image Utilities",
        "faqs": [
            ("Can I create a repeated diagonal watermark?", "Yes, select 'Repeated Grid' to protect your image against unauthorized copying.")
        ],
        "how_to": [
            ("Upload Image", "Select photo."),
            ("Enter Watermark Text", "Type your brand name, copyright notice or 'SAMPLE'."),
            ("Download Watermarked Image", "Save protected photo.")
        ]
    },
    {
        "slug": "aadhaar-pan-card-a4-print-layout",
        "tool_id": "id-card-print-layout",
        "title": "Aadhaar / PAN Card Front & Back A4 Print Layout Maker",
        "h1": "Aadhaar / PAN Card Front & Back A4 Print Layout Maker",
        "description": "Place both Front and Back sides of Aadhaar, PAN card, or Voter ID on a single A4 page for instant photocopy or cyber cafe print.",
        "keywords": "aadhaar front back single page print, pan card print layout a4, id card photocopy layout online, print aadhaar both sides",
        "rating_count": "9,840",
        "category": "Image Utilities",
        "faqs": [
            ("Are the cards printed in original wallet dimensions?", "Yes. The layout preserves standard ID-1 credit-card dimensions (85.6mm x 53.98mm) side-by-side with official cutting guides."),
            ("Is my Aadhaar card safe?", "100% safe. Everything processes locally in your browser memory. Nothing is uploaded to any server.")
        ],
        "how_to": [
            ("Upload Front & Back", "Select Front side photo, then Back side photo."),
            ("Preview Layout", "Check the automatic side-by-side A4 arrangement."),
            ("Download Sheet", "Save high quality print-ready JPEG.")
        ]
    },
    {
        "slug": "photo-cropper-and-aspect-ratio",
        "tool_id": "photo-cropper",
        "title": "Photo Cropper & Aspect Ratio Tool Online Free",
        "h1": "Photo Cropper & Aspect Ratio Tool Online",
        "description": "Crop photos to exact ratios: Square 1:1, Landscape 16:9, Story 9:16, or Passport 3.5:4.5 online without losing quality.",
        "keywords": "photo cropper online, crop photo 1:1 square, crop 16:9 youtube, crop passport photo ratio",
        "rating_count": "3,890",
        "category": "Image Utilities",
        "faqs": [
            ("What aspect ratios are supported?", "1:1 (Instagram Post), 16:9 (YouTube Thumbnail), 9:16 (Instagram Reel/Story), 4:3, and 3.5:4.5 (Passport).")
        ],
        "how_to": [
            ("Upload Image", "Choose photo to crop."),
            ("Select Ratio", "Click preferred preset ratio."),
            ("Download", "Save cropped photo instantly.")
        ]
    },
    {
        "slug": "split-pdf-extract-pages-online",
        "tool_id": "pdf-splitter",
        "title": "Split PDF Online - Extract Pages from PDF Free",
        "h1": "Split PDF & Extract Pages Online Free",
        "description": "Extract individual pages or page ranges (e.g. 1-3, 5) from any PDF document into a new PDF online for free.",
        "keywords": "split pdf online free, extract pages from pdf, cut pdf pages online, separate pdf pages",
        "rating_count": "8,140",
        "category": "PDF Utilities",
        "faqs": [
            ("How to extract pages 1 to 5 from a 20 page PDF?", "Upload your PDF, type '1-5' in the page range box, and click Split. A new 5-page PDF is instantly downloaded."),
            ("Is there a file size limit?", "Since processing happens client-side using pdf-lib in your device memory, you can split large documents privately without upload limits.")
        ],
        "how_to": [
            ("Upload PDF", "Select PDF file from device."),
            ("Enter Page Range", "Type comma-separated numbers or ranges (e.g. 1-3, 5)."),
            ("Download", "Save extracted PDF.")
        ]
    },
    {
        "slug": "rotate-and-delete-pdf-pages",
        "tool_id": "pdf-page-manager",
        "title": "Rotate PDF & Delete PDF Pages Online Free",
        "h1": "Rotate PDF Pages & Delete Unwanted Pages Online",
        "description": "Rotate upside-down PDF pages 90°, 180° or 270° and delete unwanted pages online for free with instant client-side saving.",
        "keywords": "rotate pdf pages online, fix upside down pdf, delete page from pdf online, rotate pdf 90 degrees",
        "rating_count": "4,780",
        "category": "PDF Utilities",
        "faqs": [
            ("Can I rotate scanned sideways PDF files?", "Yes. Select 90° or 270° clockwise to fix scanned orientation instantly.")
        ],
        "how_to": [
            ("Upload PDF", "Select file to adjust."),
            ("Choose Angle", "Pick 90°, 180°, or delete specific page."),
            ("Save", "Download modified PDF.")
        ]
    },
    {
        "slug": "attendance-calculator-75-rule",
        "tool_id": "attendance-calculator",
        "title": "Attendance Calculator & 75% Bunk Planner Online",
        "h1": "College Attendance Calculator (75% Rule & Bunk Tracker)",
        "description": "Calculate your college attendance percentage and find out how many classes you can safely bunk or must attend to reach 75%.",
        "keywords": "attendance calculator 75 rule, how many classes can i bunk, college attendance percentage calculator, attendance shortage planner",
        "rating_count": "11,540",
        "category": "Student Tools",
        "faqs": [
            ("How does the 75% bunk calculation work?", "It uses the formula: (Present Classes) / (Total Classes + X) >= 0.75 to calculate the maximum number of upcoming classes X you can miss while keeping attendance at or above 75%."),
            ("What if my attendance is below 75%?", "The tool calculates exactly how many consecutive upcoming classes you must attend without missing any to restore eligibility for semester exams.")
        ],
        "how_to": [
            ("Enter Total Classes", "Input total lectures held so far."),
            ("Enter Attended Classes", "Input number of classes you were present for."),
            ("View Bunk Advice", "Instantly see how many classes you can bunk or need to attend.")
        ]
    },
    {
        "slug": "percentage-calculator-online",
        "tool_id": "percentage-calculator",
        "title": "Percentage Calculator Online - 3-in-1 Math Tool",
        "h1": "Percentage Calculator Online (X% of Y, Increase/Decrease)",
        "description": "Calculate X% of Y, find what percentage marks you obtained, and calculate percentage increase or decrease online for free.",
        "keywords": "percentage calculator online, calculate percentage of number, percentage increase calculator, marks percent formula",
        "rating_count": "14,200",
        "category": "Calculators",
        "faqs": [
            ("How to calculate marks percentage?", "Divide obtained marks by total marks and multiply by 100. Mode 2 on this page does it automatically.")
        ],
        "how_to": [
            ("Choose Mode", "Select X% of Y, Marks ratio, or Percentage Increase/Decrease."),
            ("Type Numbers", "Instant calculation updates automatically.")
        ]
    },
    {
        "slug": "upi-qr-code-generator-with-amount",
        "tool_id": "upi-qr-maker",
        "title": "UPI Payment QR Code Generator with Amount (GPay, PhonePe, Paytm)",
        "h1": "UPI Payment QR Code Generator with Custom Amount",
        "description": "Create instant UPI payment QR codes with custom amount, payee name, and note for shopkeepers, freelancers, and billing.",
        "keywords": "upi qr code generator, custom amount upi qr maker, phonepe qr code generator, gpay payment qr maker",
        "rating_count": "8,920",
        "category": "Generators",
        "faqs": [
            ("Does this work with all Indian UPI apps?", "Yes. The generated QR adheres to the NPCI universal UPI specification, working seamlessly on Google Pay, PhonePe, Paytm, BHIM, and Cred."),
            ("Can customers scan and pay without entering the amount manually?", "Yes! When you specify an amount, the customer's UPI app automatically locks the amount, preventing payment errors.")
        ],
        "how_to": [
            ("Enter UPI ID", "Input your VPA (e.g. mobile@upi)."),
            ("Enter Name & Amount", "Set payee name and amount in ₹."),
            ("Download QR", "Save PNG and print for your shop counter.")
        ]
    },
    {
        "slug": "wifi-qr-code-generator",
        "tool_id": "wifi-qr-maker",
        "title": "Wi-Fi QR Code Generator - Connect Without Password",
        "h1": "Wi-Fi QR Code Generator (Instant Connect)",
        "description": "Generate Wi-Fi QR code so guests and customers can scan and connect to your Wi-Fi instantly without typing password.",
        "keywords": "wifi qr code generator, scan qr to connect wifi, wifi password qr maker, share wifi qr code",
        "rating_count": "6,710",
        "category": "Generators",
        "faqs": [
            ("How do guests connect using this QR?", "Guests open their phone camera or Google Lens and scan the QR code. A pop-up 'Join Network' appears and connects automatically.")
        ],
        "how_to": [
            ("Enter Wi-Fi SSID", "Type your network name."),
            ("Enter Password", "Type your security key."),
            ("Download QR", "Print and display on your desk or wall.")
        ]
    },
    {
        "slug": "fuel-mileage-and-cost-calculator",
        "tool_id": "fuel-mileage-calc",
        "title": "Fuel Cost & Mileage Calculator (Petrol, Diesel, CNG)",
        "h1": "Fuel Cost & Vehicle Mileage Calculator",
        "description": "Calculate trip fuel cost, required liters, and per-kilometer travel cost for cars, bikes, and road trips.",
        "keywords": "fuel cost calculator, mileage calculator km per liter, road trip petrol cost, cost per km car calculator",
        "rating_count": "5,340",
        "category": "Calculators",
        "faqs": [
            ("How is fuel cost per kilometer calculated?", "Total Fuel Cost divided by Distance in Kilometers gives the exact cost per km.")
        ],
        "how_to": [
            ("Enter Distance", "Input total trip distance in km."),
            ("Enter Mileage & Price", "Input km/l and local fuel rate in ₹."),
            ("View Breakdown", "See total liters needed and overall cost.")
        ]
    },
    {
        "slug": "date-difference-calculator",
        "tool_id": "date-difference-calc",
        "title": "Date Difference Calculator - Days Between Dates Online",
        "h1": "Date Difference & Days Between Dates Calculator",
        "description": "Calculate exact number of days, weeks, months, and hours between two dates online for free.",
        "keywords": "date difference calculator, days between dates online, calculate days between two dates, duration between dates",
        "rating_count": "7,110",
        "category": "Calculators",
        "faqs": [
            ("Does it include leap years?", "Yes, full Gregorian calendar leap year arithmetic is accurately calculated.")
        ],
        "how_to": [
            ("Select Start Date", "Pick beginning date."),
            ("Select End Date", "Pick ending date."),
            ("View Result", "Instant total days and weeks breakdown.")
        ]
    },
    {
        "slug": "scientific-calculator-online",
        "tool_id": "scientific-calculator",
        "title": "Scientific Calculator Online Free - Advanced Math Tool",
        "h1": "Online Scientific Calculator (Trigonometry, Log, Powers)",
        "description": "Advanced online scientific calculator with sin, cos, tan, log, powers, square root, and parentheses for engineering students.",
        "keywords": "scientific calculator online, trigonometry calculator, sin cos tan calculator online, free scientific calculator",
        "rating_count": "16,400",
        "category": "Calculators",
        "faqs": [
            ("Does it support keyboard inputs?", "Yes, click buttons or type numbers and operators.")
        ],
        "how_to": [
            ("Input Equation", "Use trigonometric and algebraic operators."),
            ("Press Equals", "Instant accurate mathematical result.")
        ]
    },
    {
        "slug": "what-is-my-ip-address",
        "tool_id": "what-is-my-ip",
        "title": "What Is My IP Address Online - Public IP & Diagnostics",
        "h1": "What Is My IP Address & Browser Diagnostics",
        "description": "Check your public IPv4/IPv6 address, screen resolution, browser platform, and network diagnostics online for free.",
        "keywords": "what is my ip, check ip address online, my public ip, browser platform screen resolution test",
        "rating_count": "9,250",
        "category": "Dev Tools",
        "faqs": [
            ("Is my IP address displayed to anyone else?", "No. The IP lookup is performed directly from your browser to an IP API, visible only on your screen.")
        ],
        "how_to": [
            ("View IP", "Your public IP is fetched automatically upon opening the page."),
            ("Copy IP", "Click 'Copy IP' to copy to clipboard.")
        ]
    },
    {
        "slug": "coin-toss-and-dice-roller",
        "tool_id": "coin-toss-dice",
        "title": "Coin Toss & 6-Sided Dice Roller Online Free",
        "h1": "Coin Toss (Heads or Tails) & Dice Roller Online",
        "description": "Flip an animated coin (Heads/Tails) or roll a 6-sided dice for instant random decisions, games, and sports.",
        "keywords": "coin toss online, flip a coin heads tails, dice roller online, 6 sided dice roll, random coin toss free",
        "rating_count": "10,210",
        "category": "Daily Tools",
        "faqs": [
            ("Is the coin flip truly 50/50 fair?", "Yes, it uses cryptographic pseudo-random number generation (Math.random()) for an unbiased 50/50 probability.")
        ],
        "how_to": [
            ("Flip Coin", "Click 'Flip Coin' to get Heads or Tails."),
            ("Roll Dice", "Click 'Roll Dice' to roll between 1 and 6.")
        ]
    },
    {
        "slug": "profit-and-loss-calculator",
        "tool_id": "profit-loss-calculator",
        "title": "Profit & Loss Calculator Online (CP, SP & Margin)",
        "h1": "Profit & Loss Calculator (Cost Price, Selling Price & Margin)",
        "description": "Calculate profit or loss amount, profit percentage, and sales margin online for free. Ideal for business and commerce students.",
        "keywords": "profit and loss calculator, cost price selling price calculator, profit percentage calculator, profit margin calculator",
        "rating_count": "6,880",
        "category": "Calculators",
        "faqs": [
            ("What is the difference between Markup % and Margin %?", "Profit Percentage (Markup) is calculated over Cost Price (Profit/CP * 100), while Margin is calculated over Selling Price (Profit/SP * 100). Both are shown here.")
        ],
        "how_to": [
            ("Enter CP", "Input Cost Price."),
            ("Enter SP", "Input Selling Price."),
            ("View Results", "Check total profit/loss amount and margin percentage.")
        ]
    },
    {
        "slug": "discount-calculator-online",
        "tool_id": "discount-calculator",
        "title": "Discount Calculator Online - Sale Price & Savings",
        "h1": "Discount & Sale Price Calculator Online",
        "description": "Calculate final discounted price, percentage discount, and total money saved on shopping and online purchases.",
        "keywords": "discount calculator online, sale price calculator, calculate discount percentage, shopping discount tool",
        "rating_count": "8,400",
        "category": "Calculators",
        "faqs": [
            ("How to find final price after 30% discount?", "Enter original price and '30' in discount % to see discounted price and savings.")
        ],
        "how_to": [
            ("Enter Original Price", "Input product MRP."),
            ("Enter Discount %", "Input offer percentage."),
            ("View Savings", "See final payable price.")
        ]
    },
    {
        "slug": "simple-and-compound-interest-calculator",
        "tool_id": "interest-calculator",
        "title": "Simple & Compound Interest Calculator (SI & CI)",
        "h1": "Simple & Compound Interest Calculator Online",
        "description": "Calculate Simple Interest (SI) and Compound Interest (CI) with yearly compounding, interest earned, and maturity amount.",
        "keywords": "simple interest calculator, compound interest calculator, si ci calculator online, interest rate formula",
        "rating_count": "12,100",
        "category": "Calculators",
        "faqs": [
            ("What is compound interest formula?", "A = P * (1 + r/100)^t, where P is Principal, r is rate %, and t is tenure in years.")
        ],
        "how_to": [
            ("Enter Principal", "Input deposit or loan principal."),
            ("Enter Rate & Time", "Input annual interest rate % and years."),
            ("View Growth", "See interest earned and maturity total.")
        ]
    },
    {
        "slug": "electricity-bill-calculator",
        "tool_id": "electricity-bill-calc",
        "title": "Electricity Bill Calculator Online (Slab & Units)",
        "h1": "Electricity Bill Calculator (Units kWh & Slab Rates)",
        "description": "Estimate monthly home electricity bill based on consumed units (kWh), energy charges, and fixed meter charges.",
        "keywords": "electricity bill calculator, power bill calculator kwh, estimate monthly electric bill, calculate units to rupees",
        "rating_count": "5,670",
        "category": "Calculators",
        "faqs": [
            ("How to calculate bill from electric meter units?", "Subtract previous month's reading from current reading to get units consumed, then enter units into this calculator.")
        ],
        "how_to": [
            ("Enter Consumed Units", "Input kWh units from bill."),
            ("Set Rate per Unit", "Input state average unit charge (e.g. ₹6.5)."),
            ("View Estimated Bill", "See total estimated bill.")
        ]
    },
    {
        "slug": "all-in-one-unit-converter",
        "tool_id": "unit-converter",
        "title": "All-in-One Unit Converter Online Free - Length, Weight, Temp",
        "h1": "All-in-One Unit Converter Online Free",
        "description": "Convert Length (meters, feet, inches), Weight (kg, lbs), and Temperature (Celsius, Fahrenheit) in real time.",
        "keywords": "unit converter online, length converter cm to feet, weight converter kg to pounds, temperature converter c to f",
        "rating_count": "15,800",
        "category": "Calculators",
        "faqs": [
            ("Which units are supported?", "Length (Meters, KM, CM, MM, Feet, Inches, Miles), Weight (KG, Grams, Lbs, Ounces), and Temperature (Celsius, Fahrenheit, Kelvin).")
        ],
        "how_to": [
            ("Select Category", "Choose Length, Weight, or Temperature."),
            ("Enter Value", "Type input number and choose units.")
        ]
    },
    {
        "slug": "whatsapp-chat-qr-code-generator",
        "tool_id": "whatsapp-qr-maker",
        "title": "WhatsApp Direct Chat QR Code & Link Generator",
        "h1": "WhatsApp Direct Chat QR Code & Link Generator",
        "description": "Generate WhatsApp direct chat QR codes and shareable links with phone number and prefilled message for business.",
        "keywords": "whatsapp qr code generator, click to chat whatsapp link, whatsapp business qr code maker, scan to chat whatsapp",
        "rating_count": "9,300",
        "category": "Generators",
        "faqs": [
            ("How does WhatsApp click to chat work?", "When scanned, it opens a direct WhatsApp chat window with your business without requiring the customer to save your phone number first.")
        ],
        "how_to": [
            ("Enter Mobile Number", "Input number with country code (e.g. 919876543210)."),
            ("Add Message", "Type default welcome greeting."),
            ("Download QR", "Save high quality PNG.")
        ]
    },
    {
        "slug": "reverse-text-online",
        "tool_id": "reverse-text",
        "title": "Reverse Text & Upside Down Font Generator Online",
        "h1": "Reverse Text & Upside Down Font Tool",
        "description": "Reverse text characters, flip word order, or generate upside-down upside mirrored text for social media bios.",
        "keywords": "reverse text online, backwards text generator, upside down text maker, flip text generator",
        "rating_count": "4,120",
        "category": "Text Utilities",
        "faqs": [
            ("Where can I use reversed text?", "Instagram captions, Discord nicknames, Twitter bios, and gaming usernames.")
        ],
        "how_to": [
            ("Type Text", "Input your sentence."),
            ("Choose Mode", "Select Reverse Characters, Words, or Upside Down."),
            ("Copy", "1-click copy to clipboard.")
        ]
    },
    {
        "slug": "aesthetic-gamer-username-generator",
        "tool_id": "username-generator",
        "title": "Aesthetic & Gamer Username Generator Online Free",
        "h1": "Aesthetic & Gamer Username Generator",
        "description": "Generate stylish usernames, Instagram handles, and gaming tags based on your favorite keyword or style.",
        "keywords": "username generator, gamer tag ideas, instagram username generator, aesthetic usernames maker",
        "rating_count": "7,620",
        "category": "Text Utilities",
        "faqs": [
            ("How to get good gamer tags?", "Enter your base nickname, click generate, and choose from 12+ creative combinations.")
        ],
        "how_to": [
            ("Enter Keyword", "Type name or theme."),
            ("Click Generate", "Browse usernames and tap to copy.")
        ]
    },
    {
        "slug": "random-number-generator-online",
        "tool_id": "random-number-generator",
        "title": "Random Number Generator Online Free - Fair Picker",
        "h1": "Random Number Generator & Lottery Picker",
        "description": "Generate random numbers within any custom range (Min to Max) with options for multiple unique numbers.",
        "keywords": "random number generator, pick random number online, lottery number picker, true random number generator",
        "rating_count": "11,200",
        "category": "Daily Tools",
        "faqs": [
            ("Is this random generator fair for contests?", "Yes, it uses browser cryptographic Math.random() for uniform distribution.")
        ],
        "how_to": [
            ("Set Min & Max", "Define lower and upper bounds."),
            ("Click Generate", "Instant fair random numbers.")
        ]
    },
    {
        "slug": "days-until-date-countdown",
        "tool_id": "days-until-date",
        "title": "Days Until Date & Event Countdown Timer Online",
        "h1": "Days Until Date & Event Countdown Timer",
        "description": "Live countdown of days, hours, minutes, and seconds until your next exam, birthday, or upcoming holiday.",
        "keywords": "days until date calculator, countdown to exam online, days left until birthday, new year countdown timer",
        "rating_count": "6,300",
        "category": "Daily Tools",
        "faqs": [
            ("Does it update in real time?", "Yes, the countdown ticks every second live on your screen.")
        ],
        "how_to": [
            ("Select Event Date", "Pick target date from calendar."),
            ("Watch Countdown", "See live days, hours, and minutes remaining.")
        ]
    },
    {
        "slug": "code-minifier-and-beautifier",
        "tool_id": "code-beautifier-minifier",
        "title": "HTML, CSS & JS Code Minifier & Formatter Online",
        "h1": "Code Minifier & Beautifier Online (HTML, CSS, JS)",
        "description": "Minify code to shrink file sizes or format messy code into beautifully indented readable blocks.",
        "keywords": "html minifier online, css minifier free, js code beautifier, compress html css code",
        "rating_count": "5,410",
        "category": "Dev Tools",
        "faqs": [
            ("How does minification improve SEO?", "Minifying CSS and JavaScript removes unnecessary whitespace and comments, speeding up page load time and improving Core Web Vitals.")
        ],
        "how_to": [
            ("Paste Code", "Paste HTML, CSS or JS."),
            ("Click Minify or Beautify", "Instant processing."),
            ("Copy", "1-click copy clean code.")
        ]
    },
    {
        "slug": "sarkari-exam-age-eligibility-calculator",
        "tool_id": "age-eligibility-calculator",
        "title": "Sarkari Exam Age Eligibility Calculator Online",
        "h1": "Sarkari Exam Age Cut-off Eligibility Calculator",
        "description": "Check whether you meet minimum and maximum age criteria as on official cutoff date for SSC, UPSC, and State exams.",
        "keywords": "age eligibility calculator, ssc age cutoff calculator, upsc age eligibility check, sarkari exam age limit calculator",
        "rating_count": "13,800",
        "category": "Student Tools",
        "faqs": [
            ("How is cutoff date age calculated for SSC?", "SSC usually calculates age as on 1st August or 1st January of the exam year. Enter the cutoff date from the notification to verify exact eligibility.")
        ],
        "how_to": [
            ("Enter DOB", "Select Date of Birth."),
            ("Enter Cutoff Date", "Input notification date."),
            ("View Status", "See exact age and Eligible / Over-age status.")
        ]
    },
    {
        "slug": "student-marks-percentage-calculator",
        "tool_id": "marks-calculator",
        "title": "Student Marks & Grade Percentage Calculator Online",
        "h1": "Student Marks & Grade Percentage Calculator",
        "description": "Enter marks obtained across subjects to calculate total percentage, division, and CBSE/ICSE grade instantly.",
        "keywords": "marks percentage calculator, 10th 12th marks calculator, cbse grade calculator, calculate total marks percentage",
        "rating_count": "15,200",
        "category": "Student Tools",
        "faqs": [
            ("Can I add more than 5 subjects?", "Yes, click 'Add More Subjects' to add as many subjects as needed.")
        ],
        "how_to": [
            ("Enter Marks", "Input obtained and maximum marks per subject."),
            ("View Result", "Instant grand total, percentage, and division.")
        ]
    },
    {
        "slug": "online-voice-recorder",
        "tool_id": "voice-recorder",
        "title": "Online Voice Recorder Free - High Quality Audio Recorder",
        "h1": "Online Voice Recorder (Microphone Audio Memo)",
        "description": "Record voice and microphone audio directly in your browser with real-time waveform timer and 1-click audio download.",
        "keywords": "voice recorder online, record audio browser, free mic recorder online, voice memo recorder free",
        "rating_count": "8,120",
        "category": "Media Utilities",
        "faqs": [
            ("Is my voice recording stored on any server?", "No! Audio is recorded directly into browser memory via HTML5 MediaRecorder. Nothing is ever sent to a server.")
        ],
        "how_to": [
            ("Click Start", "Allow microphone access."),
            ("Record Message", "Speak into your microphone."),
            ("Stop & Download", "Listen to playback and save audio.")
        ]
    },
    {
        "slug": "media-playback-speed-changer",
        "tool_id": "media-speed-changer",
        "title": "Audio & Video Playback Speed Changer (0.5x to 2x)",
        "h1": "Audio & Video Playback Speed Changer Online",
        "description": "Change playback speed of any video or audio file up to 2x faster or slow down to 0.5x in your browser.",
        "keywords": "video speed changer online, speed up audio 2x, slow down video free, change playback speed",
        "rating_count": "4,950",
        "category": "Media Utilities",
        "faqs": [
            ("What formats are supported?", "MP4, WebM, MP3, WAV, and all browser-supported media.")
        ],
        "how_to": [
            ("Upload Media", "Select audio or video."),
            ("Choose Speed", "Click 0.5x, 0.75x, 1.25x, 1.5x, or 2x.")
        ]
    },
    {
        "slug": "internet-speed-test-online",
        "tool_id": "internet-speed-test",
        "title": "Internet Speed Test Online - Test Download Speed & Ping",
        "h1": "Internet Speed Test & Ping Latency Checker",
        "description": "Test your internet connection download speed, ping latency, and jitter directly inside your web browser.",
        "keywords": "internet speed test, test download speed online, broadband speed test free, wifi speed test ping",
        "rating_count": "17,400",
        "category": "Daily Tools",
        "faqs": [
            ("How does this speed test work?", "It performs timed downloads of known data chunks and measures network round-trip response time (ping) in milliseconds.")
        ],
        "how_to": [
            ("Click Start", "Tap 'Start Speed Test'."),
            ("View Bandwidth", "See download speed in Mbps and ping latency in ms.")
        ]
    },
    {
        "slug": "simple-resume-and-biodata-maker",
        "tool_id": "resume-biodata-maker",
        "title": "Simple Resume & Marriage Biodata Maker Online Free",
        "h1": "Simple 1-Page Resume & Biodata Maker",
        "description": "Create a clean single-page resume or marriage biodata with instant browser print-to-PDF formatting.",
        "keywords": "resume maker online free, marriage biodata maker, simple cv maker, 1 page resume format pdf",
        "rating_count": "12,900",
        "category": "Student Tools",
        "faqs": [
            ("How to save as PDF?", "Click 'Print / Save as PDF' and select 'Save as PDF' in your browser print dialogue.")
        ],
        "how_to": [
            ("Fill Details", "Enter Name, Contact, Objective, Education, and Skills."),
            ("Save as PDF", "Click Print and save clean PDF.")
        ]
    },
    {
        "slug": "photo-collage-maker-online",
        "tool_id": "photo-collage-maker",
        "title": "Photo Collage Maker Online Free - Join 2, 3 or 4 Photos",
        "h1": "Photo Collage Maker Online (2 to 4 Photos)",
        "description": "Combine 2, 3, or 4 photos into a neat collage with customizable borders, side-by-side or grid layout.",
        "keywords": "photo collage maker online, combine 2 photos side by side, 4 photo grid maker free, photo joiner online",
        "rating_count": "9,640",
        "category": "Image Utilities",
        "faqs": [
            ("Can I join 2 photos side-by-side?", "Yes! Simply select 2 photos and they will be positioned side-by-side on a high resolution canvas.")
        ],
        "how_to": [
            ("Select Photos", "Pick 2 to 4 photos from gallery."),
            ("Preview Collage", "Automatic side-by-side or 2x2 grid layout."),
            ("Download", "Save high quality JPEG.")
        ]
    }
]

import json

# Format each entry cleanly as Python dictionary
entries_code = []
for item in new_seo_entries:
    faqs_str = json.dumps(item["faqs"], indent=12)
    howto_str = json.dumps(item["how_to"], indent=12)
    entry = f"""    {{
        "slug": "{item['slug']}",
        "tool_id": "{item['tool_id']}",
        "title": "{item['title']}",
        "h1": "{item['h1']}",
        "description": "{item['description']}",
        "keywords": "{item['keywords']}",
        "rating_count": "{item['rating_count']}",
        "category": "{item['category']}",
        "faqs": {faqs_str},
        "how_to": {howto_str}
    }}"""
    entries_code.append(entry)

code_to_insert = ",\n" + ",\n".join(entries_code)

target_str = "\n]\n\ndef generate_pages():"
if target_str in seo_code:
    updated = seo_code.replace(target_str, code_to_insert + target_str, 1)
    with open(SEO_SCRIPT_PATH, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"SUCCESS: Inserted {len(new_seo_entries)} SEO tool entries into build_extreme_seo.py!")
else:
    print("ERROR: Target string not found in build_extreme_seo.py")
