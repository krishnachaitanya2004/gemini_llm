import streamlit as st
import os
import google.generativeai as genai
import time

#Title
st.title("GenAI - Generative AI for Everyone")

#Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDmn9ObT4lGQc5omfnvbjGvLo0h2KsvqPs"
api_key = os.environ.get('GOOGLE_API_KEY')
genai.configure()

#Creating the model
model = genai.GenerativeModel('gemini-pro')

#type writing effect
def typerwriter(query):
    full_response = ""     
    message_placeholder = st.empty()
    for chunk in query.split(" "):
        full_response += chunk + " "
        time.sleep(0.1)
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
    

#Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#User input
if query := st.chat_input("Enter your message"):
    with st.chat_message("user"):
        st.markdown(query)
        st.session_state.messages.append({"role": "user", "content": query})

    with st.spinner("Generating response..."):
        response = model.generate_content(query)

        with st.chat_message("assistant"): 
            typerwriter(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
