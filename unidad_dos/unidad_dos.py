import streamlit as st

def app():
    st.title("📚 Unidad 2: Funciones")
    
    # Sección 2.1
    st.markdown("## 2.1 Definición de Función")
    
    st.markdown("""
    - **Función:** Regla de correspondencia que asigna a cada elemento de un conjunto $A$ (dominio) un **único** elemento de un conjunto $B$ (codominio).
    - **Notación:** $f: A \\to B$
    - **Relación vs Función:** En una relación, un elemento de $A$ puede asociarse con múltiples elementos de $B$. En una función, cada elemento de $A$ tiene **exactamente una** imagen en $B$.
    - **Prueba de la recta vertical:** Una gráfica representa una función si toda recta vertical corta a la gráfica en **a lo más un punto**.
    """)
    
    # Sección 2.2
    st.markdown("## 2.2 Notación y Valor Numérico")
    
    st.markdown("""
    - **Notación:** $y = f(x)$
      - $x$: variable independiente
      - $y$: variable dependiente  
      - $f$: función (regla de asignación)
    - **Valor numérico:** $f(a)$ es el valor que toma la función cuando $x = a$
    - **Ejemplo:** Si $f(x) = 3x^2 - 5x - 2$, entonces $f(-3) = 3(-3)^2 - 5(-3) - 2 = 40$
    """)
    
    # Sección 2.3
    st.markdown("## 2.3 Dominio, Rango y Codominio")
    
    st.markdown("""
    - **Dominio ($Dom_f$):** Conjunto de todos los valores posibles para $x$
    - **Codominio:** Conjunto $B$ en $f: A \\to B$
    - **Rango/Imagen ($Im_f$):** Conjunto de todos los valores $f(x)$ obtenidos
    - **Relación:** $Im_f \\subseteq B$ (puede ser subconjunto propio)
    """)
    
    st.markdown("### Criterios para determinar el dominio:")
    st.markdown("""
    - **Denominadores:** No pueden ser cero
    - **Radicales de índice par:** Radicando $\\geq 0$
    - **Contexto del problema:** Puede restringir el dominio
    """)
    
    st.markdown("### Ejemplos:")
    st.markdown("""
    - $f(x) = \\sqrt{25-x^2}$ $\\Rightarrow$ $Dom_f = [-5,5]$
    - $f(x) = 1 + \\sqrt{5x-2}$ $\\Rightarrow$ $Dom_f = \\left[\\frac{2}{5}, \\infty\\right)$
    - $f(x) = \\frac{1}{\\sqrt{x^2-1}}$ $\\Rightarrow$ $Dom_f = (-\\infty,-1) \\cup (1,\\infty)$
    """)
    
    # Sección 2.4
    st.markdown("## 2.4 Clasificación de Funciones")
    
    st.markdown("### Por estructura:")
    st.markdown("""
    - **Algebraicas:** Polinomiales, racionales, con radicales
    - **Trascendentes:** Trigonométricas, exponenciales, logarítmicas
    - **Explícitas:** $y = f(x)$ (variable despejada)
    - **Implícitas:** $F(x,y) = 0$ (variables mezcladas)
    """)
    
    st.markdown("### Por propiedades:")
    st.markdown("""
    - **Inyectiva (uno a uno):** Si $f(a_1) = f(a_2)$ implica $a_1 = a_2$
      - **Prueba:** $f(x_1) = f(x_2) \\Rightarrow x_1 = x_2$
    
    - **Sobreyectiva:** $Im_f = B$ (todo el codominio es imagen)
      - **Prueba:** Para todo $b \\in B$, existe $a \\in A$ tal que $f(a) = b$
    
    - **Biyectiva:** Inyectiva y sobreyectiva $\\Leftrightarrow$ invertible
    """)
    
    # Sección 2.5
    st.markdown("## 2.5 Operaciones entre Funciones")
    
    st.markdown("**Dominio de operaciones:** $Dom(f \\circ g) = Dom_f \\cap Dom_g$ (con restricciones)")
    
    st.markdown("""
    - **Suma:** $(f + g)(x) = f(x) + g(x)$
    - **Multiplicación:** $(fg)(x) = f(x)g(x)$
    - **División:** $\\left(\\frac{f}{g}\\right)(x) = \\frac{f(x)}{g(x)}$, $Dom = \\{x \\in Dom_f \\cap Dom_g : g(x) \\neq 0\\}$
    """)
    
    st.markdown("### Composición:")
    st.markdown("""
    - $(g \\circ f)(x) = g(f(x))$
    - $Dom(g \\circ f) = \\{x \\in Dom_f : f(x) \\in Dom_g\\}$
    - **No conmutativa:** $(g \\circ f)(x) \\neq (f \\circ g)(x)$ en general
    - **Asociativa:** $(h \\circ g) \\circ f = h \\circ (g \\circ f)$
    """)
    
    st.markdown("### Propiedades:")
    st.markdown("""
    - Conmutativa y asociativa para suma y multiplicación
    - Distributiva: $f(g + h) = fg + fh$
    - Elemento neutro: $f + 0_R = f$, $f \\cdot 1_R = f$
    - Identidad: $I_R \\circ f = f \\circ I_R = f$
    """)
    
    # Sección 2.6
    st.markdown("## 2.6 Tipos Especiales de Funciones")
    
    st.markdown("### Funciones básicas:")
    st.markdown("""
    - **Constante:** $f(x) = c$
    - **Identidad:** $I(x) = x$
    - **Lineal:** $f(x) = ax + b$
    - **Cuadrática:** $f(x) = ax^2 + bx + c$
    - **Polinomial:** $f(x) = a_0 + a_1x + \\cdots + a_nx^n$
    - **Racional:** $f(x) = \\frac{P(x)}{Q(x)}$
    """)
    
    st.markdown("### Funciones no elementales:")
    st.markdown("""
    - **Máximo entero:** $[x] = \\max\\{k \\in \\mathbb{Z} : k \\leq x\\}$
      - Ejemplos: $[3.4] = 3$, $[0.8] = 0$, $[-1.2] = -2$
    - **Valor absoluto:** $|x| = 
    \\begin{cases}
    x & \\text{si } x \\geq 0 \\\\
    -x & \\text{si } x < 0
    \\end{cases}$
    - **Seccionadas:** Diferentes reglas en diferentes partes del dominio
    """)
    
    # Sección Funciones Inversas
    st.markdown("## Funciones Inversas")
    
    st.markdown("""
    - $f^{-1}$ es inversa de $f$ si:
      - $f^{-1} \\circ f = I_A$
      - $f \\circ f^{-1} = I_B$
    - **Teorema:** $f$ es biyectiva $\\Leftrightarrow$ $f$ es invertible
    - **Método para encontrar $f^{-1}$:**
      1. Verificar que $f$ es biyectiva
      2. Escribir $y = f(x)$
      3. Despejar $x$ en términos de $y$
      4. Intercambiar $x$ por $y$: $f^{-1}(x) = \\text{expresión obtenida}$
    """)
    
    # Sección Aplicaciones
    st.markdown("## Aplicaciones de Funciones")
    
    st.markdown("### Ejemplos de modelado:")
    st.markdown("""
    - **Ganancia:** $g(x) = 0.40x$ (ganancia por venta de $x$ barras)
    - **Distancia:** $d(t) = \\frac{3}{2}\\sqrt{t^2 + 400}$ (distancia globo-casa)
    - **Volumen caja:** $V(x) = x(8-2x)^2$ (caja de cartón)
    - **Área lata:** $A(r) = \\frac{1.6}{r} + 2\\pi r^2$ (área superficial)
    """)

if __name__ == "__main__":
    app()