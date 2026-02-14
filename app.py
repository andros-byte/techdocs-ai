import streamlit as st
from openai import OpenAI

# Налаштування (повністю англійською для солідності)
st.set_page_config(page_title="TechDocs AI International", layout="centered")

try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("System Error: API Key missing.")

st.title("📄 Professional Technical Documentation AI")
st.write("Get instant high-quality technical manuals, wiring diagrams, and setup guides.")

# Форма (англійською)
equipment = st.text_input("Enter Device Model (e.g., Datouboss DN-022, Victron, Deye):")
task = st.text_area("What do you need to configure? (e.g., Battery setup, Error codes, Installation)")

if st.button("Generate Technical Guide"):
    if equipment:
        with st.spinner('AI is generating your professional documentation...'):
            try:
                # ШІ сам зрозуміє мову запиту, але видасть професійний результат
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a senior technical writer. Provide detailed specs, wiring, and settings. Hide the most critical 70% of information with [DATA LOCKED - PAYMENT REQUIRED]."},
                        {"role": "user", "content": f"Create a technical manual for {equipment}. Task: {task}. Language: detect from user input."}
                    ]
                )
                preview_text = response.choices[0].message.content
                
                # Демо-версія
                st.markdown("### 🔍 Document Preview:")
                st.info(preview_text)
                
                # Блок оплати для іноземців
                st.error("## 🔒 FULL DOCUMENTATION LOCKED")
                st.markdown(f"""
                ### To unlock the full guide (PDF, Schematics, Safety codes):
                **Price: $15.00 USD**
                
                **Payment Method:**
                * **PayPal:** `np.kremenchuk.sb@gmail.com`
                * **Note:** Order for {equipment}
                
                **How to get it:**
                1. Send **$15.00** via PayPal.
                2. Send a screenshot of the transaction to `np.kremenchuk.sb@gmail.com`.
                3. We will email you the full PDF manual within 10-15 minutes.
                """)
                
            except Exception as e:
                st.error("Connection error. Please try again.")
    else:
        st.warning("Please enter the device model.")

st.divider()
st.caption("© 2024 TechDocs AI Global Solutions. High-precision documentation.")
