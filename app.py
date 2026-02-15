import streamlit as st
import openai

# 1. Налаштування сторінки
st.set_page_config(page_title="Technical Guide AI", page_icon="🤖")

# 2. Твої дані (OpenAI та PayPal)
# Твій баланс OpenAI: $4.88
openai.api_key = "ТВІЙ_OPENAI_API_KEY" 
MY_PAYPAL_EMAIL = "np.kremenchuk.sb@gmail.com"

# 3. Дизайн інтерфейсу
st.title("🤖 AI Technical Guide Assistant")
st.write("Отримайте професійну інструкцію всього за **$1.99**")

# Створення прямого посилання на оплату (Plan B, оскільки бізнес-кнопки глючать)
payment_url = f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business={MY_PAYPAL_EMAIL}&item_name=Technical%20Guide%20Access&amount=1.99&currency_code=USD"

# 4. Логіка оплати та доступу
if "payment_done" not in st.session_state:
    st.session_state.payment_done = False

if not st.session_state.payment_done:
    st.info("Щоб скористатися ШІ-помічником, будь ласка, здійсніть оплату.")
    
    # Кнопка оплати
    st.markdown(f'''
        <a href="{payment_url}" target="_blank">
            <div style="display: inline-block; padding: 0.5em 1em; color: white; background-color: #ffc439; border-radius: 5px; text-decoration: none; font-weight: bold; text-align: center; border: 1px solid #ffc439;">
                <span style="color: #003087;">Pay with </span><span style="color: #009cde;">PayPal</span>
            </div>
        </a>
    ''', unsafe_allow_html=True)
    
    st.write("---")
    if st.button("Я вже оплатив (активувати доступ)"):
        # Тут можна додати перевірку, але для старту просто активуємо
        st.session_state.payment_done = True
        st.rerun()

# 5. Робоча зона ШІ (відкривається після "оплати")
if st.session_state.payment_done:
    st.success("✅ Доступ активовано! Запитуйте ШІ.")
    user_input = st.text_input("Опишіть вашу технічну проблему:")
    
    if user_input:
        with st.spinner("ШІ думає..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_input}]
                )
                st.write("### Відповідь ШІ:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Помилка OpenAI: {e}")
