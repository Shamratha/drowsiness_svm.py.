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
OUTPUT


<img width="918" height="1202" alt="Screenshot 2025-07-15 105914" src="https://github.com/user-attachments/assets/f8a1ba06-60a7-4e5d-83b6-943209f09142" />


 ## 🔮 Future Enhancements

Here are some ideas to take this project to the next level:

- 🎥 **Live Video-Based EAR Detection**  
  Integrate OpenCV to calculate real-time EAR from webcam footage and feed it into the SVM model.

- 🧠 **Use Pre-Trained Models for Face & Eye Landmark Detection**  
  Combine with libraries like `dlib` or `mediapipe` to automatically extract eye landmarks for EAR calculation.

- 📈 **Train on Real Drowsiness Datasets**  
  Use publicly available datasets (like NTHU Drowsy Driver Dataset) for more realistic performance testing.

- 📲 **Deploy as a Mobile or Web App**  
  Build a lightweight UI using **Flask**, **Streamlit**, or **Android Studio** for user-friendly deployment.

- 🔄 **Compare Multiple ML Models**  
  Benchmark against Logistic Regression, Random Forest, or Neural Networks for accuracy and generalization.

- 🚗 **Automotive Integration**  
  Design the system as a dashboard assistant in cars with alert triggers (sound/beep) when drowsiness is detected.

- 📊 **Logging & Analytics**  
  Record EAR values over time and provide graphical analytics (e.g., "You were drowsy 3 times during the drive").

- 🧪 **Add Alert Mechanism**  
  Play a warning sound or vibrate the device when drowsiness is detected in real-time.




