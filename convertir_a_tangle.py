def convertir_a_tangle(fraccion_continua):
    """
    Convierte una fracción continua en un tangle.
    :param fraccion_continua: La lista que representa la fracción continua.
    :return: Una cadena que representa el tangle.
    """
    tangle = ""
    for i, coeficiente in enumerate(fraccion_continua):
        # Ignorar los coeficientes que son 0, ya que T^0 es la identidad
        if coeficiente != 0:
            tangle += f"T^{coeficiente}"
            if i < len(fraccion_continua) - 1:  # No añadir 'R' después del último 'T'
                tangle += "R"
    return tangle

# Fracción continua de ejemplo [3, 7, 0]
fraccion_continua_ejemplo = [4, 3, 2]

# Convertir la fracción continua al tangle
tangle_resultante = convertir_a_tangle(fraccion_continua_ejemplo)
print(tangle_resultante)  

