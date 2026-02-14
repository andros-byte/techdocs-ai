import streamlit as st
import streamlit.components.v1 as components
from openai import OpenAI
from fpdf import FPDF

# --- 1. ПРИХОВАНА ВЕРИФІКАЦІЯ ---
st.set_page_config(page_title="TechDocs AI Pro", page_icon="⚙️", layout="wide")

# ЦЕЙ БЛОК Я ДОДАВ: він дублює верифікацію прямо в HTML, щоб Google її "з'їв"
st.markdown(
    """
    <div style="display:none;">
        <p>google-site-verification: google29d1211dcf00efa3.html</p>
        <meta name="google-site-verification" content="BmsbNUrS4gl2qA5tTqT3sexFNz51u0tx3AKMGGhgY_A" />
        <meta name="google-site-verification" content="MObJ6DkfeVQ8u1q8IQfCccX4lyAa3qAw" />
    </div>
    """, 
    unsafe_allow_html=True
)

# Твоя вставка Analytics (залишаємо як є)
components.html(
    """
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-QT8BPB0F44"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-QT8BPB0F44');
    </script>
    <meta name="google-site-verification" content="BmsbNUrS4gl2qA5tTqT3sexFNz51u0tx3AKMGGhgY_A" />
    <meta name="google-site-verification" content="MObJ6DkfeVQ8u1q8IQfCccX4lyAa3qAw" />
    """,
    height=0,
)

# --- 2. ЛОГІКА ДОДАТКА (ТВІЙ ОРИГІНАЛ) ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
PAYPAL_EMAIL = "np.kremenchuk.sb@gmail.com"
MASTER_CODE = st.secrets["ACCESS_CODE"]

class TechPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'TECHDOCS AI - PROFESSIONAL SERIES', 0, 1, 'R')
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pro_pdf(text, query):
    pdf = TechPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    clean_text = text.encode('ascii', 'ignore').decode('ascii')
    pdf.multi_cell(0, 7, txt=clean_text)
    return pdf.output(dest='S').encode('latin-1')

st.title("⚙️ TechDocs AI Professional")
query = st.text_input("Enter device model (e.g., Datouboss DN-022):")

if query:
    if 'manual_content' not in st.session_state:
        with st.spinner('Accessing database...'):
            res = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": f"Create manual for {query}"}]
            )
            st.session_state.manual_content = res.choices[0].message.content

    st.markdown("---")
    col_pre, col_pay = st.columns([2, 1])
    with col_pre:
        st.subheader("📄 Preview")
        st.info(st.session_state.manual_content[:500] + "...")
    with col_pay:
        st.subheader("🔓 Unlock")
        user_code = st.text_input("Enter Access Code:", type="password")
        if user_code == MASTER_CODE:
            pdf_data = create_pro_pdf(st.session_state.manual_content, query)
            st.download_button("📥 DOWNLOAD PDF", data=pdf_data, file_name=f"TechDocs_{query}.pdf")
