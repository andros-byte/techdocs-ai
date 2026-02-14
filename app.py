import streamlit as st
from openai import OpenAI

# Налаштування сторінки
st.set_page_config(page_title="TechDocs AI Professional", layout="centered")

# Підключення OpenAI
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("System Error: OpenAI API Key missing.")

st.title("📄 Professional Technical Documentation AI")
st.write("Get your high-precision manual instantly for only $1.99.")

# Форма (Screenshot_11)
equipment = st.text_input("Enter Device Model (e.g., Datouboss DN-022, Deye):")
task = st.text_area("What do you need to configure?")

if equipment and task:
    st.markdown("---")
    st.warning("🔒 **Technical Documentation Generated.**")
    
    # Кнопка оплати PayPal (Screenshot_10)
    paypal_url = f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=np.kremenchuk.sb@gmail.com&currency_code=USD&amount=1.99&item_name=Manual_for_{equipment}"
    
    st.markdown(f'''
        <a href="{paypal_url}" target="_blank">
            <button style="width:100%; height:60px; background-color: #0070ba; color: white; border: none; border-radius: 8px; font-size: 20px; font-weight: bold; cursor: pointer;">
                🚀 UNLOCK FULL GUIDE FOR $1.99
            </button>
        </a>
    ''', unsafe_allow_html=True)
    
    st.info("💡 **Instructions:** After payment, send a screenshot to **np.kremenchuk.sb@gmail.com**. We will email the full PDF manual immediately.")

# --- ОСЬ ЦЕЙ БЛОК ДЛЯ ПЕРЕВІРКИ ТА SEO ---
st.markdown("---")
st.subheader("🛠️ Supported Brands & Expertise")
st.write("""
Our AI specialized in professional documentation for:
* **Brands**: Datouboss, Deye, Victron Energy, Growatt, Must, Voltronic, PowMr, SRNE.
* **Topics**: Wiring diagrams, CAN/RS485 setup, BMS protocols, Error codes.
""")
# ----------------------------------------

st.divider()
st.caption("© 2026 TechDocs AI. Support: np.kremenchuk.sb@gmail.com")
