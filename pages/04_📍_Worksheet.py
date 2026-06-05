import streamlit as st
import base64

st.set_page_config(page_title="수업 학습지", page_icon="📝", layout="centered")
st.title("📝 Student Worksheet (Research Note)")
st.write("Jigsaw 활동을 하며 채워 넣을 Research Note 학습지입니다.")
st.write("---")

try:
    with open("pages/worksheet.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # 다운로드 버튼 추가 (학생들이 인쇄하거나 다운로드할 수 있게 조치)
    st.download_button(
        label="📥 학습지 PDF 다운로드 받기",
        data=base64.b64decode(base64_pdf),
        file_name="student_worksheet.pdf",
        mime="application/pdf",
        use_container_width=True
    )
    st.write("")
    
    # 화면에 PDF 내장
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    
except FileNotFoundError:
    st.warning("pages 폴더 안에 'worksheet.pdf' 파일이 아직 업로드되지 않았습니다. GitHub를 확인해 주세요.")
