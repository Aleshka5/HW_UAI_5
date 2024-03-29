import os
import sys
import shutil

def create_folder(i):
    os.mkdir(f"new_folder{i}") if not os.path.exists(f"new_folder{i}") else print('Такая папка уже существует')
def delete_element(i):
    os.rmdir(f"new_folder{i}") if os.path.exists(f"new_folder{i}") else print('Такая папка уже существует')
def copy_element(name_file):
    if '.' in name_file:
        name = name_file.split('.')
        shutil.copy(name_file,f"{name[0]}_copy{name[1]}")
    else:
        shutil.copy(name_file, f"{name_file}_copy")

def view_in_folder():
    return os.listdir()

def view_only_folders():
    list_all = os.listdir()
    generate_directory = [i for i in list_all if os.path.isdir(i)]
    print(generate_directory)

def view_only_files():
    list_all = os.listdir()
    generate_files = [i for i in list_all if os.path.isfile(i)]
    print(generate_files)
def os_info():
    return sys.platform
def programm_creator():
    return 'Aleshka5'
def user_bank_accaunt(user_money):
    print(f"На вашем счету {user_money} рублей")
def change_current_directory(new_directory):
    os.chdir(new_directory)
def delete_all_created_folders(count_folders):
    for i in range(count_folders,0,-1):
        if os.path.exists(f"new_folder{i}"):
            os.rmdir(f"new_folder{i}")