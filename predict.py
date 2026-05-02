import tensorflow as tf
import numpy as np
import cv2
import os

# Load model
model = tf.keras.models.load_model("model.keras")
classes = ["Burnt", "Fresh", "Spoiled"]

def predict_image(image_path):

    if not os.path.exists(image_path):
        return "❌ Image file not found"

    img = cv2.imread(image_path)

    if img is None:
        return "❌ Error reading image"

    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.reshape(img, (1, 224, 224, 3))

    prediction = model.predict(img)

    print("\n🔍 Detailed Prediction:")
    for i, prob in enumerate(prediction[0]):
        print(f"{classes[i]}: {prob:.2f}")

    class_index = np.argmax(prediction)
    confidence = np.max(prediction)

    result = classes[class_index]

    if confidence < 0.70:
        return "⚠ Not sure (image unclear, try better image)"

    return f"\n✅ Prediction: {result} (Confidence: {confidence:.2f})"


# Test image
test_image = "spoiled img.jpg"   

output = predict_image(test_image)
print(output) 