print('''
    Autor: William Vieira
    Engenharia de Software
''')

lista = [] * 10

while True:
    print('''Comando válidos:      
    1 - Inserir
    2 - Apagar o primeiro (FIFO)
    3 - Apagar o ultimo (LIFO)
    4 - Lista
    5 - Sair''')
    print('-' * 35)

    op = int(input('Digite a opção: '))
    while 5 > op < 1:
        op = int(input('Digite a opção: '))

    print('-' * 35)

    if op == 1:
        if len(lista) == 10:
            print('Lista cheia')
            print('-' * 35)
        else:
            novo = int(input('Digite um valor: '))
            lista.append(novo)
            print(f'Valor inserido na lista: {novo}')
            print('-' * 35)

    elif op == 2:
        if len(lista) < 1:
            print('Lista vazia.')
        else:
            print(f'O valor {lista[0]} foi retirado da lista')
            lista.remove(lista[0])
        print('-' * 35)

    elif op == 3:
        if len(lista) < 1:
            print('Lista vazia')
        else:
            print(f'O valor {lista[-1]} foi retirado da lista')
            lista.pop()
        print('-' * 35)

    elif op == 4:
        for i in lista:
            print(f'{i} - ', end='')
        print('Fim da lista')
        print('-' * 35)

    elif op == 5:
        break
