def actualizar_tangle(tangle_actual, nuevo_movimiento):
    """
    Añade un nuevo movimiento (T o R) al tangle actual.
    """
    if nuevo_movimiento == 'T':
        if not tangle_actual:
            return 'T'
        
        # Separar el tangle en componentes basados en 'T' y 'R'
        componentes = []
        temp = ''
        for char in tangle_actual:
            if char in 'TR' and temp:
                componentes.append(temp)
                temp = char
            else:
                temp += char
        componentes.append(temp)

        # Manejar la adición de una nueva 'T'
        if componentes[-1].startswith('T'):
            if '^' in componentes[-1]:
                partes = componentes[-1].split('^')
                potencia = int(partes[1]) + 1
                componentes[-1] = f"T^{potencia}"
            else:
                componentes[-1] = "T^2"
        else:
            componentes.append('T')

        tangle_actualizado = ''.join(componentes)

    elif nuevo_movimiento == 'R':
        tangle_actualizado = f"{tangle_actual}R"

    return tangle_actualizado

# Prueba de la función
tangle_inicial = ""
tangle_actualizado = actualizar_tangle(tangle_inicial, 'T')  # 'T'
tangle_actualizado = actualizar_tangle(tangle_actualizado, 'T')  # 'T^2'
tangle_actualizado = actualizar_tangle(tangle_actualizado, 'T')  # 'T^3'
tangle_actualizado = actualizar_tangle(tangle_actualizado, 'R')  # 'T^3R'
tangle_actualizado = actualizar_tangle(tangle_actualizado, 'T')  # 'T^3RT'
print(tangle_actualizado)  # Debería imprimir 'T^3RT'


