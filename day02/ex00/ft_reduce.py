from functools import reduce
def ft_reduce(function_to_apply, list_of_inputs):
    return [function_to_apply(list_of_inputs[x],list_of_inputs[x+1]) for x in range(len(list_of_inputs) - 1) ]
f = lambda a,b: a if (a > b) else b
print(reduce(f, [47,11,42,102,13]))
f1 = lambda x,y: x+y
c = [0,1,2,3,4,5]
def add1(t):
    return t+1
print(reduce(f1,[0,1,2,3,4,5]))
print(ft_reduce(f1,c))