def torsion(x):
    return x + 1

def rotacion(x):
    if x == 0:
        return float('inf')  # Evitar la división por cero
    return -1 / x