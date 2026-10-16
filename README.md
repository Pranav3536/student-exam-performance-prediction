# 🎓 Student Exam Performance Prediction

An end-to-end **Machine Learning project** that predicts students' Mathematics Scores using demographic details and academic performance. The project covers EDA, data preprocessing, model training, evaluation, and web-based prediction using Flask and Streamlit.

🔗 **Live Demo:** [Score Insight – Streamlit App](https://score-insight-ml.streamlit.app/)

## 🚀 Project Overview

The goal is to predict a student's math score using seven input features:

- Gender
- Race / Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

**Dataset:** 1,000 student records with 8 columns, including the target variable `math_score`.

## 🧠 Machine Learning Workflow

```text
Dataset → EDA → Data Ingestion → Preprocessing
       → Model Training → Evaluation
       → Model Serialization → Web App → Prediction
```

## 🛠️ Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn, CatBoost, XGBoost
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Flask, Streamlit
- **Frontend:** HTML, CSS
- **Tools:** Jupyter Notebook, Git, GitHub, VS Code

## 📁 Project Structure

```text
student-exam-performance-prediction/
│
├── artifacts/
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│   ├── data/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
├── app.py
├── streamlit_app.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

## 🔍 Exploratory Data Analysis (EDA)

The EDA notebook explores:

- Student score distributions and feature correlations
- Reading and writing score relationships
- Performance patterns by gender and lunch type
- Test preparation and parental education
- Relationships between academic and demographic features

## ⚙️ Data Preprocessing

The preprocessing pipeline includes:

- Handling missing values using imputation
- One-Hot Encoding for categorical features
- Standard scaling for numerical features
- Train-test splitting
- Saving the fitted preprocessor as `preprocessor.pkl`

The same preprocessing object is reused for new inputs during prediction.

## 🤖 Model Training & Evaluation

Multiple regression algorithms were explored:

- Linear Regression and Ridge Regression
- Lasso Regression
- K-Neighbors Regressor
- Decision Tree and Random Forest
- AdaBoost and Gradient Boosting
- XGBoost and CatBoost

Models were evaluated using **R² Score, Mean Absolute Error (MAE), and Mean Squared Error (MSE)**.

### 📈 Model Results

The model training notebook reported the following R² scores:

| Model | R² Score |
|---|---:|
| Ridge Regression | 0.8806 |
| Linear Regression | 0.8804 |

Linear Regression achieved an R² score of approximately **0.88**, indicating that the model explained around 88% of the variance in math scores on the evaluated test data. Ridge Regression performed similarly in the notebook experiments.

The selected model and preprocessing pipeline are serialized as `.pkl` files for reuse without retraining on every prediction.

## 🌐 Web Application

The project provides interfaces for making predictions through Flask and Streamlit.

**Prediction flow:**

```text
Student Details → Preprocessor → Trained Model
                → Predicted Math Score
```

- **Live Streamlit Demo:** [Try the application](https://score-insight-ml.streamlit.app/)
- **Flask Application:** Accepts student details through an HTML form and displays the predicted score.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Pranav3536/student-exam-performance-prediction.git
cd student-exam-performance-prediction
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

To run the Streamlit interface separately, install Streamlit if required and execute:

```bash
streamlit run streamlit_app.py
```

## 🔮 Future Improvements

- Model explainability using SHAP
- REST API for predictions
- Docker and CI/CD integration
- Cloud deployment and automated model retraining
- Prediction history and UI improvements

## 👨‍💻 Author

**Pranav Shrivastav**  
B.Tech – Computer Science & Engineering (Data Science)

- [GitHub](https://github.com/Pranav3536)
- [Live Project Demo](https://score-insight-ml.streamlit.app/)

---

⭐ If you find this project useful, consider giving the repository a star!
