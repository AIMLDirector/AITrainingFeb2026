import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

st.title("AI Chatbot")

# Initialize chat storage
if "chats" not in st.session_state:
    st.session_state.chats = {"Chat 1": []}

if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Chat 1"

# Sidebar for chat history
st.sidebar.title("Chats")

# Create new chat
if st.sidebar.button("➕ New Chat"):
    chat_name = f"Chat {len(st.session_state.chats)+1}"
    st.session_state.chats[chat_name] = []
    st.session_state.current_chat = chat_name

# Display chats
for chat in st.session_state.chats.keys():
    if st.sidebar.button(chat):
        st.session_state.current_chat = chat

# Delete current chat
if st.sidebar.button("🗑 Delete Chat"):
    del st.session_state.chats[st.session_state.current_chat]

    if st.session_state.chats:
        st.session_state.current_chat = list(st.session_state.chats.keys())[0]
    else:
        st.session_state.chats["Chat 1"] = []
        st.session_state.current_chat = "Chat 1"

current_chat = st.session_state.current_chat
messages = st.session_state.chats[current_chat]

# Display messages
for msg in messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("Ask something")

if prompt:
    messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)