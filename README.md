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

This project consists of four essential components that work together to create a fully functional and effective chatbot.

## 1. Web Scraping
The chatbot is trained using data scraped from the Qura database. This data is stored and used for training the intent-based model.

## 2. Intent-Based Chatbot Development
A feed-forward neural network (FNN) is used to train the intent-classification model. The training process utilizes several key NLTK techniques for pre-processing both training data and user inputs:

| Technique       | Description                                          | Usage                                                                                      |
| --------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Tokenization    | Breaking text into words or phrases (tokens).        | Allows the chatbot to process individual components of user input.                         |
| Stemming        | Reducing words to their base or root form.            | Groups similar words to improve text analysis.                                              |
| Bag of Words    | Represents text as an unordered set of words.         | Transforms text into numerical feature vectors for training the model to recognize intents. |

## Additional Notes:
- **Training Data**: The FNN model requires the training data to be prepared in JSON format.
- **`intents.json`**: This file defines user intents and provides training examples for each. It plays a crucial role in helping the chatbot accurately recognize and respond to user inputs.
****

