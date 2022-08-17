from functional import *
from victory import start
from bank_account import my_account
import files_module

counts_folders = 0
while True:
    print("1 - создать папку\n2 - удалить (файл/папку)\n3 - копировать (файл/папку)\n4 - просмотр содержимого рабочей директории\n5 - посмотреть только папки")
    print("6 - посмотреть только файлы\n7 - просмотр информации об операционной системе\n8 - создатель программы\n9 - играть в викторину")
    print("10 - мой банковский счет\n11 - смена рабочей директории (*необязательный пункт)\n12 - сохранить содержимое рабочей папки в файл yaml\n13 - выход")
    user_input = input("Введите какой пункт меню хотите запустить: ")
    if user_input == '1':
        create_folder(counts_folders)
        counts_folders += 1
    elif user_input == '2':
        delete_element(counts_folders-1)
        counts_folders -= 1
    elif user_input == '3':
        name_new_file = input()
        copy_element(name_new_file)
    elif user_input == '4':
        print(view_in_folder())
    elif user_input == '5':
        view_only_folders()
    elif user_input == '6':
        view_only_files()
    elif user_input == '7':
        print(os_info())
    elif user_input == '8':
        print(programm_creator())
    elif user_input == '9':
        start()
    elif user_input == '10':
        name_file = 'user_wallet.json'

        data = files_module.check_file_wallet_in_current_directory(name_file)
        user_wallet = data['user_wallet']
        user_shopping_history = data['user_shopping_history']

        user_wallet, user_shopping_history = my_account(user_wallet, user_shopping_history)

        files_module.save_data(name_file, user_wallet, user_shopping_history)
    elif user_input == '11':
        name_new_folder = input()
        change_current_directory(name_new_folder)
    elif user_input == '12':
        name_file = 'current_directory.txt'
        files_module.save_diretory_in_file(name_file)
    elif user_input == '13':
        delete_all_created_folders(counts_folders)
        break
    else:
        print('Введена неизвестная команда')