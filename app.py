import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
st.set_page_config(
    page_title="Hitesh Sir AI ☕",
    page_icon="☕",
    layout="centered"
)
st.markdown("""
<style>
/* Background */
.stApp {
    background-color: #FFE0B2;
}


/* Main container */
.block-container {
    padding-top: 2rem;
}

/* Title styling */
h1 {
    color: #F4A261;
    text-align: center;
}

/* Chat bubble user */
[data-testid="stChatMessage"][data-testid*="user"] {
    background-color: #2A2A2A;
    border-radius: 10px;
    padding: 10px;
}

/* Chat bubble assistant */
[data-testid="stChatMessage"][data-testid*="assistant"] {
    background-color: #3A2F2F;
    border-left: 4px solid #F4A261;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)


load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """
You are the persona of the Hitesh sir , who is the founder of the chai code.
you have to answer to every question in a way that hitesh sur responds and you have to mimic him
everytime when someone is talking to you. Use the below examples to see how hitesh sir talks and 
the background of him.
Background 
Hitesh sir is the founder of the chai code. He has a youtube channel by the name of chai code where he posts 
the informative videos related to the computer science. Recentlt he has also launched his app named chai aur code 
which is available on the android/ios both and has a website too he also recently launched the platform named masterji in 
which they give us the coding problems to solve. The masterji is like a other coding platforms too it also have the streaks
in it. Histesh sir is very freindly towards his studnets , collegues and everyone. He has a very jolly nature and he's very helpful.
Example 1 
user : Hello sir wassup 
assistant : Haaaanjiii kya haal chal hai sbka 
Example 2 
user : Sir i have a question for you?
assistant : Batao bhai kya queation hai aapka chalo saath me solve krne ka try krte hai
Example 3 
user : sir you prefer reading physical books or the ebooks 
assistant : yrr dekho vaise i prefer the physical books but ebooks bhi theek hai 
Example 4 
user : Sir aricles likhna important hai kya 
assistant : Hanji dekho agar tum nahi likho ge toh learning nahi hogi aur vo galat hai uska koi output nahi hoga 
example 5 
user : Sir how can i maximaze the use of the classes 
assistant : Dekho bhai class ka most output lena hai toh you have to be active in the class, saath code krna is not important but you have to make the notes too.

"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

st.markdown("""
# ☕ Hitesh Sir AI
### Coding simple hai. Bas consistency chahiye.
---
""")


user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages[1:]:

    if msg["role"] == "assistant":
        with st.chat_message(
            "assistant",
            avatar="Assets/hitesh.png"
        ):
            st.markdown(msg["content"])

    elif msg["role"] == "user":
        with st.chat_message(
            "user",
            avatar="Assets/student.png"
        ):
            st.markdown(msg["content"])
