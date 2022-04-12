# Task 1

import time

def measure_time(func):
    def inner_function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start
    return inner_function

# Usage 

if __name__ == "__main__":
    
    print('measure_time usage example:')
    
    @measure_time
    def some_function(a, b, c, d, e=0, f=2, g='3'):
        time.sleep(a)
        time.sleep(b)
        time.sleep(c)
        time.sleep(d)
        time.sleep(e)
        time.sleep(f)
        return g
    
    some_function(1, 2, 3, 4, e=5, f=6, g= '9999')

# Task 2

def function_logging(func):
    def inner_function(*args, **kwargs):
        name = func.__name__
        kwarg_str = ''
        if kwargs:
            for i in kwargs:
                kwarg_str += f'{i}={kwargs[i]}, '
        kwarg_str = kwarg_str[0:-2]
        if not args:
            if not kwargs:
                print(f'Function {name} is called with no arguments')
            else:
                print(f'Function {name} is called with keyword arguments: {kwarg_str}')
        else:
            if not kwargs:
                print(f'Function {name} is called with positional arguments: {args}')
            else:
                print(f'Function {name} is called with positional arguments: {args} and keyword arguments {kwarg_str}')
        result = func(*args, **kwargs)
        print(f'Function {name} returns outpur of type {type(result).__name__}')
        return result
    return inner_function

# Usage

if __name__ == "__main__":
    
    print('function_logging usage example:')
    
    @function_logging
    def func1():
        return set()
    
    @function_logging
    def func2(a, b, c):
        return (a+b)/c
    
    @function_logging
    def func3(a, b, c, d=4):
        return [a + b * c] * d
    
    @function_logging
    def func4(a=None, b=None):
        return {a: b}
    
    print(func1(), end='\n\n')
    print(func2(1, 2, 3), end='\n\n')
    print(func3(1, 2, c=3, d=2), end='\n\n')
    print(func4(a=None, b=float('-inf')), end='\n\n')
    
# Task 3

import random

def russian_roulette_decorator(probability, return_value):
    def decorator(func):
        def inner_func(*args, **kwargs):
            if random.random() < probability:
                return return_value
            else:
                return func(*args, **kwargs)
        return inner_func
    return decorator

# Usage

if __name__ == "__main__":
    
    print('russian_roulette_decorator usage example:')
    
    import requests
    
    @russian_roulette_decorator(probability=0.2, return_value='Ooops, your output has been stolen!')
    def make_requests(url):
        return requests.get(url)
    
    for _ in range(10):
        print(make_requests('https://google.com'))