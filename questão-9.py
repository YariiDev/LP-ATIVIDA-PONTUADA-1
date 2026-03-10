
renda_mensal = float(input("Digite a renda mensal do solicitante: R$ "))
valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado: R$ "))
num_prestacoes = int(input("Digite o número de prestações desejadas: "))
valor_prestacao = valor_emprestimo / num_prestacoes
limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30

criterio_um = valor_emprestimo <= limite_emprestimo
criterio_dois = valor_prestacao <= limite_prestacao

if criterio_um and criterio_dois:
        print("Empréstimo CONCEDIDO!")
        print(f"Valor da parcela: R$ {valor_prestacao:.2f} em {num_prestacoes}x")
else:
        print("Empréstimo NEGADO:")
        
