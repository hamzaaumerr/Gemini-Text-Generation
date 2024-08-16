import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api = os.getenv('GEMINI_API')
genai.configure(api_key=gemini_api)

model = genai.GenerativeModel('gemini-1.5-flash')

def modelResponce(user_input):
  response = model.generate_content(user_input)
  return(response.text)
st.title("Google Gemini Text Generation")
user_input = st.text_input("Enter your prompt")

if st.button("Generate"):
  if user_input:
    output = modelResponce(user_input)
<<<<<<< HEAD
    st.write(f"Generated Text: {output}")
=======
    st.write(output)
>>>>>>> 73b11af (Initial commit)
  else:
    st.warning("Please enter a prompt.")