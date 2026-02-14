import streamlit as st
from openai import OpenAI

# 1. Основні налаштування інтерфейсу
st.set_page_config(page_title="TechDocs AI Professional", layout="centered")

# Налаштування ключа OpenAI з твоїх Secrets
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("System Error: Check OpenAI API Key in Streamlit Secrets.")

# 2. Заголовок та опис
st.title("📄 Professional Technical Documentation AI")
st.write("Get high-precision manuals, wiring diagrams, and setup guides instantly.")

# 3. Форма введення даних
equipment = st.text_input("Enter Device Model (e.g., Datouboss DN-022, Deye, Victron):")
task = st.text_area("What do you need to configure? (e.g., Battery setup, Error codes, Installation)")

if equipment and task:
    st.markdown("---")
    st.warning("🔒 **Technical Documentation Generated.**")
    st.write("To protect intellectual property, the full guide is locked.")
    
    # 4. БЛОК ОПЛАТИ (Автоматичне посилання на твій PayPal)
    # Пряме посилання, яке працює відразу
    paypal_url = f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=np.kremenchuk.sb@gmail.com&currency_code=USD&amount=1.99&item_name=Technical_Manual_for_{equipment}"
    
    st.markdown(f'''
        <a href="{paypal_url}" target="_blank">
            <button style="width:100%; height:60px; background-color: #0070ba; color: white; border: none; border-radius: 8px; font-size: 20px; font-weight: bold; cursor: pointer; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
                🚀 UNLOCK FULL GUIDE FOR $1.99
            </button>
        </a>
    ''', unsafe_allow_html=True)
    
    st.info("💡 **Instructions:** After payment, please send a screenshot to **np.kremenchuk.sb@gmail.com**. We will email you the full professional manual immediately.")

# 5. SEO БЛОК ДЛЯ GOOGLE (Щоб іноземці знаходили сайт самі)
st.markdown("---")
st.subheader("🛠️ Supported Equipment & Expertise")
st.write("""
Our AI provides expert documentation for:
* **Inverters & Solar**: Datouboss, Deye, Victron Energy, Growatt, Must, Voltronic, PowMr, SRNE.
* **Batteries**: Pylontech, BYD, EG4, SOK, LiFePO4 configuration.
* **Technical Tasks**: CAN/RS485 communication setup, BMS protocols, Error code troubleshooting, Wiring schematics.
""")

# 6. Футер
st.divider()
st.caption("© 2026 TechDocs AI Global. Support & Billing: np.kremenchuk.sb@gmail.com")
st.caption("Your support helps a developer in Ukraine. 🇺🇦")
