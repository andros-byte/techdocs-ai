import streamlit as st
from openai import OpenAI

# 1. Налаштування сторінки та Google Verification (Search Console)
# Ми вставляємо код у title та menu_items, щоб Google міг його побачити
st.set_page_config(
    page_title="TechDocs AI | google-site-verification: BmsbNUrS4gl2qA5tTqT3sexFNz51u0tx3AKMGGhgY_A",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "Technical Manual Generator. Verification: BmsbNUrS4gl2qA5tTqT3sexFNz51u0tx3AKMGGhgY_A"
    }
)

# Клієнт OpenAI (бере ключ із твоїх Secrets)
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    st.error("API Key missing in Streamlit Secrets.")

# 2. Інтерфейс (Screenshot_15)
st.title("📄 Professional Technical Documentation AI")
st.write("Get your high-precision manual instantly for only **$1.99**.")

# Поля для введення (Screenshot_11)
equipment = st.text_input("Enter Device Model (e.g., Datouboss DN-022, Deye, Victron):")
task = st.text_area("What do you need to configure? (e.g., Battery setup, Error codes, Installation)")

if equipment and task:
    st.markdown("---")
    st.warning("🔒 **Technical Documentation Generated.**")
    st.write("To view the full guide, please complete the secure payment below.")
    
    # 3. КНОПКА ОПЛАТИ PAYPAL (Screenshot_10, 15)
    # Посилання автоматично формує запит на твій PayPal
    paypal_url = f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=np.kremenchuk.sb@gmail.com&currency_code=USD&amount=1.99&item_name=Manual_for_{equipment}"
    
    st.markdown(f'''
        <a href="{paypal_url}" target="_blank">
            <button style="width:100%; height:60px; background-color: #0070ba; color: white; border: none; border-radius: 8px; font-size: 20px; font-weight: bold; cursor: pointer; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
                🚀 UNLOCK FULL GUIDE FOR $1.99
            </button>
        </a>
    ''', unsafe_allow_html=True)
    
    st.info("💡 **Instructions:** After payment, please send a screenshot to **np.kremenchuk.sb@gmail.com**. We will email you the full professional manual immediately.")

# 4. SEO БЛОК ДЛЯ GOOGLE ТА BING (Screenshot_15)
# Це допоможе іноземцям знаходити твій сайт через пошук брендів
st.markdown("---")
st.subheader("🛠️ Supported Brands & Expertise")
st.write("""
Our AI specialized in professional documentation for:
* **Brands**: Datouboss, Deye, Victron Energy, Growatt, Must, Voltronic, PowMr, SRNE.
* **Topics**: Wiring diagrams, CAN/RS485 setup, BMS protocols, Error code troubleshooting, Lithium battery configuration.
""")

# 5. Футер
st.divider()
st.caption("© 2026 TechDocs AI Global. Support & Billing: np.kremenchuk.sb@gmail.com")
st.caption("Your support helps a developer in Ukraine. 🇺🇦")
