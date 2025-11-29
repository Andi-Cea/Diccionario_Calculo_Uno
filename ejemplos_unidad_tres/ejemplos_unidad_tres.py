import streamlit as st
import numpy as np

def app():
    st.title("📚 Ejercicios Interactivos - Cálculo Diferencial: Límites y Continuidad Unidad III")
    
    # Menú de temas
    tema = st.sidebar.selectbox(
        "Selecciona un tema:",
        [
            "3.1 Concepto de límite de una función",
            "3.2 Teoremas sobre límites de funciones",
            "3.3 Límites unilaterales", 
            "3.4 Límites infinitos",
            "3.5 Límites en infinito",
            "3.6 Concepto de continuidad en un punto",
            "3.7 Teoremas sobre continuidad",
            "3.8 Continuidad en un intervalo",
            "3.9 Continuidad y discontinuidad",
            "3.10 Tipos de discontinuidad",
            "3.11 Discontinuidad en funciones elementales"
        ]
    )
    
    # Inicializar estado de la sesión
    if 'score_limites' not in st.session_state:
        st.session_state.score_limites = 0
    if 'exercises_completed_limites' not in st.session_state:
        st.session_state.exercises_completed_limites = 0
    
    # Diccionario de temas
    temas = {
        "3.1 Concepto de límite de una función": concepto_limite,
        "3.2 Teoremas sobre límites de funciones": teoremas_limites,
        "3.3 Límites unilaterales": limites_unilaterales,
        "3.4 Límites infinitos": limites_infinitos,
        "3.5 Límites en infinito": limites_en_infinito,
        "3.6 Concepto de continuidad en un punto": continuidad_punto,
        "3.7 Teoremas sobre continuidad": teoremas_continuidad,
        "3.8 Continuidad en un intervalo": continuidad_intervalo,
        "3.9 Continuidad y discontinuidad": continuidad_discontinuidad,
        "3.10 Tipos de discontinuidad": tipos_discontinuidad,
        "3.11 Discontinuidad en funciones elementales": discontinuidad_funciones_elementales
    }
    
    # Mostrar puntuación
    st.sidebar.markdown("---")
    st.sidebar.metric("🏆 Puntuación", st.session_state.score_limites)
    st.sidebar.metric("✅ Ejercicios Completados", st.session_state.exercises_completed_limites)
    
    if st.sidebar.button("🔄 Reiniciar Puntuación"):
        st.session_state.score_limites = 0
        st.session_state.exercises_completed_limites = 0
        st.rerun()
    
    # Ejecutar tema seleccionado
    if tema in temas:
        temas[tema]()

def check_answer_limites(correct_answer, user_answer, tolerance=0.01):
    """Verifica si la respuesta del usuario es correcta"""
    try:
        if abs(float(correct_answer) - float(user_answer)) <= tolerance:
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! +10 puntos")
            return True
        else:
            st.error("❌ Incorrecto. Intenta nuevamente.")
            return False
    except:
        st.error("❌ Formato inválido. Usa números.")
        return False

def concepto_limite():
    st.header("🔍 3.1 Concepto de Límite de una Función")
    
    st.info("Practica el concepto fundamental de límite")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Límite por factorización")
    st.write("Calcula el límite:")
    st.latex(r"\lim_{x \to 1} \frac{x^2 - 1}{x - 1}")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        user_answer1 = st.number_input("Resultado del límite:", value=0.0, step=0.1, key="concepto1")
    
    with col2:
        if st.button("Verificar ✅", key="check_concepto1"):
            check_answer_limites(2, user_answer1)
    
    # Explicación del ejercicio 1
    with st.expander("📖 Ver solución del Ejercicio 1"):
        st.write("**Solución:**")
        st.latex(r"\frac{x^2 - 1}{x - 1} = \frac{(x-1)(x+1)}{x-1} = x + 1")
        st.latex(r"\lim_{x \to 1} (x + 1) = 1 + 1 = 2")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Límite por sustitución directa")
    st.write("Calcula el límite:")
    st.latex(r"\lim_{x \to 3} \frac{x^2 - 9}{x - 3}")
    
    user_answer2 = st.number_input("Resultado del límite:", value=0.0, step=0.1, key="concepto2")
    
    if st.button("Verificar ✅", key="check_concepto2"):
        check_answer_limites(6, user_answer2)
    
    # Explicación del ejercicio 2
    with st.expander("📖 Ver solución del Ejercicio 2"):
        st.write("**Solución:**")
        st.latex(r"\frac{x^2 - 9}{x - 3} = \frac{(x-3)(x+3)}{x-3} = x + 3")
        st.latex(r"\lim_{x \to 3} (x + 3) = 3 + 3 = 6")

def teoremas_limites():
    st.header("📐 3.2 Teoremas sobre Límites de Funciones")
    
    st.info("Aplica los teoremas fundamentales de límites")
    
    # Ejercicio 1 - Suma de límites
    st.subheader("Ejercicio 1: Teorema de la suma")
    st.write("Si se sabe que:")
    st.latex(r"\lim_{x \to 2} f(x) = 3 \quad \text{y} \quad \lim_{x \to 2} g(x) = 4")
    st.write("Calcula:")
    st.latex(r"\lim_{x \to 2} [f(x) + g(x)]")
    
    user_sum = st.number_input("Resultado del límite de la suma:", value=0.0, step=0.1, key="teorema_sum")
    
    if st.button("Verificar Suma", key="check_teorema_sum"):
        check_answer_limites(7, user_sum)
    
    # Ejercicio 2 - Propiedad de sustitución directa
    st.subheader("Ejercicio 2: Sustitución directa")
    st.write("Para la función polinomial:")
    st.latex(r"f(x) = 2x^3 - 3x^2 + 5x - 1")
    st.write("Calcula:")
    st.latex(r"\lim_{x \to 2} f(x)")
    
    user_poly = st.number_input("Resultado usando sustitución directa:", value=0.0, step=0.1, key="teorema_poly")
    
    if st.button("Verificar Polinomio", key="check_teorema_poly"):
        correct = 2*(2**3) - 3*(2**2) + 5*2 - 1
        check_answer_limites(correct, user_poly)

def limites_unilaterales():
    st.header("↔️ 3.3 Límites Unilaterales")
    
    st.info("Practica límites por la izquierda y por la derecha")
    
    # Ejercicio 1 - Función por partes
    st.subheader("Ejercicio 1: Función definida por partes")
    st.write("Dada la función:")
    st.latex(r"f(x) = \begin{cases} 3x + 14 & \text{si } x \leq -2 \\ -x + 2 & \text{si } x > -2 \end{cases}")
    st.write("Calcula el límite por la izquierda:")
    st.latex(r"\lim_{x \to -2^-} f(x)")
    
    user_left = st.number_input("Límite por la izquierda:", value=0.0, step=0.1, key="unilateral_left")
    
    if st.button("Verificar Izquierda", key="check_unilateral_left"):
        check_answer_limites(8, user_left)
    
    # Ejercicio 2 - Función con valor absoluto
    st.subheader("Ejercicio 2: Función con valor absoluto")
    st.write("Dada la función:")
    st.latex(r"f(x) = \frac{x - 2}{2|x - 2|}")
    st.write("Calcula el límite por la derecha:")
    st.latex(r"\lim_{x \to 2^+} f(x)")
    
    user_right = st.number_input("Límite por la derecha:", value=0.0, step=0.1, key="unilateral_right")
    
    if st.button("Verificar Derecha", key="check_unilateral_right"):
        check_answer_limites(0.5, user_right)
    
    # Explicación del ejercicio 2
    with st.expander("📖 Ver explicación del Ejercicio 2"):
        st.write("**Explicación:**")
        st.write("Para x > 2, |x-2| = x-2, entonces:")
        st.latex(r"f(x) = \frac{x-2}{2(x-2)} = \frac{1}{2}")

def limites_infinitos():
    st.header("∞ 3.4 Límites Infinitos")
    
    st.info("Estudia el comportamiento cuando los valores crecen sin límite")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Límite infinito básico")
    st.write("Analiza el comportamiento:")
    st.latex(r"\lim_{x \to 0} \frac{1}{x^2}")
    
    option_inf1 = st.radio(
        "¿Qué ocurre con este límite?",
        ["Tiende a 0", "Tiende a ∞", "No existe", "Tiende a 1"],
        key="infinito1"
    )
    
    if st.button("Verificar Comportamiento 1", key="check_infinito1"):
        if option_inf1 == "Tiende a ∞":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! Cuando x→0, 1/x² crece sin límite")
        else:
            st.error("❌ Incorrecto. Revisa el comportamiento cerca de x=0")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Asíntota vertical")
    st.write("Para la función:")
    st.latex(r"f(x) = \frac{2x}{x - 3}")
    st.write("¿Qué ocurre con el límite por la derecha en x=3?")
    
    option_inf2 = st.radio(
        "Selecciona la respuesta correcta:",
        [r"$\lim_{x \to 3^+} f(x) = \infty$", 
         r"$\lim_{x \to 3^+} f(x) = -\infty$",
         r"$\lim_{x \to 3^+} f(x) = 0$",
         r"$\lim_{x \to 3^+} f(x) = 2$"],
        key="infinito2"
    )
    
    if st.button("Verificar Comportamiento 2", key="check_infinito2"):
        if option_inf2 == r"$\lim_{x \to 3^+} f(x) = \infty$":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! El denominador es positivo pequeño y el numerador ≈6")
        else:
            st.error("❌ Incorrecto. Analiza el signo del denominador cuando x→3⁺")

def limites_en_infinito():
    st.header("⎯ 3.5 Límites en el Infinito")
    
    st.info("Estudia el comportamiento cuando x tiende a infinito")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Límite de función racional")
    st.write("Calcula el límite:")
    st.latex(r"\lim_{x \to \infty} \frac{3x^2 - x - 2}{5x^2 + 4x + 1}")
    
    user_inf1 = st.number_input("Resultado del límite:", value=0.0, step=0.1, key="en_infinito1")
    
    if st.button("Verificar Límite 1", key="check_en_infinito1"):
        check_answer_limites(0.6, user_inf1, 0.01)
    
    # Explicación del ejercicio 1
    with st.expander("📖 Ver solución del Ejercicio 1"):
        st.write("**Solución:** Dividimos numerador y denominador entre x²:")
        st.latex(r"\frac{3 - \frac{1}{x} - \frac{2}{x^2}}{5 + \frac{4}{x} + \frac{1}{x^2}} \to \frac{3}{5} = 0.6")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Límite con raíz cuadrada")
    st.write("Calcula el límite:")
    st.latex(r"\lim_{x \to \infty} \frac{\sqrt{x^2 + 1}}{x + 1}")
    
    user_inf2 = st.number_input("Resultado del límite:", value=0.0, step=0.1, key="en_infinito2")
    
    if st.button("Verificar Límite 2", key="check_en_infinito2"):
        check_answer_limites(1, user_inf2, 0.01)

def continuidad_punto():
    st.header("🔗 3.6 Concepto de Continuidad en un Punto")
    
    st.info("Analiza la continuidad de funciones en puntos específicos")
    
    # Ejercicio 1
    st.subheader("Ejercicio 1: Discontinuidad evitable")
    st.write("Para la función:")
    st.latex(r"f(x) = \frac{x^2 - 1}{x - 1}")
    st.write("¿Es continua en x = 1?")
    
    option_cont1 = st.radio(
        "Selecciona la respuesta correcta:",
        ["Sí, es continua", "No, tiene discontinuidad evitable", "No, tiene discontinuidad infinita", "No, tiene discontinuidad de salto"],
        key="continuidad1"
    )
    
    if st.button("Verificar Continuidad 1", key="check_continuidad1"):
        if option_cont1 == "No, tiene discontinuidad evitable":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! f(1) no está definida, pero el límite existe")
        else:
            st.error("❌ Incorrecto. Verifica si f(1) está definida")
    
    # Ejercicio 2
    st.subheader("Ejercicio 2: Análisis gráfico de continuidad")
    st.write("Si una función cumple que:")
    st.latex(r"\lim_{x \to a} f(x) = L \quad \text{y} \quad f(a) = M")
    st.write("¿Qué condición adicional se necesita para que sea continua en x=a?")
    
    option_cont2 = st.radio(
        "Selecciona la condición necesaria:",
        ["L > M", "L < M", "L = M", "L ≠ M"],
        key="continuidad2"
    )
    
    if st.button("Verificar Continuidad 2", key="check_continuidad2"):
        if option_cont2 == "L = M":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! Para continuidad se requiere que el límite sea igual al valor de la función")
        else:
            st.error("❌ Incorrecto. Revisa la definición de continuidad")

def teoremas_continuidad():
    st.header("📊 3.7 Teoremas sobre Continuidad")
    
    st.info("Aplica los teoremas fundamentales sobre funciones continuas")
    
    # Ejercicio 1 - Teorema de la compresión
    st.subheader("Ejercicio 1: Teorema del sándwich")
    st.write("Si se sabe que para x cerca de 0:")
    st.latex(r"-x^2 \leq x^2 \sin\left(\frac{1}{x}\right) \leq x^2")
    st.write("¿Cuál es el valor de?")
    st.latex(r"\lim_{x \to 0} x^2 \sin\left(\frac{1}{x}\right)")
    
    user_sandwich = st.number_input("Resultado del límite:", value=0.0, step=0.1, key="teorema_sandwich")
    
    if st.button("Verificar Teorema Sándwich", key="check_teorema_sandwich"):
        check_answer_limites(0, user_sandwich)
    
    # Ejercicio 2 - Continuidad de funciones elementales
    st.subheader("Ejercicio 2: Continuidad de polinomios")
    st.write("¿En qué puntos es continua la función?")
    st.latex(r"f(x) = 3x^4 - 2x^3 + 5x - 1")
    
    option_poly = st.radio(
        "Selecciona la respuesta correcta:",
        ["Solo en x=0", "En todos los números reales", "Solo en números positivos", "Solo en números enteros"],
        key="teorema_poly"
    )
    
    if st.button("Verificar Polinomio", key="check_teorema_poly"):
        if option_poly == "En todos los números reales":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! Los polinomios son continuos en todo ℝ")
        else:
            st.error("❌ Incorrecto. Recuerda que los polinomios son continuos en todo su dominio")

def continuidad_intervalo():
    st.header("📈 3.8 Continuidad en un Intervalo")
    
    st.info("Estudia la continuidad en intervalos completos")
    
    # Ejercicio 1 - Función por partes en intervalo
    st.subheader("Ejercicio 1: Continuidad en punto de unión")
    st.write("Dada la función:")
    st.latex(r"f(x) = \begin{cases} \sqrt{x - 4} & \text{si } x > 4 \\ 8 - 2x & \text{si } x < 4 \end{cases}")
    st.write("¿Existe el límite en x=4?")
    
    option_intervalo1 = st.radio(
        "Selecciona la respuesta correcta:",
        ["Sí, y vale 0", "Sí, y vale 4", "No existe", "Sí, y vale 2"],
        key="intervalo1"
    )
    
    if st.button("Verificar Existencia", key="check_intervalo1"):
        if option_intervalo1 == "Sí, y vale 0":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! Ambos límites unilaterales valen 0")
        else:
            st.error("❌ Incorrecto. Calcula los límites por la izquierda y derecha")
    
    # Ejercicio 2 - Función tangente
    st.subheader("Ejercicio 2: Intervalos de continuidad")
    st.write("Para la función tangente f(x) = tan x, ¿en qué intervalos es continua?")
    
    option_intervalo2 = st.radio(
        "Selecciona la respuesta correcta:",
        ["En todo ℝ", "En intervalos abiertos entre asíntotas verticales", "Solo en [0,π]", "Solo en números pares"],
        key="intervalo2"
    )
    
    if st.button("Verificar Intervalos", key="check_intervalo2"):
        if option_intervalo2 == "En intervalos abiertos entre asíntotas verticales":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! tan x es continua en (-π/2 + kπ, π/2 + kπ)")
        else:
            st.error("❌ Incorrecto. Recuerda las asíntotas verticales de la tangente")

def continuidad_discontinuidad():
    st.header("⚡ 3.9 Continuidad y Discontinuidad")
    
    st.info("Diferencia entre funciones continuas y discontinuas")
    
    # Ejercicio 1 - Función con salto
    st.subheader("Ejercicio 1: Discontinuidad de salto")
    st.write("Para la función máximo entero f(x) = ⌊x⌋, ¿en qué puntos es discontinua?")
    
    option_salto = st.radio(
        "Selecciona la respuesta correcta:",
        ["En todos los números reales", "Solo en x=0", "En todos los números enteros", "Solo en números racionales"],
        key="salto"
    )
    
    if st.button("Verificar Discontinuidad Salto", key="check_salto"):
        if option_salto == "En todos los números enteros":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! La función parte entera tiene saltos en cada entero")
        else:
            st.error("❌ Incorrecto. Observa el comportamiento en los números enteros")
    
    # Ejercicio 2 - Identificar tipo de discontinuidad
    st.subheader("Ejercicio 2: Clasificación de discontinuidad")
    st.write("Para la función:")
    st.latex(r"f(x) = \begin{cases} \frac{x^2 - x - 2}{x - 2} & \text{si } x \neq 2 \\ 1 & \text{si } x = 2 \end{cases}")
    st.write("¿Qué tipo de discontinuidad tiene en x=2?")
    
    option_tipo = st.radio(
        "Selecciona el tipo correcto:",
        ["Discontinuidad evitable", "Discontinuidad de salto", "Discontinuidad infinita", "Es continua"],
        key="tipo_disc"
    )
    
    if st.button("Verificar Tipo", key="check_tipo"):
        if option_tipo == "Discontinuidad evitable":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! El límite existe pero no coincide con f(2)")
        else:
            st.error("❌ Incorrecto. Calcula el límite cuando x→2")

def tipos_discontinuidad():
    st.header("🎯 3.10 Tipos de Discontinuidad")
    
    st.info("Clasifica los diferentes tipos de discontinuidades")
    
    # Ejercicio 1 - Discontinuidad evitable
    st.subheader("Ejercicio 1: Discontinuidad evitable")
    st.write("¿Cuál de estas funciones tiene discontinuidad evitable en x=1?")
    
    option_evitable = st.radio(
        "Selecciona la función correcta:",
        [
            r"$f(x) = \frac{x^2 - 1}{x - 1}$",
            r"$f(x) = \frac{1}{x - 1}$", 
            r"$f(x) = \lfloor x \rfloor$",
            r"$f(x) = \sqrt{x - 1}$"
        ],
        key="evitable"
    )
    
    if st.button("Verificar Evitable", key="check_evitable"):
        if option_evitable == r"$f(x) = \frac{x^2 - 1}{x - 1}$":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! Se puede simplificar y el límite existe")
        else:
            st.error("❌ Incorrecto. Busca una función que se pueda simplificar")
    
    # Ejercicio 2 - Discontinuidad de salto
    st.subheader("Ejercicio 2: Discontinuidad de salto")
    st.write("Para la función:")
    st.latex(r"f(x) = \frac{x - 2}{2|x - 2|}")
    st.write("¿Qué tipo de discontinuidad tiene en x=2?")
    
    option_salto2 = st.radio(
        "Selecciona el tipo correcto:",
        ["Eliminable", "De salto", "Infinita", "Es continua"],
        key="salto2"
    )
    
    if st.button("Verificar Salto", key="check_salto2"):
        if option_salto2 == "De salto":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! Los límites laterales existen pero son diferentes")
        else:
            st.error("❌ Incorrecto. Calcula los límites por la izquierda y derecha")

def discontinuidad_funciones_elementales():
    st.header("📊 3.11 Discontinuidad en Funciones Elementales")
    
    st.info("Analiza discontinuidades en funciones comunes")
    
    # Ejercicio 1 - Función logaritmo
    st.subheader("Ejercicio 1: Función logaritmo natural")
    st.write("Para la función f(x) = ln x, ¿qué ocurre en x=0?")
    
    option_ln = st.radio(
        "Selecciona la respuesta correcta:",
        [
            r"$\lim_{x \to 0^+} \ln x = -\infty$",
            r"$\lim_{x \to 0^+} \ln x = \infty$", 
            r"$\lim_{x \to 0^+} \ln x = 0$",
            r"$\lim_{x \to 0^+} \ln x = 1$"
        ],
        key="ln"
    )
    
    if st.button("Verificar Logaritmo", key="check_ln"):
        if option_ln == r"$\lim_{x \to 0^+} \ln x = -\infty$":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! El logaritmo tiende a -∞ por la derecha")
        else:
            st.error("❌ Incorrecto. Recuerda el comportamiento del logaritmo cerca de 0")
    
    # Ejercicio 2 - Función tangente
    st.subheader("Ejercicio 2: Asíntotas verticales de la tangente")
    st.write("¿En qué puntos tiene la función tan x discontinuidades infinitas?")
    
    option_tan = st.radio(
        "Selecciona la respuesta correcta:",
        [
            r"$x = \frac{\pi}{2} + k\pi$",
            r"$x = k\pi$", 
            r"$x = \frac{\pi}{4} + k\pi$",
            r"$x = 2k\pi$"
        ],
        key="tan"
    )
    
    if st.button("Verificar Tangente", key="check_tan"):
        if option_tan == r"$x = \frac{\pi}{2} + k\pi$":
            st.session_state.score_limites += 10
            st.session_state.exercises_completed_limites += 1
            st.success("🎉 ¡Correcto! tan x tiene asíntotas verticales en π/2 + kπ")
        else:
            st.error("❌ Incorrecto. Recuerda que tan x = sen x / cos x")