import numpy as np 
from ex01.ImageProcessor import ImageProcessor

image = ImageProcessor().load("./resources/42AI.png")
ImageProcessor().display(image)
# print("real image \n{}".format(image))
# print(image.shape)
# print(image[:,:,0])
class ColorFilter(object):
	def invert(self, array):
		return 255 - array
	def to_blue(self, array):
		array.zeros((0,1))
		return array
	def to_green(self, array):
		array = array[:,:,:] * [0,1,0]
		return array
	def to_red(self, array):
		array[:,:,2] = 0
		array[:,:,1] = 0
		return array
	def celluloid(self, array):
		return array

color = ColorFilter()
img_invert = color.celluloid(image)
print(img_invert.shape)
ImageProcessor().display(img_invert)