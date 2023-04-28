from logic import logic
from decouple import config

money = int(config('MY_MONEY'))


while True:
    if money > 0:
        answer = input(f'Будете играть? (остаток:{money}) ')
        if answer.lower() == 'да':
            number = input('Число на которое хотите поставить: ')
            if not number.isnumeric():
                print('Число должно быть только из цифр')
                continue
            number = int(number)
            if number < 1 or number > 30:
                print('Число должно быть от 1 до 30 включительно')
                continue
            amount = input('Сколько хотите поставить: ')
            if not amount.isnumeric():
                print('Сумма ставки должна быть целым числом')
                continue

            amount = int(amount)

            if amount < 0 or amount > money:
                print(f'сумма должна быть больше нуля и  меньше {money}')
                continue

            money += logic(number, amount)
        else:
            print(f'До свидания у вас осталось {money}')

        if money <= 0:
            print(f'у вас не осталось денег! Приходите когда будут')
    else:
        print(f'У вас недостаточно денег чтобы сыграть, ваш баланс: ({money}$)')
        break