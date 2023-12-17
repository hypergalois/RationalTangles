from fractions import Fraction
import math

def calcular_numero_racional_como_par(tangle):
    def torsion(x):
        return x + 1

    def rotacion(x):
        if x == 0:
            return float('inf')  # Evitar la división por cero
        return -1 / x

    x = 0
    i = 0

    while i < len(tangle):
        if tangle[i] == 'T':
            potencia = 1
            i += 1
            if i < len(tangle) and tangle[i] == '^':
                i += 1
                start = i
                while i < len(tangle) and tangle[i].isdigit():
                    i += 1
                potencia = int(tangle[start:i]) if i > start else 1
            for _ in range(potencia):
                x = torsion(x)
        elif tangle[i] == 'R':
            x = rotacion(x)
            i += 1

    # Comprobar si x es infinito
    if math.isinf(x):
        return (0, 0)  # Devolver un valor especial para representar infinito

    fraccion = Fraction(x).limit_denominator()
    return (fraccion.numerator, fraccion.denominator)

# Prueba
print(calcular_numero_racional_como_par("T^2RT^3RT^2RT^2"))  # Ejemplo
# print(calcular_numero_racional_como_par("T^2T"))  # Ejemplo
