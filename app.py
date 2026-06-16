import streamlit as st
import json
from difflib import get_close_matches

# -------------------------
# PAGE SETTINGS
# -------------------------

st.set_page_config(
    page_title="FAQ CHATBOT",
    page_icon="🧠",
    layout="centered"
)

# -------------------------
# LOAD FAQ DATA
# -------------------------

with open("faq_data.json", "r", encoding="utf-8") as file:
    faq_data = json.load(file)

# -------------------------
# FIND ANSWER
# -------------------------

def get_answer(question):

    question = question.lower()

    matches = get_close_matches(
        question,
        faq_data.keys(),
        n=1,
        cutoff=0.3
    )

    if matches:
        return faq_data[matches[0]]

    return "Sorry, I couldn't find a suitable answer. Please contact customer support."

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

body {
    background-color: #0B1120;
}

.title {
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:white;
}

.subtitle {
    text-align:center;
    color:#BDBDBD;
    margin-bottom:25px;
}

.user-box {
    background: linear-gradient(
        90deg,
        #6D5BFF,
        #9D4EDD
    );

    color:white;
    padding:15px;
    border-radius:20px;
    margin-top:15px;
}

.bot-box {
    background:#1E293B;
    color:white;
    padding:15px;
    border-radius:20px;
    margin-top:10px;
}

.footer {
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------

st.markdown(
    "<div class='title'>🧠 YOUR FAQ CHATBOT</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Your Intelligent Shopping Companion</div>",
    unsafe_allow_html=True
)

# -------------------------
# WELCOME
# -------------------------

st.info("""
👋 Welcome!

Ask me about:

• Orders

• Shipping

• Tracking

• Refunds

• Returns

• Payments
""")

# -------------------------
# SESSION
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# CHAT INPUT
# -------------------------

question = st.chat_input(
    "Type your question..."
)

if question:

    answer = get_answer(question)

    st.session_state.messages.append(
        ("user", question)
    )

    st.session_state.messages.append(
        ("bot", answer)
    )

# -------------------------
# DISPLAY CHAT
# -------------------------

for message in st.session_state.messages:

    if message[0] == "user":

        st.markdown(
            f"""
            <div class="user-box">
            👤 {message[1]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="bot-box">
            🤖 {message[1]}
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------
# FOOTER
# -------------------------

st.markdown(
"""
<div class="footer">
Developed by Kashish Salman Ali<br>
CodeAlpha AI Internship
</div>
""",
unsafe_allow_html=True
)