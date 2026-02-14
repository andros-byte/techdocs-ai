import streamlit as st
from openai import OpenAI
import base64

# Налаштування сторінки
st.set_page_config(page_title="TechDocs AI Pro", page_icon="📄")

# Клієнт OpenAI (Ключ має бути в secrets.toml або Settings -> Secrets у Streamlit)
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("Будь ласка, додайте OPENAI_API_KEY у Secrets вашого Streamlit додатку.")

st.title("📄 TechDocs AI Professional")
st.subheader("Генератор технічних інструкцій")

# Опис для користувачів
st.info("Цей сервіс працює автоматично. Введіть модель вашого обладнання та отримайте інструкцію.")

# Форма введення
equipment = st.text_input("Модель обладнання (напр. EcoFlow, Must, Victron):")
problem = st.text_area("Яке завдання потрібно виконати?")

if st.button("Згенерувати документацію"):
    if equipment and problem:
        with st.spinner('ШІ Andrii Maslii (Kremenchuk) створює інструкцію...'):
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
                st.success("✅ Готово! Ви можете скопіювати цей текст.")
            except Exception as e:
                st.error(f"Помилка з'єднання: {e}")
    else:
        st.warning("Будь ласка, заповніть поля.")

# Реквізити (автоматично показуються всім користувачам)
st.divider()
st.markdown("### 💳 Підтримати проект та ЗСУ")
st.write("Якщо сервіс був корисним, ви можете надіслати підтримку:")
st.write("**PayPal / Email:** np.kremenchuk.sb@gmail.com")
st.caption("Всі кошти йдуть на підтримку родини в Кременчуці та допомогу нашим захисникам. 🇺🇦")
