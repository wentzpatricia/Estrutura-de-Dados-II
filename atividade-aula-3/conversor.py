# Entrada: D (data)
# Saída: Lógico
# Objetivo: método que recebe uma data e a escreve por extenso. Por exemplo:
# 10/03/2020 deve ser escrito como 10 de março de 2020. Retorna verdadeiro se a
# operação foi realizada com sucesso e falso , caso contrário.

def conversorDeDatas():

    mes_ext = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    while True:
        data = input("Qual a data que você gostaria de converter para extenso? ")
        if "/" in data and data.count("/") == 2:
            dia, mes, ano = data.split("/")

            print(f"\n{dia} de {mes_ext[int(mes)-1]} de {ano}")
          
            return True
        
        else:
            print("\nNão foi possível converter a data, tente novamente.")
            return False
