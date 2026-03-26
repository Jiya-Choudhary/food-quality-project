# food-quality-project
AI-Based Fast Food Freshness and Quality Detection System that analyzes food images using machine learning to classify them as fresh, burnt, or spoiled, and stores results in a database.

---


# 🍔 AI-Based Fast Food Freshness and Quality Detection System

## 📌 Project Overview

This project presents an AI-based system that detects the freshness and cooking quality of fast food using image processing and machine learning. The system analyzes food images and classifies them into categories such as **Fresh, Burnt, Oily, or Spoiled**, and provides a **health risk assessment**.

The goal of this project is to improve food safety awareness and help users make better food consumption decisions.

---

## 🎯 Objectives

* Detect food freshness using image processing
* Identify cooking quality issues (burnt, over-fried, oily)
* Classify food into multiple categories
* Store results in a database
* Provide health risk analysis

---

## 🧠 Features

* 📤 Upload food image
* 🤖 AI-based classification
* 🗄️ Store results in database
* 📊 Display prediction and risk level
* ⚡ Fast and automated system

---

## 🏗️ System Architecture

**Flow:**
User → UI → AI Model → Database → Result

---

## 🛠️ Technologies Used

* Python
* Flask (Backend)
* SQLite (Database)
* OpenCV (Image Processing)
* TensorFlow / Keras (Machine Learning)

---

## 📂 Project Structure

```
food-quality-project/
│
├── app.py              # Flask Backend
├── predict.py          # AI Prediction Code
├── model.h5            # Trained Model
├── food.db             # SQLite Database
├── templates/
│     └── index.html    # UI
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/food-quality-project.git
cd food-quality-project
```

### 2️⃣ Install Dependencies

```
pip install flask tensorflow opencv-python numpy
```

### 3️⃣ Run Application

```
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📊 Sample Output

| Food Item | Prediction | Risk |
| --------- | ---------- | ---- |
| Burger    | Burnt      | High |
| Fries     | Fresh      | Low  |

---

## ⚠️ Limitations

* Accuracy depends on dataset quality
* Sensitive to lighting conditions
* Cannot detect internal contamination (bacteria/chemicals)

---

## 🚀 Future Scope

* Real-time detection using camera
* Mobile application integration
* Advanced deep learning models
* Cloud-based deployment

---

## 👥 Team Members

* Person A – AI Model Development
* Person B – Backend & Database

---

## 📚 Conclusion

This project demonstrates how AI and computer vision can be used to solve real-world problems like food quality detection. It provides a fast, efficient, and user-friendly system for evaluating food safety.

---

## ⭐ Acknowledgement

This project is developed as part of academic learning to explore AI, machine learning, and database integration.

---
