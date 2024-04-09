
def iter_of_string_but_a(word):

    letters = (letter for letter in word if letter !='a')
    for letter in letters:
        yield letter
