import streamlit as st
from openai import OpenAI

# 1. Налаштування сторінки та ідентифікація для пошуковиків
st.set_page_config(
    page_title="TechDocs AI | Technical Manual Generator",
    page_icon="📄",
    layout="centered"
)

# Клієнт OpenAI (використовує ключ із твоїх Secrets)
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    st.error("API Key missing. Please check Streamlit Secrets.")

# 2. Головний інтерфейс
st.title("📄 Professional Technical Documentation AI")
st.write("Generate high-precision manuals, wiring diagrams, and error codes instantly.")

# Поля для введення даних клієнтом
equipment = st.text_input("Enter Device Model (e.g., Datouboss DN-022, Deye, Victron):")
task = st.text_area("What do you need to configure? (e.g., Battery setup, CAN/RS485 communication)")

if equipment and task:
    st.markdown("---")
    st.warning("🔒 **Professional Documentation Ready.**")
    st.write("To unlock the full technical guide, please complete the secure payment.")

    # 3. КНОПКА PAYPAL (Чітка та зрозуміла для іноземця)
    # Пошта np.kremenchuk.sb@gmail.com автоматично підтягується як отримувач
    paypal_url = f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=np.kremenchuk.sb@gmail.com&currency_code=USD&amount=1.99&item_name=Manual_for_{equipment}"
    
    st.markdown(f'''
        <a href="{paypal_url}" target="_blank">
            <button style="width:100%; height:70px; background-color: #0070ba; color: white; border: none; border-radius: 10px; font-size: 22px; font-weight: bold; cursor: pointer; box-shadow: 0px 4px 15px rgba(0,0,0,0.2);">
                💳 PAY $1.99 VIA PAYPAL
            </button>
        </a>
    ''', unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; color: gray;'>Secure payment via PayPal (Credit Card supported)</p>", unsafe_allow_html=True)
    
    st.info("💡 **Next Step:** After payment, send a screenshot to **np.kremenchuk.sb@gmail.com**. You will receive your PDF manual via email immediately.")

# 4. SEO БЛОК (Щоб сайт знаходили в Google)
st.markdown("---")
st.subheader("🛠️ Supported Brands & Expertise")
st.write("""
Our AI specialized in professional documentation for:
* **Brands**: Datouboss, Deye, Bluetti, Victron Energy, Growatt, Must, Voltronic, PowMr, SRNE.
* **Technical Topics**: Wiring diagrams, BMS protocols, CAN/RS485 setup, Error code troubleshooting.
""")

# 5. Футер (Перекладений)
st.divider()
st.caption("© 2026 TechDocs AI Global. Підтримка та оплата: np.kremenchuk.sb@gmail.com")
st.caption("Your support helps a developer in Ukraine. 🇺🇦")
