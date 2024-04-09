
def animal_crackers(text):
    first_word, second_word = text.lower().split()
    return first_word[0] == second_word[0]
