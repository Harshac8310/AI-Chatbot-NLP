import json
import random
import joblib

from src.preprocess import preprocess_text


# Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


# Load chatbot intents
with open("./data/intents.json", "r") as file:
    data = json.load(file)


def get_response(user_input):

    tokens = preprocess_text(user_input)
    processed_text = " ".join(tokens)

    vector = vectorizer.transform([processed_text])

    probabilities = model.predict_proba(vector)[0]

    # Get the highest probability
    predicted_index = probabilities.argmax()

    # Get predicted intent
    predicted_intent = model.classes_[predicted_index]

    # Highest confidence
    confidence = probabilities[predicted_index]

    # Get the second-highest probability
    sorted_probabilities = sorted(probabilities, reverse=True)
    second_highest = sorted_probabilities[1]

    # Difference between first and second prediction
    margin = confidence - second_highest

    #print("Predicted intent:", predicted_intent)
    #print("Confidence:", confidence)
    #print("Margin:", margin)



    if confidence < 0.10 or margin < 0.05:
        return "Sorry, I don't have information about that. I can help with admissions, courses, fees, attendance, facilities, hostel, library, scholarships, events, and other student-support queries."

    for intent in data["intents"]:
        if intent["tag"] == predicted_intent:
            return random.choice(intent["responses"])

    return "Sorry, I don't understand your question."

