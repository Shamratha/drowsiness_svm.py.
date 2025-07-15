# drowsiness_svm.py

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 1. Simulated Dataset (Eye Aspect Ratio values)
# EAR < 0.25 → Drowsy (1), EAR >= 0.25 → Alert (0)
ear_values = np.array([0.2, 0.21, 0.19, 0.24, 0.3, 0.32, 0.28, 0.35, 0.27, 0.29])
labels = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])

# 2. Reshape and Split Data
X = ear_values.reshape(-1, 1)
y = labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Train SVM Model
svm_model = SVC(kernel='linear')  # You can change kernel to 'rbf', 'poly', etc.
svm_model.fit(X_train, y_train)

# 4. Prediction
y_pred = svm_model.predict(X_test)

# 5. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 6. Visualization
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', marker='x', label='Predicted')
plt.xlabel('Eye Aspect Ratio (EAR)')
plt.ylabel('Driver State (0 = Alert, 1 = Drowsy)')
plt.title('SVM Drowsiness Detection')
plt.legend()
plt.grid(True)
plt.show()

# 7. Try your own EAR input
custom_ear = float(input("Enter EAR value to predict (e.g., 0.23): "))
prediction = svm_model.predict([[custom_ear]])
state = "Drowsy 😴" if prediction[0] == 1 else "Alert 🙂"
print(f"Predicted State: {state}")
