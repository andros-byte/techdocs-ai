import streamlit as st
from openai import OpenAI
from fpdf import FPDF

# Підключаємо ключ та пароль із "Secrets"
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
MASTER_CODE = st.secrets["ACCESS_CODE"]
PAYPAL_EMAIL = "np.kremenchuk.sb@gmail.com"

st.set_page_config(page_title="TechDocs AI Pro", page_icon="⚙️")

def create_pdf(text, query):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="TechDocs AI: Professional Manual", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=11)
    clean_text = text.encode('ascii', 'ignore').decode('ascii')
    pdf.multi_cell(0, 7, txt=clean_text)
    return pdf.output(dest='S').encode('latin-1')

st.title("⚙️ TechDocs AI Professional")
query = st.text_input("Enter device model:")

if query:
    if 'manual_content' not in st.session_state:
        with st.spinner('Generating...'):
            res = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": f"Detailed manual for {query}"}]
            )
            st.session_state.manual_content = res.choices[0].message.content

    st.markdown("---")
    st.info(st.session_state.manual_content[:300] + "...")
    st.error("🔒 FULL PACKAGE IS LOCKED ($1.99)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Send payment to:")
        st.code(PAYPAL_EMAIL)
    with col2:
        user_code = st.text_input("Enter Access Code:", type="password")
        if user_code == MASTER_CODE:
            st.success("Unlocked!")
            pdf_data = create_pdf(st.session_state.manual_content, query)
            st.download_button("📥 Download PDF", data=pdf_data, file_name="manual.pdf")

st.sidebar.caption("Secured by PayPal")
