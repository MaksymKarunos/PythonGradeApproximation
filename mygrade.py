import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Constants
average = 0.56 * 59
std = 0.23* 59
max_score = 63
list_of_grades = [52]
best_guesses = []
students = 'Solano, Stella; Sweeney, Cameron; Eshwer, Karl; Sari, Erin; Bonnelycke, Jack; Sharma, Drupit; Garza, Manuel; Tejada, Marcus; Ahrabinejad, Kaveh; Almonte, Jeremy; Gonzalez, Lenny; Alfaro, Brian; Karunos, Maksym; Tang, Guo; Cowell, Jevon; Chai, Edric; Manipon, Czarina; Al Saud, Saad; Chen, Zheming; Kepler, Abbi; Taylor, John; Arredondo, Rafael; Ramirez, Diego; Vazquez, Ruth Ann; Cardillo, Julia; Velilla, Michael; Carlson, Thomas-James; Bhiro, Tristan'
number_of_students = students.count(';')
# average 56 % ; average grade = 33.04
# stadtanrd deivation = 13.57
def fill_the_grades():
    for i in range(100000000):
        index = 0
        list_of_grades = [52,63]
        for student in range(number_of_students-2):
            list_of_grades.append(np.random.randint(7,63)) 
        if ((np.abs(np.mean(list_of_grades) - average) < 0.1) and np.abs(np.std(list_of_grades) - std) < 0.1 ):
            print('good one')
            best_guesses.append(list_of_grades)
    return best_guesses
def accurate_percentile(best_guesses, grade):
    better_than = []
    for best_list in best_guesses:
        better_than.append(my_percentile(np.array(best_list),grade))
    print(better_than)
    np_better_than = np.array(better_than)
    plt.plot(np_better_than)
    plt.show()
    return np_better_than.sum()/number_of_students
def my_percentile(np_list, grade):
    count = 0
    np_bool = np_list < grade
    for grade in np_bool:
        if grade:
            count+=1
    return count/number_of_students * 100

best_guesses = fill_the_grades()
percentile = accurate_percentile(best_guesses, 52)
list_of_grades = best_guesses[0]
np_list = np.array(list_of_grades)
print("I am better than"  + str(percentile))
print("mean is " + str(np.mean(np_list)))
print("standard deviation is " + str(np.std(np_list)))
print(list_of_grades)
plt.hist(np_list)
plt.title("Distribution of grades: midterm")
plt.xlabel("Grades")
plt.ylabel("Students")
plt.show()