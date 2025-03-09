import pandas as pd
import numpy as np

# load data
diabetes_data = pd.read_csv('diabetes.csv')

#inspect dataframe
print(diabetes_data.shape)

print(diabetes_data.isnull().sum())

print(diabetes_data.describe())

diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

print(diabetes_data.isnull().sum())

print(diabetes_data[diabetes_data.isnull().any(axis=1)])

print(diabetes_data.dtypes)

print(diabetes_data.Outcome.unique())

diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', 0)
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype(int)
