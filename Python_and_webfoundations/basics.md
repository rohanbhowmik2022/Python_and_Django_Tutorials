Class Inheritance in Python allows a class to inherit attributes and methods from another class known as parent class

We can use super() in Python to call a method from the parent class allowing us to modify or extend inherited behaviour

### Define a Class in Python
--------------------------

class Employee:
    def __init__(self, name, age):
    self.name = name
    self.age = age

If we want to store each employee as a seperate list like:

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spork", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2256]

Issues with this approach
1. First It makes larger code files difficult to manage Like if you reference kirk[0] several lines away from where you declared the kirk list
2. It introduces errors if employees don't have the same number of elements in their respective list 

To make the code manageable and more maintainable is to use classes

### Classes vs Instances
--------------------
Classes -> Allows you to create user defined structures. It defines methods which identify the behaviours and actions that an object created from the class can perform with its data.

With the class as the blueprint, an instance is an object that's built from a class and contains real data. An instance of the Dog is not a blueprint anymore. Its an actual dog with a name like Mike who's four years old.

In simple terms, a class is like a form or questionnaire. An instance is like a form that you have filled out with information. Just like many people can fill out the same form with their own unique information we can create many instances from a single class.

Note: Python class names are written in CapitalizedWords notation by covention. For example, a class for a specific breed of dog, like Jack Russell Terrier, would be written as JackRussellTerrier.

__init__() -> Accepts any number of parameters but the first parameter will always be a variable called self
When we create a new class instance then Python automatically passes the instance to the self parameter in .__init__() so that Python can define the new attributes on the object.

self.name = name -> creates an attribute called name and assigns the value of the parameter to it.
self.age = age -> creates an attribute called age and assigns the value of the age paramter to it

Attributes created in .__init__() are called instance attributes. 
All objects have an name and age but the values for the name and age attributes will vary depending on the Dog instance

### How do we inherit from another class in Python?
-----------------------------------------------

class Parent:
    hair_colour = 'brown'

class Child(Parent):
    pass

Child classes can override or extend the attributes and methods of parent classes. In other words, child classes inherit all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.

Although the analogy isn’t perfect, you can think of object inheritance sort of like genetic inheritance.

You may have inherited your hair color from your parents. It’s an attribute that you were born with. But maybe you decide to color your hair purple. Assuming that your parents don’t have purple hair, you’ve just overridden the hair color attribute that you inherited from your parents:

You also inherit, in a sense, your language from your parents. If your parents speak English, then you’ll also speak English. Now imagine you decide to learn a second language, like German. In this case, you’ve extended your attributes because you’ve added an attribute that your parents don’t have:

class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")

