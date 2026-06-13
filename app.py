import streamlit as st

# 1. 페이지 레이아웃 및 기본 설정 (메인 사이드바 무조건 확장)
st.set_page_config(
    page_title="Namyang Enlgish Learning Space",
    page_icon="🏩",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. 각 기능별 서브 페이지 선언 함수 (실제 파일 내부의 run 함수들을 부르거나 직접 링킹)
def run_home_dashboard():
    st.title("📢 Welcome to Namyang English Classroom! 📢")
    st.markdown("---")

    # 🎬 움직이는 웰컴 모션 영상(MP4) 삽입 파트
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

    # 학생들이 한눈에 알아보는 이용 안내문
    st.markdown("""
    ### 📌 이용 안내
    왼쪽 사이드바 메뉴에 정렬된 숫자를 확인하고, 오늘 수업 흐름에 맞춰 원하는 영어 학습 활동을 순서대로 진행하세요!

    * **1️⃣ Word Game:** 본격적인 본문 읽기 전, 떨어지는 영단어를 맞추며 필수 어휘를 복습합니다.
    * **2️⃣ Quiz:** 읽기 활동이 끝난 후, 확인문제를 통해 스스로의 성취도를 점검합니다.
    * **3️⃣ Textbook:** 4단원 본문 텍스트 파일입니다.
    * **4️⃣ Worksheet:** 활동지 파일입니다..
    * **5️⃣ Video:** 본문 읽기을 읽기 전 봐야할 활용하는 동영상입니다.
    * **6️⃣ Timer:** 타이머 창입니다.
    * **7️⃣ Guide:** 플랫폼 이용이 낯선 분들을 위한 사용 설명서입니다.
    """)
    st.caption("© 2026 Ahjin T. All rights reserved. Powered by Streamlit & Canva AI.")

# 3. 🛠️ 완벽한 네비게이션 매핑 시스템 (가장 바깥 app.py에서 딱 한 번만 통합 제어!)
page_00 = st.Page(run_home_dashboard, title="🐋 HOME", icon="🐋", default=True)
page_01 = st.Page("pages/01_Word_Game.py", title="01 🕹️ 단어 게임 앱", icon="🕹️")
page_02 = st.Page("pages/02_Quiz.py", title="02 📖 본문 확인 퀴즈", icon="📖")
page_03 = st.Page("pages/03_Textbook.py", title="03 📘 Textbook", icon="📘")
page_04 = st.Page("pages/04_Worksheet.py", title="04 📝 Worksheet", icon="📝")
page_05 = st.Page("pages/05_Video.py", title="05 🎬 In-class Video", icon="🎬")
page_06 = st.Page("pages/06_Timer.py", title="06 ⏳ Class Timer", icon="⏳")
page_07 = st.Page("pages/07_Guide.py", title="07 📽️ Video Guide for Apps", icon="📽️")

# 정의된 페이지 목록을 사이드바 빌더에 주입하여 실행합니다.
pg = st.navigation([page_00, page_01, page_02, page_03, page_04, page_05, page_06, page_07])
pg.run()
