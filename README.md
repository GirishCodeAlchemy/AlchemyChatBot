# 📁 AlchemyChatBot 🚀

<p align="center">
  <img src="./alchemychatbot.png" width="300" alt="Top N Disk Analyzer">  
</p>
<h2 align="center">🚀 AlchemyChatBot is a chatbot for answering common questions from quora. 🚀</h2>

This project focuses on creating a smart chatbot using deep learning and Natural Language Processing (NLP). The primary goal is to build an intent-based conversational virtual assistant capable of understanding and responding to user inputs in a human-like manner.

## Usage Screenshot

<img width="1696" alt="image" src="https://github.com/GirishCodeAlchemy/AlchemyChatBot/assets/143807663/b7b05b91-6ebd-4805-ac72-817a617fde28">

<img width="416" alt="image" src="https://github.com/GirishCodeAlchemy/AlchemyChatBot/assets/143807663/f21faba2-de61-4efc-a899-4cc36a1953fc">


# Project Overview

This project focuses on building a fully functional and effective chatbot system. The key components work together to create a robust platform capable of understanding and responding to user queries based on trained intents.

## 1. Web Scraping for Data Collection
The chatbot’s training data is obtained by scraping the **Qura database**. The scraped data is structured and stored for training the intent-based model. This step is crucial for gathering the data that will be used to teach the chatbot how to recognize various user intents and respond appropriately.

## 2. Intent-Based Chatbot Development
The core of the chatbot is an **intent-classification model** built using a **Feed-Forward Neural Network (FNN)**. The model is trained to classify user inputs into predefined intents. To achieve this, several **Natural Language Processing (NLP)** techniques from **NLTK** are utilized to preprocess both training data and real-time user inputs, enhancing the accuracy of the chatbot’s responses.

### Key NLP Techniques:

| Technique       | Description                                          | Usage                                                                                      |
| --------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Tokenization**| Splits text into words or phrases (tokens).          | Helps the chatbot process and understand individual components of user input.               |
| **Stemming**    | Reduces words to their base or root form.            | Groups similar words together to improve text analysis.                                     |
| **Bag of Words**| Represents text as an unordered set of words.        | Converts text into numerical vectors, making it easier to train the model to recognize intents. |

### Additional Details:
- **Training Data**: The chatbot’s model is trained using a dataset that must be prepared in a **JSON format**.
- **`intents.json`**: This critical file defines the user intents and provides associated training examples. It teaches the chatbot how to recognize and respond to different inputs by mapping sample phrases to specific intents.

## 3. Graphical User Interface (GUI) with Tkinter
The project also includes a user-friendly interface built using **Tkinter**, a popular Python library for creating graphical interfaces. The GUI allows users to interact with the chatbot in real time, making it easy to input queries and view the chatbot’s responses.

### Key Features of the Tkinter UI:
- Simple and intuitive interface for chatbot interaction.
- Real-time response display for user inputs.
- Easy integration with the intent-classification model.

---

### Future Enhancements:
- **Advanced NLP Techniques**: Additional preprocessing techniques such as **Lemmatization** could be used to improve the chatbot’s understanding of complex inputs.
- **Model Fine-tuning**: Regular updates to the training data and fine-tuning the FNN model for improved accuracy.
- **Multi-language Support**: Expanding the chatbot to handle multiple languages for a broader audience.


 ## Install Dependencies
 Activate your virtual environment and install the required packages:

 ```bash
 (venv) pip install Flask torch torchvision nltk
 ```

 Or, install from the `requirements.txt` file:

 ```bash
 (venv) pip install -r requirements.txt
 ```

 ## Install NLTK Data
 To download necessary NLTK data, run the following:

 ```bash
 (venv) python
 >>> import nltk
 >>> nltk.download('punkt')
 ```

 ## Customize `intents.json`
 
 Modify the `intents.json` file to include your own intents and responses. This is where you can tailor the chatbot to your specific use case.

 ## Model Training
 Once the data is prepared, train the model using:

 ```bash
 (venv) python train.py
 ```

