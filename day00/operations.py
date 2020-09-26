import sys

Sum: 52
Difference: 32
Product: 420
Quotient: 4.2
Remainder: 2

def operation(num1,num2):
	print("Sum: 		{}".format(num1 + num2))
	print("Difference: 	{}".format(num1 - num2))
	print("Product: 	{}".format(num1 * num2))
	try:
		print("Quotient: 	{}".format(num1 / num2))
	except:
		print("Quotient: 	 ERROR (div by zero)")
	try:
		print("Remainder:	{}".format(num1 % num2))
	except:
		print("Remainder:	 ERROR (modulo by zero)")
	

def error():
	print("Usage: python operations.py <number1> <number2>")
	print("Example:")
	print("     python operations.py 10 3")
def input_error(num):
	if num == 0:
		print("InputError: too many arguments")
	elif num == 1:
		print("InputError: only numbers")
def main(argv):
	if len(argv) == 0:
		error()
	elif len(argv) > 2:
		input_error(0)
		print("")
		error()
	else:
		if argv[0].isnumeric() and argv[1].isnumeric():
			operation(int(argv[0]),int(argv[1]))
		else:
			input_error(1)
			print("")
			error()

	



if __name__ == "__main__":
   main(sys.argv[1:])