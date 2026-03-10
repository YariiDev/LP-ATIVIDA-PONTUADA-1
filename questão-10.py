import os 

os.system("cls")

preco_alcool = 3.79
preco_gasolina = 6.59

litros = float(input("Digite a quantidade de litros: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()

if tipo_combustivel == "A":
    if litros <= 20:
        desconto = 0.02
else:
    desconto = 0.04

valor_bruto = litros * preco_alcool
valor_final = valor_bruto - (valor_bruto * desconto)

if tipo_combustivel == "G":
    if litros <= 25:
        desconto = 0.03
else:
    desconto = 0.05

valor_bruto = litros * preco_gasolina
valor_final = valor_bruto - (valor_bruto * desconto)

print(f"O valor a pagar é: R$ {valor_final:.2f}")