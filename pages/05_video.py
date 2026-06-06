import streamlit as st
import os

# 페이지 대문 제목 설정
st.title("🎬 In-class Video")
st.write("오늘 수업 시간에 함께 시청할 멀티미디어 영상 자료입니다.")
st.write("---")

# 🛠️ 파일 경로 추적 엔진 (pages 폴더 내 동영상 파일 추적)
current_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(current_dir, "class_video.mp4")

# 만약 최상위 경로에 파일이 있을 경우를 위한 백업 경로
if not os.path.exists(video_path):
    video_path = os.path.join(os.path.dirname(current_dir), "class_video.mp4")

# 🔍 동영상 파일 존재 확인 후 플레이어 구동
if os.path.exists(video_path):
    
    # 🎥 Streamlit 순정 비디오 플레이어 컴포넌트
    # 브라우저 보안 정책에 구애받지 않고 부드럽게 스트리밍됩니다.
    st.video(video_path)
    
    st.write("")
    st.info("💡 영상이 끊기거나 정상적으로 재생되지 않는 경우, 우측 하단의 전체화면 버튼을 누르거나 새로고침을 해주세요.")

else:
    # 파일이 아직 업로드되지 않았을 때 출력되는 정갈한 안내창
    st.error("🚨 'class_video.mp4' 동영상 파일을 서버에서 찾을 수 없습니다.")
    st.info("""
    **💡 조치 방법 안내:**
    1. 준비하신 수업용 동영상 파일의 이름을 영어 소문자로 정확하게 **`class_video.mp4`** 로 변경합니다.
    2. GitHub 저장소의 **`pages` 폴더 안**에 해당 파일을 업로드해 주세요!
    3. 업로드가 완료되면 이 자리에 멋진 비디오 플레이어가 자동으로 활성화됩니다.
    """)
