import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from db_connection import conn

# Load loan applicants data
query = "SELECT * FROM loan_applicants"
df = pd.read_sql(query, conn)

# Display basic info
print(df.info())
print(df.head())

# Close connection
conn.close()
