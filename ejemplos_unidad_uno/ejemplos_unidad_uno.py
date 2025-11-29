import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def app():
    st.title("🎯 Ejercicios Interactivos - Cálculo I")
    
    # Menú de temas
    tema = st.sidebar.selectbox(
        "Selecciona un tema:",
        [
            "1.1 Axiomas de Campo y Orden",
            "1.2 Conjuntos Infinitos", 
            "1.3 Teoremas Números Reales",
            "1.4 Intervalos",
            "1.5 Valor Absoluto"
        ]
    )
    
    # Inicializar estado de la sesión
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'exercises_completed' not in st.session_state:
        st.session_state.exercises_completed = 0
    
    # Diccionario de temas
    temas = {
        "1.1 Axiomas de Campo y Orden": axiomas_campo_orden,
        "1.2 Conjuntos Infinitos": conjuntos_infinitos,
        "1.3 Teoremas Números Reales": teoremas_reales,
        "1.4 Intervalos": intervalos,
        "1.5 Valor Absoluto": valor_absoluto
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
        if abs(float(correct_answer) - float(user_answer)) <= tolerance:
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! +10 puntos")
            return True
        else:
            st.error("❌ Incorrecto. Intenta nuevamente.")
            return False
    except:
        st.error("❌ Formato inválido. Usa números.")
        return False

def axiomas_campo_orden():
    st.header("🔢 Axiomas de Campo y Orden")
    
    st.info("Practica los axiomas de cuerpo y propiedades de orden")
    
    # Ejercicio 1 - Propiedad conmutativa
    st.subheader("Ejercicio 1: Propiedad Conmutativa")
    st.write("Si a + b = 8 y b + a = 8, ¿qué propiedad se está aplicando?")
    
    propiedad = st.radio(
        "Selecciona la propiedad correcta:",
        ["Propiedad Asociativa", "Propiedad Conmutativa", "Propiedad Distributiva", "Elemento Neutro"],
        key="prop1"
    )
    
    if st.button("Verificar Propiedad 1", key="check_prop1"):
        if propiedad == "Propiedad Conmutativa":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! La conmutatividad establece que a+b = b+a")
        else:
            st.error("❌ Incorrecto. Revisa la propiedad conmutativa")
    
    # Ejercicio 2 - Orden
    st.subheader("Ejercicio 2: Propiedades de Orden")
    st.write("Si a < b y c > 0, ¿cómo se relaciona ac con bc?")
    
    relacion = st.radio(
        "Selecciona la relación correcta:",
        ["ac > bc", "ac < bc", "ac = bc", "No se puede determinar"],
        key="orden1"
    )
    
    if st.button("Verificar Orden", key="check_orden"):
        if relacion == "ac < bc":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Al multiplicar por positivo se mantiene la desigualdad")
        else:
            st.error("❌ Incorrecto. Si c > 0, la desigualdad se mantiene")

def conjuntos_infinitos():
    st.header("∞ Conjuntos Infinitos")
    
    st.info("Identifica conjuntos numerables y no numerables")
    
    # Ejercicio 1 - Conjuntos numerables
    st.subheader("Ejercicio 1: Conjuntos Numerables")
    st.write("¿Cuál de estos conjuntos es numerable?")
    
    conjunto = st.radio(
        "Selecciona el conjunto numerable:",
        [
            "Los números reales entre 0 y 1",
            "Los números racionales Q", 
            "Los números irracionales",
            "El conjunto potencia de los naturales"
        ],
        key="numerable"
    )
    
    if st.button("Verificar Numerable", key="check_numerable"):
        if conjunto == "Los números racionales Q":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Los racionales son numerables")
        else:
            st.error("❌ Incorrecto. Solo los racionales son numerables")
    
    # Ejercicio 2 - Cardinalidad
    st.subheader("Ejercicio 2: Cardinalidad Infinita")
    st.write("¿Cuál es la cardinalidad del conjunto de los números naturales?")
    
    cardinalidad = st.radio(
        "Selecciona la respuesta correcta:",
        ["ℵ₀ (aleph cero)", "c (continuo)", "Finita", "No definida"],
        key="cardinal"
    )
    
    if st.button("Verificar Cardinalidad", key="check_cardinal"):
        if cardinalidad == "ℵ₀ (aleph cero)":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Los naturales tienen cardinalidad ℵ₀")
        else:
            st.error("❌ Incorrecto. Los naturales son el conjunto infinito más pequeño")

def teoremas_reales():
    st.header("📐 Teoremas sobre Números Reales")
    
    st.info("Aplica teoremas fundamentales de los números reales")
    
    # Ejercicio 1 - Producto cero
    st.subheader("Ejercicio 1: Teorema del Producto Cero")
    st.write("Si (x - 2)(x + 3) = 0, ¿cuáles son los posibles valores de x?")
    
    col1, col2 = st.columns(2)
    with col1:
        x1 = st.number_input("Primer valor de x:", value=0, key="x1")
    with col2:
        x2 = st.number_input("Segundo valor de x:", value=0, key="x2")
    
    if st.button("Verificar Soluciones", key="check_sol"):
        correctos = {2, -3}
        usuario = {x1, x2}
        if correctos == usuario:
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! x = 2 o x = -3")
        else:
            st.error("❌ Incorrecto. Las soluciones son x = 2 y x = -3")
    
    # Ejercicio 2 - Propiedad arquimediana
    st.subheader("Ejercicio 2: Propiedad Arquimediana")
    st.write("Para x = 5.7, encuentra un número natural n tal que n > x")
    
    n_value = st.number_input("Ingresa un natural n > 5.7:", value=0, step=1, min_value=0)
    
    if st.button("Verificar Natural", key="check_nat"):
        if n_value > 5.7 and n_value == int(n_value):
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success(f"🎉 ¡Correcto! {n_value} > 5.7")
        else:
            st.error("❌ Debe ser un número natural mayor que 5.7")

def intervalos():
    st.header("📊 Intervalos")
    
    st.info("Trabaja con notación de intervalos y desigualdades")
    
    # Ejercicio 1 - Notación de intervalo
    st.subheader("Ejercicio 1: Notación de Intervalo")
    st.write("Convierte a notación de intervalo: {x ∈ ℝ | -2 ≤ x < 3}")
    
    intervalo = st.radio(
        "Selecciona el intervalo correcto:",
        ["(-2, 3)", "[-2, 3)", "(-2, 3]", "[-2, 3]"],
        key="intervalo1"
    )
    
    if st.button("Verificar Intervalo", key="check_interval"):
        if intervalo == "[-2, 3)":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! [-2, 3) incluye -2 y excluye 3")
        else:
            st.error("❌ Incorrecto. Revisa los extremos incluidos/excluidos")
    
    # Ejercicio 2 - Operaciones con intervalos
    st.subheader("Ejercicio 2: Intersección de Intervalos")
    st.write("Encuentra la intersección de: [-1, 4] ∩ (2, 6)")
    
    interseccion = st.radio(
        "Selecciona la intersección correcta:",
        ["[-1, 6)", "(2, 4]", "[2, 4]", "(2, 4]"],
        key="inter"
    )
    
    if st.button("Verificar Intersección", key="check_inter"):
        if interseccion == "(2, 4]":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! La intersección va desde >2 hasta ≤4")
        else:
            st.error("❌ Incorrecto. La intersección es (2, 4]")

def valor_absoluto():
    st.header("🔍 Valor Absoluto")
    
    st.info("Resuelve ecuaciones y desigualdades con valor absoluto")
    
    # Ejercicio 1 - Ecuación con valor absoluto
    st.subheader("Ejercicio 1: Ecuación con Valor Absoluto")
    st.write("Resuelve: |x - 3| = 5")
    
    col1, col2 = st.columns(2)
    with col1:
        sol1 = st.number_input("Primera solución:", value=0, key="sol1")
    with col2:
        sol2 = st.number_input("Segunda solución:", value=0, key="sol2")
    
    if st.button("Verificar Ecuación", key="check_abs_eq"):
        correctas = {8, -2}
        usuario = {sol1, sol2}
        if correctas == usuario:
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! x = 8 o x = -2")
        else:
            st.error("❌ Incorrecto. Las soluciones son x = 8 y x = -2")
    
    # Ejercicio 2 - Desigualdad con valor absoluto
    st.subheader("Ejercicio 2: Desigualdad con Valor Absoluto")
    st.write("Resuelve: |x + 1| < 4")
    
    desigualdad = st.radio(
        "Selecciona el intervalo solución:",
        ["(-5, 3)", "(-3, 5)", "(-∞, -5) ∪ (3, ∞)", "(-5, 3]"],
        key="desig"
    )
    
    if st.button("Verificar Desigualdad", key="check_abs_des"):
        if desigualdad == "(-5, 3)":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! |x + 1| < 4 → -5 < x < 3")
        else:
            st.error("❌ Incorrecto. |x + 1| < 4 equivale a -5 < x < 3")

# Función principal para ejecutar la app
if __name__ == "__main__":
    app()