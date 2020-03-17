import random

class Fruta:
    def __init__(self):
        self.__lista_frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
        self.__lista_numero_tentativas = []
        self.__lista_letras_inseridas = []

    def jogo(self):
        lista_frutas = self.__lista_frutas
        lista_numero_tentativas = self.__lista_numero_tentativas
        lista_letras_inseridas = self.__lista_letras_inseridas
        menu = input('===JOGO DA FRUTA===\n1 - Jogar\n2 - Sair\nSelecione a opção desejada: ')
        while True:
            try:
                if menu == '1':
                    nome_da_fruta = random.choice(lista_frutas)
                    adivinhar_palavra = input('Insira uma letra: ')
                    lista_numero_tentativas.append(1)
                    print(lista_numero_tentativas)
                    if adivinhar_palavra in nome_da_fruta:
                        print(f'A letra {adivinhar_palavra} faz parte da palavra!')
                    else:
                        pass
                elif menu == '2':
                    print('Obrigado por jogar!')
                    break
                else:
                    print('Insira uma operação válida')
            except ValueError:
                print('Insira uma operação válida')

teste = Fruta()
teste.jogo()