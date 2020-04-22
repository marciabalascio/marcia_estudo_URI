dados = input().split(" ")

a, b, c = dados

maiorAB = ( (int(a) + int(b)) + abs(int(a) - int(b)) ) / 2
maiorBC = ( (int(c) + int(b)) + abs(int(c) - int(b)) ) / 2
maior = ( (int(maiorAB) + int(maiorBC)) + abs(int(maiorAB) - int(maiorBC)) ) / 2


print(int(maior), "eh o maior")