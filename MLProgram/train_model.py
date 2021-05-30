# Importing Required Modules
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
from joblib import dump

# Loading the Dataset
dataset = pd.read_csv('SalaryData.csv')
X = dataset['YearsExperience']
y = dataset['Salary']

# Creating a Model
model = LinearRegression()

# Data Preprocessing
X = X.values.reshape(-1,1)

# Spliting the dataset in Training and Testing Set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Model
model.fit(X_train, y_train)

# Print the Weight and Bias
print("\n\n----------------------------\nWeight: {}".format(model.coef_))
print("Intercept: {}\n----------------------------\n".format(model.intercept_))

# Save the Model
dump(model,'salarypred.pk1')
print("--------------------------\n|Model Saved Successfully|\n--------------------------\n\n")