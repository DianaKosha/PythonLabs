import os
import hashlib


def files_finding(root_folder):#ф-ція знаходить всі шляхи і файли у вказаному каталозі
    FilesInFolder = []

    for root, dirs, files in os.walk(root_folder): #параметри root_folder - де шукати папку, де треба знайти дуплікати
        for file in files:
            FilesInFolder.append(os.path.join(root, file))

    return FilesInFolder #повертає список файлів каталогу - шлях+імя файлу


def hash_file(file_name, chunk_size=1024): #чому 1023, тому що по замовчуванню
    #ф-ція кешує контент файлів
    hasher = hashlib.md5()

    with open(file_name, 'rb') as file_content: #параметри file_name (стрічка) шлях і імя файлу, що хешується
        file_chunk = file_content.read(chunk_size)  #chunk_size фрагмент файлу для оброкби
        while file_chunk:
            hasher.update(file_chunk)
            file_chunk = file_content.read(chunk_size)

    return hasher.hexdigest() #повертає все ту ж стрічку прохешований файл контенту


def find_duplicates(folder_path): #ф-ція шукає дуплікати в папці і в підпапках
    duplicates_list = []
    all_files = files_finding(folder_path) #параметри folder_path шлях до папки де шукати дуплікати
    cached_dict = {}

    for file in all_files:
        cached_dict[file] = hash_file(file)

        if 1 < len(cached_dict) <= len(all_files):
            for key, file_content in cached_dict.items():
                if file != key and cached_dict[file] == file_content:
                    duplicates_list.append((file, key))

    return duplicates_list #повертає список кортежів, де кожен кортеж є парою файлів з тим самим контентом


print(find_duplicates('/home/diana/laboratorna6/duplicates/conventions'))
