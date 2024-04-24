import json
import re

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Load the dataset
df = pd.read_csv("./data/quora_questions_and_answers.csv").dropna(axis=0)


# Preprocess the data
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    clean_text = ' '.join(tokens)
    return clean_text

# Define intents dictionary
intents = {}
# Iterate over the dataset to extract intents and patterns
for index, row in df.iterrows():
    question = row['question']
    answer = row['answer']

    # Define intent based on keywords in question or answer
    intent = None
    if "machine learning" in question.lower() or "machine learning" in answer.lower():
        intent = "machine_learning"
    elif "python" in question.lower() or "python" in answer.lower():
        intent = "python"
    elif "artificial intelligence" in question.lower() or "artificial intelligence" in answer.lower():
        intent = "artificial_intelligence"
    elif "data science" in question.lower() or "data science" in answer.lower():
        intent = "data_science"
    elif "deep learning" in question.lower() or "deep learning" in answer.lower():
        intent = "deep_learning"
    elif "software engineer" in question.lower() or "software engineer" in answer.lower():
        intent = "software_engineering"
    else:
        intent = "other"

    # Add pattern to the intent
    if intent in intents:
        intents[intent]['patterns'].append(question)
        intents[intent]['responses'].append(answer)
    # else:
    #     intents[intent] = {'tag': intent, 'patterns': [question]}
    else:
        intents[intent] = {'tag': intent, 'patterns': [question], 'responses': [answer]}

intents_list = []

with open('./data/greeting.json', 'r') as f:
    greeting_data = json.load(f)
    intents_list.extend(greeting_data)

quora_list = [{'tag': intent_data['tag'], 'patterns': intent_data['patterns'], 'responses': intent_data['responses']} for intent_data in intents.values()]
intents_list.extend(quora_list)
# Save intents to JSON file
with open('intents.json', 'w') as json_file:
    json.dump({'intents': intents_list}, json_file, indent=4)