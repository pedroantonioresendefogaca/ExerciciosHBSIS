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
                    numeros = random.choice(list(dict.keys(dict_cartas)))
                    if numeros is not int:
                        if numeros == 'A':
                            if not lista_pontuacao:
                                del(dict_cartas['A'])
                                dict_cartas.update({'A':11})
                                lista_pontuacao.append(dict_cartas[numeros])
                            else:
                                if 'A' in lista_pontuacao[0]:
                                    lista_pontuacao.append(dict_cartas[numeros])
                                    del(lista_pontuacao[0])
                                    lista_pontuacao.insert(0, 1)
                                else:
                                    pass
                        else:
                            pass
                        lista_pontuacao.append(dict_cartas[numeros])
                    else:
                        lista_pontuacao.append(numeros)
                    print(f'A carta retirada foi {numeros}')
                    print(f'Sua pontuação atual é de {sum(lista_pontuacao)} pontos!')
                elif menu_selecao == 2:
                    print(f'Sua pontuação foi de {sum(lista_pontuacao)} pontos, obrigado por jogar!')
                    break
                else:
                    print('Insira uma operação válida')
                if sum(lista_pontuacao) == 21:
                    print('Parabéns! Você ganhou!')
                    break
                elif sum(lista_pontuacao) > 21:
                    print('Que pena! Você perdeu!')
                    break
                else:
                    pass
            except ValueError:
                print('Insira uma operação válida')
                
testando = Baralho()
testando.jack()