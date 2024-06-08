import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="Post-Test", page_icon="⌛")

st.image("assets/posttest.gif")

def loadQuizData():
    with open("data/pretestquiz.json", "r") as file:
        return json.load(file)

required_session_state_vars = [
    "quiz_data", "total_questions", "curr_idx",
    "correct_answers", "incorrect_answers", "results"
]

if any(var not in st.session_state for var in required_session_state_vars):
    quiz_data = loadQuizData()
    st.session_state.quiz_data = quiz_data["qna"]
    st.session_state.total_questions = quiz_data["count"]
    st.session_state.curr_idx = 0
    st.session_state.correct_answers = 0
    st.session_state.incorrect_answers = 0
    st.session_state.results = {}

def getQuestion():
    return st.session_state.quiz_data[st.session_state.curr_idx]

def getCount():
    return st.session_state.curr_idx + 1

quiz_data = getQuestion()
count = getCount()

st.markdown("""
    <style>
    .e1f1d6gn0, .e1f1d6gn3, .e1f1d6gn4{
        align-items:center;
        text-align:center;
    } 
    p{
        text-align:left;
    }
    img{
        align-items:center;
        width:250px;
    }
    .e115fcil2 {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    </style>""", unsafe_allow_html=True)
st.title("Post-Test ⌛", anchor = False)

st.markdown(f"Question {count} :\n  {quiz_data['question']}")

form = st.form(key=f"quiz_form_{count}")
user_choice = form.radio("Choose an answer:", quiz_data['options'])
submitted = form.form_submit_button("Submit your answer 📬", type="primary", use_container_width = True)

if submitted:
    if user_choice == quiz_data['correct_answer']:
        st.session_state.correct_answers += 1
        st.success("Correct", icon="✅")
    else:
        st.session_state.incorrect_answers += 1
        st.error("Incorrect", icon="❌")

    st.markdown(f"**:red[Explanation :]** \n\n{quiz_data['explanation']}")

next_question = st.button(
    "Next Question ➡️",
    use_container_width = True,
    disabled = count >= st.session_state.total_questions
)
if next_question and count < st.session_state.total_questions:
    if count < st.session_state.total_questions:
        st.session_state.curr_idx += 1
        st.rerun()
else:
    st.header(f"**:orange[Statistics 👨‍🔬]**", anchor = False)
    container = st.container(border=True)
    
    container.subheader(f"**:green[Correct :] {st.session_state.correct_answers}/{st.session_state.total_questions}**")
    container.subheader(f"**:red[Incorrect :] {st.session_state.incorrect_answers}/{st.session_state.total_questions}**")
    