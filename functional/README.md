# Functional programming homework
I created functional.py with the following functions:

1) sequential_map - the function takes as arguments any number of functions (positional arguments), as well as a container with some values. The function returns a list of the results of sequential application of the passed functions to the values in the container.
2) consensus_filter - the function takes as arguments any number of functions (positional arguments) which return True or False, as well as a container with some values. The function returns a list of values which give True after they have passed to all functions.
3) conditional_reduce - the function takes 2 functions, as well as a container with values. The first function takes 1 argument and returns True or False, the second takes 2 arguments and returns a value (just like in a normal reduce function). conditional_reduce must returns one value - the result of reduce, skipping the values with which the first function returned False.
4) func_chain - the function takes any number of functions as arguments (positional arguments). The function returns a function that concatenates everything passed by sequential execution.
5) multiple_partial - analogous to the partial function, but which takes an unlimited number of functions as arguments and returns a list of the same number of "partial functions"
