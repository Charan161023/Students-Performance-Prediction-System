# 🎓 Student Performance Prediction System

## 📌 Project Introduction

This project is developed to predict a student's performance based on different factors such as study hours, previous scores, extracurricular activities, sleep hours, and sample question papers practiced.

The project uses Machine Learning Linear Regression algorithm to estimate the Performance Index of a student.

A Flask web application is also developed so that users can enter their details and get predictions instantly.

---

## 🎯 Objective

The main objective of this project is:

- To understand Machine Learning concepts.
- To predict student performance using data.
- To build a real-time prediction system.
- To learn Flask web development.
- To integrate Machine Learning model with a web application.

---

## 📊 Dataset Information

The dataset contains information about students and their academic activities.

### Input Features

1. Hours Studied
   - Number of hours spent studying.

2. Previous Scores
   - Previous academic score of the student.

3. Extracurricular Activities
   - Participation in activities.
   - Yes = 1
   - No = 0

4. Sleep Hours
   - Average sleeping hours per day.

5. Sample Question Papers Practiced
   - Number of sample papers solved.

### Target Variable

Performance Index

The model predicts this value based on the above features.

---

## ⚙️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Pickle

### Framework
- Flask

### Frontend
- HTML
- CSS

---

## 🔍 Project Workflow

### Step 1: Data Collection

The dataset is loaded from CSV file.

```python
df = pd.read_csv("data/Student_Performance.csv")
```
### Step 2: Data Analysis

Data is analyzed using:

- head()
- shape
- describe()
- dtypes
- missing values

### Step 3: Data Visualization

Graphs are created using:

- Histogram
- Heatmap

This helps understand data distribution and feature relationships.

### Step 4: Data Preprocessing

Extracurricular Activities column is converted:

```python
Yes → 1
No → 0
```

Machine Learning algorithms work only with numerical values.

### Step 5: Feature Selection

Input Features:

- Hours Studied
- Previous Scores
- Extracurricular Activities
- Sleep Hours
- Sample Question Papers Practiced

Target:

- Performance Index

### Step 6: Train-Test Split

Dataset is divided into:

- 80% Training Data
- 20% Testing Data

```python
train_test_split()
```

### Step 7: Model Training

Linear Regression algorithm is used.

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

### Step 8: Prediction

Model predicts student performance.

```python
prediction = model.predict(data)
```

### Step 9: Model Evaluation

Performance Metrics:

- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

Results:

R² Score = 0.98

This indicates excellent model performance.

### Step 10: Model Saving

The trained model is saved using Pickle.

```python
pickle.dump(model, open("model.pkl","wb"))
```

---

## 🌐 Flask Web Application

A user-friendly web interface is developed using Flask.

Users can:

- Enter student details
- Click Predict Performance
- View predicted Performance Index

---

## 📁 Project Structure

Student_Performance_Regression/

├── data/

│ └── Student_Performance.csv

│

├── templates/

│ └── index.html

│

├── app.py

├── main.py

├── model.pkl

├── requirements.txt

└── README.md
   Screenshots


---

## 🚀 Future Improvements

This project can be improved by using:

- Random Forest Regression
- Decision Tree Regression
- Deep Learning Models
- Cloud Deployment

---

## 🎓 Learning Outcomes

Through this project I learned:

- Data Analysis
- Data Visualization
- Feature Engineering
- Machine Learning
- Linear Regression
- Model Evaluation
- Flask Web Development
- Model Deployment

---

## 👨‍💻 Author

Teja N

B.Tech (ECE)

Machine Learning Project

Vihara Tech

2026
## Screenshots

### Home Page
![Home Page](Screenshots/home_page.png)

### Prediction Result
![Prediction Result](Screenshots/prediction_result.png)

### GitHub Repository
![GitHub Repository](Screenshots/github_repo.png)