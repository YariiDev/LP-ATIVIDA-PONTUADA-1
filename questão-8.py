import os 

os.system("cls")
print("""
 =====VERDE AZUL AMARELO VERMELHO=====
      """)
cor = input("Digite a cor do produto: ").lower()
match cor:
    case "verde":
        print("O valor é R$ 10.00")
    case "azul":
        print("O valor é R$ 20.00")
    case "amarelo":
        print("O valor é R$ 30.00")
    case "vermelho":
        print("O valor é R$ 40.00")
    case _:
        print("Cor não reconhecida.")
