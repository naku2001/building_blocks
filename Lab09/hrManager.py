#Author: Perfect-Princess Makuwerere
#Date: April 14, 2026
#Description: Functional logic to manage employees and calculate total payroll.

from Worker import Worker
from Supervisor import Supervisor

def calcTotalPay(employee_list):
    """
    Calculates total pay for all employees assuming 40 hours.
    """
    total = 0.0
    for emp in employee_list:
        total += emp.calcPay(40)
    return total

def listEmployees(employee_list):
    """
    Outputs employee information using isinstance to handle types.
    """
    for emp in employee_list:
        print(f"Name: {emp.get_name()}")
        print(f"ID: {emp.get_id_number()}")
        print(f"Pay Rate: ${emp.get_pay_rate():.2f}")
        
        if isinstance(emp, Worker):
            shift_name = "Day Shift" if emp.get_shift() == 1 else "Night Shift"
            print(f"Shift: {shift_name}")
        elif isinstance(emp, Supervisor): 
             print(f"Level: {emp.get_level()}")
        

def main():
    employees = [] 
    try:
        num_emp = int(input("How many employees would you like to add: "))
    except ValueError:
        print("Invalid input.")
        return

    count = 0
    while count < num_emp:
        choice = input("Would you like to add a worker or a supervisor: ").lower().strip() 
        
        if choice == "supervisor":
            name = input("Please enter the name of the supervisor: ") 
            emp_id = input("Please enter the id of the supervisor: ")
            rate = float(input("Please enter the pay rate of the supervisor: "))
            level = int(input("Please enter the level of the supervisor: "))
            employees.append(Supervisor(name, emp_id, rate, level))
            count += 1
        elif choice == "worker":
            name = input("Please enter the name of the worker: ") 
            emp_id = input("Please enter the id of the worker: ") 
            rate = float(input("Please enter the pay rate of the worker: ")) 
            shift = int(input("Please enter the shift of the worker (1 for day, 2 for night): ")) 
            employees.append(Worker(name, emp_id, rate, shift))
            count += 1
        else:
            print(f"{choice} is not a worker or supervisor. Try again!")

    listEmployees(employees) 
    total_payroll = calcTotalPay(employees)
    print(f"The total cost of all of the worker's pay is ${total_payroll:.2f}") 

if __name__ == "__main__":
    main() 