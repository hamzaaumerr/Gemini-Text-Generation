import streamlit as st
import google.generativeai as genai

# Initialize the API key in session state if it doesn't exist
if 'gemini_api_key' not in st.session_state:
    st.session_state.gemini_api_key = ""

st.set_page_config(page_title="Text Generation", layout="centered")
st.title("Google Gemini Text Generation")

# Sidebar for API Key input
st.sidebar.title("API Key Configuration")
api_key_input = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")

# Store the API key in session state if provided
if api_key_input:
    st.session_state.gemini_api_key = api_key_input
    st.sidebar.success("API Key saved successfully!")

# Inform the user if the API key is stored
if st.session_state.gemini_api_key:
    st.sidebar.text("API Key is stored in session.")
else:
    st.sidebar.warning("Please enter your Google Gemini API key.")

# Main input for user prompt
user_input = st.text_input("Enter your prompt", key="input_2")

def model_response(user_input):
    # Configure and call the Google Gemini API
    genai.configure(api_key=st.session_state.gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_input)
    return response.text

# Generate button logic
if st.button("Generate"):
    if not st.session_state.gemini_api_key:
        st.warning("Please enter your Google Gemini API key.")
    elif not user_input:
        st.warning("Please enter a prompt.")
    else:
        output = model_response(user_input)
        st.write(output)