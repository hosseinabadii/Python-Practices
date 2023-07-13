# Instance Methods, Class Methods, Static Methods

## Instance Methods (and Instance attributes):
In Python, instance methods are used to define behavior that is specific to instances of a class. An instance method is a method that is defined on a class and can be called on an instance of the class. 

Instance methods are typically used to access and manipulate the attributes of an instance. Using instance methods allows us to define behavior that is specific to each instance of a class, and makes it easy to encapsulate and manipulate the state of each instance.

> In Python, instance attributes are variables that are specific to each instance of a class. Instance attributes are used to store data that is specific to each instance of a class.
> Using instance attributes allows each instance of a class to have its own state and data, making it possible to create multiple instances of a class with different data.

## Class Methods (and Class Attributes):
In Python, `classmethods` are used in situations where a method needs to be defined on a class level rather than an instance level. 

A `classmethod` is a method that is bound to the class and not the instance of the class. It can be called on the class itself, rather than on an instance of the class. (Although you are able to call a `classmethod` on an instance, too!)

One common use case for `classmethods` is to provide alternative constructors for a class. For example, consider a class `Person` that is initialized with a first name and a last name. We can define a `classmethod` to create a `Person` object from a full name.

Using a `classmethod` in this way allows for greater flexibility in creating objects while still maintaining the benefits of object-oriented programming.
> In Python, a class attribute is a variable that is defined on the class level, outside of any method.
Class attributes are typically used to define constants or default values that are shared by all instances of a class.
Using class attributes allows for defining values that are shared by all instances of a class, reducing code duplication and making code more efficient.

## Static Methods:

In Python, `staticmethods` are used to define methods that are not bound to the instance or the class. They are defined on the class level, but they don't have access to the instance or the class itself. (Although you are able to call a `staticmethod` on an instance, too!)

A `staticmethod` is a method that does not receive any special first argument, such as `self` or `cls`. It can be called on the class itself, without needing to create an instance of the class. 

One common use case for `staticmethods` is to define utility functions that are related to the class but do not require access to the instance or class attributes.

Using a `staticmethod` in this way allows for greater flexibility in defining functions that are related to the class but do not require access to the instance or class attributes.