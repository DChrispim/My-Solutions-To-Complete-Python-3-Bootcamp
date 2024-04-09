
import random

def yield_n_random(low_number, high_number, n_of_numbers):
    for n in range(n_of_numbers):
        yield random.randint(low_number,high_number)
