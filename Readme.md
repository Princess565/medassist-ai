🩺 MedAssist AI – Health Guidance Chatbot

MedAssist AI is an NLP-powered health guidance chatbot built with Rasa, Python, and Streamlit.
It understands symptom-related queries, extracts key health information (such as symptoms, duration, and severity), and provides safe, non-diagnostic guidance through an interactive chat interface.

🚀 Project Overview

This project demonstrates how to build an end-to-end conversational AI system combining:

Natural Language Processing (NLP)
Entity extraction
Custom backend logic
API communication
Interactive frontend UI

The chatbot simulates a first-level health assistant, helping users understand symptoms and when to seek medical care.

📸 Screenshots
🏠 Home Interface

🤒 Symptom Guidance

🤕 Severity Detection

🚨 Emergency Detection

⚠️ Disclaimer

This chatbot provides general health guidance only.
It does NOT provide medical diagnosis or replace professional medical advice.
In case of emergency, please consult a qualified healthcare professional immediately.

🧠 Features
✅ Intent classification (e.g., fever, headache, emergency)
✅ Entity extraction:
Symptom
Duration
Severity
✅ Custom action handling (dynamic symptom responses)
✅ Emergency detection responses
✅ Rule-based + ML-based dialogue management
✅ Streamlit chat interface
✅ Modular architecture (Rasa + Action Server + UI)
🔄 How It Works
User inputs a message in the Streamlit interface
Message is sent to the Rasa server via REST API
Rasa:
Classifies intent
Extracts entities (symptom, duration, severity)
If needed, a custom action is triggered via the action server
A safe, structured response is returned to the user
📊 Results

The chatbot was evaluated using Rasa’s testing framework:

🎯 Intent classification: 100% accuracy on test set
🧩 Entity extraction: high accuracy with minimal errors
⚙️ Custom actions: successfully triggered context-aware responses
💻 UI: fully functional chat interface via Streamlit

Note: Results are based on a controlled dataset. Future improvements will focus on scaling and generalization.

🧠 What I Learned

Through this project, I developed skills in:

Designing NLP pipelines for real-world applications
Structuring training data for intent classification and entity recognition
Building custom logic using Rasa SDK
Integrating backend AI systems with a frontend interface
Debugging API, endpoint, and environment issues
Structuring production-ready data science projects
🏗️ Tech Stack
Python
Rasa (NLU + Core)
Rasa SDK (Custom Actions)
Streamlit (Frontend UI)
Requests (API communication)
📁 Project Structure
medassist-ai/
│
├── actions/
│   └── actions.py
├── data/
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
├── screenshots/
│   ├── home.jpeg
│   ├── fever-chat.jpeg
│   ├── headache-chat.jpeg
│   └── emergency.jpeg
├── app.py
├── config.yml
├── credentials.yml
├── domain.yml
├── endpoints.yml
├── requirements.txt
├── README.md
└── .gitignore
⚙️ How to Run Locally
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
6. Open the application
http://localhost:8501
💬 Example Queries
“I have had fever for two days”
“my headache is severe”
“what are the symptoms of malaria”
“when should I go to the hospital”
“I have chest pain”
🔮 Future Improvements
Docker containerization
Cloud deployment (Render / AWS / Hugging Face Spaces)
Integration with medical knowledge APIs
Multilingual support
Improved model generalization with larger datasets
👤 Author

Efe Ikharo

Data Analyst | Aspiring Data Scientist
Background in Biomedical Science
Transitioning into AI & Data Science
🌟 Why This Project Matters

This project showcases the ability to:

Build end-to-end AI systems
Apply NLP to real-world healthcare scenarios
Combine machine learning + backend + UI
Think beyond models and build usable products