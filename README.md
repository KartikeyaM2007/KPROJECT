# 📊 Student Exam Performance Predictor

A Machine Learning web application that predicts a student’s **math score** based on demographic and academic features. Built with an end-to-end pipeline including data ingestion, preprocessing, model training, and a Flask-based web interface.

---

## 🚀 Features

- 📥 Data Ingestion & Train-Test Split  
- 🔄 Data Transformation Pipeline (Scaling + Encoding)  
- 🤖 Machine Learning Model Training  
- 🔮 Prediction Pipeline with saved model & preprocessor  
- 🌐 Flask Web App for user interaction  
- ☁️ Deployment-ready (Render / AWS)

---

## 🧠 Problem Statement

Predict the **math score** of a student using:

- Gender  
- Race/Ethnicity  
- Parental Level of Education  
- Lunch Type  
- Test Preparation Course  
- Reading Score  
- Writing Score  

---

## 🏗️ Project Structure

```
KPROJECT/
│
├── artifacts/
│   ├── train.csv
│   ├── test.csv
│   ├── preprocessor.pkl
│   └── model.pkl
│
├── notebook/
│   └── data/
│       └── stud.csv
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   │
│   ├── utils.py
│   ├── logger.py
│   └── exception.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository
```
git clone https://github.com/KartikeyaM2007/KPROJECT.git
cd KPROJECT
```

### 2. Create virtual environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

---

## ▶️ Run the Project Locally

### Step 1: Run pipeline (optional if already trained)
```
python src/components/data_ingestion.py
```

### Step 2: Start Flask app
```
python app.py
```

### Step 3: Open browser
```
http://localhost:5000
```

---

## 🧪 How It Works

1. User enters data via web form  
2. Data is converted into a DataFrame  
3. Preprocessing (scaling + encoding) is applied  
4. Model predicts math score  
5. Result displayed on UI  

---

## 📦 Model Pipeline

- **Numerical Features** → Median Imputation + StandardScaler  
- **Categorical Features** → Most Frequent Imputation + OneHotEncoding  
- **Model** → Trained ML model (e.g., Linear Regression / Random Forest)

---

## 🌐 Deployment (Render)

### Build Command:
```
pip install -r requirements.txt
```

### Start Command:
```
gunicorn -b 0.0.0.0:$PORT app:app
```

---

## ⚠️ Important Notes

- Ensure `model.pkl` and `preprocessor.pkl` exist in `artifacts/`
- Field names in HTML must match backend (`race_ethnicity`, etc.)
- Do NOT use Flask dev server in production

---

## 🔧 Tech Stack

- Python  
- Pandas / NumPy  
- Scikit-learn  
- Flask  
- Gunicorn  

---

## 🚀 Future Improvements

- Add model comparison (XGBoost, Random Forest, etc.)  
- Add feature importance visualization  
- Add user authentication  
- Deploy with Docker  

---

## 👨‍💻 Author

**Kartikeya**  
AI/ML Developer  

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
