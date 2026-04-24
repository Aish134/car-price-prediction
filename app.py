import streamlit as st
import pickle
try:
    model = pickle.load(open('final_model.pkl','rb'))
    scaler = pickle.load(open('scaler.pkl','rb'))
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

d1 = {'Comprehensive':0,'Third Party insurance':1,
      'Zero Dep':2,'Not Available':3,'Third Party':1}
d2 = {'Petrol':0,'Diesel':1,'CNG':2}
d3 = {'Manual':0,'Automatic':1}
d4 = {'First Owner':1,'Second Owner':2,'Third Owner':3,
      'Fourth Owner':4,'Fifth Owner':5}

st.title("Car Price Prediction")

insurance_validity = st.selectbox("Insurance", list(d1.keys()))
fuel_type = st.selectbox("Fuel Type", list(d2.keys()))
kms_driven = st.number_input("KMs Driven", min_value=0)
ownsership = st.selectbox("Ownership", list(d4.keys()))
transmission = st.selectbox("Transmission", list(d3.keys()))
registration_year = st.number_input("Year", min_value=2000, max_value=2025)

if st.button("Predict"):
    try:
        test = [[
            d1[insurance_validity],
            d2[fuel_type],
            kms_driven,
            d4[ownsership],
            d3[transmission],
            int(str(registration_year)[-2:])
        ]]

        test_scaled = scaler.transform(test)
        yp = model.predict(test_scaled)[0]

        st.success(f"Price: {yp:.2f} Lakhs")
        st.success(f"₹ {yp*100000:,.0f}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
