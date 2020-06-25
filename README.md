### Generator pipeline to efficiently process large CSV files
## Note
### Generator
    - Introduced with PEP 255, generator functions are a special kind of function that return a lazy iterator. 
    - Lazy iterators do not store their contents in memory. 
    - Using yield will result in a generator object and Using return will result in the first line of the file only.
    - Two primary ways of creating generators: by using generator functions and generator expressions
    - Generator functions use the Python yield keyword instead of return.
    - If the list is smaller than the running machine’s available memory, then list comprehensions can be faster to evaluate than the equivalent generator expression.
### Yield
    - On the whole, yield is a fairly simple statement. Its primary job is to control the flow of a generator function in a way that’s similar to return statements. 
    - Use .send() to send data to a generator
    - Use .throw() to raise generator exceptions
    - Use .close() to stop a generator’s iteration

Link: https://realpython.com/introduction-to-python-generators/#using-generators
