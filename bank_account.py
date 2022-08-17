"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
def add_money(user_wallet):
    print('*'*30)
    try:
        add_sum = int(input('Введите сумму пополнения (руб):'))
    except:
        print('Ошибка')
        return user_wallet
    user_wallet += add_sum
    print(f'Пополнение прошло успешно!\nНа вашем счету сейчас {user_wallet} руб')
    print('*' * 30)
    return user_wallet

def send_money(user_wallet,user_shopping_history):
    print('*' * 30)
    product = input('Введите название покупаемого товара')
    send_sum = int(input('Введите цену товара (руб):'))
    if (user_wallet >= send_sum):
        user_wallet -= send_sum
        if product in user_shopping_history:
            if user_shopping_history[product][1] == send_sum:
                    user_shopping_history[product][0] += 1
            else:
                for i in range(1, 101):
                    if f'{product}_{i}' in user_shopping_history:
                        if user_shopping_history[f'{product}_{i}'][1] == send_sum:
                            user_shopping_history[f'{product}_{i}'][0] += 1
                            break
                        else:
                            continue
                    else:
                        user_shopping_history[f'{product}_{i}'] = [1, send_sum]
                        break
        else:
            user_shopping_history[product] = [1,send_sum]

        print(f'Списание прошло успешно!\nНа вашем счету сейчас {user_wallet} руб')
        print('*' * 30)
        return user_wallet, user_shopping_history
    else:
        print('На вашем счету недостаточно средств для совершения покупки!')
        print('*' * 30)
        return user_wallet, user_shopping_history

def print_shopping_history(user_shopping_history):
    print('*' * 30)
    print('Продукт  | Количество | Цена')
    for product, info in user_shopping_history.items():
        print('{:<9}|{:^9}шт.| {} руб.'.format(product,info[0],info[1]))
    print('*' * 30)
    return None

def my_account(user_wallet, user_shopping_history):
    while True:
        print('='*30)
        print(f'На вашем счету {user_wallet} руб')
        print('='*30)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print('=' * 30)
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            user_wallet = add_money(user_wallet)
        elif choice == '2':
            user_wallet,user_shopping_history = send_money(user_wallet,user_shopping_history)
        elif choice == '3':
            print_shopping_history(user_shopping_history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
    return user_wallet, user_shopping_history

if __name__ == '__main__':
    name_file = 'user_wallet.json'

    data = files_module.check_file_wallet_in_current_directory(name_file)
    user_wallet = data['user_wallet']
    user_shopping_history = data['user_shopping_history']

    user_wallet, user_shopping_history = my_account(user_wallet, user_shopping_history)

    files_module.save_data(name_file,user_wallet,user_shopping_history)
