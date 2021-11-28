# Object Orientated Programming in Python

print("Object Orientated Programming Practice\n")


# Classes and Objects

print("Classes and Objects\n")

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)


# Create students
s1 = Student("Marie", 13, 93)
s2 = Student("Claire", 14, 68)
s3 = Student("Tom", 13, 82)
s4 = Student("John", 15, 60)
s5 = Student("Lilly", 14, 74)

# Create course
course = Course("Math", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(f'The first student of {course.name} is: {course.students[0].name}')
# The first student of Math is: Marie
print(f'The average grade of {course.name} students is: {course.get_average_grade()}')
# The average grade of Math students is: 81.0


# Class attributes

print("\nClass attributes\n")

class Person:
    people = 1 # Class attribute
    number_of_legs = 2
    # This class attributes are exportable with the classes

    def __init__(self,name):
        self.name = name

p1 = Person("melisa")
p2 = Person("mariano")

print(p1.people) # 1
print(Person.people) # 1

Person.people = 2

print(p1.people) # 2
print(Person.people) # 2

# Redefine Person class
class Person:
    people = 0 # Class attribute

    def __init__(self,name):
        self.name = name
        Person.people += 1

p1 = Person("Melisa")
print(Person.people) # 1

p2 = Person("Mariano")
print(Person.people) # 2


# Class methods

print("\nClass methods\n")

class Person:
    people = 0 # Class attribute

    def __init__(self,name):
        self.name = name
        Person.add_person() # Use the class method

    @classmethod #decorator
    def number_of_people(cls): # Class method: acts on the class itself
        return cls.people

    @classmethod #decorator
    def add_person(cls): # Class method
        cls.people += 1

p1 = Person("Melisa")
print(Person.number_of_people()) # 1

p1 = Person("Mariano")
print(Person.number_of_people()) # 2

p3 = Person("Azul")
p4 = Person("Carlos")

print(Person.number_of_people()) # 4


# Class static methods

print("\nClass static methods\n")

# Work well in classes that organize functions together
class Math:
    @staticmethod # They do sth but don't change anything
    def add(x, y):
        "It adds x to y"
        return x + y

    @staticmethod
    def substract(x, y):
        "It substracts y from x"
        return x - y

    @staticmethod
    def multiply(x, y):
        "It multiply x and y"
        return x * y


print(Math.add(10,5)) # 15
print(Math.substract(10,5)) # 5
print(Math.multiply(10,5)) # 50



# Inheritance

# Inheritance is the ability of one class to inherit the attributes 
# and methods of another, since pre-existing, something that allows us to reuse code

print("\nInheritance\n")

# Super Class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def presentation(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print("I don't speak")

# Subclasses
class Dog(Animal):
    def __init__(self, name, age, kind):
        super().__init__(name, age) # No need to overwrite the whole thing
        self.kind = kind

    def speak(self):
        print("Guau")

    def presentation(self): #polymorphism: we overwrite the presentation method and change to another form
        print(f'I am a {self.kind}, my name is {self.name} and I am {self.age} years old')


class Cat(Animal):
    def speak(self):
        print("Meow")

class Turtle(Animal):
    pass
    
# Create objects
a = Animal("Pongo", 10)
a.presentation() # I am Pongo and I am 10 years old

c = Cat("Nina", 4)
c.presentation() # I am Nina and I am 4 years old
#Cat doesn't have presentation method but it inharited from Animal
c.speak() # Meow

d = Dog("Nigeria", 5, "dog")
d.presentation() # I am a dog, my name is Nigeria and I am 5 years old
# Dog has the presentation method and overwrites the Animal presentation method
d.speak() # Guau

t = Turtle("Roma", 30)
t.presentation() # I am Roma and I am 30 years old
t.speak() # I don't speak

# Multiple Inheritance 
# When the subclass has more than one parent and it inherits from all of the parents


# Abstraction

# An abstract method is a method which only has declaration and doesn't have definition.
# An abstract class has at least one abstract method
# When you inherit an abstract class as a parent to the child class, the child class
# should define all the abstract method present in parent class.
# If it is not done then child class also becomes abstract class automatically.
# Python doesn't support abstract classes so we import abc module
# to create abstract classes and to use the decorator abstractmethod

print("\nAbstraction\n")

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        print("I prefer working with ", end="")

class Desktop(Computer):
    def definition(self):
        print("I am a desktop")

    def process(self):
        super().process()
        print("desktops")

class Laptop(Computer):
    def definition(self):
        print("I am a laptop")

    def process(self):
        super().process()
        print("laptops")

class Tablet(Computer):
    def definition(self):
        print("I am a tablet")

    def process(self):
        super().process()
        print("tablets")

class Programmer:
    def work(self, computer):
        print("I am a programmer who writes code and solves bugs")
        computer.process()


d = Desktop()
d.definition() # I am a desktop

l = Laptop()
l.definition() # I am a laptop

t = Tablet()
t.definition() # I am a tablet

# Abstract classes define a common methods and attributes to all subclasses. 
# We skip duplicated code.

programmer1 = Programmer()
programmer1.work(d) # I am a programmer who writes code and solves bugs
                    # I prefer working with desktops

programmer2 = Programmer()
programmer2.work(l) # I am a programmer who writes code and solves bugs
                    # I prefer working with laptops

programmer3 = Programmer()
programmer3.work(t) # I am a programmer who writes code and solves bugs
                    # I prefer working with tablets


# Polymorphism

# The ability to take mutiple forms
# Change from one form to another


print("\nPolymorphism\n")

class Language():
    def __init__(self, language):
        self.language = language

    def which_language(self):
        print(f'This is {self.language} language')

    def say_hello(self):
        print("I don't speak this language")

class French(Language):
    def say_hello(self): # Overwrite say_hello() and change form
        print("In French hello is: Bounjour")

    def say_thanks(self):
        print("In French thanks is: Merci")

class Chinese(Language):
    def say_hello(self):
        print("In Chinese hello is: 你好")

    def say_thanks(self):
        print("In Chinese thanks is: 谢谢")


def choose_language(lang):
    lang.say_hello()

french = French("French")
chinese = Chinese("Chinese")

french.which_language() # This is French language
french_hello = choose_language(french) # In French hello is: Bounjour
french_thanks = french.say_thanks() # In French thanks is: Merci

chinese.which_language() # This is Chinese language
chinese_hello = choose_language(chinese) # In Chinese hello is: 你好

spanish = Language("Spanish") 
spanish.which_language() # This is Spanish language
spanish_hello = choose_language(spanish) # I don't speak this language


# Encapsulation

# It refers to wrapping up of data under a single unit.
# Encapsulating consists of making the attributes or methods internal to 
# a class cannot be accessed or modified from outside, just the object itself can access them. 
# Protective shield that prevents data from being acces by the code outside the shield


print("\nEncapsulation\n")

class Course:
    def __init__(self):
        self.course = "OOP Course"        
        self.language = "Python"

    def CourseName(self):
        print(self.language, self.course)

mycourse = Course()
print(mycourse.language) # Python
mycourse.CourseName() # Python OOP Course

# If we want to hide the language, change to __language to make it private:

class Course:
    def __init__(self):
        self.course = "OOP Course"        
        self.__language = "Python"

    def CourseName(self):
        print(self.__language, self.course)

mycourse = Course()
# print(mycourse.__language) # AttributeError: 'Course' object has no attribute '__language'

# The way to access to the private attribute
print(mycourse._Course__language) # Python


# Setter and Getter

# Getters have the functions that allow us to access a private variable. In Python
# they are declared by creating a function with the @property decorator.

# Setters correspond to the functions that we use to overwrite the information of a
# variable and is generated by defining a method with the name of the variable and
# using as decorator the name of the variable plus .setter.


class Course:
    def __init__(self):
        self.course = "Machine Learning Course"        
        self.__language = "Python"

    def CourseName(self):
        print(self.__language, self.course)

    #Getter
    @property #decorator. We are defining out language as a method but access like an attribute
    def get_language(self):
        return self.__language
        
    #Setter
    @get_language.setter
    def set_language(self, language):
        self.__language = language

mycourse = Course()
# We call set_language as an attribute not a method
# Python changes to R
mycourse.set_language = "R" 
mycourse.CourseName() # R Machine Learning Course