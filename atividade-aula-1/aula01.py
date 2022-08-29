# faça um programa em python que implemente uma busca sequencial de um número inteiro.
# -Dica:
#    -duas classes: classe de busca e classe de teste
#    - utilize uma lista vazia para iniciar
# 1. Faça uma função que crie uma lista de 500 valores inteiros randômicos
# 2. Faça uma função chamada buscaSequencial(elemento) que entre um valor e retorne a sua posição na lista
# ou uma mensagem caso não tenha encontrado
# 3.Faça uma classe de teste com as seguintes chamadas:
#     ret = buscaSequencial(10)
#     print(ret)
#     ret = buscaSequencial(100)
#     print(ret)
#     ret = buscaSequencial(355)
#     print(ret)
#     ret= buscaSequencial (433)
#     print(ret)

import random

listaNumeros = []

class Busca:
    def __init__(self):
        self.listaNumeros = []

    def randomValues():
        #aqui cria outra lista dentro da listaNumeros ):
        listaNumeros.append(random.sample(range(501), k=501))
        return listaNumeros

    def buscaSequencial(elemento):
        #por criar uma lista dentro de outra lista, precisei primeiro percorrer 
        # a lista externa e depois a lista interna
        for sub in listaNumeros:
            #verificando se o valor buscado esta dentro de alguma lista interna
            if elemento in sub:
                index = sub.index(elemento)
                print(f" O index do número {elemento} é {index}")
                break # sai do loop
        
        else:
            # caso o valor buscado nao seja encontrado
            print(f"Ops, valor {elemento} não foi encontrado ):")
            return "Valor Inválido ):"

        return index
class Teste:
    def buscaTeste():
        ret = Busca.buscaSequencial(10)
        print(f"POSIÇÃO: {ret}\n")
        ret = Busca.buscaSequencial(100)
        print(f"POSIÇÃO: {ret}\n")
        ret = Busca.buscaSequencial(355)
        print(f"POSIÇÃO: {ret}\n")
        ret= Busca.buscaSequencial (433)
        print(f"POSIÇÃO: {ret}\n")


        
  
           
Busca.randomValues()
Teste.buscaTeste()

