# from PIL import Image
# import numpy as np
# # from matplotlib import im 

# class ImageProcessor(object):
# 	# def __init__(self):
# 	# 	super.__init__()
# 	def load(self, path):
# 		image = Image.open(path)
# 		print("Loading image of dimensions {} x {}".format(image.size[0],image.size[1]))
# 		return np.asarray(image)
# 	def display(self,array):
# 		Image.fromarray(array).show()
# if __name__ == "__main__":

# 	f = ImageProcessor().load("./resources/42AI.png")
# 	print(f)
# 	ImageProcessor().display(f)


from PIL import Image
import numpy as np
from matplotlib import image 
from matplotlib import pyplot 


class ImageProcessor(object):
	# def __init__(self):
	# 	super.__init__()
	def load(self, path):
		img = image.imread(path)
		# print("Loading image of dimensions {} x {}".format(image.size[0],image.size[1]))
		return img
	def display(self,array):
		pyplot.imshow(array)
		pyplot.show()
if __name__ == "__main__":

	f = ImageProcessor().load("./resources/42AI.png")
	print(f)
	ImageProcessor().display(f)