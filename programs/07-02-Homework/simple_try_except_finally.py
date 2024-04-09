
if __name__ == '__main__':
    try:
        x = 5
        y = 0
        z = x/y
    except ZeroDivisionError:
        print("Division by zero if ill-defined.") 
    finally:
        print("All Done.") 
