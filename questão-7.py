import os

os.system("cls")


nome_produto = input("Digite o nome do produto: ")
quantidade_do_produto = int(input("Digite a quantidade do produto: "))
preco_unitario = float(input("Digite o preço unitário: "))

total_bruto = quantidade_do_produto * preco_unitario


if quantidade_do_produto <= 5:
    desconto =  0.02

elif quantidade_do_produto <= 10:
    desconto = 0.03

else:
    desconto = 0.05


valor_desconto = total_bruto * desconto
total_a_pagar  =   total_bruto - valor_desconto

print(f"O valor total a ser pago pelo produto {nome_produto} é: R$ {total_a_pagar:.2f}")

