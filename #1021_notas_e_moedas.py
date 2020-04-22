valor = float(input())

nota_100 = valor // 100
aux_100 = valor % 100

nota_50 = aux_100 // 50
aux_50 = aux_100 % 50

nota_20 = aux_50 // 20
aux_20 = aux_50 % 20

nota_10 = aux_20 // 10
aux_10 = aux_20 % 10

nota_5 = aux_10 // 5
aux_5 = aux_10 % 5

nota_2 = aux_5 // 2
aux_2 = aux_5 % 2

moeda_1 = aux_2 // 1
aux_1 = aux_2 % 1

moeda_050 = aux_1 // 0.5
aux_050 = aux_1 % 0.5

moeda_025 = aux_050 // 0.25
aux_025 = aux_050 % 0.25

moeda_010 = aux_025 // 0.10
aux_010 = aux_025 % 0.10

moeda_005 = aux_010 // 0.05
aux_005 = aux_010 % 0.05

moeda_001 = aux_005 // 0.01
aux_001 = aux_005 % 0.01

print(aux_001)
print("NOTAS:")
print("{:.0f} nota(s) de R$ 100,00"   .format(nota_100))
print("{:.0f} nota(s) de R$ 50,00"    .format(nota_50))
print("{:.0f} nota(s) de R$ 20,00"    .format(nota_20))
print("{:.0f} nota(s) de R$ 10,00"    .format(nota_10))
print("{:.0f} nota(s) de R$ 5,00"     .format(nota_5))
print("{:.0f} nota(s) de R$ 2,00"     .format(nota_2))
print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1,00"    .format(moeda_1))
print("{:.0f} moeda(s) de R$ 0,50"    .format(moeda_050))
print("{:.0f} moeda(s) de R$ 0,25"    .format(moeda_025))
print("{:.0f} moeda(s) de R$ 0,10"    .format(moeda_010))
print("{:.0f} moeda(s) de R$ 0,05"    .format(moeda_005))
print("{:.0f} moeda(s) de R$ 0,01"    .format(moeda_001))