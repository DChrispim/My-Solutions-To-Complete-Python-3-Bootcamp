
if __name__ == '__main__':
    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError:
        print("Error: You used the wrong data type") 
