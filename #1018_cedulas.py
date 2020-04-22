valor = int(input())

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

nota_1 = aux_2 // 1

print(valor)
print(nota_100,"nota(s) de R$ 100,00")
print(nota_50,"nota(s) de R$ 50,00")
print(nota_20,"nota(s) de R$ 20,00")
print(nota_10,"nota(s) de R$ 10,00")
print(nota_5,"nota(s) de R$ 5,00")
print(nota_2,"nota(s) de R$ 2,00")
print(nota_1,"nota(s) de R$ 1,00")
