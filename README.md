# 🤖 Dual Chatbot System – Personal Assistant & Data Expert

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Uvais5/chatbot)

A dual chatbot system built using **Python, NLTK, and TensorFlow/Keras**, designed to answer both **personal* and **data-related** questions. These bots are trained using custom JSON intent files and deployed on Heroku for global accessibility.

---

## 📌 Table of Contents

- [📖 Overview](#-overview)
- [🎯 Problem Solving](#-problem-solving)
- [💼 Use Cases](#-use-cases)
- [🧠 How It Works](#-how-it-works)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [📝 Example Usage](#-example-usage)
- [🚀 Deploy on Heroku](#-deploy-on-heroku)
- [🔧 Train Your Own Chatbot](#-train-your-own-chatbot)
- [🛣️ Roadmap](#roadmap)
- [📜 License](#-license)
- [🤝 Contributing](#-contributing)

---

## 📖 Overview

This project provides **two chatbots**:

- **Personal Bot (`pschatbot`)**: answers your biography, hobbies, proficiencies, etc., based on `personal.json`.
- **Data Bot (`datachatbot`)**: handles queries in Data Science/ML using `data.json`.

Both use a Bag‑of‑Words + feed‑forward NN framework in Keras.

---

## 🎯 Problem Solving

| 🔍 Problem | ✅ Solution |
|------------|-------------|
| Repetitive FAQs about your profile | *Personal Bot* automates answers. |
| Hard to explain data/ML topics clearly | *Data Bot* gives clear, friendly insights. |
| Heavy chatbot platforms are hard to customize | This codebase is **< 300 lines**, easy to modify. |

---

## 💼 Use Cases

- Embed on portfolio websites.
- Slack/Discord helper for teammate questions.
- Study aid for learning data science.
- Extendable for voice assistants.

---

## 🧠 How It Works

1. **Preprocessing**: Tokenization + Lemmatization (NLTK).
2. **Bag of Words (BoW)**: Sentence → binary vector.
3. **Neural Network**: Dense layers → `softmax` over intents.
4. **Response**: Choose random reply from matched intent.
5. **Two Models**: `pschatbot` & `datachatbot`.

---

## 🚀 Quick Start

### Requirements

```bash
pip install tensorflow keras nltk numpy
