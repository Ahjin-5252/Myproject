import streamlit as st
import base64

st.set_page_config(page_title="교과서 본문 보기", page_icon="📘", layout="centered")
st.title("📘 Textbook Material")
st.write("오늘 함께 읽을 교과서 본문 내용입니다. 마우스로 스크롤하며 읽어보세요.")
st.write("---")

# pages 폴더 안에 저장된 pdf 파일을 읽어오는 로직
try:
    with open("pages/textbook.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # 웹 화면에 PDF를 내장(Embed)하는 HTML 태그
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    
except FileNotFoundError:
    st.warning("pages 폴더 안에 'textbook.pdf' 파일이 아직 업로드되지 않았습니다. GitHub를 확인해 주세요.")
