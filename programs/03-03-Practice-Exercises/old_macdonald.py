
def old_macdonald(name):
    if len(name) < 4:
        raise Exception("Use a string name greater than 3.")
    
    name1 = name[0:3]
    name2 = name[3:]
    return name1.capitalize() + name2.capitalize()
