import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="본문 내용 확인 퀴즈", page_icon="📖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .q-box { padding: 20px; border-radius: 10px; background-color: #f8f9fa; margin-bottom: 20px; border-left: 5px solid #2AM2FF; font-size: 16px; }
    .feedback-correct { color: #0066CC; font-weight: bold; margin-top: 5px; }
    .feedback-wrong { color: #FF3333; font-weight: bold; margin-top: 5px; }
    .exp-box { padding: 15px; background-color: #f1f8ff; border-radius: 8px; border: 1px solid #c8e1ff; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_quiz_data():
    try:
        df = pd.read_csv("pages/quizdata.csv", encoding="utf-8")
        return df
    except Exception as e:
        st.error(f"데이터 로드 실패: {e}")
        return pd.DataFrame()

df_quiz = load_quiz_data()

# 세션 상태 제어 변수 초기화
if "quiz_submitted" not in st.session_state: st.session_state.quiz_submitted = False
if "wrong_indices" not in st.session_state: st.session_state.wrong_indices = []
if "show_explanation" not in st.session_state: st.session_state.show_explanation = False
if "review_mode" not in st.session_state: st.session_state.review_mode = False
if "review_submitted" not in st.session_state: st.session_state.review_submitted = False

st.title("📖 본문 내용 확인 퀴즈")

if df_quiz.empty:
    st.warning("quizdata.csv 파일 내용을 읽을 수 없거나 형식이 맞지 않습니다. GitHub 저장소를 확인해 주세요.")
else:
    # 보기 분리 함수
    def parse_choices(choice_str):
        if not isinstance(choice_str, str):
            return ["", "", "", ""]
        if "T / F" in choice_str or "T/F" in choice_str:
            return ["T", "F"]
        tokens = re.split(r'[①②③④\n\r]+', choice_str)
        choices = [t.strip() for t in tokens if t.strip()]
        while len(choices) < 4:
            choices.append("")
        return choices[:4]

    # 정답 인덱스 변환 함수
    def parse_answer(ans_val, choices_list):
        ans_str = str(ans_val).strip()
        if ans_str in ["1", "2", "3", "4"]: return int(ans_str)
        if "①" in ans_str: return 1
        if "②" in ans_str: return 2
        if "③" in ans_str: return 3
        if "④" in ans_str: return 4
        if ans_str.upper() in ["T", "F"]:
            if ans_str.upper() in choices_list:
                return choices_list.index(ans_str.upper()) + 1
        return 1

    # ==================== [모드 2] 틀린 문제만 다시 풀기 모드 ====================
    if st.session_state.review_mode:
        st.subheader("🔄 오답 노트: 틀린 문제 다시 풀기")
        st.write("틀렸던 문제들을 다시 찬찬히 읽고 정답을 골라보세요.")
        st.write("---")
        
        # ⚠️ 폼 내부 렌더링 꼬임 방지를 위해 폼 선언과 파일 매칭 순서를 정돈함
        with st.form("review_form"):
            review_answers = {}
            for index in st.session_state.wrong_indices:
                row = df_quiz.iloc[index]
                q_num = row['번호']
                st.markdown(f"<div class='q-box'><b>Q{q_num}. {row['문제']}</b></div>", unsafe_allow_html=True)
                
                parsed_opts = parse_choices(row['보기'])
                
                # 💡 [조치 완료] key값 뒤에 '_review' 접미사를 붙여서 메인 퀴즈의 라디오 버튼 key와 절대로 충돌하지 않도록 차단
                user_select = st.radio(
                    "정답을 고르세요:", options=list(range(1, len(parsed_opts) + 1)),
                    format_func=lambda x: parsed_opts[x-1], key=f"review_q_{index}_review"
                )
                review_answers[index] = user_select
                st.write("")
                
            review_submit = st.form_submit_button("오답 채점하기", use_container_width=True)
            
        if review_submit:
            st.session_state.review_submitted = True
            st.rerun() # ⚠️ 제출 즉시 화면을 갱신하여 Missing Submit Button 구조 오류 파괴
            
        if st.session_state.review_submitted:
            st.write("### 📊 오답 확인 결과")
            still_wrong = []
            for index in st.session_state.wrong_indices:
                row = df_quiz.iloc[index]
                parsed_opts = parse_choices(row['보기'])
                correct_idx = parse_answer(row['정답'], parsed_opts)
                
                st.write(f"**Q{row['번호']}번 문제**")
                # 세션에 기록된 컴포넌트 데이터 상태를 안전하게 참조
                u_ans = st.session_state.get(f"review_q_{index}_review", None)
                
                if u_ans == correct_idx:
                    st.markdown("<p class='feedback-correct'>⭕ 정답입니다! 완벽히 이해하셨네요.</p>", unsafe_allow_html=True)
                else:
                    still_wrong.append(index)
                    st.markdown("<p class='feedback-wrong'>❌ 아직 조금 헷갈리나 봐요. 아래 해설을 참고해 보세요!</p>", unsafe_allow_html=True)
                st.write("---")
                
            if not still_wrong:
                st.success("🎉 축하합니다! 틀린 문제를 모두 맞췄습니다!")
            else:
                st.warning(f"아직 {len(still_wrong)}문제가 더 남아있습니다. 다시 복습해 보세요!")
                
            if st.button("전체 퀴즈 화면으로 돌아가기", use_container_width=True):
                st.session_state.quiz_submitted = False
                st.session_state.review_mode = False
                st.session_state.review_submitted = False
                st.session_state.show_explanation = False
                st.rerun()

    # ==================== [모드 1] 최초 15문항 전체 풀기 모드 ====================
    else:
        st.write("오늘 읽은 본문 내용을 잘 기억하고 있나요? 문제를 풀고 확인해 보세요!")
        st.write("---")

        with st.form("quiz_form"):
            user_answers = {}
            for index, row in df_quiz.iterrows():
                q_num = row['번호']
                st.markdown(f"<div class='q-box'><b>Q{q_num}. {row['문제']}</b></div>", unsafe_allow_html=True)
                
                parsed_opts = parse_choices(row['보기'])
                
                user_select = st.radio(
                    "정답을 고르세요:", options=list(range(1, len(parsed_opts) + 1)),
                    format_func=lambda x: parsed_opts[x-1], key=f"quiz_q_{index}_main"
                )
                user_answers[index] = user_select
                st.write("")
            submitted = st.form_submit_button("제출 및 채점하기", use_container_width=True)

        if submitted:
            st.session_state.quiz_submitted = True
            st.session_state.wrong_indices = []
            
            # 채점 연산을 제출 즉시 연동하여 스냅샷 확보
            for index, row in df_quiz.iterrows():
                parsed_opts = parse_choices(row['보기'])
                correct_idx = parse_answer(row['정답'], parsed_opts)
                if user_answers[index] != correct_idx:
                    st.session_state.wrong_indices.append(index)
            st.rerun()

        if st.session_state.quiz_submitted:
            st.write("### 📊 채점 결과")
            total = len(df_quiz)
            score = total - len(st.session_state.wrong_indices)
                    
            st.success(f"총 {total}문제 중 **{score}문제**를 맞췄습니다.")
            st.write("---")
            
            col1, col2 = st.columns(2)
            with col1:
                if len(st.session_state.wrong_indices) > 0:
                    if st.button("❌ 틀린 문제만 다시 풀기", use_container_width=True):
                        st.session_state.review_mode = True
                        st.session_state.review_submitted = False
                        st.rerun()
                else:
                    st.button("⭕ 틀린 문제가 없습니다!", disabled=True, use_container_width=True)
                    
            with col2:
                if st.button("💡 전체 문제 해설 확인", use_container_width=True):
                    st.session_state.show_explanation = not st.session_state.show_explanation
                    st.rerun()

            if st.session_state.show_explanation:
                st.write("")
                st.subheader("📋 퀴즈 전체 문항 해설 일람")
                for index, row in df_quiz.iterrows():
                    parsed_opts = parse_choices(row['보기'])
                    correct_idx = parse_answer(row['정답'], parsed_opts)
                    
                    if 0 < correct_idx <= len(parsed_opts):
                        correct_text = parsed_opts[correct_idx-1]
                    else:
                        correct_text = str(row['정답'])
                        
                    exp_text = str(row['해설']) if '해설' in df_quiz.columns else "등록된 해설이 없습니다."
                    
                    st.markdown(f"""
                    <div class='exp-box'>
                        <b>Q{row['번호']}. {row['문제']}</b><br>
                        <span style='color: #0066CC;'>• 정답: {row['정답']} ({correct_text})</span><br>
                        <span style='color: #555555;'>• 해설: {exp_text}</span>
                    </div>
                    """, unsafe_allow_html=True)
