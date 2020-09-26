import os



def main():
	t = ( 0, 4, 132.42222, 10000, 12345.67)
	print("{}, {} : {:.2f}, {:.2e}, {:.2e}".format("day_0"+str(t[0]),("ex_0"+str(t[1])),t[2],t[3],t[4]))
if __name__ == "__main__":
	main()