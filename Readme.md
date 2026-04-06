🩺 MedAssist AI – Health Guidance Chatbot

MedAssist AI is an intelligent health guidance chatbot built using Rasa, Python, and Streamlit.
It provides general health information based on user symptoms while emphasizing safety and non-diagnostic use.

# Project Overview

This project demonstrates:

Natural Language Processing (NLP)
Intent classification
Entity extraction (symptoms, duration, severity)
Custom action handling
API-based chatbot architecture
Interactive UI with Streamlit

The chatbot is designed to simulate a first-level health assistant, helping users understand symptoms and when to seek medical care.

⚠️ Disclaimer

This chatbot provides general health guidance only.
It does NOT provide medical diagnosis or replace professional medical advice.
In case of emergency, consult a healthcare professional immediately.

# Features
✅ Intent recognition (e.g., fever, headache, emergency)
✅ Entity extraction:
Symptom
Duration
Severity
✅ Custom action for symptom-based guidance
✅ Predefined medical safety responses
✅ Emergency detection responses
✅ Streamlit chat interface
✅ Modular architecture (Rasa + Action Server + UI)
🏗️ Tech Stack
Python
Rasa (NLU + Core)
Rasa SDK (Custom Actions)
Streamlit (Frontend UI)
Requests (API communication)
📁 Project Structure
medassist-ai/
│
├── actions/                # Custom action logic
│   └── actions.py
│
├── data/
│   ├── nlu.yml            # Training data (intents + entities)
│   ├── rules.yml          # Rule-based conversations
│   └── stories.yml        # Conversation flows
│
├── models/                # Trained models
├── tests_backup/          # Test stories (optional)
│
├── app.py                 # Streamlit UI
├── domain.yml             # Bot responses & intents
├── config.yml             # Model configuration
├── credentials.yml        # Channels
├── endpoints.yml          # Action server config
│
├── requirements.txt
├── README.md
⚙️ How to Run the Project
1. Clone the repository
git clone https://github.com/Princess565/medassist-ai.git
cd medassist-ai
2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Train the model
rasa train
5. Run the chatbot system
Terminal 1 – Action Server
rasa run actions
Terminal 2 – Rasa Server
rasa run --enable-api --cors "*" --credentials credentials.yml --endpoints endpoints.yml
Terminal 3 – Streamlit UI
streamlit run app.py
6. Open the app
http://localhost:8501
💬 Example Queries
“I have had fever for two days”
“my headache is severe”
“what are the symptoms of malaria”
“when should I go to the hospital”
“I have chest pain”
 # Key Learning Outcomes

This project demonstrates:

Building conversational AI systems with Rasa
Designing structured NLP pipelines
Handling real-world user inputs with entities
Creating custom business logic via action servers
Connecting backend AI systems to a UI
Structuring production-ready projects
# Future Improvements
Docker containerization
Deployment (Render / AWS / Hugging Face Spaces)
Integration with real medical APIs
Multilingual support
User session tracking
Improved ML model tuning
# Author

Efe Ikharo
Data Analyst | Aspiring Data Scientist
Background in Biomedical Science
Transitioning into AI & Data Science
🌟 Why This Project Matters

This project bridges:

Healthcare + AI
NLP + real-world use case
Data Science + product thinking
It showcases the ability to build end-to-end intelligent systems, not just models.