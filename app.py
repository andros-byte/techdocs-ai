import streamlit as st
from openai import OpenAI
import base64

# Налаштування сторінки
st.set_page_config(page_title="TechDocs AI Pro", page_icon="📄")

# Клієнт OpenAI (Ключ має бути в Settings -> Secrets у Streamlit)
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("Будь ласка, додайте OPENAI_API_KEY у Secrets вашого Streamlit додатку.")

st.title("📄 TechDocs AI Professional")
st.subheader("Генератор технічних інструкцій")

# Форма введення
equipment = st.text_input("Модель обладнання (напр. EcoFlow, Must, Victron):")
problem = st.text_area("Яке завдання потрібно виконати?")

if st.button("Згенерувати документацію"):
    if equipment and problem:
        with st.spinner('ШІ генерує інструкцію...'):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "Ти — професійний техписьменник. Створюй чіткі інструкції українською мовою."},
                        {"role": "user", "content": f"Створи детальну інструкцію для {equipment}. Тема: {problem}."}
                    ]
                )
                answer = response.choices[0].message.content
                st.markdown("---")
                st.markdown(answer)
                st.success("✅ Готово!")
            except Exception as e:
                st.error(f"Помилка: {e}")
    else:
        st.warning("Будь ласка, заповніть поля.")

# Блок контактів
st.divider()
st.markdown("### 💳 Контакти та підтримка проекту")
st.write("**PayPal / Email:** np.kremenchuk.sb@gmail.com")
