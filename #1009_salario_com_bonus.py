vendedor = str(input())
salario_fixo = float(input())
total_vendas = float(input())
salario_total = (0.15 * total_vendas) + salario_fixo


print("TOTAL = R$","%.2f" % salario_total)