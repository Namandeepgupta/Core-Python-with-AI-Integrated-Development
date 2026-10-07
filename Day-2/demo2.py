'''
Given a List
Emp = ['101, john, sales, 1000', '102, ram, prod, 2000', '103, raju, hr, 3000', '104, bibu, sales, 4000']
- iterate a emp list
- split each element of the list using ',' as a delimiter
- display empName in title case and emp department in upper case 
- calculate sum of emp salary and display the total salary
'''

Emp = ['101, john, sales, 1000', '102, raam, prod, 2000', '103, raju, hr, 3000', '104, bibu, sales, 4000']

total = 0
for var in Emp:
    e_id, e_name, e_dept, e_cost = var.split(',')

    print(f"Emp Name : {e_name.title()}\t Emp Dept : {e_dept.upper()}") # display empName in title case and emp department in upper case
    total = total + int(e_cost)
    
print(f"\nTotal Salary : {total}") # display the total salary
