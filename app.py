import streamlit as st
from openai import OpenAI

# Налаштування інтерфейсу (як на Screenshot_11)
st.set_page_config(page_title="TechDocs AI Professional", layout="centered")

try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("System Error: OpenAI API Key missing in Secrets.")

st.title("📄 Professional Technical Documentation AI")
st.write("Get instant high-quality technical manuals, wiring diagrams, and setup guides.")

# Форма (відповідно до Screenshot_11)
equipment = st.text_input("Enter Device Model (e.g., Datouboss DN-022, Victron, Deye):")
task = st.text_area("What do you need to configure? (e.g., Battery setup, Error codes, Installation)")

if st.button("Generate Technical Guide"):
    if equipment:
        with st.spinner('AI is generating your documentation...'):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a senior technical writer. Provide professional specs. Hide 70% of content with [LOCKED - PAYMENT REQUIRED]."},
                        {"role": "user", "content": f"Manual for {equipment}. Task: {task}."}
                    ]
                )
                preview = response.choices[0].message.content
                
                st.markdown("### 🔍 Preview:")
                st.info(preview)
                
                # Блок оплати з ціною $1.99
                st.error("## 🔒 FULL DOCUMENTATION LOCKED")
                st.markdown(f"""
                ### To unlock the full guide (PDF, Schematics, Safety codes):
                **Price: $1.99 USD**
                
                **Payment Method:**
                * **PayPal:** `np.kremenchuk.sb@gmail.com`
                
                **How to get it:**
                1. Send **$1.99** via PayPal.
                2. Send a screenshot of the transaction to `np.kremenchuk.sb@gmail.com`.
                3. We will email you the full professional manual immediately.
                """)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter the device model.")

st.divider()
st.caption("© 2024 TechDocs AI Global Solutions. High-precision documentation.")
