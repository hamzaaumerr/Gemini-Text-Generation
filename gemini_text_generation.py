import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["gemini_api"])

model = genai.GenerativeModel('gemini-1.5-flash')

def modelResponce(user_input):
  response = model.generate_content(user_input)
  return(response.text)
st.title("Google Gemini Text Generation")
user_input = st.text_input("Enter your prompt")

if st.button("Generate"):
  if user_input:
    output = modelResponce(user_input)
    st.write(output)
  else:
    st.warning("Please enter a prompt.")