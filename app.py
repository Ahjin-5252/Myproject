import streamlit as st

# 1. 페이지 레이아웃 및 기본 설정 (메인 사이드바 무조건 확장)
st.set_page_config(
    page_title="Namyang Enlglish Learning Space",
    page_icon="🏩",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. 플랫폼 대문 타이틀
st.title("📢 Welcome to Namyang English Classroom! 📢")
st.markdown("---")

# 3. 🎬 움직이는 웰컴 모션 영상(MP4) 삽입 파트
try:
    with open("greeting.mp4", "rb") as video_file:
        video_bytes = video_file.read()
    
    st.video(
        video_bytes,
        format="video/mp4",
        loop=False,        
        autoplay=True,     
        muted=True         
    )
    st.caption("🎬 Ahjin T's Welcoming Greeting")

except FileNotFoundError:
    st.warning("⚠️ 'greeting.mp4' 비디오 파일을 최상위 루트 폴더에 업로드해 주세요!")

st.markdown("---")

# 4. 학생들이 한눈에 알아보는 이용 안내문 (삼중 따옴표 완전 차단)
st.markdown("""
### 📌 이용 안내
왼쪽 사이드바 메뉴에 정렬된 숫자를 확인하고, 오늘 수업 흐름에 맞춰 원하는 영어 학습 활동을 순서대로 진행하세요!

* **1️⃣ Word Game:** 본격적인 본문 읽기 전, 떨어지는 영단어를 맞추며 필수 어휘를 복습합니다.
* **2️⃣ Quiz:** 읽기 활동이 끝난 후, 형성평가를 통해 스스로의 성취도를 점검합니다.
* **3️⃣ Textbook:** 4단원 'Humpback Whale Observation Journal' 본문 텍스트입니다.
* **4️⃣ Worksheet:** 수업 시간에 활용하는 활동지입니다.
* **5️⃣ Guide:** 플랫폼 이용이 낯선 분들을 위한 사용 설명서입니다.
* **6️⃣ Timer:** 실시간으로 남은 시간을 체크하는 타이머 창입니다.
""")

st.markdown("---")

# 5. 하단 정갈한 풋터 라인 (Syntax 에러 유발 요소 완전 제거)
st.caption("© 2026 Ahjin T. All rights reserved. Powered by Streamlit & Canva AI.")

