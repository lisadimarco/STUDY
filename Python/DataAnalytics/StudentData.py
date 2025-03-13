# Load libraries
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
#print(students.head(5))

# Print summary statistics for all columns
#print(students.describe(include='all'))

# Calculate mean
math_grade_mean = students.math_grade.mean()
print(math_grade_mean)
# Calculate median
math_grade_median = students.math_grade.median()
print(math_grade_median)
# Calculate mode
math_grade_mode = students.math_grade.mode()[0]
print(math_grade_mode)
# Calculate range
math_grade_range = students.math_grade.max()-students.math_grade.min()
print(math_grade_range)
# Calculate standard deviation
math_grade_std = students.math_grade.std()
print(math_grade_std)
# Calculate MAD
math_grade_mad = students.math_grade.mad()
print(math_grade_mad)
# Create a histogram of math grades
sns.histplot(data=students, x='math_grade')

plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(data=students, x='math_grade')

plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
M_job = students.Mjob.value_counts()
print(M_job)
# Calculate proportion of students with mothers in each job category
M_job = students.Mjob.value_counts(normalize=True)
print(M_job)
# Create bar chart of Mjob
sns.countplot(data=students, x='Mjob')

plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()

plt.show()
