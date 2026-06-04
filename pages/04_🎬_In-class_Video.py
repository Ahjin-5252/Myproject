import streamlit as st

# 페이지 레이아웃 및 제목 설정
st.set_page_config(page_title="수업 도입 영상", page_icon="🎬", layout="centered")

st.title("🎬 In-class Video")
st.write("오늘 함께 읽을 본문의 내용을 동영상을 보며 찬찬히 추론해 봅시다.")
st.write("---")

# 🔗 선생님이 제공해주신 구글 드라이브 주소를 시스템 임베드 규격(preview)으로 자동 변환하여 연동했습니다.
video_url = "https://drive.google.com/preview?id=1eqmKJ6KVofHcvLfYCLJrflVy8PNbVUoD"

# 구글 플레이어를 가로폭에 꽉 차게 맞추고 고해상도(height=480)로 화면에 임베드하는 HTML 태그
video_html = f"""
    <div style="display: flex; justify-content: center; width: 100%;">
        <iframe src="{video_url}" width="100%" height="480" allow="autoplay; fullscreen" allowfullscreen style="border: none; border-radius: 8px;"></iframe>
    </div>
"""

# 화면에 플레이어 출력
st.markdown(video_html, unsafe_allow_html=True)
st.write("")


st.info("💡 영상이 재생되지 않거나 권한 요청 메시지가 뜨는 경우, 구글 드라이브 파일의 공유 설정이 '링크가 있는 모든 사용자에게 공개'로 되어 있는지 다시 한번 확인해 주세요.")
