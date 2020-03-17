import pandas as pd
import numpy as np

grades = pd.read_csv('CS232/Grades.csv')
grades['HW'] = [103,'Nan','NaN','NaN']
hwPercent = 0.03
labPercent = 0.20
quizPercent = 0.05
new_labs = pd.Series([125] + list(grades["labs"]), name='labs')
grades.update(new_labs)
print(grades.head())

