
#Generalization to sum of n numbers
def makes_twenty(*args):
    return sum(args) == 20 or any(arg==20 for arg in args)
