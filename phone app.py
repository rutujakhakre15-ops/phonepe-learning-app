import re
import streamlit as st

st.set_page_config(
    page_title="PhonePe Learning App",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# PhonePe Learning App — educational prototype only
# This app is not affiliated with or endorsed by PhonePe.
# It does not connect to bank accounts or perform real payments.
# -----------------------------------------------------------------------------

TEXT = {
    "English": {
        "app_name": "PhonePe Learning App",
        "tagline": "Learn digital payments one safe step at a time.",
        "home": "Home",
        "tutorials": "Visual Tutorials",
        "security": "OTP & Security",
        "detector": "Scam Message Checker",
        "faq": "FAQs & Help",
        "language": "Language / भाषा",
        "welcome": "Welcome!",
        "welcome_body": "Build confidence with simple lessons. You can learn at your own pace.",
        "important": "Important safety note",
        "important_body": "This is an independent learning project, not the official PhonePe app. Never enter your real OTP, UPI PIN, password, or bank details here.",
        "start": "Start learning",
        "choose_lesson": "Choose a lesson",
        "lesson": "Lesson",
        "step": "Step",
        "previous": "Previous",
        "next": "Next",
        "finish": "You have completed this demo lesson!",
        "analyzer_title": "Check a suspicious message",
        "analyzer_help": "Paste the message after removing personal details. This demo checks for common warning signs; it cannot prove whether a message is genuine.",
        "analyze": "Analyze message",
        "clear": "Clear text",
        "your_message": "Suspicious SMS / WhatsApp / email text",
        "empty": "Paste a message first, then select Analyze message.",
        "privacy": "Privacy reminder: Do not paste OTPs, UPI PINs, passwords, card numbers, account numbers, or other private information.",
        "faq_search": "Search for a question or topic",
    },
    "हिंदी": {
        "app_name": "PhonePe सीखने वाला ऐप",
        "tagline": "डिजिटल भुगतान सुरक्षित तरीके से, एक-एक कदम सीखें।",
        "home": "होम",
        "tutorials": "वीडियो और चरण-दर-चरण सीखें",
        "security": "OTP और सुरक्षा",
        "detector": "संदेश की जाँच",
        "faq": "सामान्य प्रश्न और मदद",
        "language": "भाषा / Language",
        "welcome": "स्वागत है!",
        "welcome_body": "सरल पाठों से आत्मविश्वास बढ़ाएँ। अपनी गति से सीखें।",
        "important": "ज़रूरी सुरक्षा सूचना",
        "important_body": "यह एक स्वतंत्र शैक्षिक प्रोजेक्ट है, आधिकारिक PhonePe ऐप नहीं। यहाँ अपना असली OTP, UPI PIN, पासवर्ड या बैंक विवरण न डालें।",
        "start": "सीखना शुरू करें",
        "choose_lesson": "पाठ चुनें",
        "lesson": "पाठ",
        "step": "चरण",
        "previous": "पिछला",
        "next": "अगला",
        "finish": "आपने यह डेमो पाठ पूरा कर लिया है!",
        "analyzer_title": "संदिग्ध संदेश की जाँच करें",
        "analyzer_help": "निजी जानकारी हटाकर संदेश पेस्ट करें। यह डेमो सामान्य चेतावनी संकेत ढूँढता है; यह संदेश की सत्यता साबित नहीं कर सकता।",
        "analyze": "संदेश जाँचें",
        "clear": "टेक्स्ट हटाएँ",
        "your_message": "SMS / WhatsApp / ईमेल संदेश",
        "empty": "पहले संदेश पेस्ट करें, फिर संदेश जाँचें चुनें।",
        "privacy": "गोपनीयता: OTP, UPI PIN, पासवर्ड, कार्ड या बैंक खाता नंबर जैसी निजी जानकारी पेस्ट न करें।",
        "faq_search": "प्रश्न या विषय खोजें",
    },
    "मराठी": {
        "app_name": "PhonePe शिकण्याचे अॅप",
        "tagline": "डिजिटल पेमेंट सुरक्षितपणे, एका वेळी एक पाऊल शिका.",
        "home": "मुख्यपृष्ठ",
        "tutorials": "चित्रांसह मार्गदर्शन",
        "security": "OTP आणि सुरक्षा",
        "detector": "संशयास्पद संदेश तपासा",
        "faq": "प्रश्न आणि मदत",
        "language": "भाषा / Language",
        "welcome": "स्वागत आहे!",
        "welcome_body": "सोप्या धड्यांमधून आत्मविश्वास वाढवा. आपल्या गतीने शिका.",
        "important": "महत्त्वाची सुरक्षा सूचना",
        "important_body": "हा स्वतंत्र शैक्षणिक प्रकल्प आहे; अधिकृत PhonePe अॅप नाही. येथे खरा OTP, UPI PIN, पासवर्ड किंवा बँक तपशील टाकू नका.",
        "start": "शिकायला सुरुवात करा",
        "choose_lesson": "धडा निवडा",
        "lesson": "धडा",
        "step": "टप्पा",
        "previous": "मागे",
        "next": "पुढे",
        "finish": "हा प्रात्यक्षिक धडा पूर्ण झाला!",
        "analyzer_title": "संशयास्पद संदेश तपासा",
        "analyzer_help": "वैयक्तिक माहिती काढून टाकल्यानंतर संदेश पेस्ट करा. हे डेमो सामान्य धोक्याची चिन्हे शोधते; संदेश खरा आहे याची खात्री देत नाही.",
        "analyze": "संदेश तपासा",
        "clear": "मजकूर पुसा",
        "your_message": "SMS / WhatsApp / ईमेल संदेश",
        "empty": "आधी संदेश पेस्ट करा आणि नंतर संदेश तपासा निवडा.",
        "privacy": "गोपनीयता: OTP, UPI PIN, पासवर्ड, कार्ड किंवा बँक खाते क्रमांक पेस्ट करू नका.",
        "faq_search": "प्रश्न किंवा विषय शोधा",
    },
}

LESSONS = {
    "Check transaction history": [
        ("Open the PhonePe app on your own phone.", "MOCK PHONE SCREEN\n\nPhonePe\n\n[ Home ]   [ History ]\n\nThis is a sample screen, not a live PhonePe screen."),
        ("Choose the History option. Look for the transaction list.", "MOCK HISTORY SCREEN\n\nRecent activity\n\n• Example payment — ₹100\n• Example recharge — ₹199\n\nAll entries above are fictional."),
        ("Select a transaction to read its status and details. Never share a screenshot containing private information.", "MOCK TRANSACTION DETAILS\n\nStatus: Successful (sample)\nAmount: ₹100 (sample)\n\nDo not use this mock screen as proof of payment."),
    ],
    "Send money safely (demo only)": [
        ("Open the app and choose the option to pay a person. Check that you selected the intended contact.", "MOCK PAYMENT SCREEN\n\nPay a contact\n\n[ Select contact ]\n\nNo real contact or payment is available in this demo."),
        ("Check the recipient name and amount carefully before proceeding.", "MOCK REVIEW SCREEN\n\nRecipient: Example Person\nAmount: ₹10 (sample)\n\nAlways verify the recipient independently."),
        ("Only enter your UPI PIN inside your genuine payment app when you are intentionally making a payment. Never tell it to another person.", "SECURITY CHECK\n\nUPI PIN: Never share\nOTP: Never share\n\nThis learning app will never ask for either."),
    ],
    "Understand QR codes": [
        ("A QR code can be used to identify a payment recipient. Scan only when you intend to pay.", "MOCK SCAN SCREEN\n\n[ Camera preview placeholder ]\n\nThis is not a working scanner."),
        ("After scanning, read the recipient name and amount shown in your payment app. Stop if anything looks unexpected.", "MOCK REVIEW\n\nRecipient: Example Shop\nAmount: Check before paying\n\nNever approve a payment you did not intend."),
        ("Remember: scanning a QR code is not a way to receive money. Be cautious if someone asks you to scan a code to collect a refund or prize.", "REMEMBER\n\nScan only when you intend to pay.\nA QR scan does not mean money is being received."),
    ],
    "Understand bank account settings": [
        ("Open the payment app and find its bank-account or payment-settings area.", "MOCK SETTINGS SCREEN\n\nBank accounts\nPayment settings\n\nDo not share account details or screenshots publicly."),
        ("Check the bank name and masked account information. Use only the official app on your own device.", "MOCK BANK DETAILS\n\nBank: Example Bank\nAccount: XXXX XXXX 1234\n\nAll details are fictional."),
        ("Never install an app or share your screen because a caller says they need to help link your bank account.", "SAFETY REMINDER\n\nDo not install unknown apps.\nDo not give remote access to strangers."),
    ],
}

FAQS = [
    ("Someone asks me for an OTP. What should I do?", "Do not share it. A genuine support representative should not ask you to tell them your OTP. End the conversation and contact the service through its official app or website."),
    ("Can I scan a QR code to receive money?", "Be careful. A QR code used in a payment flow is commonly part of paying someone. Do not scan a code or enter a UPI PIN just because a stranger says it will help you receive a refund or prize."),
    ("I received a payment screenshot. Is that proof?", "A screenshot can be edited or misleading. Check the transaction in your own app or bank account before handing over goods or treating a payment as received."),
    ("A caller says my account will be blocked unless I act now.", "Urgency and threats are common pressure tactics. Do not click their link or share details. Contact the provider using the official app or a number from its official website."),
    ("What should I do after entering my UPI PIN on a suspicious screen?", "Contact your bank immediately using its official channel, explain what happened, and ask about blocking or disputing the transaction. In India, you can also report suspected cyber financial fraud through the official cybercrime helpline 1930 or the National Cyber Crime Reporting Portal."),
    ("How do I know whether a message is genuine?", "Do not rely on the sender name or logo alone. Check through the official app or website that you open yourself, not through a link in the message."),
]

# Simple local rule-based warning-sign checker. It is not an AI model and cannot
# determine with certainty whether any message is genuine or fraudulent.
RULES = [
    ("Urgency or threats", r"\b(urgent|immediately|right now|act now|within\s*\d+\s*(hour|minute|day)s?|account (will be )?(blocked|suspended)|last warning|आज ही|तुरंत|तात्काळ)\b", "The message pressures you to act quickly or threatens a consequence."),
    ("OTP / PIN / password request", r"\b(otp|one[- ]time password|upi pin|mpin|cvv|password|verification code)\b", "It mentions sensitive authentication details. Never tell these to another person or enter them on a page opened from an unsolicited message."),
    ("Suspicious link", r"https?://|www\.|bit\.ly|tinyurl|t\.co", "It contains a link. Do not open unexpected links; visit the official app or type the official website address yourself."),
    ("Remote-access request", r"\b(anydesk| teamviewer|quick support|screen.?share|remote access|apk install|install this app)\b", "It may be asking you to install an app or give someone access to your screen or device."),
    ("Prize / refund / cashback bait", r"\b(prize|lottery|winner|free gift|cashback|refund|reward|claim your|lucky draw)\b", "Unexpected rewards or refunds can be used to lure people into clicking links or authorizing payments."),
    ("Request to scan a code or approve a collect request", r"\b(scan (this )?(qr|code)|receive money|collect request|approve payment|refund through qr)\b", "The message may be asking you to approve or initiate a payment under the pretext of receiving money."),
    ("Unusual payment or bank-detail request", r"\b(send money|transfer now|bank details|account number|card number|pay a fee)\b", "It asks for money or financial details. Verify the request independently before taking any action."),
]


def t(key: str) -> str:
    return TEXT[st.session_state.get("language", "English")].get(key, TEXT["English"].get(key, key))


def analyze_message(message: str):
    findings = []
    for title, pattern, explanation in RULES:
        if re.search(pattern, message, flags=re.IGNORECASE):
            findings.append((title, explanation))
    return findings


def render_lesson_card(title: str, description: str, icon: str):
    st.markdown(
        f"""
        <div class="lesson-card">
          <div class="lesson-icon">{icon}</div>
          <div><div class="lesson-title">{title}</div><div class="muted">{description}</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
      html, body, [class*="css"] { font-family: Inter, sans-serif; }
      .stApp { background: #f6f8fc; }
      .block-container { max-width: 1120px; padding-top: 1.5rem; padding-bottom: 3rem; }
      .hero { background: linear-gradient(120deg,#5b21b6,#7c3aed); color: white; padding: 2rem; border-radius: 22px; }
      .hero h1 { color: white; font-size: clamp(1.8rem,4vw,2.7rem); margin-bottom: .4rem; }
      .hero p { color: #f3e8ff; font-size: 1.08rem; margin-bottom: 0; }
      .notice { background: #fff7e6; border: 1px solid #f5d58c; border-left: 6px solid #d97706; border-radius: 12px; padding: 1rem 1.1rem; color: #422006; }
      .lesson-card { display:flex; align-items:center; gap:16px; background:white; border:1px solid #e5e7eb; border-radius:16px; padding:17px; margin:8px 0; min-height:92px; }
      .lesson-icon { min-width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center; background:#f3e8ff; font-size:26px; }
      .lesson-title { font-size:1.08rem; font-weight:750; color:#1f2937; margin-bottom:4px; }
      .muted { color:#5b6472; font-size:.96rem; }
      .mock-screen { background:#171923; color:#f8fafc; border:5px solid #303545; border-radius:26px; padding:24px 18px; min-height:280px; white-space:pre-wrap; font-family:monospace; line-height:1.8; box-shadow:0 10px 24px #11182722; }
      .safe-box { background:#ecfdf5; border:1px solid #a7f3d0; border-radius:14px; padding:14px 16px; color:#064e3b; }
      .warning-box { background:#fff7ed; border:1px solid #fed7aa; border-radius:14px; padding:14px 16px; color:#7c2d12; }
      div.stButton > button { border-radius:12px; min-height:46px; font-weight:650; }
      .small-label { color:#6b7280; font-size:.85rem; }
      h1, h2, h3 { letter-spacing:-.02em; }
      @media (max-width: 700px) { .hero { padding:1.35rem; } .lesson-card { align-items:flex-start; } }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.markdown("# 📱 Learn safely")
    language = st.selectbox(t("language"), list(TEXT.keys()), index=list(TEXT.keys()).index(st.session_state.get("language", "English")))
    st.session_state.language = language
    pages = [t("home"), t("tutorials"), t("security"), t("detector"), t("faq")]
    page = st.radio("Menu", pages, label_visibility="collapsed")
    st.divider()
    st.caption("Independent educational prototype • No real payments")

# Header
st.markdown(f"<div class='small-label'>{t('app_name')}</div>", unsafe_allow_html=True)

if page == t("home"):
    st.markdown(
        f"<div class='hero'><h1>{t('welcome')}</h1><p>{t('tagline')}<br>{t('welcome_body')}</p></div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(f"<div class='notice'><strong>⚠️ {t('important')}</strong><br>{t('important_body')}</div>", unsafe_allow_html=True)
    st.write("")
    st.subheader("Choose what you want to learn")
    col1, col2 = st.columns(2)
    with col1:
        render_lesson_card("Visual tutorials", "Practice common tasks using fictional sample screens.", "📘")
        render_lesson_card("OTP & security", "Understand OTPs, UPI PINs, and safe habits.", "🔐")
    with col2:
        render_lesson_card("Scam message checker", "Look for warning signs in a suspicious message.", "🛡️")
        render_lesson_card("FAQs & troubleshooting", "Find simple answers to common questions.", "💬")
    st.write("")
    st.markdown("### Three rules to remember")
    a, b, c = st.columns(3)
    a.markdown("<div class='safe-box'><strong>1. Keep secrets private</strong><br>Never share OTPs or UPI PINs.</div>", unsafe_allow_html=True)
    b.markdown("<div class='safe-box'><strong>2. Pause before paying</strong><br>Check the recipient and amount.</div>", unsafe_allow_html=True)
    c.markdown("<div class='safe-box'><strong>3. Verify independently</strong><br>Use the official app or website.</div>", unsafe_allow_html=True)

elif page == t("tutorials"):
    st.title("📚 Visual Tutorials")
    st.write("Follow one step at a time. The screens below are fictional examples for learning—not screenshots of the live PhonePe app.")
    lesson_name = st.selectbox(t("choose_lesson"), list(LESSONS.keys()))
    steps = LESSONS[lesson_name]
    state_key = f"step_{lesson_name}"
    if state_key not in st.session_state:
        st.session_state[state_key] = 0
    current = st.session_state[state_key]
    current = max(0, min(current, len(steps) - 1))
    st.progress((current + 1) / len(steps), text=f"{t('step')} {current + 1} of {len(steps)}")
    left, right = st.columns([1.1, 1])
    with left:
        st.markdown(f"### {t('step')} {current + 1}: {steps[current][0]}")
        st.info("Take your time. Read the instruction before moving to the next step.")
        if current == len(steps) - 1:
            st.success(t("finish"))
    with right:
        st.markdown(f"<div class='mock-screen'>{steps[current][1]}</div>", unsafe_allow_html=True)
    nav1, nav2, nav3 = st.columns([1, 1, 2])
    with nav1:
        if st.button(f"← {t('previous')}", disabled=current == 0, use_container_width=True):
            st.session_state[state_key] = max(0, current - 1)
            st.rerun()
    with nav2:
        if st.button(f"{t('next')} →", disabled=current == len(steps) - 1, type="primary", use_container_width=True):
            st.session_state[state_key] = min(len(steps) - 1, current + 1)
            st.rerun()
    with nav3:
        if st.button("Restart lesson", use_container_width=True):
            st.session_state[state_key] = 0
            st.rerun()
    st.caption("Video tutorial slot: add a reviewed, accessible video URL here when you have permission to use it.")

elif page == t("security"):
    st.title("🔐 OTP & Security Guide")
    st.write("An OTP (one-time password) is a temporary code used to confirm certain actions. Treat it like a key to your account.")
    st.markdown("### Never share these details")
    st.error("Never tell anyone your OTP, UPI PIN, ATM PIN, CVV, or password—not even someone claiming to be customer support, a bank employee, or a police officer.")
    st.markdown("### Safe payment habits")
    habits = [
        "Enter your UPI PIN only inside your trusted payment app when you are intentionally making a payment.",
        "Check the recipient name and amount before approving a payment.",
        "A QR code or collect request can lead to a payment. Do not approve one just to receive a refund or prize.",
        "Do not install remote-access apps or share your screen with unknown callers.",
        "Do not open unexpected links. Open the official app yourself to check account or transaction status.",
        "Keep your phone lock and app updates enabled. Never let another person operate your payment app unsupervised.",
    ]
    for habit in habits:
        st.markdown(f"- {habit}")
    st.markdown("### If you think a payment scam has happened")
    st.warning("Contact your bank immediately through its official channel. In India, report suspected cyber financial fraud by calling **1930** as soon as possible, and use the National Cyber Crime Reporting Portal. Keep transaction references and messages for the report; do not forward OTPs or PINs to anyone.")
    st.caption("This is general safety education, not financial or legal advice. Use official government and bank channels for urgent assistance.")

elif page == t("detector"):
    st.title(f"🛡️ {t('analyzer_title')}")
    st.write(t("analyzer_help"))
    st.markdown(f"<div class='warning-box'>🔒 {t('privacy')}</div>", unsafe_allow_html=True)
    message = st.text_area(t("your_message"), height=190, placeholder="Example: Your account will be blocked today. Click this link to update KYC and share your OTP...")
    c1, c2 = st.columns([1, 1])
    with c1:
        analyze_clicked = st.button(t("analyze"), type="primary", use_container_width=True)
    with c2:
        clear_clicked = st.button(t("clear"), use_container_width=True)
    if clear_clicked:
        st.session_state.pop("last_message_analysis", None)
        st.rerun()
    if analyze_clicked:
        if not message.strip():
            st.info(t("empty"))
        else:
            findings = analyze_message(message)
            st.session_state.last_message_analysis = {
                "findings": findings,
                "message": message,
            }
    if "last_message_analysis" in st.session_state:
        findings = st.session_state.last_message_analysis["findings"]
        st.divider()
        if len(findings) >= 3:
            st.error("High caution: several common warning signs were found.")
        elif len(findings) >= 1:
            st.warning("Caution: one or more warning signs were found.")
        else:
            st.info("No common warning signs were detected by this simple demo. That does NOT mean the message is safe or genuine.")
        if findings:
            st.markdown("### Why it may be suspicious")
            for title, explanation in findings:
                st.markdown(f"**{title}** — {explanation}")
        st.markdown("### What to do next")
        st.markdown("1. Do not reply, click the link, scan a code, install an app, or approve a payment from the message.\n2. Do not share OTPs, UPI PINs, passwords, or financial details.\n3. Open the official app yourself or contact your bank using a trusted official number.\n4. Ask a trusted person for help if you are unsure.")
        st.caption("Prototype limitation: this is a keyword/rule-based educational checker, not a verified scam-detection service. It can miss scams and can flag legitimate messages. Never make a financial decision based only on this result.")

elif page == t("faq"):
    st.title("💬 FAQs & Troubleshooting")
    query = st.text_input(t("faq_search"), placeholder="Try: OTP, QR code, screenshot, blocked account...")
    filtered = [(q, a) for q, a in FAQS if query.lower() in (q + " " + a).lower()] if query.strip() else FAQS
    if not filtered:
        st.info("No matching question found. Try a shorter search term.")
    for question, answer in filtered:
        with st.expander(question):
            st.write(answer)
    st.markdown("### Still unsure?")
    st.info("Pause before acting. Ask a trusted family member or visit your bank's official branch/support channel. Never let a stranger take control of your phone.")

st.divider()
st.caption("PhonePe Learning App • Student learning prototype • Not affiliated with PhonePe • No real payments, bank login, or account linking")
