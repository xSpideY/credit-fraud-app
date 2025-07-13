# Credit Card Fraud Detection App
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-2E2E2E?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)


A Streamlit app that detects fraudulent credit card transactions using a Random Forest classifier trained on anonymized data.

## 🚀 Launch the App

👉 Click below to open the live Streamlit app:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://credit-fraud-app-qjfbpmv8f7gnuskaz5fet2.streamlit.app/)

## Open in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xSpideY/credit-fraud-app/blob/main/Credit_Card_Fraud_Analysis.ipynb)


## 🔍 Features
- Upload CSV and get instant predictions
- Fraud probability with `predict_proba`
- Clean Streamlit dashboard
- Downloadable results

## 🧠 Tech Stack
- Python, Streamlit, Scikit-learn, Pandas
- Trained on 29 features (V1–V28 + Amount)

## 🚀 How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/credit-fraud-app.git
cd credit-fraud-app
pip install -r requirements.txt
streamlit run app.py
