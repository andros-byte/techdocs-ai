import streamlit as st
import openai

# 1. Налаштування сторінки
st.set_page_config(page_title="AI Technical Guide", page_icon="🤖", layout="centered")

# 2. Твої дані
openai.api_key = "ТВІЙ_OPENAI_API_KEY" 
MY_PAYPAL_EMAIL = "np.kremenchuk.sb@gmail.com"

# --- СТИЛІЗАЦІЯ ЗЕЛЕНОЇ КНОПКИ ---
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #28a745;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #218838;
        color: white;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Головний інтерфейс
st.title("🤖 AI Technical Guide Assistant")
st.subheader("Професійні технічні інструкції та рекомендації")

# --- КРОК 1: ВВЕДЕННЯ ЗАПИТУ ---
st.write("### 1. Опишіть вашу ситуацію")

example_text = "Наприклад: Помилка F56 інвертора Deye 5кВт, як перевірити налаштування батареї або усунути несправність..."

with st.form("technical_form"):
    user_query = st.text_area(
        "Введіть ваше технічне питання або проблему:", 
        placeholder=example_text,
        height=150
    )
    
    st.markdown(f"""
        <div style="background-color: #e8f0fe; padding: 20px; border-radius: 10px; border: 2px solid #0070ba; text-align: center; margin-top: 10px; margin-bottom: 10px;">
            <p style="font-size: 20px; font-weight: bold; color: #003087; margin: 0;">
                ⚠️ ЩОБ ВІДКРИТИ РОЗДІЛ ОПЛАТИ, НАТИСНІТЬ <span style="color: #d93025;">CTRL + ENTER</span> <br> АБО ЗЕЛЕНУ КНОПКУ НИЖЧЕ
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Ця кнопка тепер жирна та зелена завдяки CSS вище
    submit_button = st.form_submit_button("ЗАФІКСУВАТИ ЗАПИТ")

# --- КРОК 2: ОПЛАТА ТА ШІ ---
if submit_button and user_query:
    st.write("---")
    st.write("### 2. Отримайте професійну рекомендацію")
    st.info("Запит зафіксовано. Тепер ви можете здійснити оплату.")
    st.write("Вартість послуги: **$1.99**")

    payment_url = (
        f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick"
        f"&business={MY_PAYPAL_EMAIL}"
        f"&item_name=Technical%20Recommendation&amount=1.99&currency_code=USD"
    )

    # СОЛІДНА СИНЯ КНОПКА PAYPAL
    st.markdown(f'''
        <a href="{payment_url}" target="_blank" style="text-decoration: none;">
            <div style="
                display: inline-block; 
                padding: 16px 32px; 
                color: #ffffff; 
                background-color: #0070ba; 
                border-radius: 8px; 
                font-weight: bold; 
                font-size: 20px;
                text-align: center; 
                box-shadow: 0px 4px 12px rgba(0,112,186,0.3);
            ">
                Сплатити $1.99 через PayPal
            </div>
        </a>
    ''', unsafe_allow_html=True)

    st.write("")
    st.write("---")
    
    # Кнопка для ШІ (використовуємо інший ключ в CSS, щоб вона не була зеленою, 
    # або залишаємо стандартною Streamlit для контрасту)
    if st.button("Отримати рекомендацію (я вже оплатив)"):
        with st.spinner("Формуємо відповідь..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Ти професійний технічний консультант."},
                        {"role": "user", "content": user_query}
                    ]
                )
                st.write("---")
                st.success("✅ Ваша професійна рекомендація готова:")
                st.write(response.choices[0].message.content)
                st.balloons()
            except Exception as e:
                st.error(f"Помилка: {e}")

elif not user_query and submit_button:
    st.error("Будь ласка, введіть опис проблеми.")

# 4. Футер
st.markdown("---")
st.caption("© 2026 TechDocs Pro — Професійна технічна підтримка")
