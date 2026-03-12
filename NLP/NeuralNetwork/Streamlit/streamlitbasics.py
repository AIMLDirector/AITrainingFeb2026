import streamlit as st

st.title("Streamlit Basics")
input = st.text_input("Enter your text here ", key="input")
if input:
    st.write(f"You entered: {input}")

def clear_text():
    st.session_state.input = ""

st.button("Clear text", on_click=clear_text)

# st.button("Clear text", on_click=lambda: st.session_state.update({"input": ""}))

value = st.slider("Select a value", 0, 100, 50,5)
st.write(f"Selected value: {value}")
choices = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {choices}")
checkbox = st.checkbox("i agree with the terms and conditions")
if checkbox:
    st.write("Thank you for agreeing!")
