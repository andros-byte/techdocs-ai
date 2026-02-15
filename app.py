import streamlit as st
import openai

# 1. Налаштування сторінки
st.set_page_config(
    page_title="AI Technical Guide",
    page_icon="🤖",
    layout="centered"
)

# 2. Твої дані (OpenAI та PayPal)
openai.api_key = "ТВІЙ_OPENAI_API_KEY" 
MY_PAYPAL_EMAIL = "np.kremenchuk.sb@gmail.com"

# 3. Головний інтерфейс
st.title("🤖 AI Technical Guide Assistant")
st.subheader("Професійні технічні інструкції та рекомендації")

# --- КРОК 1: ВВЕДЕННЯ ЗАПИТУ ---
st.write("### 1. Опишіть вашу ситуацію")

placeholder_text = "Наприклад: Помилка F56 інвертора Deye 5кВт, як перевірити налаштування батареї або усунути несправність..."

user_query = st.text_area(
    "Введіть ваше технічне питання або проблему:", 
    placeholder=placeholder_text,
    height=150
)

# --- ДОДАНО: ІНСТРУКЦІЯ ДЛЯ ПІДТВЕРДЖЕННЯ ---
if not user_query:
    st.warning("⚠️ Введіть опис проблеми вище.")
else:
    # Великий і жирний напис для застосування запиту
    st.markdown("""
        <div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #0070ba; margin-bottom: 20px;">
            <p style="font-size: 20px; font-weight: bold; color: #003087; margin: 0;">
                👉 Натисніть <span style="color: #ff4b4b;">CTRL + ENTER</span>, щоб підтвердити запит та перейти до оплати!
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- КРОК 2: ОПЛАТА ТА ГЕНЕРАЦІЯ ---
if user_query:
    st.write("---")
    st.write("### 2. Отримайте професійну рекомендацію")
    st.info("Для формування персональної відповіді на ваш запит, будь ласка, здійсніть оплату.")
    st.write("Вартість послуги: **$1.99**")

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
                padding: 14px 28px; 
                color: #ffffff; 
                background-color: #0070ba; 
                border-radius: 8px; 
                font-weight: bold; 
                font-size: 18px;
                text-align: center; 
                box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
                border: none;
            ">
                Сплатити $1.99 через PayPal
            </div>
        </a>
    ''', unsafe_allow_html=True)

    st.write("")
    st.write("---")
    
    # Кнопка активації ШІ
    if st.button("Отримати рекомендацію (я вже оплатив)"):
        with st.spinner("Формуємо вашу персональну інструкцію..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Ти професійний технічний консультант. Відповідай мовою запиту користувача."},
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
