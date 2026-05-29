# 🤖 Gemini AI Chatbot

An AI-powered chatbot built using Streamlit and Google Gemini API with real-time conversational AI capabilities.

## 🌐 Live Demo
👉 [Click Here to Use the App](https://gemini-ai-chatbot-haygzpo26jresxh26jfbbk.streamlit.app/)

## ✨ Features
- Real-time AI-generated responses
- Chat history support
- Clear chat functionality
- Modern Streamlit chat interface
- Sidebar with project information
- Secure API key handling using `.env`
- Graceful error handling for API limits or service issues

## 🛠 Technologies Used
- Python
- Streamlit
- Google Gemini API
- google-genai SDK
- python-dotenv

## 🧠 Project Workflow

gemini-ai-chatbot/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── chatbot_output.jpg
User Input → Streamlit UI → Gemini API → Gemini LLM → AI Response


## ⚙️ Setup Instructions

**1. Clone the repository**
git clone https://github.com/Gautams1990/gemini-ai-chatbot.git
cd gemini-ai-chatbot
**2. Create and activate virtual environment**
python -m venv .venv
.venv\Scripts\activate

**3. Install dependencies**
pip install -r requirements.txt

**4. Add your Gemini API key**

Create a `.env` file and add:
GEMINI_API_KEY=your_api_key_here

streamlit run app.py
## 🔐 Environment Variables
This project uses a `.env` file to keep the API key secure.
Make sure `.env` is added to `.gitignore`.

## 📸 Screenshots
![Chatbot Output](chatbot_output.jpg)
![Live Deployment](live_deployment_output.jpg)

## 💡 What I Learned
- Streamlit app development
- Gemini API integration
- Chat UI development
- Session state for chat history
- Secure API key management
- Error handling for API limits

## 🚀 Future Improvements
- Add voice input
- Add dark mode
- Add multi-turn memory improvements
- Support file upload and PDF question answering
- Add multiple model support

## 👨‍💻 Author
Gautam Sharma
GitHub: [Gautams1990](https://github.com/Gautams1990)
📫 xploregautam@gmail.com




ure
