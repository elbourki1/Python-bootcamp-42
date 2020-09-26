from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('./athlete_events.csv')
def proportionBySport(data, year, sport, gender):
    maj = data.query('Sex == "{}" and Year == {}'.format(gender,year)).shape[0]
    min = data.query('Sex == "{}" and Year == {} and Sport == "{}"'.format(gender,year,sport)).shape[0]
    print(min / maj)


# print(data.query('Sport == '))
# print(data['Sport'].unique())
proportionBySport(data, 2004, 'Tennis', 'F')