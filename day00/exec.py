import sys

def rev(x):
    if x.isupper():
        x = x.lower()
    else:
        x = x.upper()
    return x

def reverse(arg):
    s = ""
    for i in arg:
       s += rev(i)
    return s[::-1]
def main(argv):
    s = ""
    for arg in argv[:-1]:
        s += reverse(arg) + " ";
    s += reverse(argv[-1]);
    print(s)
if __name__ == "__main__":
   main(sys.argv[1:])