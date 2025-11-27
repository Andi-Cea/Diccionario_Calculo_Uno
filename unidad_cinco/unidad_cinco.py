import streamlit as st

def app():
    st.title("📚 Unidad 1: Los Números Reales")
    
    # Sección 1.1
    st.markdown("## 1.1 Axiomas de Campo y de Orden")
    
    st.markdown("### A. Axiomas de Campo (para la suma $+$ y el producto $\\cdot$)")
    st.markdown("""
    1. **Conmutatividad:** $x + y = y + x$, $xy = yx$
    2. **Asociatividad:** $x + (y + z) = (x + y) + z$, $x(yz) = (xy)z$
    3. **Distributividad:** $x(y + z) = xy + xz$
    4. **Elementos Neutros:** Existen $0$ y $1$ (distintos) tales que $0 + x = x + 0 = x$ y $1 \\cdot x = x \\cdot 1 = x$
    5. **Inverso Aditivo (Negativos):** Para todo $x$, existe $y$ tal que $x + y = y + x = 0$. Se denota $y = -x$
    6. **Inverso Multiplicativo (Recíproco):** Para todo $x \\neq 0$, existe $y$ tal que $xy = yx = 1$. Se denota $y = 1/x$ o $x^{-1}$
    """)
    
    st.markdown("### B. Axiomas de Orden")
    st.markdown("Los axiomas de orden permiten comparar números reales y tienen las siguientes propiedades ($a, b, c \\in \\mathbb{R}$):")
    st.markdown("""
    1. **Tricotomía:** Se cumple siempre una y solo una de:
    $a < b$,\\quad $a = b$,\\quad $b < a$
    
    2. **Transitividad:** Si $a < b$ y $b < c$, entonces $a < c$
    
    3. **Preservación del orden bajo la suma:** Si $a < b$, entonces $a + c < b + c$
    
    4. **Preservación del orden bajo el producto por positivos:** Si $a < b$ y $c > 0$, entonces $ac < bc$
    """)
    
    st.markdown("### Notación y Definiciones")
    st.markdown("""
    - $a \\leq b$ si $a < b$ o $a = b$
    - $a > b$ si $b < a$
    - $a$ es **positivo** si $a > 0$
    - $a$ es **negativo** si $a < 0$
    """)
    
    st.markdown("### Propiedades y Proposiciones Importantes")
    st.markdown("""
    - **Transitividad extendida:**
      - Si $a \\leq b$ y $b < c$, entonces $a < c$
      - Si $a < b$ y $b \\leq c$, entonces $a < c$
      - Si $a \\leq b$ y $b \\leq c$, entonces $a \\leq c$
    
    - **Criterio de igualdad:** Si $a \\leq b$ y $b \\leq a$, entonces $a = b$
    
    - **Caracterización mediante diferencia:** 
      $a < b$ si y sólo si $0 < b - a$
      $a < 0$ si y sólo si $0 < -a$
    
    - **Producto de positivos:** Si $a > 0$ y $b > 0$, entonces $ab > 0$
    
    - **Inversión de desigualdad:** Si $a < b$ y $c < 0$, entonces $ac > bc$
    
    - **Cuadrado positivo:** Si $a \\neq 0$, entonces $a^2 > 0$. En particular, $1 = 1^2 > 0$
    
    - **Lema de acotación:** Si $0 \\leq a \\leq \\epsilon$ para todo $\\epsilon > 0$, entonces $a = 0$
    """)
    
    st.markdown("### Definiciones Derivadas (Desigualdades)")
    st.markdown("""
    - $x > y$ significa que $x - y \\in \\mathbb{R}^+$ (es positivo)
    - $x < y$ significa que $y > x$
    - $x \\geq y$ significa que $x > y$ o $x = y$
    """)
    
    st.markdown("### Teoremas Importantes (Consecuencias de los Axiomas)")
    st.markdown("""
    - **Ley de Simplificación:** Si $a + b = a + c$, entonces $b = c$. Si $ab = ac$ y $a \\neq 0$, entonces $b = c$
    - $a \\cdot 0 = 0$
    - **Regla de los Signos:** $(-a)b = -(ab)$ y $(-a)(-b) = ab$
    - Si $ab = 0$ entonces $a = 0$ o $b = 0$
    """)
    
    # Sección 1.2
    st.markdown("## 1.2 Conjuntos Infinitos, Numerables y No Numerables")
    
    st.markdown("### Conceptos Básicos de Conjuntos")
    st.markdown("""
    - **Conjunto Finito:** Tiene un número definido de elementos (cardinalidad $n(A) = k$)
    - **Conjunto Infinito:** Su cardinalidad no está definida ($n(A) = \\infty$). Ejemplo: Números Naturales ($\\mathbb{N}$)
    - **Conjunto Vacío ($\\emptyset$):** No tiene elementos. $n(\\emptyset) = 0$
    """)
    
    st.markdown("### Principio de Inducción Matemática")
    st.markdown("Método para demostrar que una propiedad $P(n)$ se cumple para todos los números naturales $n$.")
    st.markdown("""
    1. **Base Inductiva:** Probar que $P(1)$ es verdadera
    2. **Hipótesis Inductiva:** Suponer que $P(k)$ es verdadera para un $k$ arbitrario
    3. **Paso Inductivo:** Probar que $P(k+1)$ es verdadera, usando la hipótesis
    """)
    st.markdown("**Conclusión:** Si se cumplen los pasos 1 y 3, entonces $P(n)$ es verdadera para todo $n \\in \\mathbb{N}$")
    
    st.markdown("### Conjuntos Numéricos")
    st.markdown("""
    - **Naturales ($\\mathbb{N}$):** $\\{1, 2, 3, \\ldots\\}$
    - **Enteros ($\\mathbb{Z}$):** $\\{\\ldots, -2, -1, 0, 1, 2, \\ldots\\}$
    - **Racionales ($\\mathbb{Q}$):** $\\left\\{\\dfrac{p}{q} \\mid p, q \\in \\mathbb{Z}, q \\neq 0\\right\\}$ (Incluye decimales finitos y periódicos)
    - **Irracionales:** Números que NO pueden escribirse como $\\dfrac{p}{q}$ (Incluye decimales infinitos no periódicos). Ej: $\\sqrt{2}$, $\\pi$, $e$
    - **Reales ($\\mathbb{R}$):** Unión de los conjuntos de números racionales e irracionales
    """)
    
    st.markdown("### Teorema Fundamental")
    st.markdown("**Teorema:** $\\sqrt{2}$ es irracional")
    st.markdown("**Demostración:** Por contradicción, suponiendo que se puede escribir como una fracción irreducible $\\dfrac{p}{q}$ y llegando a un absurdo (que $p$ y $q$ son ambos pares)")
    
    # Sección 1.3
    st.markdown("## 1.3 Teoremas sobre Números Reales")
    
    st.markdown("### Axioma del Supremo (Completitud de los Reales)")
    st.markdown("""
    - **Cota Superior:** Un número $M$ es cota superior de un conjunto $A$ si $a \\leq M$ para todo $a \\in A$
    - **Supremo ($\\sup(A)$):** Es la **menor** de todas las cotas superiores de $A$
    - **Axioma:** Todo conjunto no vacío y acotado superiormente tiene un supremo en $\\mathbb{R}$
    - **Caracterización del Supremo:** $\\alpha = \\sup(A)$ si y solo si:
      1. $a \\leq \\alpha$ para todo $a \\in A$
      2. Para todo $\\varepsilon > 0$, existe $a \\in A$ tal que $\\alpha - \\varepsilon < a$
    """)
    st.markdown("*(Análogamente se definen **Cota Inferior** e **Ínfimo ($\\inf(A)$)**)*")
    
    st.markdown("### Propiedad Arquimediana")
    st.markdown("**Teorema:** Dado cualquier número real $x$, existe un número natural $n$ tal que $x < n$")
    
    st.markdown("**Consecuencias:**")
    st.markdown("""
    1. Dados $a, b > 0$, existe $n \\in \\mathbb{N}$ tal que $n \\cdot a > b$
    2. Dado cualquier $b > 0$, existe $n \\in \\mathbb{N}$ tal que $0 < \\dfrac{1}{n} < b$
    """)
    
    st.markdown("### Densidad de los Reales")
    st.markdown("**Teorema:** Entre dos reales distintos, siempre hay un racional y un irracional")
    st.markdown("""
    - Dados $a, b \\in \\mathbb{R}$ con $a < b$, existe un número racional $r$ tal que $a < r < b$
    - Dados $a, b \\in \\mathbb{R}$ con $a < b$, y un irracional $\\xi > 0$, existe un racional $s$ tal que el irracional $s\\xi$ cumple $a < s\\xi < b$
    """)
    
    # Sección 1.4
    st.markdown("## 1.4 Intervalos")
    
    st.markdown("### Definición")
    st.markdown("Subconjuntos de $\\mathbb{R}$ definidos por desigualdades.")
    
    st.markdown("**Tabla de Intervalos:**")
    st.markdown("""
    | Desigualdad | Notación de Intervalo | Tipo |
    |-------------|---------------------|------|
    | $a < x < b$ | $(a, b)$ | Abierto |
    | $a \\leq x \\leq b$ | $[a, b]$ | Cerrado |
    | $a \\leq x < b$ | $[a, b)$ | Semicerrado |
    | $a < x \\leq b$ | $(a, b]$ | Semicerrado |
    | $x > a$ | $(a, \\infty)$ | Abierto |
    | $x \\geq a$ | $[a, \\infty)$ | Cerrado |
    | $x < b$ | $(-\\infty, b)$ | Abierto |
    | $x \\leq b$ | $(-\\infty, b]$ | Cerrado |
    | $-\\infty < x < \\infty$ (todo $\\mathbb{R}$) | $(-\\infty, \\infty)$ | Abierto y Cerrado |
    """)
    
    # Sección 1.5
    st.markdown("## 1.5 Valor Absoluto")
    
    st.markdown("### Definición")
    st.markdown("Para cualquier número real $a$:")
    st.latex(r"""
    |a| = 
    \begin{cases}
    a, & \text{si } a \geq 0 \\
    -a, & \text{si } a < 0
    \end{cases}
    """)
    
    st.markdown("### Interpretación Geométrica")
    st.markdown("La distancia desde $a$ hasta el 0 en la recta real.")
    
    st.markdown("### Propiedades Fundamentales")
    st.markdown("""
    1. **No negatividad:** $|a| \\geq 0$
    2. **Definición positiva:** $|a| = 0$ si y solo si $a = 0$
    3. **Multiplicativa:** $|ab| = |a||b|$
    4. **Desigualdad Triangular:** $|a + b| \\leq |a| + |b|$
    """)
    
    st.markdown("### Desigualdades con Valor Absoluto (Relación con Intervalos)")
    st.markdown("""
    - $|x| < a \\Leftrightarrow -a < x < a \\Leftrightarrow x \\in (-a, a)$
    - $|x| \\leq a \\Leftrightarrow -a \\leq x \\leq a \\Leftrightarrow x \\in [-a, a]$
    - $|x| > a \\Leftrightarrow x < -a$ o $x > a$
    - $|x - c| < r$ representa todos los puntos $x$ cuya distancia a $c$ es menor que $r$ (un intervalo centrado en $c$ con radio $r$)
    """)

if __name__ == "__main__":
    app()