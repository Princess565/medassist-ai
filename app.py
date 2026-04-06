import os
import streamlit as st
import requests

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="MedAssist AI",
    page_icon="🩺",
    layout="centered",
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown(
    """
    <style>
        .main {
            background-color: #f7f9fc;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 850px;
        }

        .app-title {
            font-size: 2.2rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.3rem;
        }

        .app-subtitle {
            color: #475569;
            font-size: 1rem;
            margin-bottom: 1rem;
        }

        .disclaimer-box {
            background-color: #fff7ed;
            border: 1px solid #fdba74;
            color: #9a3412;
            padding: 0.9rem 1rem;
            border-radius: 0.8rem;
            margin-bottom: 1.2rem;
            font-size: 0.95rem;
        }

        .info-card {
            background-color: white;
            border-radius: 1rem;
            padding: 1rem;
            border: 1px solid #e2e8f0;
            box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
            margin-bottom: 1rem;
        }

        .stChatMessage {
            border-radius: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Config
# -----------------------------
RASA_URL = os.getenv("RASA_URL", "http://localhost:5005/webhooks/rest/webhook")

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello, I am MedAssist AI. I provide general health guidance, "
                "not medical diagnosis."
            ),
        }
    ]

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="app-title">🩺 MedAssist AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">A health guidance chatbot built with Rasa, Python, and Streamlit.</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="disclaimer-box">
        <strong>Disclaimer:</strong> This chatbot provides general health guidance only.
        It does not replace professional medical advice, diagnosis, or treatment.
        If you are experiencing severe symptoms or an emergency, seek immediate medical care.
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Optional Quick Help Card
# -----------------------------
with st.expander("See example questions"):
    st.markdown(
        """
        - I have had fever for two days  
        - my headache is severe  
        - what are the symptoms of malaria  
        - when should I go to the hospital  
        - I have chest pain  
        """
    )

# -----------------------------
# Rasa Request Function
# -----------------------------
def send_message_to_rasa(user_message: str):
    payload = {"sender": "streamlit_user", "message": user_message}

    try:
        response = requests.post(RASA_URL, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        if not data:
            return ["I did not get a response from the assistant."]

        bot_messages = []
        for item in data:
            text = item.get("text")
            if text:
                bot_messages.append(text)

        if not bot_messages:
            return ["I received a response, but it did not contain text."]

        return bot_messages

    except requests.exceptions.ConnectionError:
        return [
            "I cannot connect to the Rasa server. Please make sure the Rasa server is running on port 5005."
        ]
    except requests.exceptions.Timeout:
        return ["The request timed out. Please try again."]
    except requests.exceptions.RequestException as e:
        return [f"An error occurred while contacting the assistant: {e}"]

# -----------------------------
# Chat History
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input("Describe your symptom or ask a health question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            bot_replies = send_message_to_rasa(user_input)

        for reply in bot_replies:
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("## About MedAssist AI")
    st.write(
        "This chatbot uses Rasa for intent classification, entity extraction, and custom actions."
    )

    st.markdown("### Features")
    st.write("- Intent classification")
    st.write("- Entity extraction")
    st.write("- Symptom-aware responses")
    st.write("- Custom Python actions")

    st.markdown("### Project Stack")
    st.write("Python")
    st.write("Rasa")
    st.write("Rasa SDK")
    st.write("Streamlit")

    if st.button("Clear chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello, I am MedAssist AI. I provide general health guidance, "
                    "not medical diagnosis."
                ),
            }
        ]
        st.rerun()