import numpy as np 

class ScrapBooker(object):
    def crop(self, array, dimensions, position=(0,0)):
        if (dimensions > array.shape):
            raise ValueError("error")
        return array[position[0]:dimensions[0] + position[0],position[1]:dimensions[1] + position[1]] 
    def thin(self, array, n, axis):
        if axis:
            print("vertical")
            return array[:,:n-1]
        print("horizontal")
        return array[:n-1,:]
    def juxtapose(self, array, n, axis):
        pass
    def mosaic(self, array, dimensions):
        pass


test = ScrapBooker()
array = np.eye(10)
print(array)
# print(test.crop(array,(2,2),(0,0)))
# print(test)

t = np.random.randint(10,50,(8,8))

# t[4:]
print(t)
print(test.thin(t,6,0))