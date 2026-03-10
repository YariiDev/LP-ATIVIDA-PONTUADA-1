import os

os.system("cls")

nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
media = (nota_um + nota_dois) / 2

if media >= 6.0:
    print("Parabens vc esta aprovado")
elif media >= 4.0:
    print("Voce esta de recuperação")
else:
    print("Voce esta reprovado")