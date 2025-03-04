import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split, cross_val_score
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
from sklearn.impute import SimpleImputer
import joblib

# ✅ Use SQLAlchemy instead of direct MySQL connection
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

# ✅ Define features and target variable
X = df.drop(columns=['approval_status'])
y = df['approval_status']

# ✅ Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ✅ Apply SMOTE but **not full oversampling** (keep natural distribution better)
smote = SMOTE(sampling_strategy=0.6, random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# ✅ Train a better model (RandomForest)
rf_model = RandomForestClassifier(random_state=42)

# Hyperparameter tuning using GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
    'class_weight': ['balanced', None]
}

grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
grid_search.fit(X_train_smote, y_train_smote)

# ✅ Best parameters from GridSearchCV
print(f"Best parameters found: {grid_search.best_params_}")

# ✅ Evaluate using Cross-Validation
cv_scores = cross_val_score(grid_search.best_estimator_, X_train_smote, y_train_smote, cv=5, scoring='accuracy')
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean CV Accuracy: {cv_scores.mean()}")

# ✅ Train final model with best parameters
final_model = grid_search.best_estimator_

# ✅ Model evaluation on test set
y_pred = final_model.predict(X_test)

# ✅ Print classification report
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# ✅ Save the model to disk using joblib
joblib.dump(final_model, 'final_model.joblib')
print("Model saved as 'final_model.joblib'")
