import random

def logic(number, amount):
    win_number = random.randint(1, 31)
    if number == win_number:
        print(f'You win! {amount * 2}$')
        return amount * 2

    else:
        print(f'Ups, you lose!(I warned)')
        return -amount
