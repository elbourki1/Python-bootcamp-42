import sys

def main(argv):
	if len(argv) != 1 or argv[0].isalpha():
		print("ERROR")
	else:
		if int(argv[0]) == 0:
			print("I'm Even.")
		elif int(argv[0]) % 2 == 1:
			print("I'm Zero.")
		else:
			print("I'm Even.")
if __name__ == "__main__":
   main(sys.argv[1:])