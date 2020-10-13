from config import Config

colors = Config['colors']


class DataEstutures:
    # Inicialização do vetor de dez posições
    # Init vector whit ten positions
    vector = [] * 10

    def insert(self, number) -> type(None):
        if len(self.vector) == 10:
            print(f'{colors["red"]}Vector is full!{colors["white"]}')
        else:
            self.vector.append(number)
            print(f'{colors["green"]}Value {number} successful inserted{colors["white"]}')

    def delete_first(self) -> type(None):
        if len(self.vector) < 1:
            print(f'{colors["red"]}Vector is empty.{colors["white"]}')
        else:
            print(f'{colors["red"]}Value {self.vector[0]} removed.{colors["white"]}')
            self.vector.remove(self.vector[0])

    def delete_last(self) -> type(None):
        if len(self.vector) < 1:
            print(f'{colors["red"]}Vector is empty.{colors["white"]}')
        else:
            print(f'{colors["red"]}Value {self.vector[-1]} removed.{colors["white"]}')
            self.vector.pop()

    def display(self) -> type(None):
        if len(self.vector) < 1:
            print(f'{colors["red"]}Vector is empty.{colors["white"]}')
        else:
            for i in self.vector:
                print(f'{i} - ', end='')
            print('End of vector')
