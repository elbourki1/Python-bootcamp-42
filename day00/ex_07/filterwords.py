import sys

# str.split()
def main(argv):
	# print(type(argv[0]))
	if len(argv) != 2 or argv[1].isnumeric() == 0:
		print("ERROR")
	else:
		result = []
		sep = argv[0].split(sep=' ')
		for word in sep:
			if len(word) <= int(argv[1]):
				continue
			else:
				result.append(word)
	print(result)
if __name__ == "__main__":
	main(sys.argv[1:])

