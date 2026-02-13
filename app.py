import streamlit as st
from openai import OpenAI
import requests

# Налаштування сторінки
st.set_page_config(page_title="TechDocs AI Pro", page_icon="⚙️")

# Ініціалізація клієнта (виправлений метод звернення до Secrets)
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    st.error("API Key not found in Secrets!")

st.title("⚙️ TechDocs AI Professional")
st.subheader("High-Quality Engineering Guides")

query = st.text_input("Enter device model (e.g., Victron MultiPlus-II):")

if query:
    with st.spinner('Generating professional documentation...'):
        try:
            # Покращений запит для детальнішого контенту
            prompt = f"Write a professional engineering manual for {query} in English. Include: 1. Specifications Table, 2. Detailed Connection Diagram description, 3. Step-by-step setup with examples, 4. Safety protocols, 5. Troubleshooting guide."
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            
            result_text = response.choices[0].message.content
            st.markdown(result_text)
            
            # Тимчасова інструкція для PDF (поки ми не оновили requirements)
            st.success("Manual generated! To save as PDF: Press Ctrl+P (Cmd+P) and choose 'Save as PDF'.")
            
        except Exception as e:
            st.error(f"Error: {e}")
