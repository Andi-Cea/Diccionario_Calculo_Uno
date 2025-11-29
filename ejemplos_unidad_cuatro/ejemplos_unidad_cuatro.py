import streamlit as st
import numpy as np
import sympy as sp
import math

def check_answer_diff(correct_answer, user_answer, tolerance=0.01):
    """Verifica si la respuesta del usuario es correcta"""
    try:
        if abs(float(correct_answer) - float(user_answer)) <= tolerance:
            st.session_state.score_diff += 10
            st.session_state.exercises_completed_diff += 1
            st.success("🎉 ¡Correcto! +10 puntos")
            return True
        else:
            st.error("❌ Incorrecto. Intenta nuevamente.")
            return False
    except:
        st.error("❌ Formato inválido. Usa números.")
        return False

def concepto_derivada():
    st.header("📐 4.1 Concepto de Derivada")
    
    st.info("Practica la definición fundamental de derivada usando límites")
    
    # Ejercicio 1 - Derivada por definición
    st.subheader("Ejercicio 1: Derivada por Definición")
    st.write("Calcula la derivada de f(x) = x² en x = 1 usando la definición:")
    st.latex(r"f'(1) = \lim_{h \to 0} \frac{f(1+h) - f(1)}{h}")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        user_deriv1 = st.number_input("f'(1) =", value=0.0, step=0.1, key="deriv1")
    
    with col2:
        if st.button("Verificar ✅", key="check_deriv1"):
            # f'(1) = 2(1) = 2
            check_answer_diff(2.0, user_deriv1)
    
    # Ejercicio 2 - Recta tangente
    st.subheader("Ejercicio 2: Ecuación de la Recta Tangente")
    st.write("Encuentra la ecuación de la recta tangente a y = x² en el punto P(1,1)")
    
    st.write("La ecuación tiene la forma: y - y₀ = m(x - x₀)")
    st.write("Donde m = f'(1) y (x₀, y₀) = (1, 1)")
    
    user_pendiente = st.number_input("Pendiente m =", value=0.0, step=0.1, key="pend1")
    user_intercepto = st.number_input("Término independiente (de y = mx + b) =", value=0.0, step=0.1, key="inter1")
    
    if st.button("Verificar Recta Tangente", key="check_tang1"):
        # y - 1 = 2(x - 1) → y = 2x - 1
        pendiente_correcta = 2.0
        intercepto_correcto = -1.0
        
        if check_answer_diff(pendiente_correcta, user_pendiente) and check_answer_diff(intercepto_correcto, user_intercepto):
            st.session_state.score_diff += 5  # Bonus adicional

def interpretacion_geometrica():
    st.header("📊 4.2 Interpretación Geométrica - Ángulos entre Curvas")
    
    st.info("Practica la interpretación geométrica de la derivada y ángulos entre curvas")
    
    # Ejercicio 1 - Pendiente y ángulo
    st.subheader("Ejercicio 1: Pendiente y Ángulo de Inclinación")
    st.write("Para la función f(x) = 4x - x² en el punto (1, 3):")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Calcula:**")
        st.write("1. La pendiente de la recta tangente")
        st.write("2. El ángulo de inclinación (en grados)")
    
    with col2:
        user_pendiente = st.number_input("Pendiente en (1,3):", value=0.0, step=0.1, key="pend_geo")
        user_angulo = st.number_input("Ángulo (grados):", value=0.0, step=1.0, key="ang_geo")
    
    if st.button("Verificar Geometría", key="check_geo"):
        # f'(x) = 4 - 2x, f'(1) = 2
        # ángulo = arctan(2) ≈ 63.43°
        pendiente_correcta = 2.0
        angulo_correcto = math.degrees(math.atan(2))
        
        correcto_pend = check_answer_diff(pendiente_correcta, user_pendiente)
        correcto_ang = check_answer_diff(angulo_correcto, user_angulo, 0.1)
        
        if correcto_pend and correcto_ang:
            st.session_state.score_diff += 5
    
    # Ejercicio 2 - Ángulo entre curvas
    st.subheader("Ejercicio 2: Ángulo entre Dos Curvas")
    st.write("Encuentra el ángulo entre las curvas y = x² y y = √x en su punto de intersección (1,1)")
    
    st.write("**Fórmula:** tan(θ) = |(m₂ - m₁)/(1 + m₁m₂)|")
    
    user_angulo_entre = st.number_input("Ángulo entre curvas (grados):", value=0.0, step=1.0, key="ang_entre")
    
    if st.button("Verificar Ángulo entre Curvas", key="check_ang_entre"):
        # y = x² → m₁ = 2
        # y = √x → m₂ = 1/(2√x) = 0.5 en x=1
        # θ = arctan(|(0.5-2)/(1+2*0.5)|) = arctan(0.75) ≈ 36.87°
        angulo_correcto = math.degrees(math.atan(0.75))
        check_answer_diff(angulo_correcto, user_angulo_entre, 0.1)

def teoremas_derivacion():
    st.header("🧮 4.3 Teoremas sobre Derivación de Funciones Elementales")
    
    st.info("Practica las reglas de derivación para funciones algebraicas y trascendentes")
    
    # Ejercicio 1 - Regla del producto
    st.subheader("Ejercicio 1: Regla del Producto")
    st.write("Deriva la función: f(x) = (2x⁴ - 3x²)(x³ + 4x - 6)")
    st.latex(r"f'(x) = (2x^4 - 3x^2)'(x^3 + 4x - 6) + (2x^4 - 3x^2)(x^3 + 4x - 6)'")
    
    st.write("Evalúa f'(1):")
    
    user_deriv_prod = st.number_input("f'(1) =", value=0.0, step=0.1, key="deriv_prod")
    
    if st.button("Verificar Producto", key="check_prod"):
        # f'(x) = (8x³ - 6x)(x³ + 4x - 6) + (2x⁴ - 3x²)(3x² + 4)
        # f'(1) = (8-6)(1+4-6) + (2-3)(3+4) = (2)(-1) + (-1)(7) = -2 -7 = -9
        check_answer_diff(-9.0, user_deriv_prod)
    
    # Ejercicio 2 - Regla del cociente
    st.subheader("Ejercicio 2: Regla del Cociente")
    st.write("Deriva la función: f(x) = 1/(x³ - 5x + 7)")
    st.latex(r"f'(x) = -\frac{(x^3 - 5x + 7)'}{(x^3 - 5x + 7)^2}")
    
    st.write("Evalúa f'(1):")
    
    user_deriv_coc = st.number_input("f'(1) =", value=0.0, step=0.1, key="deriv_coc")
    
    if st.button("Verificar Cociente", key="check_coc"):
        # f'(x) = -(3x² - 5)/(x³ - 5x + 7)²
        # f'(1) = -(3-5)/(1-5+7)² = -(-2)/(3)² = 2/9 ≈ 0.2222
        check_answer_diff(2/9, user_deriv_coc, 0.001)

def diferenciabilidad():
    st.header("🔍 4.4 Diferenciabilidad de Funciones Elementales y No Elementales")
    
    st.info("Analiza la diferenciabilidad de diferentes tipos de funciones")
    
    # Ejercicio 1 - Función valor absoluto
    st.subheader("Ejercicio 1: Diferenciabilidad del Valor Absoluto")
    st.write("Para la función f(x) = |x|:")
    
    pregunta = st.radio(
        "¿En qué punto NO es diferenciable f(x) = |x|?",
        ["x = -1", "x = 0", "x = 1", "x = 2"],
        key="diff_abs"
    )
    
    if st.button("Verificar Diferenciabilidad", key="check_diff_abs"):
        if pregunta == "x = 0":
            st.session_state.score_diff += 10
            st.session_state.exercises_completed_diff += 1
            st.success("🎉 ¡Correcto! f(x) = |x| no es diferenciable en x=0 (tiene un 'pico')")
        else:
            st.error("❌ Incorrecto. Revisa los límites laterales en x=0")
    
    # Ejercicio 2 - Continuidad vs Diferenciabilidad
    st.subheader("Ejercicio 2: Relación Continuidad-Diferenciabilidad")
    st.write("Selecciona la afirmación CORRECTA:")
    
    afirmacion = st.radio(
        "Sobre continuidad y diferenciabilidad:",
        [
            "Si una función es diferenciable, puede no ser continua",
            "Si una función es continua, siempre es diferenciable",
            "Si una función es diferenciable, entonces es continua", 
            "Continuidad y diferenciabilidad son equivalentes"
        ],
        key="cont_diff"
    )
    
    if st.button("Verificar Relación", key="check_cont_diff"):
        if afirmacion == "Si una función es diferenciable, entonces es continua":
            st.session_state.score_diff += 10
            st.session_state.exercises_completed_diff += 1
            st.success("🎉 ¡Correcto! Diferenciabilidad implica continuidad, pero no viceversa")
        else:
            st.error("❌ Incorrecto. La diferenciabilidad es una condición más fuerte que la continuidad")

def diferenciacion_implicita():
    st.header("🔗 4.5 Diferenciación Implícita")
    
    st.info("Practica la derivación de funciones definidas implícitamente")
    
    # Ejercicio 1 - Circunferencia
    st.subheader("Ejercicio 1: Derivada Implícita - Circunferencia")
    st.write("Para la ecuación x² + y² = 25, encuentra dy/dx en el punto (3,4)")
    
    st.latex(r"\frac{d}{dx}(x^2 + y^2) = \frac{d}{dx}(25)")
    st.latex(r"2x + 2y\frac{dy}{dx} = 0")
    
    user_deriv_imp1 = st.number_input("dy/dx en (3,4) =", value=0.0, step=0.1, key="deriv_imp1")
    
    if st.button("Verificar Implícita 1", key="check_imp1"):
        # 2(3) + 2(4)dy/dx = 0 → 6 + 8dy/dx = 0 → dy/dx = -6/8 = -0.75
        check_answer_diff(-0.75, user_deriv_imp1)
    
    # Ejercicio 2 - Folium de Descartes
    st.subheader("Ejercicio 2: Folium de Descartes")
    st.write("Para x³ + y³ = 6xy, encuentra dy/dx en (3,3)")
    
    user_deriv_imp2 = st.number_input("dy/dx en (3,3) =", value=0.0, step=0.1, key="deriv_imp2")
    
    if st.button("Verificar Implícita 2", key="check_imp2"):
        # 3x² + 3y²dy/dx = 6y + 6xdy/dx
        # En (3,3): 27 + 27dy/dx = 18 + 18dy/dx
        # 9dy/dx = -9 → dy/dx = -1
        check_answer_diff(-1.0, user_deriv_imp2)

def derivadas_orden_superior():
    st.header("📈 4.6 Derivadas de Orden Superior")
    
    st.info("Practica el cálculo de segundas y terceras derivadas")
    
    # Ejercicio 1 - Segunda derivada
    st.subheader("Ejercicio 1: Segunda Derivada")
    st.write("Para f(x) = x⁵ + 8x³, calcula f''(1)")
    
    st.latex(r"f'(x) = 5x^4 + 24x^2")
    st.latex(r"f''(x) = 20x^3 + 48x")
    
    user_segunda = st.number_input("f''(1) =", value=0.0, step=0.1, key="seg_deriv")
    
    if st.button("Verificar Segunda Derivada", key="check_seg"):
        # f''(1) = 20(1)³ + 48(1) = 20 + 48 = 68
        check_answer_diff(68.0, user_segunda)
    
    # Ejercicio 2 - Tercera derivada trigonométrica
    st.subheader("Ejercicio 2: Tercera Derivada - Función Trigonométrica")
    st.write("Para f(x) = sin(cos(x³)), calcula f'''(0)")
    
    st.write("**Pista:** Usa la regla de la cadena múltiples veces")
    
    user_tercera = st.number_input("f'''(0) =", value=0.0, step=0.1, key="ter_deriv")
    
    if st.button("Verificar Tercera Derivada", key="check_ter"):
        # f'(x) = cos(cos(x³)) * (-sin(x³)) * 3x²
        # f''(x) y f'''(x) se complican, pero f'''(0) = 0 por simetría
        check_answer_diff(0.0, user_tercera)

def regla_lhospital():
    st.header("🏥 4.7 Regla de L'Hospital - Formas Indeterminadas")
    
    st.info("Aplica la regla de L'Hospital para resolver límites indeterminados")
    
    # Ejercicio 1 - Forma 0/0
    st.subheader("Ejercicio 1: Forma 0/0")
    st.write("Calcula el límite usando L'Hospital:")
    st.latex(r"\lim_{x \to 0} \frac{\sin x}{x}")
    
    user_lim1 = st.number_input("Límite =", value=0.0, step=0.1, key="lim1")
    
    if st.button("Verificar Límite 1", key="check_lim1"):
        # L'Hospital: derivar numerador y denominador
        # cos(x)/1 → cos(0)/1 = 1
        check_answer_diff(1.0, user_lim1)
    
    # Ejercicio 2 - Forma ∞/∞
    st.subheader("Ejercicio 2: Forma ∞/∞")
    st.write("Calcula el límite usando L'Hospital:")
    st.latex(r"\lim_{x \to \infty} \frac{\ln x}{x}")
    
    user_lim2 = st.number_input("Límite =", value=1.0, step=0.1, key="lim2")
    
    if st.button("Verificar Límite 2", key="check_lim2"):
        # L'Hospital: (1/x)/1 = 1/x → 0 cuando x→∞
        check_answer_diff(0.0, user_lim2)

def app():
    st.title("📚 Ejercicios Interactivos - Cálculo Diferencial")
    
    # Menú de temas
    tema = st.sidebar.selectbox(
        "Selecciona un tema:",
        [
            "4.1 Concepto de derivada",
            "4.2 Interpretación geométrica. Ángulos entre curvas",
            "4.3 Teoremas sobre derivación de funciones elementales",
            "4.4 Diferenciabilidad de funciones elementales",
            "4.5 Diferenciación implícita", 
            "4.6 Derivadas de orden superior",
            "4.7 Regla de L'Hospital"
        ]
    )
    
    # Inicializar estado de la sesión
    if 'score_diff' not in st.session_state:
        st.session_state.score_diff = 0
    if 'exercises_completed_diff' not in st.session_state:
        st.session_state.exercises_completed_diff = 0
    
    # Diccionario de temas
    temas = {
        "4.1 Concepto de derivada": concepto_derivada,
        "4.2 Interpretación geométrica. Ángulos entre curvas": interpretacion_geometrica,
        "4.3 Teoremas sobre derivación de funciones elementales": teoremas_derivacion,
        "4.4 Diferenciabilidad de funciones elementales": diferenciabilidad,
        "4.5 Diferenciación implícita": diferenciacion_implicita,
        "4.6 Derivadas de orden superior": derivadas_orden_superior,
        "4.7 Regla de L'Hospital": regla_lhospital
    }
    
    # Mostrar puntuación
    st.sidebar.markdown("---")
    st.sidebar.metric("🏆 Puntuación", st.session_state.score_diff)
    st.sidebar.metric("✅ Ejercicios Completados", st.session_state.exercises_completed_diff)
    
    if st.sidebar.button("🔄 Reiniciar Puntuación"):
        st.session_state.score_diff = 0
        st.session_state.exercises_completed_diff = 0
        st.rerun()
    
    # Ejecutar tema seleccionado
    if tema in temas:
        temas[tema]()
    
    st.success("✅ Módulo cargado exitosamente")

# Ejecutar la aplicación
if __name__ == "__main__":
    app()