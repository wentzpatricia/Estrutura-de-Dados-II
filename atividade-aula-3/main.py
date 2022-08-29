from conversor import conversorDeDatas

def menu():

    return input(("\n"*2)+f"""
    ===============================
    -------------------------------
                 MENU
    -------------------------------
    0- Finalizar o Programa
    1- Converter datas para extenso
    -------------------------------
    ===============================
        Escolha: """)

while True:
    teclado = menu()
    if teclado =="0": 
        print("Programa finalizado.")
        break
    elif teclado == "1": conversorDeDatas() 
    else: 
        print("Opção inválida ):")
        break