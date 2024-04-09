
def palindrome(s):
    # Remove the spaces from the string
    word = s.replace(" ", "")
    return word == word[::-1]
