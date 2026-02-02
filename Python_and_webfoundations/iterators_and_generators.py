#Custom Iterator Example

#Example: Iterator that counts numbers

class CountIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
    
# Using the iterator
counter = CountIterator(1, 5)
for numbers in counter:
    print(numbers)


# Generator Functions Example

def count_generator(start, end):
    while start <= end:
        yield start
        start += 1

for number in count_generator(1, 5):
    print(number)