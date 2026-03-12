# 🤖 AI Spam Detection System

A **machine learning web application** that detects whether a message is **Spam** or **Not Spam** using **Natural Language Processing (NLP)** and a **Deep Learning model built with TensorFlow**.
The application provides a **simple interactive interface built using Streamlit** for real-time spam detection.

---

## 📌 Features

* Detects whether a message is **Spam** or **Not Spam**
* Uses **NLP preprocessing** with tokenization and padding
* Deep learning model built with **TensorFlow**
* **Real-time prediction** through a Streamlit web interface
* Displays **prediction confidence score**
* Visual **spam probability bar**

---

## 🧠 Technologies Used

* Python
* TensorFlow
* Streamlit
* Pandas
* Scikit-learn
* NumPy

---

## 📊 Dataset

The model is trained using the **SMS Spam Collection Dataset**, which contains labeled SMS messages classified as **spam** or **ham (not spam)**.

Example dataset format:

| Label | Message                                     |
| ----- | ------------------------------------------- |
| ham   | Hey, are we meeting tomorrow?               |
| spam  | Congratulations! You have won a free prize. |

---

## ⚙️ How It Works

1. The dataset is loaded and cleaned.
2. Labels are converted into numerical values.
3. Text messages are converted into sequences using **Tokenizer**.
4. Sequences are padded to ensure equal length.
5. A **Neural Network model** is trained using TensorFlow.
6. The trained model predicts whether a message is spam or not.

---

## 📁 Project Structure

```
spam-detection-system
│
├── dataset
│   └── spam.csv
│
├── model
│   ├── spam_model.h5
│   └── tokenizer.pkl
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```
git clone https://github.com/your-username/spam-detection-system.git
```

Navigate to the project folder:

```
cd spam-detection-system
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🏋️ Train the Model

Run the training script:

```
python train_model.py
```

This will train the model and save:

* `spam_model.h5`
* `tokenizer.pkl`

---

## ▶️ Run the Web Application

Start the Streamlit app:

```
python -m streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧪 Example Predictions

| Input Message                                  | Prediction |
| ---------------------------------------------- | ---------- |
| Congratulations! You won a free lottery ticket | Spam 🚨    |
| Hey, are we meeting tomorrow?                  | Not Spam ✅ |

---

## 📈 Model Performance

The deep learning model achieves approximately **97–98% accuracy** on the SMS Spam Collection dataset.

---

## 💡 Future Improvements

* Use **TF-IDF + Naive Bayes for comparison**
* Deploy the application online
* Add more datasets for better training
* Improve UI and visualization

---

## 👩‍💻 Author

**Meghana Ponna**
Computer Science Student | Aspiring Full Stack Developer | ML Enthusiast

---
