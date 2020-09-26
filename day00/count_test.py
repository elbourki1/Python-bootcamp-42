import string, sys

def text_analyzer(arg=""):
    '''
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    '''
    while 1 and arg == "":
        arg = input("What is the text to analyse?\n")
    upper_letters = lower_letters = 0
    punctuation_marks = spaces = 0
    for i in arg:
        if i == ' ':
            spaces += 1
        elif i.isupper():
            upper_letters += 1
        elif i.islower():
            lower_letters += 1
        elif i in string.punctuation:
            punctuation_marks += 1
    print("The text contains {} characters:".format(len(arg)),end='\n\n')
    print("- {} upper letters".format(upper_letters),end='\n\n')
    print("- {} lower letters".format(lower_letters),end='\n\n')
    print("- {} punctuation marks".format(punctuation_marks),end='\n\n')
    print("- {} spaces".format(spaces))



def main(argv):
    # text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
    text_analyzer()
if __name__ == "__main__":
   main(sys.argv[1:])