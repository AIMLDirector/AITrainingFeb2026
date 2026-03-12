import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
st.title("AI Chatbot")

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5, 0.1)
top_p = st.sidebar.slider("Top-p (nucleus sampling)", 0.0, 1.0, 0.9, 0.1)
max_tokens = st.sidebar.slider("Max Tokens", 1, 2048, 100, 10)
st.sidebar.write(f"Temperature: {temperature}, Top-p: {top_p}, Max Tokens: {max_tokens}")
input_prompt = st.chat_input("ask me anything")

if input_prompt:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": input_prompt}],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens
    )
    st.write(response.choices[0].message.content)
