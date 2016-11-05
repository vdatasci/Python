#Let’s say we want to find the final grades for 3 girls, and we know what their averages are for tests, projects, homework, and quizzes.
#We also know that tests are 40% of the grade, projects 15%, homework 25%, and quizzes 20%.

#Student, Tests, Projects, Homework, Quizzes
#Alexandra, 92, 100, 89, 80
#Megan, 72, 85, 80, 75
#Brittney, 88, 78, 85, 92

#type, weight
#Tests, 40%
#Projects, 15%
#Homework, 25%
#Quizzes, 20%

###
import numpy as np

a = np.array([[92,100,89,80],[72,85,80,75],[88,78,85,92]])
b = np.array([.4,.15,.25,.20])
x = np.dot(a,b)
x
