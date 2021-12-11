# sequential_map

def sequential_map(*args):
    cont = args[-1]
    for arg in args[:-1]:
        cont = list(map(arg, cont))
    return(cont)


# consensus_filter

def consensus_filter(*args):
    cont = args[-1]
    for arg in args[:-1]:
        cont = filter(arg, cont)
    return list(cont)


# conditional_reduce

def conditional_reduce(f1, f2, cont):
    cont = list(filter(f1, cont))
    while len(cont) > 1:
        cont[1] = f2(cont[0], cont[1])
        cont = cont[1:]
    return cont[0]


# func_chain

def func_chain(*args):
    def inner(f):
        for arg in args:
            f = arg(f)
        return f
    return inner


# sequential_map using func_chain

def sequential_map(*args):
    cont = args[-1]
    arguments = args[:-1]
    return func_chain(*arguments)(cont)


# multiple_partial

def multiple_partial(*args, **kwargs):
    func_list = []
    def my_partial(func, /, *args, **keywords):
        def newfunc(*fargs, **fkeywords):
            newkeywords = {**keywords, **fkeywords}
            return func(*args, *fargs, **newkeywords)
        newfunc.func = func
        newfunc.args = args
        newfunc.keywords = keywords
        return newfunc
    for arg in args:
        func_list.append(my_partial(arg, **kwargs))
    return func_list
