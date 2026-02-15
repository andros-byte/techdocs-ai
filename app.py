import streamlit as st

# Налаштування сторінки
st.set_page_config(page_title="TechDocs Pro - Expert Inverter Solutions", layout="centered")

# Заголовок сайту
st.title("🛠️ TechDocs Pro")
st.subheader("Deep Troubleshooting & Optimization Manuals")

st.write("---")

# Опис послуги
st.markdown("""
### Get your professional technical guide
Enter your inverter model and the error code or problem you are facing. 
Our AI-expert system will generate a precise step-by-step solution for your specific case.
""")

# Поле для введення запиту клієнта
user_query = st.text_area("Describe your problem (e.g., Deye 15kW Error 05 or Battery BMS communication issue):")

st.write("---")

# БЛОК ПРО ДОСТАВКУ (Delivery Info)
st.info("""
**🕒 Delivery & Quality Guarantee:**
Standard delivery time is usually **15–20 minutes**. However, since every expert guide is processed manually to ensure technical accuracy, please allow **1 to 8 hours** for delivery, depending on time zone differences. We appreciate your patience in providing you with the most reliable solution.
""")

# Кнопка оплати (Заміни 'YOUR_PAYPAL_LINK' на своє реальне посилання з PayPal)
paypal_url = "https://www.paypal.com/ncp/payment/YOUR_PAYPAL_CODE" # ТУТ ТВОЄ ПОСИЛАННЯ

if st.button("🚀 Get Expert Guide for $1.99"):
    if user_query:
        st.success("Request received! Please proceed with the payment below.")
        st.markdown(f'<a href="{paypal_url}" target="_blank" style="display: inline-block; padding: 12px 24px; background-color: #0070ba; color: white; text-align: center; text-decoration: none; font-size: 18px; border-radius: 4px;">Pay with PayPal</a>', unsafe_allow_html=True)
        st.info("After payment, your manual will be sent to your PayPal email address.")
    else:
        st.warning("Please describe your problem first so we can prepare the right manual.")

st.write("---")

# Футер
st.caption("© 2026 TechDocs Pro Services. Expert support for Solar & Inverter systems.")
