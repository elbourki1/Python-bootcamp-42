from __future__ import print_function

import sys
def main():
    phrase = "The right format"
    s = "-" * 42
    print(s,end="")
    print(phrase,file=sys.stderr,end="")
if __name__ == "__main__":
	main()