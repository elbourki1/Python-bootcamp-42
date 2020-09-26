import numpy as np 

class NumPyCreator(object):
	def from_list(self,lst):
		return np.asarray(lst)
	def from_tuple(self,tpl):
		return np.asarray(tpl)
	def from_iterable(self,itr):
		return np.asarray(list(itr))
	def from_shape(self,shape,value=0):
		return np.full(shape,value)
	def random(self,shape):
		return np.random.rand(shape[0],shape[1])
	def identity(self,n):
		return np.eye(n)

# f = NumPyCreator().from_iterable(range(5))
# print(f)

# e = np.eye(10)
# print(e)