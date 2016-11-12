#Write a version of the employee database example using shelve instead of SQLite.
#Populate the shelf with the sample data and write a function that lists the name of all employees earning more than a specifi ed amount.
#Create a fi le containing the following code (located in Exercise3_2.py in the Solutions folder of the .zip file):
###

import shelve


#'ID', 'Name', 'HireDate', 'Grade', 'ManagerID'
employees = [
['1','John Brown', '2006‐02‐23', 'Foreman', ''],
['2','Fred Smith', '2014‐04‐03', 'Laborer', '1'],
['3','Anne Jones', '2009‐06‐17', 'Laborer', '1'],
]

#'Grade','Amount'
salaries = [
['Foreman', 60000],
['Laborer', 30000]
]

def createDB(data, shelfname):
 try:
 shelf = shelve.open(shelfname,'c')
 for datum in data:
 shelf[datum[0]] = datum
 finally:
 shelf.close()
 
def readDB(shelfname):
 try:
 shelf = shelve.open(shelfname,'r')
 return [shelf[key] for key in shelf]
 finally:
 shelf.close()
 
def with_salary(n):
 grades = [salary[0] for salary in readDB('salaryshelf') if salary[1] >= n]
 for staff in readDB('employeeshelf'):
 if staff[3] in grades:
 yield staff
 
def main():
 print('Creating data files...')
 createDB(employees, 'employeeshelf')
 createDB(salaries, 'salaryshelf')
 print('Staff paid more than 30000:')
 for staff in with_salary(30000):
 print(staff[1])
 print('Staff paid more than 50000:')
 for staff in with_salary(50000):
 print(staff[1])
 
if __name__ == "__main__": main()
