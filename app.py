import streamlit as st
from google import genai

# Get API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Create Gemini client
client = genai.Client(api_key=api_key)

# Page title
st.title("🤖 Gemini AI Chatbot")

# Sidebar
with st.sidebar:

    st.header("About")

    st.write(
        "This AI chatbot is built using Streamlit "
        "and Google Gemini API."
    )

    st.write("Model: Gemini 2.5 Flash")

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# Intro text
st.write("Ask anything and chat with Gemini AI.")

# Create chat history
if "messages" not in st.session_state:

    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Type your message...")

# If user sends message
if prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show user message
    with st.chat_message("user"):

        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                answer = response.text

            except Exception as e:

                answer = str(e)

            st.markdown(answer)

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
