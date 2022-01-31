import time


class Dados:
    def __init__(self):
        self.estudar()

    def estudar(self):
        nome = input('Qual o nome? ')
        hora = int(input('informe quantas horas você vai estudar: '))
        time.sleep(hora)
        print(f'{nome}, já pode parar de estudar')


if __name__ == "__main__":
    dados = Dados()