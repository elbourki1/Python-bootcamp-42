import numpy as np 
from ex01.ImageProcessor import ImageProcessor

image = ImageProcessor().load("./resources/42AI.png")
# ImageProcessor().display(image)

class AdvancedFilter(object):
	def mean_blur(self, img):
		copy = np.copy(img)
		kernel = np.ones((3,3))
		i = 0
		j = 0
		origin = (0,0)
		ac = 0
		for j,row in enumerate(img):
			for i,pixel in enumerate(row):
				origin = (j,i)
				for py in kernel:
					for px in kernel:
						if ()
		
	def gaussian_blur(self, img):
		pass

color = AdvancedFilter()
# img_invert = color.mean_blur(image)
# print(img_invert.shape)
# ImageProcessor().display(img_invert)
tmp = np.random.randint(0,10,(10,10))
print(tmp)
print("------------------------")
id = np.eye(3)
print(tmp[:3,:3] * id)

print(sum(sum(tmp[:3,:3] * id)))