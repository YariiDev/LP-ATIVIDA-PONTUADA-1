import os

os.system("cls")

numero = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))

if numero == numero_dois:
        resultado = numero + numero_dois
else:
        resultado = numero * numero_dois

print(f"O resultado é {resultado}")

