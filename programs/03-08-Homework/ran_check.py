
def ran_check_verbose(num,low,high):
    if num in range(low,high+1):
        return "{} is in the range between {} and {}".format(num,low,high)
    else:
        return "{} is not in the range between {} and {}".format(num,low,high)

def ran_check_boolean(num,low,high):
    return num in range(low,high+1)
