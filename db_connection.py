import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",   # Change if using a different host
    user="root",
    password="Pass&word123",
    database="bank_loan_db"
)

cursor = conn.cursor()
print("Connected to MySQL successfully!")
