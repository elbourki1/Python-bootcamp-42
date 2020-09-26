import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.stats import gaussian_kde
from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('./athlete_events.csv')

class MyPlotLib(object):
	def histogram(self, data, features=[]):
		data.hist(features)
		plt.show()
	def density(self, data, features):
		data[features].plot(kind='density')
	def pair_plot(self, data, features):
		pass
	def box_plot(self, data, features):
		pass

density = gaussian_kde(data)
plt.plot(data,density)
plt.show()
# plot = MyPlotLib()
# plot.histogram(data,['Year'])
# data[['Year']].plot(kind='density')
# plot.density(data,['Year'])
# plt.hist(data)