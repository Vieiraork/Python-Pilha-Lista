from config import Config

# Values in config.py
# Recupera os valores estáticos do arquivo config.py
colors = Config['colors']
length = Config['vector_index']

# Inicialização do vetor de dez posições
# Init vector whit ten positions
vector = [] * length


def insert(number):
    if len(vector) == 10:
        print(f'{colors["red"]}Vector is full!{colors["white"]}')
    else:
        print(f'{colors["green"]}Value {number} successful inserted{colors["white"]}')
        vector.append(number)


def delete_first():
    if len(vector) < 1:
        print(f'{colors["red"]}Vector is empty.{colors["white"]}')
    else:
        print(f'{colors["red"]}Value {vector[0]} removed.{colors["white"]}')
        vector.remove(vector[0])


def delete_last():
    if len(vector) < 1:
        print(f'{colors["red"]}Vector is empty.{colors["white"]}')
    else:
        print(f'{colors["red"]}Value {vector[-1]} removed.{colors["white"]}')
        vector.pop()


def display():
    if len(vector) < 1:
        print(f'{colors["red"]}Vector is empty.{colors["white"]}')
    else:
        for i in vector:
            print(f'{i} - ', end='')
        print('End...')
