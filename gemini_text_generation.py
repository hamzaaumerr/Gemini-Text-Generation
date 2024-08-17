import streamlit as st
import google.generativeai as genai

if 'gemini_api_key' not in st.session_state:
  st.session_state.gemini_api_key = ""

st.set_page_config(page_title="Text Generation", layout="centered")
st.title("Google Gemini Text Generation")

if st.session_state.gemini_api_key == "":
  st.session_state.gemini_api_key = st.text_input("Enter your Google Gemini API Key", type="password", key="input_1")
  if st.session_state.gemini_api_key:
    st.success("API Key saved successfully!")
else:
    st.text("API Key is stored in session.")

user_input = st.text_input("Enter your prompt", key="input_2")

def model_responce(user_input):
  genai.configure(api_key=st.session_state.gemini_api_key)
  model = genai.GenerativeModel('gemini-1.5-flash')
  response = model.generate_content(user_input)
  return response.text

if st.button("Generate"):
  if not st.session_state.api_key:
    st.warning("Please enter your Google Gemini API key.")
  elif not user_input:
    st.warning("Please enter a prompt.")
  else:
    output = model_responce(user_input)
    st.write(output)