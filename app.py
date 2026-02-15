import streamlit as st
import openai

# 1. Налаштування сторінки
st.set_page_config(
    page_title="AI Technical Guide",
    page_icon="🤖",
    layout="centered"
)

# 2. Твої дані (OpenAI та PayPal)
# Не забудь вставити свій ключ OpenAI
openai.api_key = "ТВІЙ_OPENAI_API_KEY" 
MY_PAYPAL_EMAIL = "np.kremenchuk.sb@gmail.com"

# 3. Головний інтерфейс
st.title("🤖 AI Technical Guide Assistant")
st.subheader("Професійні технічні інструкції та рекомендації")

# --- КРОК 1: ВВЕДЕННЯ ЗАПИТУ ---
st.write("### 1. Опишіть вашу ситуацію")

# Цей текст БУДЕ ЗАВЖДИ в полі, поки користувач не почне писати
example_text = "Наприклад: Помилка F56 інвертора Deye 5кВт, як перевірити налаштування батареї або усунути несправність..."

user_query = st.text_area(
    "Введіть ваше технічне питання або проблему:", 
    placeholder=example_text,
    height=150
)

# --- ВЕЛИКА ІНСТРУКЦІЯ (з'являється, коли користувач почав писати) ---
if user_query:
    st.markdown("""
        <div style="background-color: #e8f0fe; padding: 20px; border-radius: 10px; border: 2px solid #0070ba; text-align: center; margin-top: 10px;">
            <p style="font-size: 24px; font-weight: bold; color: #003087; margin: 0;">
                ⚠️ ЩОБ ПРОДОВЖИТИ, НАТИСНІТЬ <span style="color: #d93025;">CTRL + ENTER</span>
            </p>
            <p style="font-size: 16px; color: #5f6368; margin-top: 5px;">
                Це зафіксує ваш запит і відкриє розділ оплати
            </p>
        </div>
    """, unsafe_allow_html=True)
else:
    # Коли поле порожнє, нагадуємо про введення
    st.info(f"💡 Підказка: {example_text}")

# --- КРОК 2: ОПЛАТА ТА ГЕНЕРАЦІЯ ---
if user_query:
    st.write("---")
    st.write("### 2. Отримайте професійну рекомендацію")
    st.info("Для формування персональної відповіді на ваш запит, будь ласка, здійсніть оплату.")
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

    # ПРОФЕСІЙНА СИНЯ КНОПКА
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
    
    if st.button("Отримати рекомендацію (я вже оплатив)"):
        with st.spinner("Аналізуємо дані та формуємо професійну інструкцію..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Ти професійний технічний консультант. Надавай відповіді українською мовою, якщо запит був українською."},
                        {"role": "user", "content": user_query}
                    ]
                )
                st.write("---")
                st.success("✅ Ваша професійна рекомендація готова:")
                st.write(response.choices[0].message.content)
                st.balloons()
            except Exception as e:
                st.error(f"Технічна помилка: {e}")

# 4. Футер
st.markdown("---")
st.caption("© 2026 TechDocs Pro — Професійна технічна підтримка")
