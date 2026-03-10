import os

os.system("cls")
    
numero_um = float(input("Digite um valor: "))
numero_dois = float(input("Digite o segundo valor: "))
numero_tres = float(input("Digite o terceiro valor: "))

if numero_um + numero_dois < numero_tres:
    print(f"A soma do {numero_um} + {numero_dois} é menor que {numero_tres}.")
else:
    print(f"A soma do {numero_um} + {numero_dois} é maior que {numero_tres}.")