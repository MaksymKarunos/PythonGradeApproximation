import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

grades = pd.read_csv('CS232/Grades.csv')
grades['HW'] = pd.Series([95])
hwPercent = 0.03
labPercent = 0.20
quizPercent = 0.05
grades['labs_weighted'] = grades['labs'].mean() * 0.2
grades['labs_weighted'].iloc[1:5] = 0
grades['quiz_avg'] = grades['quiz'] * 0.05
grades['homework_avg'] = grades['HW'] * 0.03
grades['midterm_avg'] = 100 * 0.2 * grades['midterm']/(60) 
grades['final_grade'] = (grades.iloc[:,-4:].sum(axis=1)/0.48)
print('The final grade is: ' + str(grades['final_grade'].iloc[0]))
#print(grades)
#grades = grades.fillna(0)
lab_grades = grades['labs']
lab_df = pd.DataFrame(lab_grades)
lab_df.columns = ['labs']
lab_df['lab_number'] = [i+1 for i in range(5)]
lab_df['team_size'] = [1 if i < 2 else 2 for i in range(5) ]
lab_df.to_csv('CS232/lab_df.csv')
print(lab_df)
sns.set_style('whitegrid') 
sns.lmplot(y ='labs', x ='lab_number', data = lab_df)
plt.show()
# plt.plot(lab_grades)
# plt.xlabel("Lab number")
# plt.ylabel("Grade")
# plt.title("Grades vs lab numbers")
# plt.show()
#dataset.head()