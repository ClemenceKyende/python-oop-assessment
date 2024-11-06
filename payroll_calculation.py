# Base class for employees
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

# Payroll class that manages employees
class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self):
        total_payroll = 0
        for employee in self.employees:
            # Assuming each employee has a method `calculate_salary` that returns a salary value
            total_payroll += employee.calculate_salary()
        return total_payroll

# Example usage:
# Create employees
employee1 = Employee("John Doe", 50000)
employee2 = Employee("Jane Smith", 60000)

# Create a Payroll object and add employees
payroll = Payroll()
payroll.add_employee(employee1)
payroll.add_employee(employee2)

# Calculate total payroll
print(f"Total payroll: ${payroll.calculate_total_payroll()}")
