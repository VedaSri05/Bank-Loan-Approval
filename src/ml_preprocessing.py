import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split, GridSearchCV
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# ✅ Use SQLAlchemy to connect to MySQL
DB_URI = "mysql+mysqlconnector://root:Pass&word123@localhost/bank_loan_db"
engine = create_engine(DB_URI)

# ✅ Fetch data using SQLAlchemy
query = "SELECT age, income, credit_score, loan_amount, approval_status FROM loan_applicants"
df = pd.read_sql(query, engine)

# ✅ Convert categorical target variable
df['approval_status'] = df['approval_status'].map({'Approved': 1, 'Rejected': 0})

# ✅ Handle missing values: Fill `credit_score` with median (if empty)
if df['credit_score'].isnull().all():
    print("⚠️ Warning: All credit_score values are NaN! Dropping column.")
    df = df.drop(columns=['credit_score'])
else:
    df['credit_score'].fillna(df['credit_score'].median(), inplace=True)

# ✅ Save cleaned dataset to `data` folder for Power BI
cleaned_data_path = "data/cleaned_loan_data.csv"
df.to_csv(cleaned_data_path, index=False)
print(f"✅ Cleaned dataset saved as '{cleaned_data_path}'")

# ✅ Define features and target variable
X = df.drop(columns=['approval_status'])
y = df['approval_status']

# ✅ Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ✅ Apply SMOTE for oversampling
smote = SMOTE(sampling_strategy=0.6, random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# ✅ Hyperparameter tuning with GridSearchCV for RandomForestClassifier
param_grid = {
    'n_estimators': [100, 150, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'class_weight': ['balanced', None]
}

grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42), 
                           param_grid=param_grid, 
                           scoring='accuracy', 
                           cv=5, 
                           n_jobs=-1)

# Train model with best parameters
grid_search.fit(X_train_smote, y_train_smote)

# Get best parameters
print("Best parameters found: ", grid_search.best_params_)

# Train RandomForestClassifier with best parameters
best_model = grid_search.best_estimator_

# ✅ Make predictions
y_pred_best = best_model.predict(X_test)

# ✅ Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred_best))
print(classification_report(y_test, y_pred_best))
