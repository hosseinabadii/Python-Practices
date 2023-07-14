# What is encapsulation?

The first meaning of **encapsulation** is that we group things so that each group represents the essential features of something. For example, "a company's culture document encapsulates the company's beliefs, values and practices". Or, "a customer class encapsulates the data that we consider to be essential for representing a customer".

The second meaning of encapsulation is that is defines boundaries around things. So encapsulation in that sense is about restricting access. In your code, you can do that by defining protected or private instance variables or methods as protected or private. Even though Python is a bit special in that doesn't actually restrict access.

There's another aspect related to encapsulation, which is information hiding. This is slightly different. With information hiding, you hide certain aspects of your code from the outside. And then you provide an interface to that code using functions, classes, and modules that form a black box that other parts of your program can use without knowing anything about the inner workings.

What's really interesting is how encapsulation and information hiding are related to design principles. Encapsulation, providing boundaries, is closely related to cohesion. By encapsulating things, providing boundaries and grouping things together, you're making them more cohesive. Information hiding on the hand helps to reduce coupling. Information hiding removes dependencies by introducing abstraction layers. In short, both encapsulation and information hiding are going to help you improve your design by increasing cohesion and reducing coupling.
