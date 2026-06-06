import streamlit as st
import os

# 페이지 대문 제목 설정
st.title("📝 Student Worksheet (Research Note)")
st.write("Jigsaw 활동을 하며 채워 넣을 Research Note 학습지입니다.")
st.write("---")

# 🛠️ 파일 경로 추적 엔진 (서버 내 절대 경로 추적)
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "worksheet.pdf")

# 만약 최상위 경로에 파일이 있을 경우를 위한 백업 경로
if not os.path.exists(pdf_path):
    pdf_path = os.path.join(os.path.dirname(current_dir), "worksheet.pdf")

# 🔍 PDF 파일 존재 확인 후 다운로드 컴포넌트 생성
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
    
    # 시각적 안정감을 주는 가이드 박스
    st.info("💡 아래 버튼을 누르면 Research Note 학습지(PDF)를 다운로드할 수 있습니다. 파일을 내려받아 활용하세요.")
    st.write("")
    
    # 📥 표준 다운로드 버튼 컴포넌트 (가로폭 꽉 차게 설정)
    st.download_button(
        label="📥 학습지 PDF 다운로드 받기",
        data=pdf_bytes,
        file_name="Student_Worksheet_Research_Note.pdf",
        mime="application/pdf",
        use_container_width=True
    )
    
    # Jigsaw 수업을 위한 간결한 활동 가이드 레이아웃
    st.write("")
    st.markdown("""
    ### 🧩 학습 활동 안내
    1. 각자 맡은 본문 내용을 깊이 있게 분석합니다.
    2. 분석한 핵심 정보를 **Research Note**에 요약 및 정리합니다.
    3. 모둠으로 만들어 친구들에게 자신이 공부해 온 내용을 공유해봅시다.
    """)

else:
    # 파일이 없을 때 직관적인 조치를 위한 경고창
    st.error("🚨 'worksheet.pdf' 파일을 서버에서 찾을 수 없습니다.")
    st.info("""
    **💡 조치 방법 안내:**
    1. 준비하신 학습지 PDF 파일 이름을 영어 소문자로 정확하게 **`worksheet.pdf`** 로 변경합니다.
    2. GitHub 저장소의 **`pages` 폴더 안**에 해당 파일을 업로드해 주시면 즉시 버튼이 활성화됩니다!
    """)
