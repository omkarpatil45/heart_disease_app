# 🫀 Heart Disease Detection using Machine Learning

## 📘 Project Overview
Heart disease is one of the leading causes of death worldwide. Early detection can save lives by enabling timely intervention.
This project applies **Supervised Learning Classification Algorithms** to predict whether a patient is likely to have heart disease based on clinical data.

## 🎯 Objectives
- **Build and compare** multiple classification models (Logistic Regression, Random Forest, SVM).
- **Identify** the most accurate and reliable model.
- **Deploy** a user-friendly web interface using Streamlit for real-time predictions.

## 🧠 Machine Learning Models Used

| Model | Description |
| :--- | :--- |
| **Logistic Regression** | A linear model for binary classification. |
| **Random Forest Classifier**| An ensemble of decision trees to improve accuracy. |
| **Support Vector Machine (SVM)**| Maximizes the margin between classes for robust classification. |

## 🧩 Tech Stack
*   **Language:** Python
*   **Libraries:** Pandas, NumPy, Scikit-learn, Joblib
*   **Frontend:** Streamlit
*   **Backend:** Custom Python utilities (model loading + prediction)


## ⚙️ Installation & Setup 
## **Clone this repository:**

git clone https://github.com<your-username>/heart_disease_app.git

cd heart_disease_app



## **Run the Streamlit app:**

streamlit run frontend/app.py


## **🧾 Results Summary** 

|Metric	|Best Model (Random Forest)|
| :--- | :--- |
|Accuracy	|~0.87|
|Recall	|~0.85|
|Precision	|~0.88|
|F1-score	|~0.86|
|ROC-AUC	|~0.91|


## 📂 Folder Structure
```text
heart_disease_app/
├── backend/
│   └── model_utils.py
├── dataset/
│   └── heart_disease_dataset
├── frontend/
│   └── app.py
├── model/
    └── heart_model.pkl
    └── heart_disease.ipynb
    └── hear_model_report.csv


