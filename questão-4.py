import os 

os.system("cls")

quantidade_morango = float(input("Digite a quantidade de morangos: "))
quantidade_maca = float(input("Digite a quantidade de maçãs: "))  

if quantidade_morango <= 5:
    total_morango = quantidade_morango * 2.50
else:
    total_morango = quantidade_morango * 2.20

if quantidade_maca <= 5:
    total_maca = quantidade_maca * 1.80
else:
    total_maca = quantidade_maca * 1.50

kg_total = quantidade_morango + quantidade_maca
valor_total = total_morango + total_maca

if kg_total > 10 or valor_total > 15.00:
    valor_total = valor_total * 0.90

print(f"O valor total a ser pago é: R$ {valor_total:.2f}")
