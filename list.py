from time import sleep
from config import Config
import data_estructures

print('''
    Autor: William Vieira
    Software Engineer student
''')

# Setar os valores de configurações
# Set values from config.py
colors = Config['colors']
line = Config['line_size']
options = Config['default_options']
menu = Config['menu_options']

# Instância do objeto
# New object instance
data = data_estructures
print(f'{colors["white"]}', end='')


def op():
    while True:
        print(menu)
        print('-' * line)
        opt = int(input('Type a option: '))
        print('-' * line)

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
            print(f'{colors["red"]}Invalid option, please try again.{colors["white"]}')
