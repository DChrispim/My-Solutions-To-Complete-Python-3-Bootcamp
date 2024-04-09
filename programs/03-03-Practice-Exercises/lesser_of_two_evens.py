#Generalization to n numbers
def lesser_of_two_evens(*args):
    if all(arg%2==0 for arg in args):
        return min(args)
    else:
        return max(args)
