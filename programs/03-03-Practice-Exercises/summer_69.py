
def summer_69(arr):
    gate = True
    count = 0
    for num in arr:
        if num == 6:
            gate = False
        elif num == 9:
            gate = True
        elif gate == True:
            count = count + num
    return count
