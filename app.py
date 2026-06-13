import streamlit as st


# [수정 포인트] initial_sidebar_state를 "expanded"로 주어 무조건 메뉴를 펼칩니다!
st.set_page_config(
    page_title="Namyang English Learning Space",
    page_icon="🏩",
    layout="centered",
    initial_sidebar_state="expanded"  # 이 부분이 메뉴를 강제로 띄워주는 핵심 규칙입니다.
)

# 플랫폼 대문 타이틀
st.title("📢 Welcome to Namyang English Classroom! 📢")
st.markdown("---")

# 움직이는 웰컴 모션 영상(MP4) 삽입 파트
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
    st.caption("🎬 Ahjin T's Welcome Motion Dashboard")

except FileNotFoundError:
    st.warning("⚠️ 'greeting.mp4' 비디오 파일을 최상위 루트 폴더에 업로드해 주세요!")

st.markdown("---")

# 학생들이 한눈에 알아보는 이용 안내문
st.markdown("""
### 📌 이용 안내
왼쪽 사이드바 메뉴에 정렬된 숫자를 확인하고, 오늘 수업 흐름에 맞춰 원하는 영어 학습 활동을 순서대로 진행하세요!

* **1️⃣ Word Game:** 떨어지는 영단어를 맞추며 필수 어휘를 복습합니다.
* **2️⃣ Quiz:** 읽기 활동이 끝난 후, 형성평가를 통해 스스로의 성취도를 점검합니다.
* **3️⃣ Textbook:** 4단원 본문입니다.
* **4️⃣ Worksheet:** 4단원 본문 학습지입니다.
* **5️⃣ Guide:** 플랫폼 이용이 낯선 분들을 위한 친절한 사용 설명서입니다.
* **6️⃣ Timer:** 실시간으로 남은 시간을 체크하는 타이머입니다.
""")

st.caption("© 2026 Ahjin T. All rights reserved. Powered by Streamlit & Canva AI.")",
    layout="centered",
    initial_sidebar_state="expanded"  # 이 부분이 메뉴를 강제로 띄워주는 핵심 규칙입니다.
)

# 플랫폼 대문 타이틀
st.title("📢 Welcome to Namyang English Classroom! 📢")
st.markdown("---")

# 움직이는 웰컴 모션 영상(MP4) 삽입 파트
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
    st.caption("🎬 Ahjin T's Welcome Motion Dashboard")

except FileNotFoundError:
    st.warning("⚠️ 'greeting.mp4' 비디오 파일을 최상위 루트 폴더에 업로드해 주세요!")

st.markdown("---")

# 학생들이 한눈에 알아보는 이용 안내문
st.markdown("""
### 📌 이용 안내
왼쪽 사이드바 메뉴에 정렬된 숫자를 확인하고, 오늘 수업 흐름에 맞춰 원하는 영어 학습 활동을 순서대로 진행하세요!

* **1️⃣ Word Game:** 본격적인 본문 읽기 전, 떨어지는 영단어를 맞추며 필수 어휘를 청량하게 복습합니다.
* **2️⃣ Quiz:** 조별 직소(Jigsaw) 전문가 활동 및 상호 peer-tutoring이 끝난 후, 형성평가를 통해 스스로의 성취도를 점검합니다.
* **3️⃣ Textbook:** 4단원 **'Humpback Whale Observation Journal'** 본문 텍스트와 개별 디지털 스캐폴딩 도구를 확인합니다.
* **4️⃣ Worksheet:** 수업 시간에 활용하는 활동지 및 개별 피드백 아카이브 공간입니다.
* **5️⃣ Guide:** 플랫폼 이용이 낯선 남양이들을 위한 친절한 사용 설명서입니다.
* **6️⃣ Timer:** 조별 토론 및 전문가 활동 시 실시간으로 남은 시간을 체크하는 타이머 창입니다.
""")

st.caption("© 2026 Ajin T. All rights reserved. Powered by Streamlit & Canva AI.")",
    layout="centered",
    initial_sidebar_state="expanded"  # 이 부분이 메뉴를 강제로 띄워주는 핵심 규칙입니다.
)

