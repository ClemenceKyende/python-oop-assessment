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
