from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('./athlete_events.csv')

def youngestFellah(data, year):
	res = {'M':0,'F':0}
	res['M'] = data.query('Sex == "M" and Year == {}'.format(year)).agg({'Age':min})[0]
	print(res['M'])
	res['F'] = data.query('Sex == "F" and Year == {}'.format(year)).agg({'Age':min})[0]
	print(res['F'])
	return res

# loader.display(data,10)

print(youngestFellah(data,2004))
