import streamlit as st
import os
import tempfile
import widgets as w
import time as t
import predict as p
import trafficSwitchAlgo as ts


st.title('Traffic Light Color Prediction')
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Create a temporary file, save the uploaded file into it
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    prediction = p.predict(tfile.name)
    light_color = ts.trafficSwitch(prediction)

    st.write(f'The traffic light should be: {light_color.upper()}')

    # Delete the temporary file
    tfile.close()
    os.unlink(tfile.name)

    col1, col2 = st.columns(2)
    # Add 3-second yellow light delay
    # Create placeholders for traffic lights
    light_placeholder_vehicles = col1.empty()
    light_placeholder_people = col2.empty()

    # Add 3-second yellow light delay
    light_placeholder_vehicles.markdown(w.display_traffic_light_people(
        yellow='on', category="People"), unsafe_allow_html=True)
    light_placeholder_people.markdown(w.display_traffic_light_vehicles(
        yellow='on', category="Vehicles"), unsafe_allow_html=True)

    for i in range(100):
        t.sleep(0.05)

    # Turn yellow off and show the actual colors by updating the placeholders
    if light_color == 'red':
        light_placeholder_vehicles.markdown(w.display_traffic_light_people(
            red='on', category="People"), unsafe_allow_html=True)
    else:
        light_placeholder_vehicles.markdown(w.display_traffic_light_people(
            green='on', category="People"), unsafe_allow_html=True)

    if light_color == 'red':
        light_placeholder_people.markdown(w.display_traffic_light_vehicles(
            green='on', category="Vehicles"), unsafe_allow_html=True)
    else:
        light_placeholder_people.markdown(w.display_traffic_light_vehicles(
            red='on', category="Vehicles"), unsafe_allow_html=True)
