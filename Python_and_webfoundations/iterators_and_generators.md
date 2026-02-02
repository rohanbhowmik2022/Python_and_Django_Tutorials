Iterators -> Control Loops allows us to traverse arbitary data containers one time at a time.
Iterables -> Provide the data that we want to iterate over

1. Python iterators are objects with .__iter__() and .__next__() methods.
2. Iterables are objects that can return an iterator using the .__iter__() method.
3. Generator functions use the yield statement to create generator iterators.
4. Asynchronous iterators use .__aiter__() and .__anext__() for async operations.
5. Iterators are memory-efficient and can handle infinite data streams.

What Is the Python Iterator Protocol?
A Python object is considered an iterator when it implements two special methods collectively known as the iterator protocol. These two methods make Python iterators work. So, if you want to create custom iterator classes, then you must implement the following methods:

Method	                                    Description
.__iter__()     |	Called to initialize the iterator. It must return an iterator object.
.__next__()	    |   Called to iterate over the iterator. It must return the next value in the data stream.

An iterator is an object that:
> Implements __iter__() and __next__()
> Returns one value at a time
> Remembers its state

### Iterator vs Generator (Side-by-Side)
--------------------------------------
Feature	            Iterator	Generator
-------------------------------------------
Code length	        Longer	    Short
State handling	    Manual	    Automatic
Uses yield	        ❌	       ✅
Uses __next__()	    ✅	       ❌
Memory efficient	✅	       ✅

### Why Use Iterators & Generators?
--------------------------------
✔ Handle large data without loading everything into memory
✔ Perfect for streams, files, logs, APIs
✔ Clean and readable code
✔ Widely used in Django, DRF, DevOps scripts