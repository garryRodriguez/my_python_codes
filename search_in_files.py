#!/usr/bin/env python3

import os

def search_in_files(folder_path, search_string):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    if search_string in content:
                        print(f'Found  "{search_string}" in file: {file_path}')
            except Exception as e:
                print(f'Not found in file {file_path}:{e}')

folder_path = os.path.expanduser('~/Desktop/programs/files/new_folder')
search_string = input("Enter a string to search: ")

search_in_files(folder_path, search_string)