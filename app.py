import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Streamlit title
st.title("🤖 Gemini AI Chatbot")

st.write("Ask any question and get AI-generated answers.")

# User input
user_input = st.text_input("Ask me anything:")

# Generate response
if user_input:

    with st.spinner("Thinking..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        st.write("🤖 AI Response:")
        st.write(response.text)