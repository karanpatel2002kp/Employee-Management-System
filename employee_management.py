class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary


# Store employees
employees = []


# 1. Add Employee
def add_employee():
    emp_id = int(input("Enter Employee ID: "))

    # Check duplicate ID
    for emp in employees:
        if emp.emp_id == emp_id:
            print("Employee ID already exists!")
            return

    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))

    employee = Employee(emp_id, name, salary)
    employees.append(employee)

    print("Employee added successfully!")


# 2. Display Employees
def display_employees():
    if not employees:
        print("No employees found!")
        return

    for emp in employees:
        print("--------------------")
        print("ID:", emp.emp_id)
        print("Name:", emp.name)
        print("Salary:", emp.salary)


# 3. Update Salary
def update_salary():
    emp_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp.emp_id == emp_id:
            new_salary = float(input("Enter New Salary: "))
            emp.salary = new_salary
            print("Salary updated successfully!")
            return

    print("Employee not found!")


# 4. Search Employee
def search_employee():
    emp_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp.emp_id == emp_id:
            print("Employee Found!")
            print("ID:", emp.emp_id)
            print("Name:", emp.name)
            print("Salary:", emp.salary)
            return

    print("Employee not found!")


# 5. Check Salary Status
def check_salary():
    emp_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp.emp_id == emp_id:
            if emp.salary >= 30000:
                print("Good Salary")
            else:
                print("Low Salary")
            return

    print("Employee not found!")


# 6. Delete Employee
def delete_employee():
    emp_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            print("Employee deleted successfully!")
            return

    print("Employee not found!")


# 7. Main Menu
while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Salary")
    print("4. Search Employee")
    print("5. Check Salary Status")
    print("6. Delete Employee")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employees()

    elif choice == "3":
        update_salary()

    elif choice == "4":
        search_employee()

    elif choice == "5":
        check_salary()

    elif choice == "6":
        delete_employee()

    elif choice == "7":
        print("Thank you for using Employee Management System!")
        break

    else:
        print("Invalid choice.")
