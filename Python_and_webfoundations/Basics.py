# Python Object-Oriented Programming

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

emp_1 = Employee('Emon','24') #Instances of a class - Contains data 
emp_2 = Employee('Sneha',25) #Instances of a class

print(emp_1)
print(emp_2)
print(emp_1 != emp_2)

#Inheritance Example

#Parent -> Dog

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


