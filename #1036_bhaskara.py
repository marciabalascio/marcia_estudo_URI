import math


def main():
    a, b, c = map(float, input().split())
    imprime_raizes(a,b,c)
    
    
def delta(a,b,c):
    return b ** 2 - 4* a* c


def imprime_raizes(a,b,c):
    d = delta(a,b,c)
    
    
    
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print("a raiz desta equação é %0.5f" %raiz1)
    else:
        if d < 0 or a == 0:
            print("Impossivel calcular")
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print("R1 = %0.5f" %raiz1)
            print("R2 = %0.5f" %raiz2)

main()