import streamlit as st
from openai import OpenAI
from streamlit_chat import message
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
def api_calling(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


st.title("ChatGPT Chatbot")

# Initialize session state
if "user_input" not in st.session_state:
    st.session_state.user_input = []

if "openai_response" not in st.session_state:
    st.session_state.openai_response = []

# Welcome message
st.write("👋 Ask me anything!")

user_input = st.text_input("Write here")

if user_input:
    output = api_calling(user_input)

    st.session_state.user_input.append(user_input)
    st.session_state.openai_response.append(output)

# Display messages
for i in range(len(st.session_state.user_input)):
    message(st.session_state.user_input[i], is_user=True, key=f"user{i}")
    message(st.session_state.openai_response[i], key=f"bot{i}")