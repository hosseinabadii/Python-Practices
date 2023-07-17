# Threading
It is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL.

## Thread

A thread is a separate flow of execution within a program. A program can have multiple threads running concurrently, each executing a different task or function. 

Threads can be used to perform multiple tasks simultaneously, such as handling user input while a background process is running, or performing multiple network requests at the same time.

## Concurrency
It is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

The Python standard library has offered longstanding support through its `threading`, and `concurrent.futures` packages.

