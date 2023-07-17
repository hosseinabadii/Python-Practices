# Threading

The traditional model of dealing with asynchronous and parallel code is the thread model. When you run a program, this starts a so-called process. A process has its own slice of memory that it gets from the operating system that's separate from other processes. Within a process, you have one or more threads. The operation system has a scheduling system that determines which processes get how much CPU time to run and switches between them automatically. So what's the difference between threads and processes? Well, as opposed to processes, threads share their memory. This means that you can perform multiple tasks concurrently that use the same memory. Especially if those tasks involve waiting for files to be loaded, or waiting for network requests to receive a response, then using threads can be very efficient because you don't have to wait for the server on the network to reply to you, but you can do something else while you wait.

While threads are a powerful tool, there are difficulties to be aware of. The first that shared memory is notorious for being the source of race condition bugs. To avoid these bugs, mutual exclusion is used (i.e. locks). However, mutual exclusion can lead to performance penalties and deadlocks if the programmer is not careful. Therefore, avoiding shared data as much as possible is typically considered best practice. Lastly, it is important to be cognizant not to overuse threads. Just because something can be run concurrently on a separate thread does not mean that you will reap performance improvements for doing so. Furthermore, there is also a performance overhead when using threads because of the context switch that the operating system must perform. Don't optimize prematurely / apply the YAGNI (You Ain't Gonna Need It) principle.

## Thread

A thread is a separate flow of execution within a program. A program can have multiple threads running concurrently, each executing a different task or function. Threads can be used to perform multiple tasks simultaneously, such as handling user input while a background process is running, or performing multiple network requests at the same time.

## Concurrency
It is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

The Python standard library has offered longstanding support through its `threading`, and `concurrent.futures` packages.

