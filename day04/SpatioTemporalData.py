from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('./athlete_events.csv')
class SpatioTemporalData(object):
	def __init__(self, data):
		self.__data = data
	def where(self, year):
		print(self.__data.query('Year == {}'.format(year))['City'].unique())
	def when(self, city):
		print(self.__data.query('City == "{}"'.format(city))['Year'].unique())
# from SpatioTemporalData import SpatioTemporalData
sp = SpatioTemporalData(data)

sp.where(1896)

sp.when('Athina')