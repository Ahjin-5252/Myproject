import streamlit as st
import os

# 페이지 대문 제목 설정
st.title("📘 Textbook Material")
st.write("오늘 수업에 필요한 교과서 본문 자료입니다. 아래 버튼을 눌러 확인하세요.")
st.write("---")

# 🛠️ 파일 경로 추적 엔진
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "textbook.pdf")

# 만약 최상위 경로에 파일이 있을 경우를 위한 백업 경로
if not os.path.exists(pdf_path):
    pdf_path = os.path.join(os.path.dirname(current_dir), "textbook.pdf")

# 🔍 PDF 파일 존재 확인 후 다운로드 컴포넌트 생성
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
    
    # 시각적 안내를 주는 대형 가이드 박스
    st.info("💡 아래의 다운로드 버튼을 클릭하면 교과서 본문 PDF 파일을 내 컴퓨터나 스마트폰에 바로 저장하여 편리하게 읽을 수 있습니다.")
    st.write("")
    
    # 📥 Streamlit 공식 표준 다운로드 버튼 컴포넌트 (use_container_width로 가로폭 꽉 차게 디자인)
    st.download_button(
        label="📥 교과서 본문 PDF 다운로드 받기",
        data=pdf_bytes,
        file_name="textbook_material.pdf",
        mime="application/pdf",
        use_container_width=True
    )
    
    # 추가적인 학습 안내 메시지 배치 공간
    st.write("")
    st.markdown("""
    ### 📝 학습 안내
    1. 다운로드한 교과서 본문을 읽고 오늘의 학습 과제를 풀어봅시다.
    2. 본문 내용 파악이 끝나면 사이드바의 **02 📖 본문 확인 퀴즈**로 이동하여 문제를 풀어봅니다.
    """)

else:
    # 만약의 사태를 대비한 안전망 경고창
    st.error("🚨 'textbook.pdf' 자원을 서버에서 로드하지 못했습니다. 파일 위치를 다시 확인해 주세요.")
