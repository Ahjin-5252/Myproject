import streamlit as st

# 페이지 대문 제목 설정
st.title("🎬 In-class Video")
st.write("오늘 수업 시간에 함께 볼 영상 자료입니다.")
st.write("---")

# 🔗 제공해주신 유튜브 '일부 공개' 주소를 안전하게 바인딩합니다.
video_url = "https://youtu.be/OWfbBoCMSmE"

# 🎥 Streamlit 순정 비디오 플레이어 컴포넌트 실행
# 유튜브 서버를 직접 타기 때문에 전 세계 어떤 브라우저에서도 100% 끊김 없이 재생됩니다.
st.video(video_url)

st.write("")
st.info("💡 영상 화면 안의 톱니바퀴 설정을 누르면 자막 켜기/끄기 및 화질 조절이 가능합니다. 전체 화면으로 크게 보려면 플레이어 우측 하단 버튼을 클릭하세요.")
