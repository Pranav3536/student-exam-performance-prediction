# 🎓 Student Exam Performance Prediction

An end-to-end **Machine Learning project** that predicts a student's **Mathematics Score** based on demographic, academic, and previous performance-related factors.

This project demonstrates a complete machine learning workflow — from **Exploratory Data Analysis and data ingestion to preprocessing, model training, evaluation, model serialization, and deployment using Flask**.

---

## 🚀 Project Overview

The objective of this project is to develop a machine learning model that predicts a student's mathematics score using different academic and demographic features.

### Input Features

* Gender
* Race / Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

The trained model is integrated with a **Flask web application**, allowing users to enter student details and receive a predicted mathematics score through a simple web interface.

---

## 🧠 Machine Learning Workflow

The project follows an end-to-end machine learning pipeline:

```text
Dataset
   ↓
Exploratory Data Analysis
   ↓
Data Ingestion
   ↓
Data Transformation
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Model Serialization
   ↓
Flask Deployment
   ↓
Prediction
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning & Data Processing

* Pandas
* NumPy
* Scikit-learn
* CatBoost
* XGBoost

### Data Visualization

* Matplotlib
* Seaborn

### Web Development

* Flask
* HTML
* CSS

### Tools

* Jupyter Notebook
* Git
* GitHub
* VS Code

---

## 📁 Project Structure

```text
student-exam-performance-prediction/
│
├── artifacts/
│   ├── data.csv
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   └── test.csv
│
├── catboost_info/
│   ├── learn/
│   ├── catboost_training.json
│   ├── learn_error.tsv
│   └── time_left.tsv
│
├── notebook/
│   ├── catboost_info/
│   ├── data/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
│
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │
│   ├── __inti__.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│
├── .gitignore
├── README.md
├── app.py
├── requirements.txt
└── setup.py
```

---

## 📊 Dataset

The project uses the **Student Performance Dataset**, which contains information related to students' demographic background, parental education, lunch type, test preparation, and previous academic performance.

### 🎯 Target Variable

**Math Score**

The machine learning model predicts the expected mathematics score based on the available input features.

---

## 🔍 Exploratory Data Analysis

The project includes a dedicated EDA notebook:

```text
1. EDA STUDENT PERFORMANCE.ipynb
```

The exploratory analysis focuses on understanding:

* Distribution of student scores
* Relationship between reading and writing scores
* Impact of test preparation on performance
* Effect of parental education
* Gender-wise performance
* Lunch type and academic performance
* Relationships between numerical features
* Feature correlations

---

## ⚙️ Data Preprocessing

The project uses a preprocessing pipeline to prepare the dataset for machine learning.

The preprocessing process includes:

* Numerical feature processing
* Categorical feature processing
* One-Hot Encoding
* Feature scaling
* Train-test splitting
* Feature transformation

The trained preprocessing object is saved as:

```text
artifacts/preprocessor.pkl
```

This same preprocessing object is reused when making predictions on new student data.

---

## 🤖 Model Training

The model training process is implemented in:

```text
2. MODEL TRAINING.ipynb
```

Multiple regression algorithms can be evaluated during the training process, including:

* Linear Regression
* Ridge Regression
* Lasso Regression
* K-Neighbors Regressor
* Decision Tree Regressor
* Random Forest Regressor
* AdaBoost Regressor
* Gradient Boosting Regressor
* XGBoost Regressor
* CatBoost Regressor

The best-performing model is selected based on the evaluation metrics and serialized for deployment.

The trained model is stored as:

```text
artifacts/model.pkl
```

---

## 📈 Model Evaluation

The regression models are evaluated using standard regression metrics:

* **R² Score**
* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**

The model with the best overall performance is selected for the final prediction pipeline.

---

## 💾 Model Serialization

After training, the selected model and preprocessing pipeline are saved using Python serialization.

### Saved Artifacts

```text
artifacts/
├── model.pkl
└── preprocessor.pkl
```

These files allow the Flask application to load the trained machine learning components without retraining the model every time the application starts.

---

## 🌐 Flask Web Application

The trained machine learning model is deployed using **Flask**.

The application allows users to enter student information through a web interface and receive a predicted mathematics score.

### Application Flow

```text
User Input
     ↓
Flask Application
     ↓
Prediction Pipeline
     ↓
Preprocessor
     ↓
Trained Model
     ↓
Predicted Math Score
     ↓
Result Displayed on Web Page
```

---

## 💻 How to Run the Project Locally

Follow the steps below to run the project on your local machine.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pranav3536/student-exam-performance-prediction.git
```

Navigate to the project directory:

```bash
cd student-exam-performance-prediction
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

---

### 4️⃣ Run the Flask Application

Start the application:

```bash
python app.py
```

The Flask server should start running locally.

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## ⚡ Quick Start

If the virtual environment and dependencies are already configured:

```bash
venv\Scripts\activate
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

---

## 🎯 Making a Prediction

Once the Flask application is running:

1. Open the application in your browser.
2. Enter the required student information.
3. Submit the prediction form.
4. The input data is passed to the prediction pipeline.
5. The saved preprocessor transforms the input.
6. The trained model generates the predicted mathematics score.
7. The prediction is displayed on the web page.

---

## 🔮 Future Improvements

Potential improvements for the project include:

* Deploying the application on cloud platforms such as Render, AWS, or Azure
* Adding prediction history
* Improving UI/UX
* Adding model explainability using SHAP
* Creating a REST API for predictions
* Adding Docker support
* Implementing CI/CD with GitHub Actions
* Adding automated model retraining

---

## 👨‍💻 Author

### Pranav Shrivastav

**B.Tech – Computer Science & Engineering (Data Science)**

GitHub: **Pranav3536**

---

## ⭐ If You Like This Project

If you found this project useful, consider giving the repository a ⭐ on GitHub.
