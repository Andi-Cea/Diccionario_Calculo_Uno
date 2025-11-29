import streamlit as st
import numpy as np
import sympy as sp

def app():
    st.title("🎯 Ejercicios Interactivos - Cálculo I: Funciones")
    
    # Menú de temas
    tema = st.sidebar.selectbox(
        "Selecciona un tema:",
        [
            "2.1 Definición de Función",
            "2.2 Notación y Valor Numérico",
            "2.3 Dominio y Rango",
            "2.4 Funciones Inyectivas, Sobreyectivas y Biyectivas",
            "2.5 Operaciones entre Funciones",
            "2.6 Gráficas de Funciones"
        ]
    )
    
    # Inicializar estado de la sesión
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'exercises_completed' not in st.session_state:
        st.session_state.exercises_completed = 0
    
    # Diccionario de temas
    temas = {
        "2.1 Definición de Función": definicion_funcion,
        "2.2 Notación y Valor Numérico": notacion_valor,
        "2.3 Dominio y Rango": dominio_rango,
        "2.4 Funciones Inyectivas, Sobreyectivas y Biyectivas": tipos_funciones,
        "2.5 Operaciones entre Funciones": operaciones_funciones,
        "2.6 Gráficas de Funciones": graficas_funciones
    }
    
    # Mostrar puntuación
    st.sidebar.markdown("---")
    st.sidebar.metric("🏆 Puntuación", st.session_state.score)
    st.sidebar.metric("✅ Ejercicios Completados", st.session_state.exercises_completed)
    
    if st.sidebar.button("🔄 Reiniciar Puntuación"):
        st.session_state.score = 0
        st.session_state.exercises_completed = 0
        st.rerun()
    
    # Ejecutar tema seleccionado
    if tema in temas:
        temas[tema]()

def check_answer(correct_answer, user_answer, tolerance=0.01):
    """Verifica si la respuesta del usuario es correcta"""
    try:
        # Para respuestas numéricas
        if isinstance(correct_answer, (int, float)):
            if abs(float(correct_answer) - float(user_answer)) <= tolerance:
                st.session_state.score += 10
                st.session_state.exercises_completed += 1
                st.success("🎉 ¡Correcto! +10 puntos")
                return True
            else:
                st.error("❌ Incorrecto. Intenta nuevamente.")
                return False
        # Para respuestas de texto
        elif str(correct_answer).lower() == str(user_answer).lower():
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! +10 puntos")
            return True
        else:
            st.error("❌ Incorrecto. Intenta nuevamente.")
            return False
    except:
        st.error("❌ Formato inválido.")
        return False

def definicion_funcion():
    st.header("🔍 2.1 Definición de Función")
    
    st.info("Determina si los siguientes diagramas representan funciones o relaciones")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Diagrama de Flechas")
    st.write("Dados los conjuntos:")
    st.write("A = {2, 3, 4, 5}, B = {4, 9, 16, 25}")
    st.write("Con el mapeo: 2→4, 3→9, 4→16, 5→25")
    
    opcion1 = st.radio(
        "¿Este diagrama representa una función o una relación?",
        ["Función", "Relación"],
        key="diag1"
    )
    
    if st.button("Verificar Ejercicio 1", key="check1"):
        if opcion1 == "Función":
            check_answer("correcto", "correcto")
        else:
            st.error("❌ Incorrecto. Cada elemento de A se mapea a un único elemento de B")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Diagrama con Múltiples Salidas")
    st.write("Dados los conjuntos:")
    st.write("A = {2, 4, 5}, B = {9, 8, 3, 2}")
    st.write("Con el mapeo: 2→9, 4→8, 5→3, 2→2")
    
    opcion2 = st.radio(
        "¿Este diagrama representa una función o una relación?",
        ["Función", "Relación"],
        key="diag2"
    )
    
    if st.button("Verificar Ejercicio 2", key="check2"):
        if opcion2 == "Relación":
            check_answer("correcto", "correcto")
        else:
            st.error("❌ Incorrecto. El elemento 2 tiene dos imágenes diferentes")

def notacion_valor():
    st.header("📝 2.2 Notación y Valor Numérico")
    
    st.info("Calcula el valor de funciones para valores específicos")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Función Cuadrática")
    st.latex(r"f(x) = 3x^2 - 5x - 2")
    st.write("Calcula f(-3)")
    
    user_f1 = st.number_input("f(-3) =", value=0.0, step=1.0, key="f1")
    
    if st.button("Verificar f(-3)", key="check_f1"):
        correct_f1 = 3*(-3)**2 - 5*(-3) - 2
        check_answer(correct_f1, user_f1, 0.1)
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Función Racional")
    st.latex(r"f(x) = \frac{3x - 1}{5 - x}")
    st.write("Calcula f(3/4)")
    
    user_f2 = st.number_input("f(3/4) =", value=0.0, step=0.1, format="%.3f", key="f2")
    
    if st.button("Verificar f(3/4)", key="check_f2"):
        correct_f2 = (3*(3/4) - 1) / (5 - (3/4))
        check_answer(correct_f2, user_f2, 0.001)

def dominio_rango():
    st.header("📊 2.3 Dominio y Rango")
    
    st.info("Determina el dominio de las siguientes funciones")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Función con Raíz en Denominador")
    st.latex(r"f(x) = \frac{1}{\sqrt{x^2 - 1}}")
    
    dominio_opcion1 = st.radio(
        "¿Cuál es el dominio de esta función?",
        [
            "Todos los números reales",
            "x < -1 o x > 1", 
            "-1 ≤ x ≤ 1",
            "x ≠ 0"
        ],
        key="dom1"
    )
    
    if st.button("Verificar Dominio 1", key="check_dom1"):
        if dominio_opcion1 == "x < -1 o x > 1":
            check_answer("correcto", "correcto")
        else:
            st.error("❌ Incorrecto. El radicando debe ser positivo y el denominador no cero")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Función Racional")
    st.latex(r"f(x) = \frac{x + 2}{x^2 - 3x - 40}")
    
    user_dom2 = st.text_input("Escribe el dominio en notación de conjuntos (ej: R-{a,b}):", key="dom2_input")
    
    if st.button("Verificar Dominio 2", key="check_dom2"):
        if user_dom2.lower() in ["r-{-5,8}", "r-{8,-5}", "todos los reales excepto -5 y 8"]:
            check_answer("correcto", "correcto")
        else:
            st.error("❌ Incorrecto. Factoriza el denominador: (x+5)(x-8)")

def tipos_funciones():
    st.header("🎯 2.4 Funciones Inyectivas, Sobreyectivas y Biyectivas")
    
    st.info("Identifica el tipo de función")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Función Lineal")
    st.latex(r"f: \mathbb{Z} \to \mathbb{Z}, \quad f(k) = 3k + 1")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        inyectiva1 = st.checkbox("Inyectiva", key="iny1")
    with col2:
        sobreyectiva1 = st.checkbox("Sobreyectiva", key="sob1")
    with col3:
        biyectiva1 = st.checkbox("Biyectiva", key="biy1")
    
    if st.button("Verificar Tipo 1", key="check_tipo1"):
        if inyectiva1 and not sobreyectiva1 and not biyectiva1:
            check_answer("correcto", "correcto")
        else:
            st.error("❌ Incorrecto. Es inyectiva pero no sobreyectiva sobre Z")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Función con Restricción")
    st.latex(r"f: \mathbb{R}-\{\frac{1}{2}\} \to \mathbb{R}-\{-\frac{1}{2}\}, \quad f(x) = \frac{x + 1}{1 - 2x}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        inyectiva2 = st.checkbox("Inyectiva", key="iny2")
    with col2:
        sobreyectiva2 = st.checkbox("Sobreyectiva", key="sob2")
    with col3:
        biyectiva2 = st.checkbox("Biyectiva", key="biy2")
    
    if st.button("Verificar Tipo 2", key="check_tipo2"):
        if inyectiva2 and sobreyectiva2 and biyectiva2:
            check_answer("correcto", "correcto")
        else:
            st.error("❌ Incorrecto. Esta función es biyectiva con los dominios dados")

def operaciones_funciones():
    st.header("🔄 2.5 Operaciones entre Funciones")
    
    st.info("Realiza operaciones con funciones")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Suma de Funciones")
    st.latex(r"f(x) = x^2 - 3x, \quad g(x) = \sqrt{2x + 1}")
    st.write("Calcula (f + g)(x) y determina su dominio")
    
    user_sum = st.text_input("(f + g)(x) =", key="sum_input")
    user_dom_sum = st.text_input("Dominio de (f + g) en notación de intervalo:", key="dom_sum")
    
    if st.button("Verificar Suma", key="check_sum"):
        if user_sum.lower() == "x^2 - 3x + sqrt(2x + 1)" and user_dom_sum.lower() == "[-1/2, ∞)":
            st.session_state.score += 20
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Ambas respuestas correctas! +20 puntos")
        elif user_sum.lower() == "x^2 - 3x + sqrt(2x + 1)":
            st.success("✅ Expresión correcta, pero verifica el dominio")
        elif user_dom_sum.lower() == "[-1/2, ∞)":
            st.success("✅ Dominio correcto, pero verifica la expresión")
        else:
            st.error("❌ Revisa ambas respuestas")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Composición de Funciones")
    st.latex(r"f(x) = 4x + 6, \quad g(x) = x + \sqrt{x}")
    st.write("Calcula (g ∘ f)(x)")
    
    user_comp = st.text_input("(g ∘ f)(x) =", key="comp_input")
    
    if st.button("Verificar Composición", key="check_comp"):
        correct_comp = "4x + 6 + sqrt(4x + 6)"
        if user_comp.lower().replace(" ", "") == correct_comp.replace(" ", ""):
            check_answer("correcto", "correcto")
        else:
            st.error("❌ Recuerda: (g ∘ f)(x) = g(f(x))")

def graficas_funciones():
    st.header("📈 2.6 Gráficas de Funciones")
    
    st.info("Analiza gráficas y funciones especiales")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Función Valor Absoluto")
    st.latex(r"f(x) = |x|")
    
    st.write("¿La función valor absoluto pasa la prueba de la recta vertical?")
    
    opcion_abs = st.radio(
        "Selecciona la respuesta correcta:",
        [
            "Sí, es una función",
            "No, es una relación",
            "Depende del dominio",
            "Solo para x ≥ 0"
        ],
        key="abs_q"
    )
    
    if st.button("Verificar Valor Absoluto", key="check_abs"):
        if opcion_abs == "Sí, es una función":
            check_answer("correcto", "correcto")
        else:
            st.error("❌ Incorrecto. |x| sí es una función")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Función Mayor Entero")
    st.latex(r"f(x) = [x] = \text{máximo } \{k \in \mathbb{Z} : k \leq x\}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        user_34 = st.number_input("[3.4] =", value=0, step=1, key="ceil1")
    with col2:
        user_08 = st.number_input("[0.8] =", value=0, step=1, key="ceil2")
    with col3:
        user_12 = st.number_input("[-1.2] =", value=0, step=1, key="ceil3")
    
    if st.button("Verificar Mayor Entero", key="check_ceil"):
        correct_34 = 3
        correct_08 = 0
        correct_12 = -2
        
        if user_34 == correct_34 and user_08 == correct_08 and user_12 == correct_12:
            st.session_state.score += 15
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Todas correctas! +15 puntos")
        elif user_34 == correct_34 and user_08 == correct_08:
            st.success("✅ 2 de 3 correctas")
        elif user_34 == correct_34 and user_12 == correct_12:
            st.success("✅ 2 de 3 correctas")
        elif user_08 == correct_08 and user_12 == correct_12:
            st.success("✅ 2 de 3 correctas")
        else:
            st.error("❌ Revisa los cálculos. Recuerda que [x] es el mayor entero ≤ x")