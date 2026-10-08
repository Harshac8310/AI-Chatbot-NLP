import json
import joblib
from preprocess import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

with open("./data/intents.json", "r") as file:
    data = json.load(file)

training_sentences = []
training_labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        training_sentences.append(preprocess_text(pattern))
        training_labels.append(intent["tag"])

training_sentences = [" ".join(sentence) for sentence in training_sentences]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_sentences)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    training_labels,
    test_size=0.2,
    random_state=42,
    stratify=training_labels
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print("Testing accuracy:", accuracy)

#print("Classification Report:")
#print(classification_report(y_test, y_pred))

#cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
#print(cm)

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and vectorizer saved successfully.")