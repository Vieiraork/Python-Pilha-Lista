from colorama import Fore, Style
from config import Config

# Values in config.py
# Recupera os valores estáticos do arquivo config.py
length = Config['vector_index']

# Inicialização do vetor de dez posições
# Init vector whit ten positions
vector = [] * length


def insert(number):
    if len(vector) == 10:
        print(f'{Fore.LIGHTRED_EX}Vector is full!{Style.RESET_ALL}')
    else:
        print(f'{Fore.LIGHTGREEN_EX}Value {number} successful inserted{Style.RESET_ALL}')
        vector.append(number)


def delete_first():
    if len(vector) < 1:
        print(f'{Fore.RED}Vector is empty.{Style.RESET_ALL}')
    else:
        print(f'{Fore.LIGHTGREEN_EX}Value {vector[0]} removed.{Style.RESET_ALL}')
        vector.remove(vector[0])


def delete_last():
    if len(vector) < 1:
        print(f'{Fore.RED}Vector is empty.{Style.RESET_ALL}')
    else:
        print(f'{Fore.LIGHTGREEN_EX}Value {vector[-1]} removed.{Style.RESET_ALL}')
        vector.pop()


def display():
    if len(vector) < 1:
        print(f'{Fore.RED}Vector is empty.{Style.RESET_ALL}')
    else:
        for i in vector:
            print(f'{Fore.LIGHTGREEN_EX}{i} - ', end='')
        print('End...')
