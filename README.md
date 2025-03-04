# Bank-Loan-Approval

## Overview
This project analyzes **bank loan approvals** based on various factors like income, loan amount, and applicant attributes. The analysis includes multiple visualizations, and the project is deployed using **Streamlit**.

## Features
1. **Correlation Heatmap** - Identifies relationships between different loan-related factors.
2. **Income & Loan Distributions** - Displays the spread of income and loan amounts among applicants.
3. **Income vs Loan Approval** - Analyzes whether higher income increases approval chances.
4. **Loan Amount vs Loan Approval** - Shows if higher loan amounts lead to rejections.
5. **Loan Approval Rate by Income** - Visualizes approval rates based on income levels.
6. **Scatter Plot (Income vs Loan Approval)** - Displays data points to observe trends.

## Dataset
The dataset consists of various applicant details such as:
- **Applicant Income**
- **Loan Amount**
- **Credit History**
- **Loan Status** (Approved/Rejected)

## Installation
Make sure you have **Python 3.8+** installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Streamlit App
Run the following command to launch the application:

```bash
streamlit run app.py
```

## Key Findings
1. **Correlation Analysis:**
   - Strong correlation between **credit history and loan approval**.
   - Weak correlation between **income and loan approval**.
2. **Income & Loan Distributions:**
   - Most applicants have an income between **$2,000-$6,000**.
   - Loan amounts mostly range between **$100,000-$300,000**.
3. **Income vs Loan Approval:**
   - Higher incomes **slightly increase** approval chances but **not significantly**.
4. **Loan Amount vs Loan Approval:**
   - Higher loan amounts lead to **lower approval rates**.
5. **Loan Approval Rate by Income:**
   - Approval rates remain stable **across different income groups**.

## Deployment
The project can be deployed using **Streamlit Sharing**, **Heroku**, or **Vercel**:
```bash
streamlit run app.py
```
