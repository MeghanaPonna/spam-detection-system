import tensorflow as tf

# Load old model
model = tf.keras.models.load_model("model/spam_model.h5", compile=False)

# Save in new format
model.save("model/spam_model.keras")

print("Model converted successfully!")