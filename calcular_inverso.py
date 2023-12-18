from fractions import Fraction
from operaciones import torsion, rotacion

def calcular_inverso(numerator, denominator):
    """
    Calcula el inverso de un número racional.
    
    :param numerator: El numerador del número racional.
    :param denominator: El denominador del número racional.
    :return: Un string que representa el enredo inverso.
    """
    tangle_number = Fraction(numerator, denominator)
    tangle = ""
    while tangle_number != 0:
        if tangle_number < 0:
            tangle += "T"
            tangle_number = torsion(tangle_number)
        else:
            tangle += "R"
            tangle_number = rotacion(tangle_number)

    return (tangle)
