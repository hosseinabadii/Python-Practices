# Iterator vs Iterable

An iterator is essentially a container object that implements the iterator protocol, which consists of two methods:

1. `__iter__()`: This method returns the iterator object itself.
2. `__next__()`: This method returns the next element in the collection. If there are no more elements, it raises the `StopIteration` exception.

Itrators store the state and remember the last value. 
When you want to use iterators, you will do the following:
- Define a class with `__iter__()` and `__next__()` methods.
- Instantiate an iterable object from your class.
- Use `iter()` function with your iterable object to convert it to an iterator object.
- Call `next()` function on the iterator object when you want.

An iterable is an object that you can get an iterator form it by using `iter()` function. For example tuple, list, string etc. are iterables. `iter(x)` is equivalent to `x.__iter()__`, that means, it calls the `__iter()__` method of that iterable object.

You can also use `iter()` function with all built-in iterable objects to get an iterator object, then call `next()` with that iterator object when you want.

For example:
```python
iterable_object = (10, 20, 30, 40)
iterator_object = iter(iterable_object)

next(generator_object)
next(generator_object)
next(generator_object)
.
.
.
```

# Generators

When you want to use generators, you will do the following:
- Define a function with `yield` statement(generator).
- Get the output of that function, which is a generator object.
- Call `next()` function on the generator object when you want.

For example:

```python
def generator_fuction(x):
    for num in range(x):
        power_two = num ** 2
        yield power_two

generator_object = generator_function(10)

next(generator_object)
next(generator_object)
next(generator_object)
.
.
.

```
You can also use generator expressions to create a generator object. 

For example:

```python
generator_object = (num ** 2 for num in range(10))

next(generator_object)
next(generator_object)
next(generator_object)
.
.
.
```
# Conclusion

One advantage of using iterators and generators is that they allow you to iterate over large collections of elements without having to load the entire collection into memory at once. Instead, you can retrieve each element one at a time, which can be more memory-efficient.