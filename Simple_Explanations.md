## __add__ vs __repr__ vs __str__ simply explained

__add__ is a special method in Python classes that allows for custom implementation of the "+" operator. 
This is used for adding two instances of a class together.

__repr__ is another special method that returns a string representation of an object. 
This is used for debugging and development, and is expected to be a representation that, if passed to eval(), would create an equivalent object.

__str__ is a special method that returns a human-readable string representation of an object. 
This is what is printed to the console when you call print on an object, or use the str() function. 
If __str__ is not defined in a class, Python will fall back to __repr__.

---

## why is __add__ used? Give an example

__add__ is used when you want to define the behavior of the "+" operator for instances of your class. 
For example, let's say you have a class Point that represents a point in 2D space with x and y coordinates:

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)  # 4 6

```
---

## why are __repr__ vs __str__ used? Give an example

__repr__ and __str__ are used in Python to define the human-readable and unambiguous string representation of an object.

__repr__ should return a string that, when passed to eval(), would create an object that is equal to the original. It is intended to be unambiguous, and is used for debugging and development purposes.

__str__ should return a string that is a more human-readable representation of the object. 
It is intended to be used as a display string, for example when printing the object to the console.

For example, let's say you have a class Person that represents a person, with attributes name and age.

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self):
        return f"{self.name}, {self.age} years old"

```
When you create an instance of the Person class:

```
person = Person("Alice", 30)

```

And print it using the print() function, the output would be:

Alice, 30 years old

And if you type the name of the instance in the interactive prompt:

```
>>> person
Person(name='Alice', age=30)

```

---

## Use __add__ to add 2 numbers in python

In Python, the + operator is used to add two numbers. For example:

```
x = 5
y = 10
result = x + y
print(result) # 15

```

If you want to use the __add__ method to add two objects, you need to define it in the object's class. For example:

```
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)

x = MyNumber(5)
y = MyNumber(10)
result = x + y  #Aqui crias a class "result" que é a soma das classes x e y
print(result.value) # 15


```

## why we use  __add__ to add 2 objects

The __add__ method is used to define the behavior of the + operator when it is applied to objects of a custom class. 

By defining __add__, you can specify how two objects of that class should be added together. 

This allows you to create more complex and sophisticated objects, such as numbers with units, for example, that can be added and subtracted in a way that makes sense for your specific use case.



