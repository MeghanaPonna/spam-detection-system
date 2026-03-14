# import pandas as pd
# import tensorflow as tf
# import pickle

# from sklearn.model_selection import train_test_split
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# # Load dataset
# data = pd.read_csv("dataset/spam.csv", encoding="latin-1")

# # Keep required columns
# data = data[['v1', 'v2']]
# data.columns = ['label', 'message']

# # Convert labels to numbers
# data['label'] = data['label'].map({'ham':0, 'spam':1})

# # Split dataset
# X_train, X_test, y_train, y_test = train_test_split(
#     data['message'], data['label'], test_size=0.2
# )

# # Tokenizer
# tokenizer = Tokenizer(num_words=5000)
# tokenizer.fit_on_texts(X_train)

# X_train_seq = tokenizer.texts_to_sequences(X_train)
# X_test_seq = tokenizer.texts_to_sequences(X_test)

# X_train_pad = pad_sequences(X_train_seq, maxlen=100)
# X_test_pad = pad_sequences(X_test_seq, maxlen=100)

# # Build model
# model = tf.keras.Sequential([
#     tf.keras.layers.Embedding(5000, 64),
#     tf.keras.layers.GlobalAveragePooling1D(),
#     tf.keras.layers.Dense(24, activation='relu'),
#     tf.keras.layers.Dense(1, activation='sigmoid')
# ])

# model.compile(
#     optimizer='adam',
#     loss='binary_crossentropy',
#     metrics=['accuracy']
# )

# # Train
# # model.fit(X_train_pad, y_train, epochs=5)
# model.fit(X_train_pad, y_train, epochs=10)

# # Evaluate
# loss, accuracy = model.evaluate(X_test_pad, y_test)

# print("Accuracy:", accuracy)

# # Save model
# model.save("model/spam_model.h5")

# # Save tokenizer
# with open("model/tokenizer.pkl", "wb") as f:
#     pickle.dump(tokenizer, f)

# print("Model and tokenizer saved successfully!")




import pandas as pd
import tensorflow as tf
import pickle

from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load dataset
data = pd.read_csv("dataset/spam.csv", encoding="latin-1")

# Keep required columns
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

# Lowercase messages
data['message'] = data['message'].str.lower()

# Convert labels
data['label'] = data['label'].map({'ham':0, 'spam':1})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    data['message'],
    data['label'],
    test_size=0.2,
    random_state=42
)

# Tokenizer
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

X_train_pad = pad_sequences(X_train_seq, maxlen=100, padding='post')
X_test_pad = pad_sequences(X_test_seq, maxlen=100, padding='post')

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(5000, 64, input_length=100),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(X_train_pad, y_train, epochs=10, batch_size=32)

# Evaluate model
loss, accuracy = model.evaluate(X_test_pad, y_test)

print("Accuracy:", accuracy)

# Save model
model.save("model/spam_model.h5")

# Save tokenizer
with open("model/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("Model and tokenizer saved successfully!")