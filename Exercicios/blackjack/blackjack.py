import random

class Baralho:
    def __init__(self):
        self.__dict_cartas = {'A':1, 2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':10,'Q':10,'K':10}
        self.__lista_pontuacao = []

    def jack(self):
        dict_cartas = self.__dict_cartas
        lista_pontuacao = self.__lista_pontuacao
        while True:
            try:
                menu_selecao = int(input('1 - Retirar carta\n2 - Sair\nSelecione a opção desejada: '))
                if menu_selecao == 1:
                    lista_cartas_chaves = list(dict.keys(dict_cartas))
                    lista_cartas_valores = list(dict.values(dict_cartas))
                    numeros = random.choice(list(dict.keys(dict_cartas)))
                    if numeros is not int:
                        lista_pontuacao.append(dict_cartas[numeros])
                    else:
                        lista_pontuacao.append(numeros)
                    print(f'A carta retirada foi {numeros}')
                    print(f'Sua pontuação atual é de {sum(lista_pontuacao)} pontos!')
                elif menu_selecao == 2:
                    print('GAME OVER')
                    break
                else:
                    print('Insira uma operação válida')
                if sum(lista_pontuacao) >= 21:
                    print('Parabéns! Você ganhou!')
                    break
                else:
                    pass
            except ValueError:
                print('Insira uma operação válida')
                
testando = Baralho()
testando.jack()