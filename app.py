import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Network Intrusion Detection AI",
    page_icon="🛡️",
    layout="wide"
)

model = joblib.load("kdd_champion_rf_model.pkl")
scaler = joblib.load("kdd_traffic_scaler.pkl")

st.title("🛡️ Network Intrusion Detection AI")
st.write("Detect whether a network connection is Normal or an Attack using Machine Learning.")

st.subheader("Enter Network Traffic Values")

feature_names = scaler.feature_names_in_

input_data = {}

for feature in feature_names:
    input_data[feature] = st.number_input(
        feature,
        value=0.0
    )

if st.button("🚀 Predict"):

    input_df = pd.DataFrame(
        [input_data],
        columns=feature_names
    )

    scaled_data = scaler.transform(input_df)

    prediction = model.predict(scaled_data)

    st.subheader("Prediction Result")

    if prediction[0] == 0:
        st.error("🚨 Attack Detected")
    else:
        st.success("✅ Normal Traffic")

    st.write("Model Output:", prediction[0])