# 🎓 Student Exam Performance Prediction

An end-to-end **Machine Learning project** that predicts a student's **math exam performance** based on various demographic and academic factors.

The project includes the complete ML pipeline — from **data ingestion and preprocessing to model training, evaluation, serialization, and deployment using Flask**.

---

## 🚀 Project Overview

The goal of this project is to build a machine learning system that can estimate a student's mathematics score using features such as:

* Gender
* Race / Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

The trained machine learning model is integrated with a **Flask web application**, allowing users to enter student information through a simple web interface and receive a predicted mathematics score.

---

## 🧠 Machine Learning Workflow

The project follows a complete end-to-end ML workflow:

```text
Data Collection
      ↓
Data Ingestion
      ↓
Data Validation
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
Flask Web Application
      ↓
Prediction
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* XGBoost

### Web Framework

* Flask
* HTML
* CSS

### Data Visualization

* Matplotlib
* Seaborn

### Development Tools

* Git
* GitHub
* VS Code

---

## 📁 Project Structure

```text
MLProject/
│
├── artifacts/
│   ├── data.csv
│   ├── train.csv
│   └── test.csv
│
├── logs/
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── prediction_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── app.py
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The project uses the **Student Performance Dataset**, containing information about students' demographic background, education, test preparation, and previous exam scores.

### Target Variable

**Math Score**

The model predicts the expected mathematics score based on the available student information.

---

## 🔍 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand:

* Distribution of student scores
* Relationship between reading and writing scores
* Impact of test preparation on performance
* Effect of parental education
* Gender-wise performance
* Lunch type and academic performance
* Correlation between numerical features

---

## ⚙️ Data Preprocessing

The preprocessing pipeline includes:

* Handling categorical features
* Handling numerical features
* One-Hot Encoding
* Feature scaling
* Train-test splitting
* Transformation using Scikit-learn pipelines

The preprocessing object is saved and reused during prediction to ensure that new input data goes through the same transformations as the training data.

---

## 🤖 Model Training

Multiple regression algorithms can be evaluated during model training, such as:

* Linear Regression
* Ridge Regression
* Lasso Regression
* K-Neighbors Regressor
* Decision Tree Regressor
* Random Forest Regressor
* AdaBoost Regressor
* Gradient Boosting Regressor
* XGBoost Regressor

The best-performing model is selected based on evaluation metrics and stored for later predictions.

---

## 📈 Model Evaluation

The regression models are evaluated using metrics such as:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

The model with the best overall performance is selected for deployment.

---

## 🌐 Flask Web Application

The trained model is deployed using **Flask**.

The web application provides a user-friendly interface where users can enter student information and get an estimated mathematics score.

### Application Flow

```text
User Input
    ↓
Flask Application
    ↓
Prediction Pipeline
    ↓
Data Transformation
    ↓
Trained ML Model
    ↓
Predicted Math Score
    ↓
Result on Web Page
```

---

## 💻 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Pranav3536/<YOUR-REPOSITORY-NAME>.git
```

```bash
cd <YOUR-REPOSITORY-NAME>
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 4. Run the Flask Application

```bash
python app.py
```

You should see Flask start running locally.

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

---

## 🎯 Example Prediction

After opening the web application:

1. Enter the student's details.
2. Submit the form.
3. The application sends the data to the prediction pipeline.
4. The trained model processes the input.
5. The predicted mathematics score is displayed on the screen.

---

## 🔮 Future Improvements

Possible improvements for the project include:

* Deploying the application on Render / AWS / Azure
* Adding a prediction history feature
* Improving UI/UX
* Adding model explainability using SHAP
* Adding more advanced models
* Creating an API endpoint for predictions
* Adding Docker support
* Implementing CI/CD using GitHub Actions

---

## 👨‍💻 Author

**Pranav Shrivastav**

B.Tech – Computer Science & Engineering (Data Science)

GitHub: **Pranav3536**

---

## ⭐ If You Like This Project

If you found this project useful, consider giving the repository a ⭐ on GitHub.
