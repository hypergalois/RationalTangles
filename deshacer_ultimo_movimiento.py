def deshacer_ultimo_movimiento(historial_tangles, historial_numeros, historial_fracciones, historial_movimientos):
    """
    Deshace el último movimiento y devuelve los estados anteriores del tangle y del par numérico.
    """
    if not historial_movimientos or len(historial_movimientos) <= 1:
        # Si no hay suficientes movimientos para deshacer, retornar los estados iniciales
        return "", (0, 1), [], []

    # Eliminar el último movimiento y obtener los estados anteriores
    historial_movimientos.pop()  # Remover el último movimiento
    historial_tangles.pop()  # Remover el último tangle
    historial_numeros.pop()  # Remover el último par numérico
    historial_fracciones.pop()  # Remover la última fracción continua

    # Obtener los estados anteriores al último movimiento
    tangle_anterior = historial_tangles[-1] if historial_tangles else ""
    par_numerico_anterior = historial_numeros[-1] if historial_numeros else (0, 1)
    fraccion_anterior = historial_fracciones[-1] if historial_fracciones else []

    return tangle_anterior, par_numerico_anterior, fraccion_anterior, historial_movimientos

# Ejemplo de uso de la función
historial_tangles_ejemplo = ["", "T^1", "T^1R", "T^1RT^1"]
historial_numeros_ejemplo = [(0, 1), (1, 1), (-1, 1), (-1, 2)]
historial_movimientos_ejemplo = ['T', 'R', 'T']
historial_fracciones_ejemplo = [[], [1], [1, 1], [1, 1, 1]]

tangle_anterior, par_numerico_anterior, fraccion_anterior, historial_movimientos_actualizado = deshacer_ultimo_movimiento(
    historial_tangles_ejemplo, 
    historial_numeros_ejemplo,
    historial_fracciones_ejemplo, 
    historial_movimientos_ejemplo
)

print(tangle_anterior, par_numerico_anterior, fraccion_anterior, historial_movimientos_actualizado)

