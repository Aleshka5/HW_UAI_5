import os
import json

def check_file_wallet_in_current_directory(name_wallet_file):
    data = None
    if os.path.exists(name_wallet_file):
        with open(name_wallet_file, 'r') as f:
            data = json.load(f)
        return data

    # Создание нового файла счёта
    empty_data = {'user_wallet':0,
                  'user_shopping_history':{}}
    with open(name_wallet_file,'w') as f:
        json.dump(empty_data, f)
    with open(name_wallet_file,'r') as f:
        data = json.load(f)
    return data

def save_data(name_wallet_file,value1,value2):
    data = {'user_wallet':value1,
            'user_shopping_history':value2}
    with open(name_wallet_file,'w') as f:
        json.dump(data, f)
    return None

def save_diretory_in_file(name_file):
    files = ''
    for i in os.listdir():
        if os.path.isfile(i):
            files += i+','
    folders = ''
    for i in os.listdir():
        if os.path.isdir(i):
            folders += i+','
    with open(name_file,'w') as f:
        f.writelines('files: '+files)
        f.writelines('\n')
        f.writelines('folders: '+folders)

