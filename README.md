<h1 align="center">😴 Driver Drowsiness Detection using SVM</h1>

<p align="center">
  A machine learning mini-project that uses Support Vector Machines (SVM) to detect driver drowsiness based on simulated eye aspect ratio (EAR) values.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/Model-Support%20Vector%20Machine-green">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
</p>

---

## 🔍 Overview

This project simulates the logic behind **driver drowsiness detection** using a machine learning classifier — **Support Vector Machine (SVM)** — trained on a dataset of **Eye Aspect Ratio (EAR)** values.

- EAR < 0.25 → **Drowsy**
- EAR ≥ 0.25 → **Alert**

The model is trained and tested using sample data, and the user can input custom EAR values to test the output in real-time.

---

## 🎯 Features

- 🧠 Trains a binary SVM classifier on EAR values
- 📊 Visualizes predictions vs actual values
- 🖥 Predicts drowsiness from user-input EAR
- ✅ Clean evaluation metrics (accuracy, classification report)
- 💡 Simple and ideal for beginners in ML

---

## 🛠 Tech Stack

- **Language**: Python 3
- **Libraries**: 
  - `scikit-learn` (SVM, training/testing)
  - `numpy` (data handling)
  - `matplotlib` (visualization)
- **Algorithm**: Support Vector Machine (SVM)

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/driver-drowsiness-svm.git
cd driver-drowsiness-svm

OUTPUT
<img width="918" height="1202" alt="Screenshot 2025-07-15 105914" src="https://github.com/user-attachments/assets/f8a1ba06-60a7-4e5d-83b6-943209f09142" />


🔮 Future Enhancements
🔁 Replace simulated EAR values with live webcam detection using OpenCV

🎥 Real-time video-based drowsiness monitoring

📱 Mobile or dashboard integration for automotive applications

🤖 Try different classifiers like Logistic Regression or Random Forest

🧪 Expand dataset with real user data


