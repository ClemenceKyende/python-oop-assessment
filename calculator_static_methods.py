class Calculator:
    count = 0  # Static attribute to track method calls

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# Demonstrating static method and static attribute
result = Calculator.add(10, 5)
print("Result:", result)
print("Add method called:", Calculator.count, "time(s)")
