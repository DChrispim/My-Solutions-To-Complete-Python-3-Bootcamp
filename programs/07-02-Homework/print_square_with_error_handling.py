from IPython.display import clear_output
import os

def print_square_with_error_handling():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            clear_screen()
            print("Looks like you did not enter an integer!")
            continue
        else:
            break
    print("The square is " + str(val**2))

def clear_screen():
    '''
    Function that clears the output, uses different function depending on the environment
    '''
    try:
        # Check if running in IPython environment
        ipython = get_ipython()
        if ipython is not None:
            # Execute in IPython environment
            clear_output(wait=True)
    except NameError:
        # Execute in Python terminal
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    print_square_with_error_handling()
