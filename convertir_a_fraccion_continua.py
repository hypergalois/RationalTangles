import math

def convertir_a_fraccion_continua(numerador, denominador):
    """
    Convierte un número racional en una fracción continua, utilizando el redondeo hacia arriba.
    
    :param numerador: El numerador del número racional.
    :param denominador: El denominador del número racional.
    :return: Una lista que representa la fracción continua.
    """
    fraccion_continua = []
    while denominador:
        # Usar math.ceil para asegurarse de que el cociente siempre se redondea hacia arriba.
        cociente = math.ceil(numerador / denominador)
        # fraccion_continua.append(cociente)
        fraccion_continua.insert(0, cociente)
        numerador = cociente * denominador - numerador  # Actualizar el numerador
        numerador, denominador = denominador, numerador  # Invertir la fracción para el siguiente paso

    return fraccion_continua  # El último término es siempre 1, que se puede omitir.

# Probar la función con el número racional 18/11
fraccion_continua = convertir_a_fraccion_continua(-3,20)
print(fraccion_continua)
