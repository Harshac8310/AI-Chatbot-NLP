# 🤖 AI Chatbot using NLP

An NLP-based **College Student Support Chatbot** designed to answer common student queries related to courses, admissions, fees, attendance, hostel, library, scholarships, events, and other college information.

The chatbot uses **TF-IDF feature extraction** and **Logistic Regression** for intent classification, with a confidence-based fallback mechanism for unsupported questions. A **Streamlit** interface provides the web-based chat experience.

## 🚀 Features

- Natural Language Processing using NLTK
- Text preprocessing with tokenization and lemmatization
- TF-IDF text feature extraction
- Logistic Regression intent classification
- 19 predefined student-support intents
- 380 training patterns
- Confidence-based fallback for unsupported queries
- Persistent chat history using Streamlit session state
- Interactive Streamlit web interface
- Saved trained model using Joblib

## 🧠 Technology Stack

- **Python**
- **NLTK** — text preprocessing
- **Scikit-learn** — TF-IDF and Logistic Regression
- **NumPy** — numerical operations
- **Joblib** — model persistence
- **Streamlit** — web interface

## 📁 Project Structure

```text
AI-Chatbot-NLP/
│
├── data/
│   └── intents.json
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── chatbot.py
│
├── model.pkl
├── vectorizer.pkl
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔄 System Flow

```text
User
 ↓
Streamlit Interface
 ↓
Chatbot Logic
 ↓
Text Preprocessing
 ↓
TF-IDF Vectorization
 ↓
Logistic Regression
 ↓
Intent Prediction
 ↓
Confidence Check
 ↓
Response / Fallback
```

## 📊 Model Performance

The chatbot was evaluated using an 80/20 train-test split.

- Training examples: **380**
- Test examples: **76**
- Test accuracy: **89.47%**

The model performs well on the predefined college-support intents while using a fallback mechanism for questions outside the supported domain.

## ⚙️ Installation

Clone the repository and navigate to the project directory.

Create and activate a virtual environment:

```bash
python -m venv venv
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Download the required NLTK resources:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('wordnet'); nltk.download('omw-1.4')"
```

## ▶️ Running the Chatbot

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🏫 Supported Queries

The chatbot can answer questions related to:

- Courses
- Admissions
- Eligibility
- Fees
- Required documents
- Application process
- Exams
- Attendance
- Facilities
- Library
- Hostel
- Scholarships
- Contact information
- College location
- Events
- Greetings and general conversation

## ⚠️ Limitations

The current chatbot uses TF-IDF and Logistic Regression, so it primarily learns from patterns and word features in the training dataset. Different phrasings of the same question may sometimes produce different confidence levels.

The chatbot is limited to the information provided in its dataset and uses a fallback response for unsupported questions.

## 🔮 Future Enhancements

- Use semantic embeddings for better understanding of different phrasings
- Add more student-support intents
- Connect to a database for dynamic college information
- Add multilingual support
- Add voice input and output
- Deploy the chatbot online
- Integrate an advanced transformer-based NLP model

## 👨‍💻 Project

**AI Chatbot using NLP**

Developed as an academic AI/NLP project.