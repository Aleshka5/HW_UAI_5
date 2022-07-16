from functional import *
from victory import start
from bank_account import my_account
counts_folders = 0
while True:
    print("1 - создать папку\n2 - удалить (файл/папку)\n3 - копировать (файл/папку)\n4 - просмотр содержимого рабочей директории\n5 - посмотреть только папки")
    print("6 - посмотреть только файлы\n7 - просмотр информации об операционной системе\n8 - создатель программы\n9 - играть в викторину")
    print("10 - мой банковский счет\n11 - смена рабочей директории (*необязательный пункт)\n12 - выход")
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
        view_in_folder()
    elif user_input == '5':
        view_only_folders()
    elif user_input == '6':
        view_only_files()
    elif user_input == '7':
        os_info()
    elif user_input == '8':
        programm_creator()
    elif user_input == '9':
        start()
    elif user_input == '10':
        my_account()
    elif user_input == '11':
        name_new_folder = input()
        change_current_directory(name_new_folder)
    elif user_input == '12':
        delete_all_created_folders(counts_folders)
        break
    else:
        print('Введена неизвестная команда')