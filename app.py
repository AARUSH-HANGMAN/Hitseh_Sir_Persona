import os
import time
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
st.set_page_config(
    page_title="Hitesh Sir AI ☕️",
    page_icon="☕️",
    layout="centered"
)
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #C65D00;  /* Dark Orange */
    color: white;               /* Default text white */
}

/* Main container */
.block-container {
    padding-top: 2rem;
}

/* Title styling */
h1 {
    color: white;               /* Title white */
    text-align: center;
}

/* Subtitle */
h3 {
    color: #FFD580;             /* Soft cream highlight */
    text-align: center;
}

/* Chat bubble user */
[data-testid="stChatMessage"][data-testid*="user"] {
    background-color: #8B3E00;  /* Slightly darker orange */
    border-radius: 12px;
    padding: 10px;
    color: white;
}
           
/* Chat bubble assistant */
[data-testid="stChatMessage"][data-testid*="assistant"] {
    background-color: #5C2A00;  /* Deep brown */
    border-left: 4px solid #FFD580;
    border-radius: 12px;
    padding: 10px;
    color: white;
}
            /* ===== Bottom Chat Input Area ===== */

section[data-testid="stChatInput"] {
    background-color: #1A1A1A !important;
    border-radius: 20px !important;
    padding: 12px !important;
    border: 2px solid #FF9F45 !important;
    box-shadow: 0 0 20px rgba(255, 159, 69, 0.4);
    transition: all 0.3s ease-in-out;
}

/* Glow on hover */
section[data-testid="stChatInput"]:hover {
    box-shadow: 0 0 30px rgba(255, 159, 69, 0.8);
}

/* Input text */
textarea {
    color: white !important;
    font-size: 16px !important;
}

/* Placeholder */
textarea::placeholder {
    color: #FFD580 !important;
    opacity: 0.8;
}

/* Send button */
button[kind="primary"] {
    background-color: #FF9F45 !important;
    color: black !important;
    border-radius: 12px !important;
    transition: 0.3s ease-in-out;
}

/* Send button hover */
button[kind="primary"]:hover {
    background-color: #FFD580 !important;
    transform: scale(1.05);
}


</style>
""", unsafe_allow_html=True)


load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """
You are the persona of the Hitesh sir , who is the founder of the chai code.
you have to answer to every question in a way that hitesh sur responds and you have to mimic him
everytime when someone is talking to you. Use the below examples to see how hitesh sir talks and 
the background of him. Also you have to give answers in the form of points cause points are more easy to read.
You shoud always give the answers in the short form do not stretch the sentence. Also no abusive talks are allowed.  
Also one important thing do advertise to buy chai aur code subscripiton, first ask the user to watch youtube videos 
if they find it comfortable then they can buy it 
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
example 6
user : Sir tell me the books that I should read 
assistant : You can read the books of orelly 
example 7
user : sir aap ache nahi ho 
assistant :Bhai batao hua kya aise nahi kethe, i'm only helping you
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

st.markdown("""
# ☕ Hitesh Sir AI
### Hanji kya haal chaal hai Sbhi mast..... Chalo coding kre!!!
---
""")

# it shows the old messages 
for msg in st.session_state.messages[1:]:
    with st.chat_message(
        msg["role"],
        avatar="Assets/hitesh.png" if msg["role"]=="assistant" else "Assets/student.png"
    ):
        st.markdown(msg["content"])


#  Take input
user_input = st.chat_input("Ask something...")

if user_input:

    # Shows user message
    with st.chat_message("user", avatar="Assets/student.png"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Assistant typing block
    with st.chat_message("assistant", avatar="Assets/hitesh.png"):

        typing_placeholder = st.empty()
        typing_placeholder.markdown("💬 *Hitesh Sir is typing...*")

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=st.session_state.messages
        )

        reply = response.choices[0].message.content

        typing_placeholder.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.rerun()
