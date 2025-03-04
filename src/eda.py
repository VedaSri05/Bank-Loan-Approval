import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from db_connection import conn

# Load data
query = "SELECT * FROM loan_applicants"
df = pd.read_sql(query, conn)

# Handle missing values
df.fillna(0, inplace=True)

# Plot approval distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='approval_status', data=df, palette='coolwarm')
plt.title('Loan Approval Status Distribution')
plt.show()

# Close connection
conn.close()
