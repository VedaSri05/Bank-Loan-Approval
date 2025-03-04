import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set the title of the Streamlit app
st.title("Bank Loan Approval Analysis")

# Load and display heatmap
st.subheader("1. Correlation Heatmap")
st.image("plots/bankloan_heatmap.png", use_column_width=True)

# Load and display distributions
st.subheader("2. Loan & Income Distributions")
st.image("plots/distributions.png", use_column_width=True)

# Loan approval based on income
st.subheader("3. Income vs Loan Approval")
st.image("plots/income_vs_loan_approval.png", use_column_width=True)

# Loan amount vs approval rate
st.subheader("4. Loan Amount vs Loan Approval Rate")
st.image("plots/loan_amount_vs_loan_approval.png", use_column_width=True)

# Loan approval rate by income
st.subheader("5. Loan Approval Rate by Income Groups")
st.image("plots/loan_approval_rate_by_income.png", use_column_width=True)

# Scatter plot: Income vs Loan Approval
st.subheader("6. Scatter Plot: Income vs Loan Approval")
st.image("plots/scatter_income_vs_loan_approval.png", use_column_width=True)

# Summary
st.subheader("Final Summary")
summary_markdown = """
## Summary

1. **Income & Loan Approval**: 
   - Applicants with higher income have a **70%+ loan approval rate**, while lower-income groups see approvals **below 40%**.
   
2. **Loan Amount & Approval**: 
   - Loans under **$50,000** have a **60-75% approval rate**, but above **$150,000**, approval drops below **30%**.

3. **Correlation Analysis**:
   - Strong correlation between **income and approval**.
   - Weak correlation between **loan amount and approval**.

4. **Approval Rate by Income Groups**:
   - **High-income** applicants (~$75K+) have the highest approval rate (~80%).
   - **Low-income** applicants (~$25K-) have the lowest approval rate (~30%).

5. **Scatter Plot Insights**:
   - Clusters of approvals for **income > $50K** and **loan amounts < $100K**.
"""

st.markdown(summary_markdown)

