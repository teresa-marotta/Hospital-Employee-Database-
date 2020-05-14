import csv, sqlite3 
from staff import Employee

con = sqlite3.connect('employee.db')
cur = con.cursor()

# cur.execute("CREATE TABLE employees (first, last, dept, pay, ext);") # use your column names here

# with open('info.csv','r') as fin: # `with` statement available in 2.5+
#     # csv.DictReader uses first line in file for column headings by default
#     dr = csv.DictReader(fin) # comma is default delimiter
#     to_db = [(i['first'], i['last'], i['dept'], i['pay'], i['ext']) for i in dr]

# cur.executemany("INSERT INTO employees (first, last, dept, pay, ext) VALUES (?, ?, ?, ?, ?);", to_db)

#Functions 
def insert_emp(emp):
  with con:  
    cur.execute("INSERT INTO employees VALUES (:first, :last, :dept, :pay, :ext)", {'first': emp.first, 'last': emp.last, 'dept': emp.dept, 'pay': emp.pay, 'ext': emp.ext}) 


def get_emps_by_name(lastname):
    cur.execute("SELECT * FROM employees WHERE last=:last",{'last': lastname})
    return cur.fetchall() 


def update_pay(emp, pay):
    with con:
        cur.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with con:
        cur.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

def get_all_emps():
    with con: 
      cur.execute("SELECT * FROM employees")
      print(cur.fetchall())

#Begining of the Information to be Displayed
print('Welcome to the Riverview Staff Database')
print('\n')

#Total List of Employees
answer = input("Would you like to see the current list of employees(Y/N): ")

while answer != "Y" and answer != "N": 
    answer = input("Please enter a valid answer (Y/N): ")

if answer == "Y": 
  get_all_emps()
else: 
  print("Thank you for your response.")

print('\n')

#Specific Employee Search 
answer_2 = input("Would you like to search for a specific employee?(Y/N): ")

while answer_2 != "Y" and answer != "N": 
    answer_2 = input("Please enter a valid answer (Y/N): ")

if answer_2 == "Y": 
  given_name = input("What is the last name of the employee?: ")
  emps = get_emps_by_name(given_name)
  print(emps)
else:
  print("Thank you for your response.")

print('\n')

#Add an Employee to the Database
answer_3 = str(input("Would you like to add an employee to the database?(Y/N): "))

while answer_3 != "Y" and answer != "N": 
    answer_3 = input("Please enter a valid answer (Y/N): ")

if answer_3 == "Y": 
  new_first = input("First name: ")
  new_last = input("Last name: ")
  new_dept = input("Department: ")
  new_pay =  input("Pay: ")
  new_ext = input("Extension: ")

  new_emp = Employee(new_first, new_last, new_dept, new_pay, new_ext)

  insert_emp(new_emp)
else: 
  print("Thank you for your response.")


# emp_1 = Employee("Joan", "Grant", "OR", "83000", "29380")
# insert_emp(emp_1)

emp_check = get_emps_by_name('Grant')
print(emp_check)


con.commit()
con.close()

