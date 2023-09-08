from roboflow import Roboflow
import streamlit as st

with open('RoboFlowAPIKey.txt', 'r') as f:
    key = f.read()


def predict(image_path):
    rf = Roboflow(api_key=key)
    project = rf.workspace().project(
        "traffic-detection-ps27b")
    model = project.version(1).model
    prediction = model.predict(image_path, confidence=40, overlap=30).json()
    model.predict(image_path, confidence=40, overlap=30).save(
        "savedprediction.jpg")
    st.image('savedprediction.jpg',
             caption="Annotated Image", use_column_width=True)
    return prediction
