import streamlit as st
import openai

# 1. Основні налаштування сторінки
st.set_page_config(
    page_title="AI Technical Guide",
    page_icon="🤖",
    layout="centered"
)

# 2. Твої дані (OpenAI та PayPal)
# Твій актуальний баланс OpenAI: $4.88
openai.api_key = "ТВІЙ_OPENAI_API_KEY" 
MY_PAYPAL_EMAIL = "np.kremenchuk.sb@gmail.com"

# 3. Стилізація та заголовок
st.title("🤖 AI Technical Guide Assistant")
st.subheader("Професійні технічні інструкції та рекомендації")
st.write("Вартість однієї професійної рекомендації: **$1.99**")

# Створення прямого посилання на оплату (Plan B, що працює 100%)
payment_url = (
    f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick"
    f"&business={MY_PAYPAL_EMAIL}"
    f"&item_name=Professional%20Technical%20Recommendation"
    f"&amount=1.99"
    f"&currency_code=USD"
)

# 4. Логіка доступу (Session State)
if "payment_done" not in st.session_state:
    st.session_state.payment_done = False

# --- ЕКРАН ОПЛАТИ ---
if not st.session_state.payment_done:
    st.info("Щоб скористатися професійною рекомендацією, будь ласка, здійсніть оплату.")
    
    # Гарна кнопка PayPal
    st.markdown(f'''
        <a href="{payment_url}" target="_blank" style="text-decoration: none;">
            <div style="
                display: inline-block; 
                padding: 12px 24px; 
                color: #003087; 
                background-color: #ffc439; 
                border-radius: 25px; 
                font-weight: bold; 
                font-size: 18px;
                text-align: center; 
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                border: none;
                cursor: pointer;
            ">
                Pay with <span style="color: #009cde;">PayPal</span>
            </div>
        </a>
    ''', unsafe_allow_html=True)
    
    st.write("")
    st.write("---")
    
    # Кнопка для активації після оплати
    if st.button("Я вже оплатив (отримати рекомендацію)"):
        st.session_state.payment_done = True
        st.rerun()

# --- ЕКРАН ПІСЛЯ ОПЛАТИ (ЗОНА ШІ) ---
else:
    st.success("✅ Доступ надано. Ви можете отримати свою професійну рекомендацію.")
    
    user_input = st.text_area("Опишіть ваше технічне питання або проблему:", placeholder="Наприклад: Як налаштувати синхронізацію в акаунті...")
    
    if st.button("Згенерувати рекомендацію"):
        if user_input:
            with st.spinner("Аналізуємо дані та формуємо професійну рекомендацію..."):
                try:
                    # Використовуємо gpt-3.5-turbo для економії твоїх $4.88
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "Ти професійний технічний консультант. Надавай чіткі, структуровані інструкції."},
                            {"role": "user", "content": user_input}
                        ]
                    )
                    st.write("---")
                    st.write("### 📋 Ваша професійна рекомендація:")
                    st.write(response.choices[0].message.content)
                    
                    # Кнопка для нового запиту
                    if st.button("Новий запит"):
                        st.session_state.payment_done = False
                        st.rerun()
                        
                except Exception as e:
                    st.error(f"Виникла помилка при зверненні до ШІ: {e}")
        else:
            st.warning("Будь ласка, введіть опис проблеми.")

# 5. Футер
st.markdown("---")
st.caption("© 2026 TechDocs Pro — Професійна технічна підтримка")
