# Iterator vs Iterable

An iterator is essentially a container object that implements the iterator protocol, which consists of two methods:

1. `__iter__()`: This method returns the iterator object itself.
2. `__next__()`: This method returns the next element in the collection. If there are no more elements, it raises the `StopIteration` exception.

Itrators store the state and remember the last value. 

An iterables is an object that you can get an iterator form it by using `iter()` function. For example tuple, list, string etc. are iterables. `iter(x)` is equivalent to `x.__iter()__`, that means, it calls the `__iter()__` method of that iterable object.

When you use a loop to iterate over a collection, Python automatically creates an iterator object for you behind the scenes, and then calls the `__next__()` method on that iterator object to retrieve each element in turn.

One advantage of using iterators is that they allow you to iterate over large collections of elements without having to load the entire collection into memory at once. Instead, you can retrieve each element one at a time, which can be more memory-efficient.