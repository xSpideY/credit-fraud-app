# Credit Card Fraud Detection App

A Streamlit app that detects fraudulent credit card transactions using a Random Forest classifier trained on anonymized data.

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
