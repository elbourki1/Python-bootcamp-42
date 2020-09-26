

def ft_filter(function_to_apply, list_of_inputs):
    return [x for x in list_of_inputs if function_to_apply(x)]

c = [0,1,2,3,4,5]
def add1(t):
    return t+1
print(list(filter(lambda x: x > 3,c)))
print(ft_filter(lambda x: x > 3,c))