import streamlit as st
import streamlit.components.v1 as components
from openai import OpenAI

# 1. ПІДТВЕРДЖЕННЯ GOOGLE (Твій персональний код)
components.html("""
<meta name="google-site-verification" content="BmsbNUrS4gl2qA5tTqT3sexFNz51u0tx3AKMGGhgY_A" />
""", height=0)

# Налаштування сторінки
st.set_page_config(page_title="TechDocs AI Professional", layout="centered")

# Клієнт OpenAI
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("System Error: OpenAI API Key missing.")

st.title("📄 Professional Technical Documentation AI")
st.write("Get your high-precision manual instantly for only $1.99.")

# Форма замовлення (Screenshot_11)
equipment = st.text_input("Enter Device Model (e.g., Datouboss DN-022, Victron, Deye):")
task = st.text_area("What do you need to configure? (e.g., Battery setup, Error codes, Installation)")

if equipment and task:
    st.markdown("---")
    st.warning("🔒 **Technical Documentation Generated.**")
    
    # Кнопка оплати PayPal (Screenshot_15)
    paypal_url = f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=np.kremenchuk.sb@gmail.com&currency_code=USD&amount=1.99&item_name=Manual_for_{equipment}"
    
    st.markdown(f'''
        <a href="{paypal_url}" target="_blank">
            <button style="width:100%; height:60px; background-color: #0070ba; color: white; border: none; border-radius: 8px; font-size: 20px; font-weight: bold; cursor: pointer; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
                🚀 UNLOCK FULL GUIDE FOR $1.99
            </button>
        </a>
    ''', unsafe_allow_html=True)
    
    st.info("💡 **Instructions:** After payment, send a screenshot to **np.kremenchuk.sb@gmail.com**. We will email the full PDF manual immediately.")

# 2. БЛОК SUPPORTED BRANDS ДЛЯ SEO
st.markdown("---")
st.subheader("🛠️ Supported Brands & Expertise")
st.write("""
Our AI specialized in professional documentation for:
* **Brands**: Datouboss, Deye, Victron Energy, Growatt, Must, Voltronic, PowMr, SRNE.
* **Topics**: Wiring diagrams, CAN/RS485 setup, BMS protocols, Error codes, Lithium battery configuration.
""")

st.divider()
st.caption("© 2026 TechDocs AI. Billing: np.kremenchuk.sb@gmail.com")
st.caption("Your support helps a developer in Ukraine. 🇺🇦")
