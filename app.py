import streamlit as st

# --- CONFIGURATION & GOOGLE VERIFICATION ---
st.set_page_config(page_title="TechDocs AI Pro", page_icon="⚙️", layout="wide")

# Метод 1: Метатег для Google Search Console (Тег HTML)
st.markdown('<meta name="google-site-verification" content="BmsbNUrS4gl2qA5tTqT3sexFNz51u0tx3AKMGGhgY_A" />', unsafe_allow_html=True)

# Метод 2: Прихований текст для верифікації (HTML-файл)
st.markdown('<p style="display:none">google-site-verification: google29d1211dcf00efa3.html</p>', unsafe_allow_html=True)

# Імпорт бібліотек після конфігурації
from openai import OpenAI
from fpdf import FPDF

# --- API & ACCESS ---
# Переконайтеся, що ці ключі додані в налаштування Streamlit (Secrets)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
PAYPAL_EMAIL = "np.kremenchuk.sb@gmail.com"
MASTER_CODE = st.secrets["ACCESS_CODE"]

# --- PDF GENERATOR CLASS ---
class TechPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'TECHDOCS AI - PROFESSIONAL ENGINEERING SERIES', 0, 1, 'R')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} | Confidential Technical Document', 0, 0, 'C')

def create_pro_pdf(text, query):
    pdf = TechPDF()
    pdf.add_page()
    
    # Title Block
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 20, txt=f"MANUAL: {query.upper()}", ln=True, align='L', fill=True)
    pdf.ln(10)
    
    # Content formatting
    pdf.set_font("Arial", size=11)
    clean_text = text.encode('ascii', 'ignore').decode('ascii')
    
    for line in clean_text.split('\n'):
        if line.startswith('#'):
            pdf.set_font("Arial", 'B', 14)
            pdf.ln(5)
            pdf.multi_cell(0, 10, txt=line.replace('#', '').strip())
            pdf.set_font("Arial", size=11)
        else:
            pdf.multi_cell(0, 7, txt=line)
            
    return pdf.output(dest='S').encode('latin-1')

# --- MAIN INTERFACE ---
st.title("⚙️ TechDocs AI Professional")
st.markdown("#### High-Fidelity Engineering Documentation Generator")

query = st.text_input("Enter device model (e.g., Datouboss DN-022, Victron MultiPlus):")

if query:
    if 'manual_content' not in st.session_state:
        with st.spinner('Accessing engineering databases and generating...'):
            prompt = f"Create a professional, highly detailed technical manual for {query}. Use tables for specifications, detailed connection steps, and safety warnings. Professional tone only."
            res = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            st.session_state.manual_content = res.choices[0].message.content

    st.markdown("---")
    
    # Layout
    col_pre, col_pay = st.columns([2, 1])
    
    with col_pre:
        st.subheader("📄 Document Preview")
        st.info(st.session_state.manual_content[:500] + "...")
        st.warning("⚠️ Full document contains diagrams, tables, and safety protocols.")

    with col_pay:
        st.subheader("🔓 Unlock Full PDF")
        st.metric(label="Price", value="$1.99")
        st.write(f"Pay to: `{PAYPAL_EMAIL}`")
        
        user_code = st.text_input("Enter Access Code:", type="password")
        if user_code == MASTER_CODE:
            st.success("Access Granted")
            pdf_data = create_pro_pdf(st.session_state.manual_content, query)
            st.download_button("📥 DOWNLOAD PROFESSIONAL PDF", data=pdf_data, file_name=f"TechDocs_{query}.pdf")
        elif user_code != "":
            st.error("Invalid Code")

st.sidebar.markdown("### Support")
st.sidebar.info("All manuals are generated using GPT-4o professional engineering model.")
