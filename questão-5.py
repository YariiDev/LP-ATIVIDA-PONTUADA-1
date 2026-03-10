import os 

os.system("cls")

numero = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))
operacao = input("Escolha qual operação + - * /: ")

match operacao:
    case "+":
        resultado = numero + numero_dois
    case "-":
        resultado = numero - numero_dois
    case "*":
        resultado = numero * numero_dois
    case "/":
        resultado = numero / numero_dois
    case _:
        resultado = "Operação inválida"

print(f"O resultado é: {resultado}")