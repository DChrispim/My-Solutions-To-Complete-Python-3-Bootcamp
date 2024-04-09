
def up_low(s):
    n_upper_letters = 0
    n_lower_letters = 0
    for letter in s:
        if letter.isupper():
            n_upper_letters += 1
        elif letter.islower():
            n_lower_letters += 1
        else: #To take in account for punctuation
            pass
    return f'''
            Original String: {s}
            No. of Upper case characters: {n_upper_letters}
            No. of Lower case Characters: {n_lower_letters}
            '''
