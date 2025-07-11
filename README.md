
# 🩺 Diabetes Prediction System

A machine learning-based web app to predict whether a patient is diabetic based on clinical data. Built with **Flask**, trained using **scikit-learn**, and deployed on **Render**.


## 🌐 Live Demo

👉 [Try it here](https://diabetes-prediction-system-k6t8.onrender.com)  

## 🚀 Features

- Predicts diabetes using medical attributes
- Trained with the PIMA Indian Diabetes dataset
- StandardScaler for feature normalization
- Intuitive web interface (HTML + Flask)
- Deployed online for public use

## 📁 Folder Structure
```
Diabetes_prediction_system/
├── app.py
├── model/
│   ├── modelForPrediction.pkl
│   └── standardScaler.pkl
├── templates/
│   ├── home.html
│   └── result.html
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🛠 Tech Stack

| Layer        | Tools/Frameworks     |
|--------------|----------------------|
| Frontend     | HTML, Bootstrap      |
| Backend      | Flask (Python)       |
| ML Model     | scikit-learn         |
| Deployment   | Render               |

---

## 📥 How to Run Locally

### 1. Clone the Repository
```
git clone https://github.com/navinyadav8919/Diabetes_prediction_system.git
cd Diabetes_prediction_system
````

### 2. Create and Activate a Virtual Environment

```
python -m venv env
env\Scripts\activate          # On Windows
# source env/bin/activate     # On macOS/Linux
```

### 3. Install Required Packages

```
pip install -r requirements.txt
```

### 4. Run the App

```
python app.py
```

Then open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📊 Input Features

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

---

## 🧑‍💻 Author

**Naveen Yadav**
🔗 GitHub: [@navinyadav8919](https://github.com/navinyadav8919)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

```


