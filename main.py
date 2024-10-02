import os
import tkinter

user_main_folder = input("Enter the name for the head folder: ")


def create_folder(main_folder, number_of_folders: int):
    os.mkdir(f'./{main_folder}')
    sub_folders = []
    user_answer = input("What is the name of the sub folders?")

    while True:
        folders = input("enter name for a folder: ")
        sub_folders.append(folders)
        for folder in sub_folders:
            os.mkdir(f'{main_folder}/{folder}')
        break

