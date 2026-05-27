# =========================================================
# LOAN PREDICTION USING MULTIPLE CLASSIFICATION ALGORITHMS
# =========================================================

# =========================
# IMPORT LIBRARIES
# =========================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning Models
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Train Test Split
from sklearn.model_selection import train_test_split

# Metrics
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("loanfile.csv")

print(df.head())

# =========================
# DATA INFORMATION
# =========================

print(df.info())

print("\nShape of Dataset:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# =========================
# HANDLE MISSING VALUES
# =========================

# Fill LoanAmount with mean
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())

# Fill Credit_History with median
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].median())

# Drop remaining null values
df.dropna(inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# =========================
# DATA VISUALIZATION
# =========================

plt.figure(figsize=(18,10))

# Gender
plt.subplot(231)
sns.countplot(x='Gender', hue='Loan_Status', data=df)

# Married
plt.subplot(232)
sns.countplot(x='Married', hue='Loan_Status', data=df)

# Education
plt.subplot(233)
sns.countplot(x='Education', hue='Loan_Status', data=df)

# Self Employed
plt.subplot(234)
sns.countplot(x='Self_Employed', hue='Loan_Status', data=df)

# Property Area
plt.subplot(235)
sns.countplot(x='Property_Area', hue='Loan_Status', data=df)

plt.tight_layout()
plt.show()

# =========================
# LABEL ENCODING
# =========================

# Target Variable
df['Loan_Status'] = df['Loan_Status'].replace({'Y':1, 'N':0})

# Gender
df['Gender'] = df['Gender'].map({'Male':1, 'Female':0})

# Married
df['Married'] = df['Married'].map({'Yes':1, 'No':0})

# Education
df['Education'] = df['Education'].map({'Graduate':1, 'Not Graduate':0})

# Self Employed
df['Self_Employed'] = df['Self_Employed'].map({'Yes':1, 'No':0})

# Property Area
df['Property_Area'] = df['Property_Area'].map({
    'Rural':0,
    'Semiurban':1,
    'Urban':2
})

# Dependents
df['Dependents'] = df['Dependents'].replace('3+', 3)
df['Dependents'] = df['Dependents'].astype(int)

# =========================
# DROP LOAN_ID
# =========================

df.drop('Loan_ID', axis=1, inplace=True)

# =========================
# FEATURE & TARGET SELECTION
# =========================

X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=0
)

# =========================================================
# FUNCTION TO EVALUATE MODELS
# =========================================================

def evaluate_model(model, model_name):

    # Train Model
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Print Results
    print("\n====================================")
    print(f"{model_name}")
    print("====================================")

    print("Accuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    print("\nConfusion Matrix:")
    print(cm)

    # Heatmap
    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt='d')

    plt.title(f"{model_name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

# =========================================================
# 1. LOGISTIC REGRESSION
# =========================================================

lr_model = LogisticRegression(max_iter=1000)

evaluate_model(lr_model, "Logistic Regression")

# =========================================================
# 2. K-NEAREST NEIGHBORS (KNN)
# =========================================================

knn_model = KNeighborsClassifier(n_neighbors=5)

evaluate_model(knn_model, "K-Nearest Neighbors")

# =========================================================
# 3. DECISION TREE
# =========================================================

dt_model = DecisionTreeClassifier(random_state=0)

evaluate_model(dt_model, "Decision Tree")

# =========================================================
# 4. RANDOM FOREST
# =========================================================

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=0
)

evaluate_model(rf_model, "Random Forest")

# =========================================================
# 5. SUPPORT VECTOR MACHINE (SVM)
# =========================================================

svm_model = SVC()

evaluate_model(svm_model, "Support Vector Machine")

# =========================================================
# 6. NAIVE BAYES
# =========================================================

nb_model = GaussianNB()

evaluate_model(nb_model, "Naive Bayes")