# 🏦 Bank Loan Approval Dashboard

An interactive data analysis and prediction dashboard for bank loan approvals. Built using **Streamlit**, this project leverages machine learning and data visualization to understand approval trends and classify loan applications based on user inputs.

---

## 📌 Overview

This project analyzes a bank's historical loan data to uncover insights and predict loan approval outcomes. It integrates:
- Data preprocessing in **MySQL Workbench**
- Analysis and modeling in **Python**
- Real-time deployment via **Streamlit**

---

## 🧰 Tech Stack & Libraries

| Purpose            | Tools/Libraries Used                          |
|--------------------|------------------------------------------------|
| Database Management| **MySQL Workbench**, `mysql-connector-python`, `SQLAlchemy` |
| Data Handling      | `pandas`                                       |
| Visualization      | `matplotlib`, `seaborn`                        |
| Machine Learning   | `scikit-learn`, `imbalanced-learn`, `joblib`  |
| Web App Interface  | `streamlit`                                    |

---

## 📂 Features

- ✅ Cleaned and preprocessed data using **SQL queries** in MySQL Workbench
- 📊 Rich visualization of loan patterns (e.g., heatmaps, distribution plots)
- 🤖 Machine learning model trained to predict loan approvals
- 🎛️ User-friendly Streamlit dashboard for real-time predictions
- 💡 Balanced data using techniques from `imbalanced-learn` for better accuracy

---

## ⚙️ How to Run the App

### 1. Clone the Repository
```bash
git clone https://github.com/VedaSri05/Bank-Loan-Approval.git
cd Bank-Loan-Approval
````

### 2. Install Required Libraries

If a `requirements.txt` file is not available, install manually:

```bash
pip install mysql-connector-python pandas matplotlib seaborn scikit-learn imbalanced-learn streamlit sqlalchemy joblib
```

### 3. Launch the Streamlit App

```bash
streamlit run app.py
```

> Make sure your database connection details in the code are correct (host, user, password, database name) before running.

---


## 📊 Visualizations Include

* Loan approval distribution by credit history, education, gender
* Heatmaps showing feature correlations
* Histograms for income and loan amount
* Pie charts for categorical distributions
