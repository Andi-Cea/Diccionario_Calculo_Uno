import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.title("🎓 Ejercicios Interactivos - Cálculo Diferencial unidad V")

    
    # Menú de temas
    tema = st.sidebar.selectbox(
        "Selecciona un tema:",
        [
            "5.1 Máximos y mínimos de una función",
            "5.2 Extremos relativos y absolutos en intervalos cerrados",
            "5.3 Teorema de Rolle y del valor medio", 
            "5.4 Concavidad de una curva y puntos de inflexión",
            "5.5 Prueba de la primera derivada",
            "5.6 Prueba de la segunda derivada"
        ]
    )
    
    # Inicializar estado de la sesión
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'exercises_completed' not in st.session_state:
        st.session_state.exercises_completed = 0
    
    # Diccionario de temas
    temas = {
        "5.1 Máximos y mínimos de una función": maximos_minimos,
        "5.2 Extremos relativos y absolutos en intervalos cerrados": extremos_intervalos,
        "5.3 Teorema de Rolle y del valor medio": rolle_valor_medio,
        "5.4 Concavidad de una curva y puntos de inflexión": concavidad_puntos_inflexion,
        "5.5 Prueba de la primera derivada": prueba_primera_derivada,
        "5.6 Prueba de la segunda derivada": prueba_segunda_derivada
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

def maximos_minimos():
    st.header("📈 5.1 Máximos y mínimos de una función")
    
    st.info("Encuentra números críticos y analiza extremos de funciones")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Números críticos")
    st.write("Encuentra los números críticos de:")
    st.latex(r"f(x) = x^{3/5}(4 - x)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Pasos a seguir:**")
        st.write("1. Calcula f'(x) usando regla del producto")
        st.write("2. Encuentra donde f'(x) = 0")
        st.write("3. Encuentra donde f'(x) no existe")
    
    with col2:
        user_critico1 = st.number_input("Primer número crítico:", value=0.0, step=0.1, key="crit1")
        user_critico2 = st.number_input("Segundo número crítico:", value=0.0, step=0.1, key="crit2")
    
    if st.button("Verificar Números Críticos", key="check_criticos"):
        correctos = [0, 1.5]
        if (abs(user_critico1 - correctos[0]) <= 0.01 and abs(user_critico2 - correctos[1]) <= 0.01) or \
           (abs(user_critico1 - correctos[1]) <= 0.01 and abs(user_critico2 - correctos[0]) <= 0.01):
            st.session_state.score += 20
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Números críticos: x = 0 y x = 1.5")
        else:
            st.error("❌ Incorrecto. Revisa tu derivada")
    
    st.markdown("---")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Análisis sin extremos")
    st.write("Demuestra que la función:")
    st.latex(r"g(x) = 2 + (x - 5)^3")
    st.write("tiene un número crítico en x = 5 pero no tiene extremo local allí.")
    
    respuesta = st.radio(
        "¿Por qué no hay extremo local en x = 5?",
        [
            "Porque f'(x) no cambia de signo alrededor de x = 5",
            "Porque f(x) no es continua en x = 5",
            "Porque f''(5) = 0",
            "Porque no es un punto crítico"
        ],
        key="no_extremo"
    )
    
    if st.button("Verificar Análisis", key="check_no_extremo"):
        if respuesta == "Porque f'(x) no cambia de signo alrededor de x = 5":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! La derivada mantiene el mismo signo")
        else:
            st.error("❌ Incorrecto. Analiza el signo de la derivada")

def extremos_intervalos():
    st.header("🎯 5.2 Extremos relativos y absolutos en intervalos cerrados")
    
    st.info("Encuentra valores máximo y mínimo absolutos en intervalos")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Extremos absolutos")
    st.write("Encuentra los valores máximo y mínimo absolutos de:")
    st.latex(r"f(x) = x^3 - 3x^2 + 1 \quad \text{en} \quad \left[-\frac{1}{2}, 4\right]")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Pasos:**")
        st.write("1. Encuentra puntos críticos")
        st.write("2. Evalúa en extremos del intervalo")
        st.write("3. Compara valores")
    
    with col2:
        user_max = st.number_input("Valor máximo absoluto:", value=0.0, step=0.1, key="max_abs")
        user_min = st.number_input("Valor mínimo absoluto:", value=0.0, step=0.1, key="min_abs")
    
    if st.button("Verificar Extremos Absolutos", key="check_extremos_abs"):
        if abs(user_max - 17) <= 0.1 and abs(user_min - (-3)) <= 0.1:
            st.session_state.score += 20
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Máximo: 17, Mínimo: -3")
        else:
            st.error("❌ Incorrecto. Revisa tus cálculos")
    
    st.markdown("---")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Función con valor absoluto")
    st.write("Encuentra los extremos absolutos de:")
    st.latex(r"f(x) = 2x - 3x^{2/3} \quad \text{en} \quad [-1, 3]")
    
    user_max2 = st.number_input("Valor máximo:", value=0.0, step=0.1, key="max2")
    user_min2 = st.number_input("Valor mínimo:", value=0.0, step=0.1, key="min2")
    
    if st.button("Verificar Segundos Extremos", key="check_extremos2"):
        if abs(user_max2 - 0) <= 0.1 and abs(user_min2 - (-5)) <= 0.1:
            st.session_state.score += 20
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Máximo: 0, Mínimo: -5")
        else:
            st.error("❌ Incorrecto. Considera x = 0 y x = -1")

def rolle_valor_medio():
    st.header("📐 5.3 Teorema de Rolle y del valor medio")
    
    st.info("Aplica los teoremas fundamentales del cálculo")
    
    # Ejercicio 1 - Teorema del Valor Medio
    st.subheader("Ejercicio 1: Teorema del Valor Medio")
    st.write("Para la función:")
    st.latex(r"f(x) = x^3 - x \quad \text{en} \quad [0, 2]")
    st.write("Encuentra el valor c que satisface:")
    st.latex(r"f'(c) = \frac{f(2) - f(0)}{2 - 0}")
    
    user_c_tvm = st.number_input("Valor de c:", value=0.0, step=0.1, key="c_tvm")
    
    if st.button("Verificar TVM", key="check_tvm"):
        correct_c = 2/np.sqrt(3)
        if check_answer(correct_c, user_c_tvm, 0.01):
            st.latex(r"c = \frac{2}{\sqrt{3}} \approx 1.155")
    
    st.markdown("---")
    
    # Ejercicio 2 - Teorema de Rolle
    st.subheader("Ejercicio 2: Teorema de Rolle")
    st.write("Demuestra que la ecuación tiene exactamente una raíz real:")
    st.latex(r"x^3 + x - 1 = 0")
    
    respuesta_rolle = st.radio(
        "¿Qué estrategia usarías?",
        [
            "Usar TVM y demostrar que f'(x) > 0 para todo x",
            "Aplicar Rolle y llegar a contradicción", 
            "Usar el teorema del valor intermedio solamente",
            "Derivar dos veces y analizar concavidad"
        ],
        key="estrategia_rolle"
    )
    
    if st.button("Verificar Estrategia", key="check_rolle"):
        if respuesta_rolle == "Aplicar Rolle y llegar a contradicción":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Se usa Rolle para demostrar unicidad")
            st.write("**Explicación:** f'(x) = 3x² + 1 ≥ 1 > 0, por lo que no puede haber dos raíces.")
        else:
            st.error("❌ Estrategia incorrecta")

def concavidad_puntos_inflexion():
    st.header("📊 5.4 Concavidad de una curva y puntos de inflexión")
    
    st.info("Analiza concavidad y encuentra puntos de inflexión")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Concavidad y puntos de inflexión")
    st.write("Para la función:")
    st.latex(r"f(x) = x^4 - 4x^3")
    st.write("Encuentra los intervalos de concavidad y puntos de inflexión")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Cálculos necesarios:**")
        st.latex(r"f'(x) = 4x^3 - 12x^2")
        st.latex(r"f''(x) = 12x^2 - 24x")
    
    with col2:
        user_inflexion1 = st.number_input("Primer punto de inflexión:", value=0.0, step=0.1, key="inf1")
        user_inflexion2 = st.number_input("Segundo punto de inflexión:", value=0.0, step=0.1, key="inf2")
        user_concava = st.selectbox("Concavidad en (2, ∞):", ["Cóncava hacia arriba", "Cóncava hacia abajo"], key="concava")
    
    if st.button("Verificar Concavidad", key="check_concavidad"):
        correctos = [0, 2]
        if (abs(user_inflexion1 - correctos[0]) <= 0.01 and abs(user_inflexion2 - correctos[1]) <= 0.01) and \
           user_concava == "Cóncava hacia arriba":
            st.session_state.score += 20
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Puntos de inflexión: x = 0, x = 2")
        else:
            st.error("❌ Incorrecto. Revisa f''(x)")
    
    st.markdown("---")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Función logarítmica")
    st.write("Para:")
    st.latex(r"f(x) = \ln(x^2 + 1)")
    st.write("¿Cuántos puntos de inflexión tiene?")
    
    user_num_inflex = st.slider("Número de puntos de inflexión:", 0, 4, 1, key="num_inflex")
    
    if st.button("Verificar Puntos Inflexión", key="check_num_inflex"):
        if user_num_inflex == 2:
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Tiene 2 puntos de inflexión")
        else:
            st.error("❌ Incorrecto. Calcula f''(x)")

def prueba_primera_derivada():
    st.header("📈 5.5 Prueba de la primera derivada")
    
    st.info("Clasifica extremos locales usando la primera derivada")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Clasificar extremos")
    st.write("Para la función:")
    st.latex(r"f(x) = 3x^4 - 4x^3 - 12x^2 + 5")
    st.write("Usa la prueba de la primera derivada para clasificar los extremos")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Punto x = -1:**")
        tipo1 = st.selectbox("Tipo:", ["Máximo local", "Mínimo local", "No es extremo"], key="tipo1")
    with col2:
        st.write("**Punto x = 0:**")
        tipo2 = st.selectbox("Tipo:", ["Máximo local", "Mínimo local", "No es extremo"], key="tipo2")
    with col3:
        st.write("**Punto x = 2:**")
        tipo3 = st.selectbox("Tipo:", ["Máximo local", "Mínimo local", "No es extremo"], key="tipo3")
    
    if st.button("Verificar Clasificación", key="check_clasif"):
        if tipo1 == "Mínimo local" and tipo2 == "Máximo local" and tipo3 == "Mínimo local":
            st.session_state.score += 20
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Clasificación exacta")
        else:
            st.error("❌ Incorrecto. Analiza el signo de f'(x)")
    
    st.markdown("---")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Función trigonométrica")
    st.write("Para:")
    st.latex(r"g(x) = x + 2\sin x \quad \text{en} \quad [0, 2\pi]")
    st.write("¿Qué tipo de extremo hay en x = 2π/3?")
    
    user_tipo_trig = st.radio(
        "Selecciona el tipo de extremo:",
        ["Máximo local", "Mínimo local", "Punto de inflexión", "No es extremo"],
        key="tipo_trig"
    )
    
    if st.button("Verificar Extremo Trig", key="check_trig"):
        if user_tipo_trig == "Máximo local":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Es un máximo local")
        else:
            st.error("❌ Incorrecto. g'(x) cambia de + a - en 2π/3")

def prueba_segunda_derivada():
    st.header("📉 5.6 Prueba de la segunda derivada")
    
    st.info("Usa la segunda derivada para clasificar extremos")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Clasificación con segunda derivada")
    st.write("Para la función:")
    st.latex(r"f(x) = x^3 - 3x^2 - 9x + 5")
    st.write("Usa la prueba de la segunda derivada en los puntos críticos")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**En x = -1:**")
        st.latex(r"f''(x) = 6x - 6")
        st.latex(r"f''(-1) = -12")
        tipo_sd1 = st.selectbox("Conclusión:", ["Máximo local", "Mínimo local", "Prueba no concluye"], key="sd1")
    
    with col2:
        st.write("**En x = 3:**")
        st.latex(r"f''(3) = 12")
        tipo_sd2 = st.selectbox("Conclusión:", ["Máximo local", "Mínimo local", "Prueba no concluye"], key="sd2")
    
    if st.button("Verificar Segunda Derivada", key="check_sd"):
        if tipo_sd1 == "Máximo local" and tipo_sd2 == "Mínimo local":
            st.session_state.score += 20
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! f''(-1) < 0 → máximo, f''(3) > 0 → mínimo")
        else:
            st.error("❌ Incorrecto. Recuerda: f''(c) < 0 → máximo, f''(c) > 0 → mínimo")
    
    st.markdown("---")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Caso especial")
    st.write("Para:")
    st.latex(r"f(x) = x e^{-x}")
    st.write("¿Qué sucede cuando aplicas la prueba de la segunda derivada en x = 1?")
    
    user_caso_especial = st.radio(
        "Selecciona la respuesta correcta:",
        [
            "f''(1) > 0, entonces es mínimo local",
            "f''(1) < 0, entonces es máximo local", 
            "f''(1) = 0, prueba no concluye",
            "No se puede calcular f''(1)"
        ],
        key="caso_esp"
    )
    
    if st.button("Verificar Caso Especial", key="check_caso_esp"):
        if user_caso_especial == "f''(1) < 0, entonces es máximo local":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! f''(1) = -e⁻¹ < 0 → máximo local")
        else:
            st.error("❌ Incorrecto. Calcula f''(x) cuidadosamente")

# Ejecutar la aplicación
if __name__ == "__main__":
    app()