# Car Price Prediction Web App
# Live DEMO 
https://car-price-prediction-7aszcix7fvjktdsc2wwzbg.streamlit.app/
##  Project Overview
This project is a **Machine Learning web application** that predicts the price of a used car based on user inputs such as fuel type, kilometers driven, ownership, insurance type, transmission, and registration year.
The application is built using:

* **Python**
* **Streamlit (for web interface)**
* **Scikit-learn (for machine learning model)**

The predicted price is shown in **Lakhs (₹)**.
---
##  Problem Statement
Buying or selling a car can be confusing because prices vary based on many factors.
This project helps users **estimate the price of a car instantly** using a trained machine learning model.
---
##  How It Works
1. User enters car details:
   * Insurance type
   * Fuel type
   * Kilometers driven
   * Ownership (1st, 2nd, etc.)
   * Transmission (Manual/Automatic)
   * Registration year

2. The app:
   * Converts inputs into numeric values
   * Scales the data (important for model accuracy)
   * Sends it to the trained ML model

3. The model predicts:
   * Car price in **Lakhs**
   * Equivalent value in **Indian Rupees (₹)**

##  Machine Learning Model
* Algorithm used: **K-Nearest Neighbors (KNN)**
* Feature scaling: **StandardScaler**
* Why scaling?
  → Ensures all features contribute equally (important for KNN)

## Project Structure

```
car-price-prediction/
│
├── app.py                # Streamlit web app
├── model.py              # Model training script
├── final_model.pkl       # Trained ML model
├── scaler.pkl            # Scaler used for normalization
├── requirements.txt      # Required libraries
├── README.md             # Project documentation
└── images/
    ├── input.png         # App input screenshot
    └── output.png        # Prediction screenshot
```
---

##  How to Run This Project (Step-by-Step)

###  Step 1: Clone the repository

```
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction
```

---

### 🔹 Step 2: Install dependencies

```
pip install -r requirements.txt
```

---

### 🔹 Step 3: Run the application

```
streamlit run app.py
```

---

### 🔹 Step 4: Open in browser

The app will open automatically, or go to:

```
http://localhost:8501
```

---

## 📸 Application Screenshots

### 🔹 Input Page

<img width="1113" height="602" alt="image" src="https://github.com/user-attachments/assets/8f48e604-c1c0-43f3-b78e-3a35080fcc08" />


### 🔹 Prediction Output

<img width="1094" height="598" alt="image" src="https://github.com/user-attachments/assets/00bbcdfd-a372-47de-9310-85cd8ca29097" />

---

## Input Features Explained

| Feature            | Description                                          |
| ------------------ | ---------------------------------------------------- |
| Insurance Validity | Type of insurance (Comprehensive, Third Party, etc.) |
| Fuel Type          | Petrol / Diesel / CNG                                |
| KMs Driven         | Total distance driven                                |
| Ownership          | Number of previous owners                            |
| Transmission       | Manual or Automatic                                  |
| Registration Year  | Year the car was registered                          |

---

##  Example

**Input:**

* Fuel Type: Petrol
* KMs Driven: 40,000
* Ownership: First Owner
* Transmission: Manual

**Output:**

```
Predicted Price: 5.75 Lakhs  
Approx Price: ₹ 5,75,000
```

---

##  Features

✅ Simple and easy-to-use interface
✅ Real-time prediction
✅ Accurate ML-based estimation
✅ Beginner-friendly project

---

##  Limitations

* Model accuracy depends on dataset quality
* Does not consider brand/model of car
* Predictions are approximate, not exact market value

---

##  Future Improvements

* Add car brand & model
* Use advanced models (Random Forest / XGBoost)
* Deploy online (Streamlit Cloud)
* Improve UI design

---

## Author

**Aishwarya**

---

##  Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share it

---

## 📬 Contact

For any questions or suggestions, feel free to reach out!
