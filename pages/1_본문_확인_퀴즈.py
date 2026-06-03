import streamlit as st
import pandas as pd

st.set_page_config(page_title="본문 내용 확인 퀴즈", page_icon="📖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .q-box { padding: 20px; border-radius: 10px; background-color: #f8f9fa; margin-bottom: 20px; border-left: 5px solid #2AM2FF; }
    .feedback-correct { color: #0066CC; font-weight: bold; margin-top: 5px; }
    .feedback-wrong { color: #FF3333; font-weight: bold; margin-top: 5px; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_quiz_data():
    try:
        # pages 폴더 안에 있는 quizdata.csv 파일을 로드합니다.
        return pd.read_csv("pages/quizdata.csv")
    except:
        return pd.DataFrame({
            "question": ["기본 질문: 고래의 숨구멍을 무엇이라 하나요?"],
            "choice1": ["분기공(Blowhole)"], "choice2": ["지느러미"], "choice3": ["꼬리"], "choice4": ["아가미"],
            "answer": [1]
        })

df_quiz = load_quiz_data()

st.title("📖 본문 내용 확인 퀴즈")
st.write("오늘 읽은 본문 내용을 잘 기억하고 있나요? 😊 문제를 풀고 확인해 보세요💪!")
st.write("---")

with st.form("quiz_form"):
    user_answers = {}
    for index, row in df_quiz.iterrows():
        st.markdown(f"<div class='q-box'><b>Q{index+1}. {row['question']}</b></div>", unsafe_allow_html=True)
        choices = [str(row['choice1']), str(row['choice2']), str(row['choice3']), str(row['choice4'])]
        user_select = st.radio(
            "정답을 고르세요:",
            options=[1, 2, 3, 4],
            format_func=lambda x: choices[x-1],
            key=f"quiz_q_{index}"
        )
        user_answers[index] = user_select
        st.write("")
    submitted = st.form_submit_button("제출 및 채점하기", use_container_width=True)

if submitted:
    st.write("### 📊 채점 결과")
    score = 0
    total = len(df_quiz)
    for index, row in df_quiz.iterrows():
        st.write(f"**Q{index+1}번 문제**")
        if user_answers[index] == int(row['answer']):
            score += 1
            st.markdown("<p class='feedback-correct'>⭕ 정답입니다!</p>", unsafe_allow_html=True)
        else:
            correct_choice_text = str(row[f'choice{int(row["answer"])}'])
            st.markdown(f"<p class='feedback-wrong'>❌ 틀렸습니다. (정답: {correct_choice_text})</p>", unsafe_allow_html=True)
        st.write("---")
    st.success(f"축하합니다! 총 {total}문제 중 **{score}문제**를 맞췄습니다.")
