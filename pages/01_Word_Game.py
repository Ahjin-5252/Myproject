import streamlit as st
import pandas as pd
import random
import time
from gtts import gTTS
import io

# 1. 스타일 설정
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    @keyframes fallDown {
        0% { transform: translateY(-50px); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(320px); opacity: 0; }
    }
    @keyframes splashEffect {
        0% { transform: scale(1); opacity: 1; letter-spacing: 0px; }
        50% { transform: scale(1.3); opacity: 0.5; letter-spacing: 4px; }
        100% { transform: scale(1.6); opacity: 0; filter: blur(4px); }
    }
    .game-canvas {
        display: flex; justify-content: center; gap: 40px; height: 350px;
        overflow: hidden; background: #ffffff; position: relative; align-items: flex-start; padding-top: 20px;
    }
    .floating-word {
        font-size: 26px; font-weight: 600; font-family: 'Helvetica Neue', sans-serif;
        text-align: center; display: inline-block; position: relative; cursor: default; user-select: none;
    }
    .w1 { animation: fallDown 10.0s linear infinite; }
    .w2 { animation: fallDown 13.0s linear infinite; animation-delay: 3.5s; }
    .w3 { animation: fallDown 11.5s linear infinite; animation-delay: 1.5s; }
    .popped-word { animation: splashEffect 0.3s ease-out forwards !important; }
    .score-box { font-size: 16px; font-weight: 500; color: #555555; text-align: center; padding: 5px; }
    div.stTextInput { margin-top: 30px; }
    
    .txt-correct { color: #0066CC !important; font-weight: bold; }
    .txt-wrong { color: #FF3333 !important; font-weight: bold; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

# 2. 데이터 세팅
@st.cache_data
def load_game_data():
    try:
        return pd.read_csv("data.csv")
    except:
        return pd.DataFrame({
            "word": ["observe", "giant", "information", "harmony", "ocean"],
            "meaning": ["관찰하다", "거인", "정보", "조화", "대양, 바다"]
        })

df_game = load_game_data()

# 3. 미국식 발음 gTTS 음원 데이터 추출 함수
def generate_gtts_bytes(text):
    clean_text = str(text).strip("* ")
    if not clean_text or clean_text.lower() == "nan":
        return None
    try:
        tts = gTTS(text=clean_text, lang='en', tld='com', slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        return fp.getvalue()
    except:
        return None

# 4. 앱 시작 시 모든 단어의 음원을 백그라운드에서 한 번에 사전 탑재
if "audio_cache" not in st.session_state:
    st.session_state.audio_cache = {}
    with st.spinner("🔊 영어 발음 음원을 준비하고 있습니다... 잠시만 기다려 주세요!"):
        for idx, row in df_game.iterrows():
            word_key = str(row['word']).strip("* ")
            st.session_state.audio_cache[word_key] = generate_gtts_bytes(word_key)

# 5. 세션 상태 관리 변수 설정
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "active_words" not in st.session_state:
    st.session_state.active_words = []
if "used_words" not in st.session_state:
    st.session_state.used_words = []
if "just_popped_word" not in st.session_state:
    st.session_state.just_popped_word = None
if "popped_index" not in st.session_state:
    st.session_state.popped_index = None
if "last_refresh_time" not in st.session_state:
    st.session_state.last_refresh_time = None
if "study_states" not in st.session_state:
    st.session_state.study_states = {}

COLORS = ["#2AM2FF", "#FF3B6F", "#2BD9A5", "#FFAA00", "#9B5DE5"]

def replace_single_word(index_to_replace):
    if index_to_replace is None:
        return
    remaining_pool = [
        item for item in df_game.to_dict(orient="records")
        if item["word"] not in st.session_state.used_words
        and item["word"] not in [w["word"] for w in st.session_state.active_words if w]
    ]
    if not remaining_pool:
        remaining_pool = [item for item in df_game.to_dict(orient="records") if item["word"] not in [w["word"] for w in st.session_state.active_words if w]]
        if not remaining_pool: 
            remaining_pool = df_game.to_dict(orient="records")
            
    new_item = random.choice(remaining_pool)
    word_info = {
        "word": new_item["word"], "meaning": new_item["meaning"],
        "color": COLORS[random.randint(0, len(COLORS)-1)], "class": f"w{index_to_replace + 1}"
    }
    if len(st.session_state.active_words) < 3:
        st.session_state.active_words.append(word_info)
    else:
        st.session_state.active_words[index_to_replace] = word_info

def init_game_words():
    st.session_state.active_words = []
    st.session_state.used_words = []
    for i in range(3):
        replace_single_word(i)
    st.session_state.last_refresh_time = time.time()

def check_answer_callback():
    user_answer = st.session_state.game_input_box.strip()
    if user_answer:
        for i, b in enumerate(st.session_state.active_words):
            valid_meanings = [m.strip() for m in b["meaning"].split(",")]
            if user_answer in valid_meanings:
                st.session_state.score += 1
                st.session_state.just_popped_word = b["word"]
                st.session_state.popped_index = i
                st.session_state.used_words.append(b["word"])
                st.session_state.last_refresh_time = time.time()
                break
    st.session_state.game_input_box = ""

# 6. 📚 단어 자가 진단 다이얼로그 팝업 창 함수
@st.dialog("📖 Word List")
def show_study_records():
    st.write("지우기 버튼을 누르면 단어나 뜻이 빈칸으로 변합니다. 정답은 파란색, 정답이 아니면 빨간색으로 표시돼요. 스스로 공부해봐요😄")
    st.write("---")
    
    current_df = load_game_data()
    
    for index, row in current_df.iterrows():
        clean_word = str(row['word']).strip("* ")
        clean_meaning = str(row['meaning']).strip()
        
        w_key = f"w_{index}"
        m_key = f"m_{index}"
        
        if w_key not in st.session_state.study_states:
            st.session_state.study_states[w_key] = {"mode": "show", "status": "none"}
        if m_key not in st.session_state.study_states:
            st.session_state.study_states[m_key] = {"mode": "show", "status": "none"}
            
        col_word_area, col_meaning_area, col_audio_area = st.columns([3, 3, 2])
        
        # 🅰️ 영어 단어 지우기/확인 제어 구역
        with col_word_area:
            state = st.session_state.study_states[w_key]
            if state["mode"] == "show":
                inner_c1, inner_c2 = st.columns([2.5, 1.5])
                with inner_c1:
                    if state["status"] == "correct":
                        st.markdown(f"<span class='txt-correct'>{clean_word}</span>", unsafe_allow_html=True)
                    else:
                        st.write(clean_word)
                with inner_c2:
                    if st.button("지우기", key=f"dialog_del_w_{index}", use_container_width=True):
                        st.session_state.study_states[w_key] = {"mode": "edit", "status": "none"}
                        st.rerun()
            else:
                in_val = st.text_input("단어 입력", key=f"dlg_ans_w_{index}", placeholder="Type...", label_visibility="collapsed")
                c_btn, c_cancel = st.columns(2)
                with c_btn:
                    if st.button("확인", key=f"dlg_chk_w_{index}", use_container_width=True):
                        if in_val.strip().lower() == clean_word.lower():
                            st.session_state.study_states[w_key] = {"mode": "show", "status": "correct"}
                        else:
                            st.session_state.study_states[w_key]["status"] = "wrong"
                        st.rerun()
                with c_cancel:
                    if st.button("취소", key=f"dlg_cnl_w_{index}", use_container_width=True):
                        st.session_state.study_states[w_key] = {"mode": "show", "status": "none"}
                        st.rerun()
                if state["status"] == "wrong":
                    st.markdown("<span class='txt-wrong'>❌ 다시 입력해보세요!</span>", unsafe_allow_html=True)

        # 🅱️ 한국어 뜻 지우기/확인 제어 구역
        with col_meaning_area:
            state_m = st.session_state.study_states[m_key]
            if state_m["mode"] == "show":
                inner_m1, inner_m2 = st.columns([2.5, 1.5])
                with inner_m1:
                    if state_m["status"] == "correct":
                        st.markdown(f"<span class='txt-correct'>{clean_meaning}</span>", unsafe_allow_html=True)
                    else:
                        st.write(clean_meaning)
                with inner_m2:
                    if st.button("지우기", key=f"dialog_del_m_{index}", use_container_width=True):
                        st.session_state.study_states[m_key] = {"mode": "edit", "status": "none"}
                        st.rerun()
            else:
                in_val_m = st.text_input("뜻 입력", key=f"dlg_ans_m_{index}", placeholder="Type...", label_visibility="collapsed")
                cm_btn, cm_cancel = st.columns(2)
                with cm_btn:
                    if st.button("확인", key=f"dlg_chk_m_{index}", use_container_width=True):
                        valid_meanings = [m.strip() for m in clean_meaning.split(",")]
                        if in_val_m.strip() in valid_meanings:
                            st.session_state.study_states[m_key] = {"mode": "show", "status": "correct"}
                        else:
                            st.session_state.study_states[m_key]["status"] = "wrong"
                        st.rerun()
                with cm_cancel:
                    if st.button("취소", key=f"dlg_cnl_m_{index}", use_container_width=True):
                        st.session_state.study_states[m_key] = {"mode": "show", "status": "none"}
                        st.rerun()
                if state_m["status"] == "wrong":
                    st.markdown("<span class='txt-wrong'>❌ 다시 입력해보세요!</span>", unsafe_allow_html=True)
                    
        # 🔊 [수정포인트] TypeError 방지 수문장 설치 (바이트 데이터 타입 검증 후 출력)
        with col_audio_area:
            cached_audio = st.session_state.audio_cache.get(clean_word, None)
            if cached_audio and isinstance(cached_audio, bytes):
                try:
                    st.audio(cached_audio, format="audio/mp3", key=f"audio_player_{index}")
                except:
                    st.caption("🔊 재생 오류")
            else:
                st.caption("🔊 음원 없음")
                
        st.write("---")

# 7. 🎮 단어 게임 메인 프레그먼트 구역
@st.fragment
def word_game_frame():
    st.title("🕹️ 아진T와 함께하는 단어 게임💕")

    # [화면 1] 로그인 및 시작 전 화면
    if not st.session_state.game_started:
        st.write("위에서 내려오는 영단어의 뜻을 시간 내에 맞춰보세요!")
        
        name_input = st.text_input("이름을 입력하세요:", value=st.session_state.user_name, key="word_game_user_name_input")
        
        if st.button("Start", use_container_width=True):
            if name_input.strip() == "":
                st.warning("이름을 입력해야 게임을 시작할 수 있습니다!")
            else:
                st.session_state.user_name = name_input.strip()
                st.session_state.game_started = True
                st.session_state.start_time = time.time()
                st.session_state.score = 0
                st.session_state.just_popped_word = None
                st.session_state.popped_index = None
                st.session_state.study_states = {}
                init_game_words()
                st.rerun()

    # [화면 2] 게임 진행 중 또는 종료 화면
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, 50 - int(elapsed_time))
        
        # ⏱️ 게임 종료 상태
        if remaining_time <= 0:
            st.title("🚨 Game Over")
            st.error(f"게임이 끝났습니다😉! {st.session_state.user_name}님의 최종 점수는 **{st.session_state.score}점**입니다.👍")
            
            if st.button("다시 도전하기", use_container_width=True):
                st.session_state.game_started = False
                st.session_state.start_time = None
                st.session_state.active_words = []
                st.session_state.used_words = []
                st.session_state.just_popped_word = None
                st.session_state.popped_index = None
                st.session_state.last_refresh_time = None
                st.session_state.study_states = {}
                st.rerun()
                
            st.write("---")
            
            if st.button("📚 단어학습하기", use_container_width=True):
                show_study_records()

        # 🕹️ 게임 진행 중 상태
        else:
            if time.time() - st.session_state.last_refresh_time > 12.0:
                for b in st.session_state.active_words:
                    st.session_state.used_words.append(b["word"])
                for i in range(3):
                    replace_single_word(i)
                st.session_state.last_refresh_time = time.time()
                st.rerun()

            col1, col2 = st.columns(2)
            with col1: 
                st.markdown(f"<div class='score-box'>👤 이름: {st.session_state.user_name}</div>", unsafe_allow_html=True)
            with col2: 
                st.markdown(f"<div class='score-box'>⭐ SCORE: {st.session_state.score}점 | ⏱️ {remaining_time}초</div>", unsafe_allow_html=True)
            st.write("---")
            
            b_html = "<div class='game-canvas'>"
            for b in st.session_state.active_words:
                if st.session_state.just_popped_word == b["word"]:
                    b_html += f"<div class='floating-word popped-word' style='color: {b['color']};'>{b['word']}</div>"
                else:
                    b_html += f"<div class='floating-word {b['class']}' style='color: {b['color']};'>{b['word']}</div>"
            b_html += "</div>"
            st.markdown(b_html, unsafe_allow_html=True)
            
            st.text_input("", key="game_input_box", placeholder="Type here...", on_change=check_answer_callback)
            
            p_idx = st.session_state.get("popped_index", None)
            if st.session_state.just_popped_word and p_idx is not None:
                time.sleep(0.3)
                replace_single_word(p_idx)
                st.session_state.just_popped_word = None
                st.session_state.popped_index = None
                st.rerun()
                
            time.sleep(0.4)
            st.rerun()

# 8. 격리된 프레그먼트 함수 구동
word_game_frame()
