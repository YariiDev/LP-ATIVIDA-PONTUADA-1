import os

os.system("cls")

nome = input("Digite seu nome: ")
sexo = "feminino"
estado_civil ="casada"

confirmacao_do_sexo = input("Digite seu sexo: ").lower()
confirmacao_do_estado_civil = input("Digite seu estado civil: ").lower()

if confirmacao_do_sexo == sexo and confirmacao_do_estado_civil == estado_civil:
    resultado = float(input("Digite quanto tempo de casada: "))
else:
    exit()

print(f"Nome: {nome}")
print(f"Sexo: {confirmacao_do_sexo}")
print(f"Estado Civil: {confirmacao_do_estado_civil}")
print(f"Tempo de Casamento: {resultado}")
