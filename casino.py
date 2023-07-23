from decouple import config
from logic import logic
from termcolor import cprint
from emoji import emojize
money = config('MY_MONEY', cast=int)

while True:
    if money > 0:
        answer = input(emojize(f'Balance {money}$:dollar_banknote:\n'
                       'Do you want play?(but i dont recommend, you can lose all your money): '))
        if answer == 'yes':
            print('Are you sure!?')
            number = input('choice number 1-30: ')
            if not number.isnumeric():
                cprint('Number must be integer', 'red', 'on_grey')
                continue
            number = int(number)
            if number < 1 or number > 30:
                print('only from 1 to 30')
                continue

            amount = input('How much: ')
            if not amount.isnumeric():
                cprint('Number must be integer', 'red', 'on_grey')
                continue

            amount = int(amount)

            if  amount < 0 or amount > money:
                print(f'Amount should be >0 and <{money}$')
                continue

            money += logic(number, amount)
        else:
            print(emojize(f'Good bye! keep yourself:red_heart:'))
    else:
        cprint(f'You cant play because your balance > 0. '
              f'better go to work ', 'red', 'on_green')
        break


