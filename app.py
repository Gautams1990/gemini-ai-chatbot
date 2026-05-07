import streamlit as st
from google import genai

# Create Gemini client
client = genai.Client(api_key="AIzaSyDemYwCVUp9bHhg6hSKSDA9SvIDilGI9VY")

# App titlestreamlit run app.py
st.title("🤖 Gemini AI Chatbot")
st.write("Ask any question and get AI-generated answers using Gemini LLM.")
# User input
user_input = st.text_input("Ask me anything:")

# Generate AI response
if user_input:

    with st.spinner("Thinking..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        st.write("🤖 AI Response:")
        st.write(response.text)