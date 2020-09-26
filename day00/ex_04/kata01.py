

languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def print_dictyionary(languages):
    for key in languages:
        print("{} was created by {}".format(key,languages[key]))

print_dictyionary(languages)