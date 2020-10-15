from colorama import Fore, Style
from os import system, name
from time import sleep
from config import Config
import data_estructures

print('''
    Autor: William Vieira
    Software Engineer student
''')

# Setar os valores de configurações
# Set values from config.py
line = Config['line_size']
options = Config['default_options']
menu = Config['menu_options']

# Instância do arquivo
# New instance from data_structures.py
data = data_estructures


def op():
    while True:
        print(f'{Fore.WHITE}{menu}')
        print('-' * line)
        opt = int(input('Type a option: '))
        print('-' * line)
        system('cls' if name == 'nt' else 'clear')

        if opt in options:
            if opt == 1:
                value = int(input('Type a number: '))
                data.insert(value)
                print('-' * line)
            if opt == 2:
                data.delete_first()
                print('-' * line)
            if opt == 3:
                data.delete_last()
                print('-' * line)
            if opt == 4:
                data.display()
                print('-' * line)
            if opt == 5:
                print('Programming close...')
                sleep(1)
                break
        else:
            print(f'{Fore.RED}Invalid option, please try again.{Style.RESET_ALL}')
