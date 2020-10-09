print('''
    Autor: William Vieira
    Engenharia de Software
''')

lista = [] * 10

while True:
    print('''Comando válidos:      
    1 - Inserir
    2 - Retirar
    3 - Listar
    4 - Sair''')
    print('-' * 30)

    op = int(input('Digite a opção: '))
    while 4 > op < 1:
        op = int(input('Digite a opção: '))

    print('-' * 30)

    if op == 1:
        if len(lista) == 10:
            print('Lista cheia')
            print('-' * 30)
        else:
            novo = int(input('Digite um valor: '))
            lista.append(novo)
            print(f'Valor inserido na lista: {novo}')
            print('-' * 30)

    elif op == 2:
        if len(lista) < 1:
            print('Lista vazia.')
        else:
            print(f'O valor {lista[0]} foi retirado da lista')
            lista.remove(lista[0])
        print('-' * 30)

    elif op == 3:
        for i in lista:
            print(f'{i} - ', end='')
        print('Fim da lista')
        print('-' * 30)

    elif op == 4:
        break
