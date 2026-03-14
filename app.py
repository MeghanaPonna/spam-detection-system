# # # # # import streamlit as st
# # # # # import tensorflow as tf
# # # # # import pickle

# # # # # from tensorflow.keras.preprocessing.sequence import pad_sequences

# # # # # # Load trained model
# # # # # model = tf.keras.models.load_model("model/spam_model.h5")

# # # # # # Load tokenizer
# # # # # with open("model/tokenizer.pkl", "rb") as f:
# # # # #     tokenizer = pickle.load(f)

# # # # # # Title
# # # # # st.title("Spam Message Detection")

# # # # # # Input text
# # # # # message = st.text_input("Enter message")

# # # # # # Prediction
# # # # # if st.button("Predict"):

# # # # #     seq = tokenizer.texts_to_sequences([message])
# # # # #     pad = pad_sequences(seq, maxlen=100)

# # # # #     prediction = model.predict(pad)

# # # # #     if prediction[0][0] > 0.5:
# # # # #         st.error("Spam 🚨")
# # # # #     else:
# # # # #         st.success("Not Spam ✅")



# # # # import streamlit as st
# # # # import tensorflow as tf
# # # # import pickle
# # # # from tensorflow.keras.preprocessing.sequence import pad_sequences

# # # # # Load model
# # # # model = tf.keras.models.load_model("model/spam_model.h5")

# # # # # Load tokenizer
# # # # with open("model/tokenizer.pkl", "rb") as f:
# # # #     tokenizer = pickle.load(f)

# # # # st.title("Spam Message Detection")

# # # # message = st.text_input("Enter message")

# # # # if st.button("Predict"):

# # # #     message = message.lower()

# # # #     seq = tokenizer.texts_to_sequences([message])
# # # #     pad = pad_sequences(seq, maxlen=100)

# # # #     prediction = model.predict(pad)[0][0]

# # # #     spam_probability = prediction
# # # #     ham_probability = 1 - prediction

# # # #     if prediction > 0.5:
# # # #         st.error(f"Spam 🚨 ({spam_probability*100:.2f}% confidence)")
# # # #     else:
# # # #         st.success(f"Not Spam ✅ ({ham_probability*100:.2f}% confidence)")


# # # import streamlit as st
# # # import tensorflow as tf
# # # import pickle
# # # from tensorflow.keras.preprocessing.sequence import pad_sequences

# # # # Load model
# # # model = tf.keras.models.load_model("model/spam_model.h5")

# # # # Load tokenizer
# # # with open("model/tokenizer.pkl", "rb") as f:
# # #     tokenizer = pickle.load(f)

# # # st.title("📩 Spam Message Detection System")

# # # st.write("Enter a message to check whether it is Spam or Not.")

# # # message = st.text_input("Enter message")

# # # if st.button("Predict"):

# # #     message = message.lower()

# # #     seq = tokenizer.texts_to_sequences([message])
# # #     pad = pad_sequences(seq, maxlen=100)

# # #     prediction = model.predict(pad)[0][0]

# # #     spam_probability = prediction
# # #     ham_probability = 1 - prediction

# # #     st.subheader("Prediction Result")

# # #     if prediction > 0.5:
# # #         st.error(f"Spam 🚨 ({spam_probability*100:.2f}% confidence)")
# # #     else:
# # #         st.success(f"Not Spam ✅ ({ham_probability*100:.2f}% confidence)")

# # #     st.subheader("Spam Probability")

# # #     st.progress(int(spam_probability * 100))

# # #     st.write(f"Spam Probability: {spam_probability*100:.2f}%")



# # import streamlit as st
# # import tensorflow as tf
# # import pickle
# # from tensorflow.keras.preprocessing.sequence import pad_sequences

# # # Load model
# # model = tf.keras.models.load_model("model/spam_model.h5")

# # # Load tokenizer
# # with open("model/tokenizer.pkl", "rb") as f:
# #     tokenizer = pickle.load(f)

# # # -------- TITLE SECTION --------

# # st.title("🤖 AI Spam Detection System")

# # st.markdown(
# # """
# # ### Built using TensorFlow & Streamlit

# # This application uses **Natural Language Processing (NLP)** and a **Deep Learning model**
# # to detect whether a message is **Spam** or **Not Spam**.
# # """
# # )

# # st.divider()

# # # -------- INPUT --------

# # message = st.text_input("📩 Enter a message")

# # if st.button("Predict"):

# #     message = message.lower()

# #     seq = tokenizer.texts_to_sequences([message])
# #     pad = pad_sequences(seq, maxlen=100)

# #     prediction = model.predict(pad)[0][0]

# #     spam_probability = prediction
# #     ham_probability = 1 - prediction

# #     st.subheader("Prediction Result")

# #     if prediction > 0.5:
# #         st.error(f"Spam 🚨 ({spam_probability*100:.2f}% confidence)")
# #     else:
# #         st.success(f"Not Spam ✅ ({ham_probability*100:.2f}% confidence)")

# #     st.subheader("Spam Probability")

# #     st.progress(int(spam_probability * 100))

# #     st.write(f"Spam Probability: {spam_probability*100:.2f}%")


# import streamlit as st
# import tensorflow as tf
# import pickle
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# # Load model
# model = tf.keras.models.load_model("model/spam_model.h5",compile=False)

# # Load tokenizer
# with open("model/tokenizer.pkl", "rb") as f:
#     tokenizer = pickle.load(f)

# # -------- HEADER --------

# st.markdown(
# """
# <h1 style='text-align: center;'>🤖 AI Spam Detection System</h1>
# <h4 style='text-align: center;'>Built using TensorFlow & Streamlit</h4>
# """,
# unsafe_allow_html=True
# )

# st.divider()

# st.info(
# """
# This application uses **Natural Language Processing (NLP)** and a **Deep Learning model**
# to detect whether a message is **Spam** or **Not Spam**.
# """
# )

# # -------- INPUT --------

# message = st.text_area("📩 Enter a message")

# # Example messages
# st.write("Example messages you can try:")

# st.code("Congratulations! You have won a free entry in a weekly competition.Call now to claim your prize.")
# st.code("Hey are we meeting tomorrow?")

# # -------- PREDICTION --------

# if st.button("🔍 Predict"):

#     message = message.lower()

#     seq = tokenizer.texts_to_sequences([message])
#     pad = pad_sequences(seq, maxlen=100)

#     prediction = model.predict(pad)[0][0]

#     spam_probability = prediction
#     ham_probability = 1 - prediction

#     st.subheader("Prediction Result")

#     if prediction > 0.5:
#         st.error(f"Spam 🚨 ({spam_probability*100:.2f}% confidence)")
#     else:
#         st.success(f"Not Spam ✅ ({ham_probability*100:.2f}% confidence)")

#     st.subheader("Spam Probability")

#     st.progress(int(spam_probability * 100))

#     st.write(f"Spam Probability: {spam_probability*100:.2f}%")



import streamlit as st
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# -------- LOAD MODEL --------

model = tf.keras.models.load_model("model/spam_model.keras", compile=False)

# -------- LOAD TOKENIZER --------

with open("model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# -------- PAGE CONFIG --------

st.set_page_config(
    page_title="AI Spam Detection",
    page_icon="🤖",
    layout="centered"
)

# -------- HEADER --------

st.markdown(
"""
<h1 style='text-align: center;'>🤖 AI Spam Detection System</h1>
<h4 style='text-align: center;'>Built using TensorFlow & Streamlit</h4>
""",
unsafe_allow_html=True
)

st.divider()

st.info(
"""
This application uses **Natural Language Processing (NLP)** and a **Deep Learning model**
to detect whether a message is **Spam** or **Not Spam**.
"""
)

# -------- INPUT --------

message = st.text_area("📩 Enter a message")

# Example messages
st.write("Example messages you can try:")

st.code("Congratulations! You have won a free entry in a weekly competition. Call now to claim your prize.")
st.code("Hey are we meeting tomorrow?")

# -------- PREDICTION --------

if st.button("🔍 Predict"):

    if message.strip() == "":
        st.warning("Please enter a message")
    else:

        message = message.lower()

        seq = tokenizer.texts_to_sequences([message])
        pad = pad_sequences(seq, maxlen=100)

        prediction = model.predict(pad)[0][0]

        spam_probability = float(prediction)
        ham_probability = 1 - spam_probability

        st.subheader("Prediction Result")

        if prediction > 0.5:
            st.error(f"Spam 🚨 ({spam_probability*100:.2f}% confidence)")
        else:
            st.success(f"Not Spam ✅ ({ham_probability*100:.2f}% confidence)")

        st.subheader("Spam Probability")

        st.progress(int(spam_probability * 100))

        st.write(f"Spam Probability: {spam_probability*100:.2f}%")