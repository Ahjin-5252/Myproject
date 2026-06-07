import streamlit as st

# 페이지 대문 제목 및 아이콘 설정
st.title("📽️ Video Guide for Apps")
st.write("수업 지도안 및 웹 애플리케이션들의 올바른 사용법과 활용 안내 영상입니다.")
st.write("---")

# 🔗 제공해주신 비디오 가이드 유튜브 주소 바인딩
guide_video_url = "https://youtu.be/_1eoc5AVbfM"

# 🎥 Streamlit 순정 비디오 플레이어 컴포넌트 실행
# 유튜브 인프라를 사용하여 버퍼링 없이 100% 안정적으로 재생됩니다.
st.video(guide_video_url)

st.write("")
st.info("💡 영상을 시청하면서 각 앱(단어 게임, 본문 퀴즈, 타이머 등)의 구체적인 조작법과 활용 방법을 확인해 보세요.")

# 📋 추가적인 학습 가이드 레이아웃 배치
st.write("")
st.markdown("""
### 🧭 Quick App Navigation Guide
1. **01 🕹️ 단어 게임 앱**: 전 차시 어휘를 복습하고 자가 진단 워크시트를 수행합니다.
2. **02 📖 본문 확인 퀴즈**: 본문 내용에 대한 확인 문제를 푸는 공간입니다.
3. **03 📘 Textbook & 04 📝 Worksheet**: 브라우저 환경에 구애받지 않고 터치 한 번으로 수업 자료를 다운로드합니다.
""")
