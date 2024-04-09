
def blackjack(a,b,c):
    sum_of_numbers = a + b + c
    if sum_of_numbers <= 21:
        return sum_of_numbers
    elif sum_of_numbers >= 21 and a == 11 or b == 11 or c == 11:
        return sum_of_numbers - 10
    elif sum_of_numbers >= 21:
        return "BUST"
