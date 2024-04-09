
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set of the alphabet
    alphaset = set(alphabet)
    # Remove all spaces from the input string
    str1 = str1.replace(" ", "")
    # Convert in all lowercase
    str1 = str1.lower()
    # Grab all unique letters using set
    str1 = set(str1)
    #Check if both are equal
    return str1 == alphaset
