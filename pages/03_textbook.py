import streamlit as st
import base64
import os

st.title("📘 Textbook Material")
st.write("오늘 함께 읽을 교과서 본문 내용입니다. 마우스로 스크롤하며 읽어보세요.")
st.write("---")

# 🛠️ 현재 실행 파일의 위치를 기준으로 교과서 PDF 경로를 안전하게 절대 경로로 추적합니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "textbook.pdf")

# 만약 최상위 루트 경로에 올리셨을 경우를 대비한 보조 경로 설정
if not os.path.exists(pdf_path):
    pdf_path = os.path.join(os.path.dirname(current_dir), "textbook.pdf")

# 🔍 PDF 파일 존재 여부 검사 및 화면 렌더링
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # 웹 화면에 PDF를 내장하는 HTML 프레임 규격
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf" style="border:1px solid #ccc; border-radius:8px;"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
else:
    # 🚨 파일이 없을 때 선생님이 직관적으로 아실 수 있도록 경고창을 명확히 띄웁니다.
    st.error("🚨 'textbook.pdf' 파일을 찾을 수 없습니다.")
    st.info("""
    **💡 조치 방법 안내:**
    1. 컴퓨터에 있는 교과서 PDF 파일 이름을 영어 소문자로 **`textbook.pdf`** 라고 변경합니다.
    2. GitHub 저장소의 **`pages` 폴더 안**에 해당 파일을 다시 업로드해 주세요!
    """)
