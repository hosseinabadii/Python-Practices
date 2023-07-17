# Async IO

Async IO is a single-threaded, single-process design: it uses **cooperative multitasking**, a term that you’ll flesh out by the end of this tutorial. It has been said in other words that async IO gives a feeling of concurrency despite using a single thread in a single process. Coroutines (a central feature of async IO) can be scheduled concurrently, but they are not inherently concurrent.

To reiterate, async IO is a style of concurrent programming, but it is not parallelism. It’s more closely aligned with threading than with multiprocessing but is very much distinct from both of these and is a standalone member in concurrency’s bag of tricks.

I’ve heard it said, “Use async IO when you can; use threading when you must.” The truth is that building durable multithreaded code can be hard and error-prone. Async IO avoids some of the potential speedbumps that you might otherwise encounter with a threaded design.

At the heart of async IO are coroutines. **A coroutine is a specialized version of a Python generator function**. Let’s start with a baseline definition and then build off of it as you progress here: a coroutine is a function that can suspend its execution before reaching `return`, and it can indirectly pass control to another coroutine for some time.

## `asyncio`

The `asyncio` package is billed by the Python documentation as a library to write concurrent code. However, async IO is not threading, nor is it multiprocessing. It is not built on top of either of these.


## Coroutine
A coroutine is a type of function that can be paused and resumed during its execution, allowing other code to be executed in the meantime. Coroutines are similar to generators, but they have some additional features that make them more powerful.

Coroutines are created using the `async def` syntax in Python 3.5 and above, which allows the function to use the `await` keyword to pause its execution until a coroutine or Future object is complete. When a coroutine is paused, it saves its state so that it can be resumed later.

One of the main benefits of coroutines is that they allow for asynchronous programming, which can make it easier to write code that performs I/O operations or interacts with external services without blocking the main thread of execution. By using coroutines and the `asyncio` library in Python, it is possible to write highly concurrent and scalable applications that can handle large amounts of I/O without using threads.

Coroutines can also be used to implement cooperative multitasking, where multiple coroutines share a single thread of execution and take turns running. This can be useful for implementing event loops or other types of non-blocking code.