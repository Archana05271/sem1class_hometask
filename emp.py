class Employee:
    def __init__(self, emp_id, emp_name, emp_sal, emp_dept):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_sal = emp_sal
        self.emp_dept = emp_dept

    def calculate_emp_salary(self, hours_worked):
        """Calculates employee salary with overtime"""
        overtime_rate = 1.5  
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_sal / 50) * overtime_rate
            total_salary = self.emp_sal + overtime_amount
        else:
            total_salary = self.emp_sal
        return total_salary

    def print_employee_details(self):
        """Prints employee details"""
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_sal}")
        print(f"Employee Department: {self.emp_dept}")

# Create employee instances
employees = [
    Employee("E7876", "Radha", 100000, "Developer"),
    Employee("E7499", "Shiny", 45000, "Tester"),
    Employee("E7900", "David", 50000, "Analyst"),
    Employee("E7698", "Raja", 55000, "Designer")
]

# Print employee details and calculate salary for 55 hours
for emp in employees:
    emp.print_employee_details()
    print(f"Salary for 55 Hours: {emp.calculate_emp_salary(55)}")
    print()
