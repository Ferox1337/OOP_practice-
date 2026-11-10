# OOP_practice.py
# Basic Object-Oriented Programming practice

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

if __name__ == "__main__":
    student1 = Student("Alice", 20)
    print(student1.introduce())

