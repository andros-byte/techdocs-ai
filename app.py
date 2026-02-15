import streamlit as st
import openai

# 1. Налаштування сторінки
st.set_page_config(page_title="AI Technical Guide", page_icon="🤖", layout="centered")

# 2. Твої дані (Screenshot_60, Screenshot_61)
openai.api_key = "ТВІЙ_OPENAI_API_KEY" 
MY_PAYPAL_EMAIL = "np.kremenchuk.sb@gmail.com"

# 3. Інтерфейс
st.title("🤖 AI Technical Guide Assistant")
st.subheader("Професійні технічні інструкції та рекомендації")

# --- КРОК 1: ВВЕДЕННЯ ЗАПИТУ ---
st.write("### 1. Опишіть вашу ситуацію")

# Приклад, який завжди в полі (Screenshot_66)
example_text = "Наприклад: Помилка F56 інвертора Deye 5кВт, як перевірити налаштування батареї або усунути несправність..."

# Використовуємо st.form, щоб розділ 2 відкривався ТІЛЬКИ після натискання кнопки або Ctrl+Enter
with st.form("technical_form"):
    user_query = st.text_area(
        "Введіть ваше технічне питання або проблему:", 
        placeholder=example_text,
        height=150
    )
    
    # Велика підказка, як на Screenshot_69
    st.markdown("""
        <div style="background-color: #e8f0fe; padding: 15px; border-radius: 10px; border: 2px solid #0070ba; text-align: center;">
            <p style="font-size: 22px; font-weight: bold; color: #003087; margin: 0;">
                ⚠️ ЩОБ ВІДКРИТИ РОЗДІЛ ОПЛАТИ, НАТИСНІТЬ <span style="color: #d93025;">CTRL + ENTER</span>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Прихована кнопка для обробки форми
    submit_button = st.form_submit_button("Зафіксувати запит")

# --- КРОК 2: ОПЛАТА ТА ШІ (З'являються ТІЛЬКИ після натискання Ctrl+Enter) ---
if submit_button and user_query:
    st.write("---")
    st.write("### 2. Отримайте професійну рекомендацію")
    st.info("Запит зафіксовано. Тепер ви можете здійснити оплату.")
    st.write("Вартість послуги: **$1.99**")

    # Формування посилання PayPal
    item_description = f"Technical Recommendation: {user_query[:40]}..."
    payment_url = (
        f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick"
        f"&business={MY_PAYPAL_EMAIL}"
        f"&item_name={item_description}"
        f"&amount=1.99"
        f"&currency_code=USD"
    )

    # СОЛІДНА СИНЯ КНОПКА (Screenshot_69)
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
    
    if st.button("Отримати рекомендацію (я вже оплатив)"):
        with st.spinner("Формуємо професійну інструкцію..."):
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
elif not user_query:
    st.info(f"💡 Підказка: {example_text}")

# 4. Футер (Screenshot_63)
st.markdown("---")
st.caption("© 2026 TechDocs Pro — Професійна технічна підтримка")
