dias_totais = int(input())

anos = dias_totais // 365
anos_aux = dias_totais % 365

meses = anos_aux // 30
meses_aux = anos_aux % 30

dias_restantes = meses_aux

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias_restantes, "dia(s)")