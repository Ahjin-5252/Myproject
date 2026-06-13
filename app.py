import streamlit as st

# 1. 페이지 레이아웃 및 기본 설정
st.set_page_config(
    page_title="Namyang Enlglish Learning Space",
    page_icon="🏩",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. 플랫폼 대문 타이틀
st.title("📢Welcome to Namyang English Classroom!📢")
st.markdown("---") # 깔끔한 상단 구분선

# 3. 🎬 움직이는 웰컴 모션 영상(MP4) 삽입 파트 (단일 재생 설정)
try:
    # 비디오 파일을 바이너리 읽기 모드로 오픈
    with open("greeting.mp4", "rb") as video_file:
        video_bytes = video_file.read()
    
    # 스트림릿 비디오 컴포넌트로 화면에 출력
    st.video(
        video_bytes,
        format="video/mp4",
        loop=False,        # [수정] True에서 False로 변경하여 무제한 반복을 해제합니다.
        autoplay=True,     # 첫 화면에 진입하자마자 자동으로 재생을 시작합니다.
        muted=True         # 교실 환경을 고려하여 기본 음소거 상태로 재생합니다.
    )
    st.caption("🎬 Ahjin T's Welcome Motion Dashboard")

except FileNotFoundError:
    st.warning("⚠️ 'greeting.mp4' 비디오 파일을 최상위 루트 폴더에 업로드해 주세요!")

st.markdown("---") # 하단 구분선

# 4. 학생들이 한눈에 알아보는 직소 협동 학습 이용 안내문
st.markdown("""
### 📌 이용 안내
왼쪽 사이드바 메뉴에 정렬된 숫자를 확인하고, 오늘 수업 흐름에 맞춰 원하는 영어 학습 활동을 순서대로 진행하세요!

* **1️⃣ Word Game:** 본격적인 본문 읽기 전, 떨어지는 영단어를 맞추며 필수 어휘를 복습합니다.
* **2️⃣ Quiz:** 읽기 활동이 끝난 후, 형성평가를 통해 스스로의 성취도를 점검합니다.
* **3️⃣ Textbook:** 4단원 본문 교과서입니다.
* **4️⃣ Worksheet:** 4단원 본문 활동지입니다.
* **5️⃣ Guide:** 플랫폼 이용이 낯선 분들을 위한 사용 설명서입니다.
* **6️⃣ Timer:** 타이머입니다.
""")

# 5. 하단 정갈한 풋터 라인
st.caption("© 2026 Ajin T. All rights reserved. Powered by Streamlit & Canva AI.")
