

def ft_map(function_to_apply, list_of_inputs):
    return [function_to_apply(x) for x in list_of_inputs]

c = [0,1,2,3,4,5]
def add1(t):
    return t+1
print(list(map(lambda x: x+1,c)))
print(ft_map(lambda x: x+1,c))