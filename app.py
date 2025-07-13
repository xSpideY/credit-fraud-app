import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")

# Get expected feature columns from model
expected_cols = model.feature_names_in_.tolist()

st.title("🕷️ Credit Card Fraud Predictor")
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    original = df.copy()

    # Drop unnecessary columns
    for col in ['Time', 'Class']:
        if col in df.columns:
            df.drop(col, axis=1, inplace=True)

    # Scale Amount
    if 'Amount' in df.columns:
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
        df.dropna(subset=['Amount'], inplace=True)
        df['Amount'] = scaler.transform(df['Amount'].values.reshape(-1, 1))
    else:
        st.error("Missing 'Amount' column.")
        st.stop()

    # Drop remaining NaNs
    df.dropna(inplace=True)

    # Check column match
    if set(df.columns) != set(expected_cols):
        st.error("❌ Column mismatch.")
        st.text(f"Expected: {expected_cols}")
        st.text(f"Got: {df.columns.tolist()}")
        st.stop()

    # Reorder columns to match model
    df = df[expected_cols]

    # Predict
    preds = model.predict(df)
    probas = model.predict_proba(df)

    # SAFELY extract class 1 probability
    try:
        fraud_index = list(model.classes_).index(1)
        fraud_probs = probas[:, fraud_index]
    except:
        fraud_probs = np.zeros(len(preds))  # fallback if only class 0 probs

    result = original.copy()
    result['Prediction'] = preds
    result['Fraud Probability'] = fraud_probs

    st.success("✅ Predictions complete!")
    st.dataframe(result.head(10))

    # Downloadable
    csv = result.to_csv(index=False).encode('utf-8')
    st.download_button("Download predictions", csv, "fraud_predictions.csv", "text/csv")
