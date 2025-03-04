create database bank_loan_db;
use bank_loan_db;

CREATE TABLE IF NOT EXISTS loan_applicants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18), 
    income DECIMAL(10,2) NOT NULL,
    credit_score INT CHECK (credit_score BETWEEN 300 AND 900),
    loan_amount DECIMAL(10,2) NOT NULL,
    approval_status ENUM('Approved', 'Rejected', 'Pending') DEFAULT 'Pending'
);

CREATE TABLE IF NOT EXISTS loan_details (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT,
    loan_type ENUM('Personal', 'Home', 'Car', 'Education', 'Business') NOT NULL,
    interest_rate DECIMAL(4,2) NOT NULL,
    tenure INT NOT NULL CHECK (tenure > 0), -- Tenure in months
    FOREIGN KEY (applicant_id) REFERENCES loan_applicants(id) ON DELETE CASCADE
);

select count(*) from bankloan;
select count(*) from loan_applicants;
select count(*) from loan_details;

SELECT COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'bankloan';

CREATE TABLE loan_applicants (
    id INT,
    age INT,
    income DECIMAL(10, 2),
    credit_score INT,
    loan_amount DECIMAL(10, 2),
    approval_status VARCHAR(10)
);

INSERT INTO loan_applicants (id, age, income, credit_score, loan_amount, approval_status)
SELECT ID, Age, Income, NULL, Mortgage, 
       CASE WHEN `Personal.Loan` = 1 THEN 'Approved' ELSE 'Rejected' END
FROM bankloan;

CREATE TABLE loan_details (
    applicant_id INT,
    loan_type VARCHAR(50),
    interest_rate DECIMAL(5, 2),
    tenure INT
);

INSERT INTO loan_details (applicant_id, loan_type, interest_rate, tenure)
SELECT b.ID, 
       CASE 
           WHEN b.Education = 1 THEN 'Undergraduate Loan' 
           WHEN b.Education = 2 THEN 'Graduate Loan'
           WHEN b.Education = 3 THEN 'Professional Loan'
           ELSE 'Unknown' 
       END,
       CCAvg * 2,  -- Assuming interest rate is derived from CCAvg (modify if needed)
       Experience  -- Using `Experience` as a proxy for tenure (modify if needed)
FROM bankloan b
JOIN loan_applicants la ON b.ID = la.id;

SELECT COUNT(*) FROM loan_applicants;
SELECT COUNT(*) FROM loan_details;
select count(*) from bankloan;

SHOW VARIABLES LIKE 'secure_file_priv';

SELECT * 
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/loan_applicants.csv'
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
FROM loan_applicants;

SELECT * 
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/loan_details.csv'
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
FROM loan_details;

















