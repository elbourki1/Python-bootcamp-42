from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('./athlete_events.csv')
def howManyMedals(data, name):
    data = data.query('Name == "{}"'.format(name))
    print(type(data))
# from HowManyMedals import howManyMedals
howManyMedals(data, 'Kjetil Andr Aamodt')