import streamlit as st
from openai import OpenAI

# Налаштування
st.set_page_config(page_title="TechDocs AI Professional", layout="centered")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("📄 Professional Technical Documentation AI")
st.write("Get your high-precision manual instantly for only $1.99.")

# Поля введення
equipment = st.text_input("Enter Device Model (e.g., Datouboss DN-022):")
task = st.text_area("What do you need to configure?")

if equipment and task:
    st.warning("🔒 Technical documentation generated. Please complete payment to view.")
    
    # Кнопка прямої оплати (працює БЕЗ Client ID)
    paypal_url = f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=np.kremenchuk.sb@gmail.com&currency_code=USD&amount=1.99&item_name=Manual_for_{equipment}"
    
    st.markdown(f'''
        <a href="{paypal_url}" target="_blank">
            <button style="width:100%; height:50px; background-color: #0070ba; color: white; border: none; border-radius: 5px; font-size: 18px; font-weight: bold; cursor: pointer;">
                PAY $1.99 VIA PAYPAL
            </button>
        </a>
    ''', unsafe_allow_html=True)
    
    st.info("💡 After payment, please send a screenshot to np.kremenchuk.sb@gmail.com. We will send the full PDF manual to your email immediately.")

st.divider()
st.caption("© 2026 TechDocs AI. Billing: np.kremenchuk.sb@gmail.com")
