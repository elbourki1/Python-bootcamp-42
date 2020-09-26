from datetime import datetime


def main():
	t = (3,30,2019,9,25)
	date = datetime(2019,9,25,3,30)
	s = date.strftime("%m/%d/%Y %H:%M")
	print(s)
if __name__ == "__main__":
	main()