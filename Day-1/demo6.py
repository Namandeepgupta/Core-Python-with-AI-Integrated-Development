'''
Write a python program 
- read a employee details(name, age, cost) from <STDIN>
- using print() - display employee's details.
- calculate emp basic salary with 18% tax and display the tax
- calculate tax + basic salary and display the total salary(including tax)
'''

e_login_status = True
e_name = input("Enter employee name: ")
e_age = input(f"Enter {e_name} age: ")
e_cost = input(f"Enter {e_name} basic salary: ")

tax = float(e_cost) * 0.18 
gs = tax + float(e_cost)

print(f'''Employee Name:{e_name}
---------------------------------------
{e_name} Age is:{e_age}
---------------------------------------
{e_name} Basic Salary is:{e_cost}
---------------------------------------
{e_name} Login Status is:{e_login_status}
-----------------------------------------
Tax is:{tax}
-----------------------------------------
Total Salary is:{gs}
----------------------------------------''')