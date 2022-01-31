import time

dados_user = open('dados_user.txt', 'r')
nome = dados_user.readline()
if nome != '':
    print(f'Bem vindo de volta, {nome}')
else:
    dados_user = open('dados_user.txt', 'w')
    nome = input('Qual o nome? ')
    dados_user.write(f'{nome}')


class Dados:
    def __init__(self):
        self.estudar()

    def estudar(self):
        hora = int(input('informe quantas horas você vai estudar: '))
        hora_form = hora * 3600
        time.sleep(hora_form)
        print(f'{nome}, já pode parar de estudar')


if __name__ == "__main__":
    dados = Dados()