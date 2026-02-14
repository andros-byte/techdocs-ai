import streamlit as st
from openai import OpenAI

# Налаштування
st.set_page_config(page_title="TechDocs AI Pro")

try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("Помилка: Перевірте OPENAI_API_KEY у Secrets!")

st.title("📄 TechDocs AI Professional")

equipment = st.text_input("Модель обладнання (напр. Datouboss DN-022):")
problem = st.text_area("Що саме потрібно (характеристики, налаштування)?")

if st.button("Згенерувати інструкцію"):
    if equipment:
        with st.spinner('Генеруємо технічні дані...'):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "Ти — технічний експерт. НЕ давай порад про пошук у Google. Надавай конкретні технічні характеристики, схеми підключення, напругу, струм та покрокові налаштування для вказаної моделі. Якщо модель невідома, опиши типові параметри для цього класу пристроїв."},
                        {"role": "user", "content": f"Надай повні технічні характеристики та інструкцію для {equipment}. Конкретне завдання: {problem}"}
                    ]
                )
                st.markdown("---")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Помилка: {e}")

st.divider()
st.markdown("### 💳 Контакти та підтримка")
st.write("**PayPal / Email:** np.kremenchuk.sb@gmail.com")
