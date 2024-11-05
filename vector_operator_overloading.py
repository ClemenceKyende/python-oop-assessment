class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Testing operator overloading
vector1 = Vector(2, 3)
vector2 = Vector(4, 5)
vector3 = vector1 + vector2
print("Result of vector addition:", vector3)
