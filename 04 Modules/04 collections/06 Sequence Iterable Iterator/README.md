# `collections` Module

This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, `dict`,
`list`, `set`, and `tuple`.

| Name          | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| `namedtuple`  | factory function for creating tuple subclasses with named fields     |
| `deque`       | list-like container with fast appends and pops on either end         |
| `ChainMap`    | dict-like class for creating a single view of multiple mappings      |
| `Counter`     | dict subclass for counting hashable objects                          |
| `OrderedDict` | dict subclass that remembers the order entries were added            |
| `defaultdict` | dict subclass that calls a factory function to supply missing values |
| `UserDict`    | wrapper around dictionary objects for easier dict subclassing        |
| `UserList`    | wrapper around list objects for easier list subclassing              |
| `UserString`  | wrapper around string objects for easier string subclassing          |

## `collections.abc` Module

The `collections.abc` module defines abstract base classes (ABCs) for the
container types provided in the `collections` module:

### `collections.abc.Iterable`

An `Iterable` is an object that can be used in a `for` loop.

```python
class Iterable(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterable:
            return _check_methods(C, "__iter__")
        return NotImplemented

    __class_getitem__ = classmethod(GenericAlias)
```

### `collections.abc.Iterator`

An `Iterator` is an object that returns items from an `Iterable` when
`__next__` is called.

```python
class Iterator(Iterable):

    __slots__ = ()

    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            return _check_methods(C, '__iter__', '__next__')
        return NotImplemented
```
