import streamlit as st

# Funciones para realizar las conversiones
from convertir_a_fraccion_continua import convertir_a_fraccion_continua
from convertir_a_tangle import convertir_a_tangle
from calcular_numero_racional_desde_tangle import calcular_numero_racional_como_par
from imprimir_fraccion_continua import imprimir_fraccion_continua_markdown
from actualizar_tangle import actualizar_tangle
from deshacer_ultimo_movimiento import deshacer_ultimo_movimiento
from calcular_inverso import calcular_inverso

import re
from PIL import Image
import requests
from io import BytesIO

image_url = "https://i.ibb.co/JzxGZx1/john-horton-conway-cce2e129-4f44-42cf-b3e8-bd390287f9e-resize-750-removebg-preview.png"

def es_entrada_valida(tangle_input):
    # Patrón de expresión regular para validar la entrada
    patron = r'^([RT](\^\d+)?)+$'
    return bool(re.match(patron, tangle_input))

sidebar_text = """
### Acerca de la Aplicación

Esta aplicación interactiva ofrece una herramienta para explorar el fascinante mundo de los enredos racionales de Conway.

**Funcionalidades:**

- **Conversión de Números Racionales a Enredos:** Introduce un número racional y observa su correspondiente enredo.
  
- **Conversión de Enredos a Números Racionales:** Explora cómo una secuencia de movimientos de rotación y torsión se traduce de nuevo a un número racional, revelando la relación entre estos dos mundos.
  
- **Análisis Interactivo de Tangles:** Manipula enredos en tiempo real para ver cómo afectan al número racional resultante, permitiendo un aprendizaje profundo y una experimentación intuitiva.

**¡Explora, aprende y diviértete!**

"""

def main():
    st.title('🤖 Calculadora de Enredos Racionales de Conway 🤖')
    st.markdown("Autor: [José Delgado](https://github.com/hypergalois/rationalTangles)")
    
    st.markdown("""
            <style>
            div.stButton > button:first-child {background-color: #4fa8f6; color: white;}
            </style>""", unsafe_allow_html=True)    
    
    st.sidebar.title('Bienvenido')
    # Hacer una solicitud para obtener el contenido de la imagen
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    
    # Mostrar la imagen en la barra lateral
    st.sidebar.image(image, caption='John Conway', use_column_width=True)
    
    st.sidebar.markdown(sidebar_text)
    
    st.header('1. Conversión de Número Racional a Enredo')
    
    with st.expander("Enredo Racional"):
        st.write("Un enredo racional es cualquier enredo que puede ser obtenido mediante las operaciones de Torsión y Rotación. A cada enredo le asociamos un número racional que lo describe únicamente y viceversa.")

    with st.form(key='mi_formulario'):
        col_num, col_den = st.columns(2)

        with col_num:
            numerador = st.text_input('Ingrese el numerador:', '18', key='numerador')

        with col_den:
            denominador = st.text_input('Ingrese el denominador:', '11', key='denominador')

        submit_button = st.form_submit_button(label='Convertir a Enredo')

    if submit_button:
        try:
            numerador = int(numerador) if numerador else 0
            denominador = int(denominador) if denominador else 1
            if denominador == 0:
                st.error("El denominador no puede ser cero.")
            else:
                fraccion_continua = convertir_a_fraccion_continua(numerador, denominador)
                tangle = convertir_a_tangle(fraccion_continua)
                
                st.latex(f'\\frac{{{numerador}}}{{{denominador}}} \sim {tangle}')
                st.latex(f'{imprimir_fraccion_continua_markdown(fraccion_continua)}')
                        
        except ValueError:
            st.error("Por favor, ingrese solo números enteros.")

            
    st.header('2. Conversión de Enredo a Número Racional')

    with st.form(key='form_tangle_racional'):
        tangle_input = st.text_input('Ingrese una secuencia de enredo (ejemplo: "RTTRT"):', 'T^3RT^2RT^2RT')
        
        submit_button = st.form_submit_button(label='Convertir a Número Racional')

    if submit_button:
        if es_entrada_valida(tangle_input):
            numerador, denominador = calcular_numero_racional_como_par(tangle_input)
            fraccion_continua = convertir_a_fraccion_continua(numerador, denominador)
            st.latex(f'{tangle_input} \sim \\frac{{{numerador}}}{{{denominador}}}')
            st.latex(f'{imprimir_fraccion_continua_markdown(fraccion_continua)}')
        else:
            st.error("Entrada inválida. Por favor, ingrese una secuencia válida con 'R', 'T', '^' y números naturales.")
    
    st.header('3. Construcción y Análisis de Enredos')
    if 'tangle' not in st.session_state:
        st.session_state.tangle = ""
        st.session_state.tangle_number = (0, 1)
        st.session_state.historial_movimientos = []
        st.session_state.historial_tangles = [st.session_state.tangle]
        st.session_state.historial_numeros = [st.session_state.tangle_number]
        st.session_state.fraccion_continua = []
        st.session_state.historial_fracciones = [st.session_state.fraccion_continua]

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:

        if st.button("Rotación (R)"):
            st.session_state.tangle = actualizar_tangle(st.session_state.tangle, 'R')
            st.session_state.tangle_number = calcular_numero_racional_como_par(st.session_state.tangle)
            st.session_state.fraccion_continua = convertir_a_fraccion_continua(st.session_state.tangle_number[0], st.session_state.tangle_number[1])
            st.session_state.historial_movimientos.append('R')
            st.session_state.historial_tangles.append(st.session_state.tangle)
            st.session_state.historial_numeros.append(st.session_state.tangle_number)
            st.session_state.historial_fracciones.append(st.session_state.fraccion_continua)
        
    with col2:
        if st.button("Torsión (T)"):
            st.session_state.tangle = actualizar_tangle(st.session_state.tangle, 'T')
            st.session_state.tangle_number = calcular_numero_racional_como_par(st.session_state.tangle)
            st.session_state.fraccion_continua = convertir_a_fraccion_continua(st.session_state.tangle_number[0], st.session_state.tangle_number[1])
            st.session_state.historial_movimientos.append('T')
            st.session_state.historial_tangles.append(st.session_state.tangle)
            st.session_state.historial_numeros.append(st.session_state.tangle_number)
            st.session_state.historial_fracciones.append(st.session_state.fraccion_continua)

    with col3:       
        if st.button("Deshacer"):
            if len(st.session_state.historial_movimientos) > 0:
                tangle_anterior, par_numerico_anterior, fraccion_anterior, historial_movimientos_anterior = deshacer_ultimo_movimiento(st.session_state.historial_tangles, st.session_state.historial_numeros, st.session_state.historial_fracciones, st.session_state.historial_movimientos)
            
                st.session_state.tangle = tangle_anterior
                st.session_state.tangle_number = par_numerico_anterior
                st.session_state.historial_movimientos = historial_movimientos_anterior
                st.session_state.fraccion_continua = fraccion_anterior
            else:
                st.error("No hay movimientos para deshacer.")

        
    with col4:
        if st.button("Reiniciar"):
            st.session_state.tangle = ""
            st.session_state.tangle_number = (0, 1)
            st.session_state.historial_movimientos = []
            st.session_state.historial_tangles = [st.session_state.tangle]
            st.session_state.historial_numeros = [st.session_state.tangle_number]
            st.session_state.fraccion_continua = []
            st.session_state.historial_fracciones = [st.session_state.fraccion_continua]

    st.markdown("#### Numero Enredo")
    if st.session_state.tangle_number != (0, 1):
        st.latex(f"\\frac{{{st.session_state.tangle_number[0]}}}{{{st.session_state.tangle_number[1]}}}")

    st.markdown("#### Palabra Enredo")
    if st.session_state.tangle != "":
        st.latex(f"{st.session_state.tangle}")

    st.markdown("#### Fracción Continua")
    if st.session_state.fraccion_continua != []:
        st.latex(f"{imprimir_fraccion_continua_markdown(st.session_state.fraccion_continua)}")

    st.markdown("#### Enredo Inverso")
    if st.session_state.fraccion_continua != []:
        st.latex(f"{calcular_inverso(st.session_state.tangle_number[0], st.session_state.tangle_number[1])}")

if __name__ == '__main__':
    main()
