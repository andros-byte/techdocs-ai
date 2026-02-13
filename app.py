import streamlit as st
from openai import OpenAI
from fpdf import FPDF

# --- CONFIGURATION ---
# Беру ключ із ваших робочих Secrets, де лежать $4.96
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
PAYPAL_EMAIL = "np.kremenchuk.sb@gmail.com" 

st.set_page_config(page_title="TechDocs AI", page_icon="⚙️")

# Function to generate a professional PDF
def create_pdf(text, query):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="TechDocs AI: Professional Technical Manual", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=11)
    # Clean text for PDF compatibility
    clean_text = text.encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 7, txt=clean_text)
    return pdf.output(dest='S').encode('latin-1')

# --- USER INTERFACE ---
st.title("⚙️ TechDocs AI")
st.markdown("### Professional Engineering Solutions")
st.write("Instant high-quality manuals and setup guides for any equipment.")

# Simple search field
query = st.text_input("Enter device model or technical issue:", placeholder="e.g. Victron Energy SmartSolar setup")

if query:
    if 'manual_content' not in st.session_state:
        with st.spinner('Generating professional documentation...'):
            res = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": f"Write a professional engineering manual for {query} in English. Include: 1. Specifications, 2. Connection Diagram description, 3. Step-by-step setup, 4. Safety protocols."}]
            )
            st.session_state.manual_content = res.choices[0].message.content

    st.markdown("---")
    st.markdown("#### 📄 Document Preview:")
    # Показуємо лише маленький шматочок, щоб клієнт захотів купити повну версію
    st.info(st.session_state.manual_content[:600] + "...")
    
    st.error("🔒 FULL TECHNICAL PDF PACKAGE IS LOCKED")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 💰 Price: $1.99")
        st.write("To unlock full access, send payment via PayPal to:")
        st.code(PAYPAL_EMAIL, language="text")
        st.caption("Instructions: Open PayPal -> Send -> Paste Email -> Enter $1.99")

    with col2:
        st.markdown("### 📥 Download")
        # Generate the PDF file
        pdf_file = create_pdf(st.session_state.manual_content, query)
        
        st.download_button(
            label="✅ Download Full PDF",
            data=pdf_file,
            file_name=f"Manual_{query.replace(' ', '_')}.pdf",
            mime="application/pdf"
        )

st.sidebar.markdown("---")
st.sidebar.write("🌍 **Global Engineering Support**")
st.sidebar.caption("Powered by GPT-4o. All payments are secured by PayPal.")
