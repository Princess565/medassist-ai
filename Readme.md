# 🩺 MedAssist AI – Health Guidance Chatbot (Rasa + NLP)

## Overview

MedAssist AI is an intelligent health guidance chatbot built using **Rasa** and **Python**.
It provides general health advice based on user symptoms using **Natural Language Processing (NLP)**.

⚠️ *Disclaimer: This chatbot does NOT provide medical diagnosis.*

---

## Key Features

* Intent classification using Rasa NLU
* Entity extraction (symptom, severity, duration)
* Custom actions for dynamic responses
* Context-aware health guidance
* Model evaluation with performance metrics

---

## NLP Capabilities

* **Intent Accuracy:** 100% on test dataset
* **Entity Extraction:** High precision (~99%)
* Supports queries like:

  * "I have a severe headache"
  * "I’ve had fever for two days"
  * "I feel weak since yesterday"

---

## Tech Stack

* Python
* Rasa
* Rasa SDK
* TensorFlow (via Rasa)
* YAML for training data

---

## Project Structure


medassist-ai/
│
├── data/              # Training data (NLU, rules, stories)
├── actions/           # Custom action logic
├── models/            # Trained models
├── results/           # Evaluation outputs
│
├── domain.yml         # Intents, entities, responses
├── config.yml         # NLP pipeline
├── endpoints.yml      # Action server config
├── requirements.txt
└── README.md


---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/medassist-ai.git
cd medassist-ai

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt


---

## ▶️ Run the Bot

### Start action server:

bash
rasa run actions


### Start chatbot:

bash
rasa shell --endpoints endpoints.yml

---

## Model Evaluation

Run:

bash
rasa test nlu


Results include:

* Confusion matrix
* Intent classification report
* Entity extraction metrics

---

## 📊 Example Interaction


User: I have a severe headache
Bot: For headaches, rest, hydrate, and reduce stress. If severe or persistent, consult a healthcare professional.


---

## Future Improvements

* Add more medical conditions
* Integrate with real healthcare APIs
* Add voice support
* Deploy as a web application

---

## Author

**Efe Ikharo**
Aspiring Data Scientist | AI Builder

---

## ⭐ If you like this project

Give it a star ⭐ and connect with me on LinkedIn!
