def imprimir_fraccion_continua_markdown(fraccion_continua):
    """
    Convierte una fracción continua en una cadena en formato Markdown para matemáticas.
    :param fraccion_continua: La lista que representa la fracción continua.
    :return: Una cadena en formato Markdown que representa la fracción continua.
    """
    if not fraccion_continua:
        return ""
    
    # Invertir la fracción continua
    fraccion_continua = fraccion_continua[::-1]

    # Iniciar con el último elemento (invertir la fracción continua)
    markdown = f"{fraccion_continua[-1]}"
    for i in range(len(fraccion_continua) - 2, -1, -1):
        markdown = f"{fraccion_continua[i]} - \\frac{{1}}{{{markdown}}}"

    return markdown

# Ejemplo de uso de la función
fraccion_continua_ejemplo = [3, 7, 0]
markdown_fraccion_continua = imprimir_fraccion_continua_markdown(fraccion_continua_ejemplo)
print(markdown_fraccion_continua)

# Ojo con esos parentesis del ultimo elemento quedan mal, no se como sera el markdwon de streamlit