# class-Is a blueprint of an object
# object-Is an instance of that class
# method-a function that is being associated with an object
# constructor-this is a must to have.
#Every class should have a constructor

class fruits:     #fruits is a class
    def __init__(self,type,price,color):  #def init is a constructor
        self.type=type
        self.price=price
        self.color=color

    def onyesha(self):   #This is a method
        print(f"I like eating {self.type} and it costs {self.price}, color being {self.color}")

#Creating an object
myobj1=fruits("bananas","Kshs.20", "Yellow")
myobj2=fruits("mangoes","Kshs.40","green")

myobj1.onyesha()
myobj2.onyesha()

# Class: A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that objects of the class will have. For example, a "Person" class might have attributes like name and age, along with methods like "speak" or "walk."

# Object: An object is an instance of a class. It is a concrete representation of the class, with its own set of attribute values. For example, if "Person" is a class, then "Alice" and "Bob" can be objects of that class.

# Encapsulation: Encapsulation is the concept of bundling the data (attributes) and the methods (functions) that operate on the data into a single unit, i.e., a class. It also involves controlling the access to data by defining access modifiers (public, private, protected).

# Inheritance: Inheritance is a mechanism that allows a class to inherit the properties and behaviors (attributes and methods) of another class. The class that is inherited from is called the base class or superclass, and the class that inherits is called the derived class or subclass.

# Polymorphism: Polymorphism allows objects of different classes to be treated as objects of a common base class. It is the ability to present the same interface for different data types. This can be achieved through method overriding and interfaces/abstract classes.

# Abstraction: Abstraction is the process of simplifying complex reality by modeling classes based on the essential properties and behaviors of an object, while hiding the irrelevant details. It provides a high-level view of an object, hiding its internal complexities.

# Method Overriding: Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This is useful for customizing behavior in the derived class.

# Constructor: A constructor is a special method in a class that gets called when an object is created. It is typically used to initialize the object's attributes. In Python, the constructor method is named
# __init__
# .

# Getter and Setter Methods: Getter methods (accessors) are used to retrieve the values of an object's attributes, while setter methods (mutators) are used to modify the values of the attributes. They are often used to implement encapsulation and control access to attributes.

# Composition: Composition is a way to create complex objects by combining simpler objects or components. It allows you to build objects that have a "has-a" relationship with other objects.

# Association: Association represents a relationship between two or more classes. It can be a simple association (one class uses another), aggregation (a whole-part relationship), or composition (stronger form of aggregation, where one class is part of another).