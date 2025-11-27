import streamlit as st

def app():
    st.title("📚 Unidad 3: Límites y Continuidad")
    
    # Sección 3.1
    st.markdown("## 3.1 Concepto de límite de una función")
    
    st.markdown("**Definición:**")
    st.latex(r"\lim_{x \to a} f(x) = L")
    st.markdown("significa que para cada $\\varepsilon > 0$ existe $\\delta > 0$ tal que:")
    st.latex(r"\text{si } 0 < |x - a| < \delta \text{ entonces } |f(x) - L| < \varepsilon")
    
    st.markdown("**Notación alternativa:** $f(x) \\to L$ cuando $x \\to a$")
    
    # Sección 3.2
    st.markdown("## 3.2 Teoremas sobre límites de funciones")
    
    st.markdown("**Leyes de los límites** (si $\\lim_{x \\to a} f(x)$ y $\\lim_{x \\to a} g(x)$ existen):")
    st.markdown("""
    1. $\\lim_{x \\to a} [f(x) + g(x)] = \\lim_{x \\to a} f(x) + \\lim_{x \\to a} g(x)$
    2. $\\lim_{x \\to a} [f(x) - g(x)] = \\lim_{x \\to a} f(x) - \\lim_{x \\to a} g(x)$
    3. $\\lim_{x \\to a} [cf(x)] = c \\lim_{x \\to a} f(x)$
    4. $\\lim_{x \\to a} [f(x)g(x)] = \\lim_{x \\to a} f(x) \\cdot \\lim_{x \\to a} g(x)$
    5. $\\lim_{x \\to a} \\frac{f(x)}{g(x)} = \\frac{\\lim_{x \\to a} f(x)}{\\lim_{x \\to a} g(x)} \\quad \\text{si } \\lim_{x \\to a} g(x) \\neq 0$
    """)
    
    st.markdown("**Propiedad de sustitución directa:** Si $f$ es polinomial o racional y $a$ está en el dominio:")
    st.latex(r"\lim_{x \to a} f(x) = f(a)")
    
    # Sección 3.3
    st.markdown("## 3.3 Límites unilaterales")
    
    st.markdown("**Límite por la izquierda:**")
    st.latex(r"\lim_{x \to a^-} f(x) = L")
    st.markdown("si $f(x) \\to L$ cuando $x \\to a$ con $x < a$")
    
    st.markdown("**Límite por la derecha:**")
    st.latex(r"\lim_{x \to a^+} f(x) = L")
    st.markdown("si $f(x) \\to L$ cuando $x \\to a$ con $x > a$")
    
    st.markdown("**Teorema fundamental:**")
    st.latex(r"\lim_{x \to a} f(x) = L \quad \text{si y solo si} \quad \lim_{x \to a^-} f(x) = L \quad \text{y} \quad \lim_{x \to a^+} f(x) = L")
    
    # Sección 3.4
    st.markdown("## 3.4 Límites infinitos")
    
    st.markdown("**Definición:**")
    st.latex(r"\lim_{x \to a} f(x) = \infty")
    st.markdown("significa que $f(x)$ crece sin cota cuando $x \\to a$")
    
    st.markdown("**Asíntota vertical:** La recta $x = a$ es asíntota vertical si:")
    st.latex(r"\lim_{x \to a} f(x) = \infty \quad \text{o} \quad \lim_{x \to a} f(x) = -\infty")
    st.markdown("(o cualquiera de los límites unilaterales)")
    
    # Sección 3.5
    st.markdown("## 3.5 Límites en el infinito")
    
    st.markdown("**Definición:**")
    st.latex(r"\lim_{x \to \infty} f(x) = L")
    st.markdown("significa que $f(x) \\to L$ cuando $x$ crece sin límite")
    
    st.markdown("**Asíntota horizontal:** La recta $y = L$ es asíntota horizontal si:")
    st.latex(r"\lim_{x \to \infty} f(x) = L \quad \text{o} \quad \lim_{x \to -\infty} f(x) = L")
    
    st.markdown("**Límites importantes:**")
    st.latex(r"\lim_{x \to \infty} \frac{1}{x^n} = 0 \quad \text{y} \quad \lim_{x \to -\infty} \frac{1}{x^n} = 0 \quad \text{para } n > 0")
    
    # Sección 3.6
    st.markdown("## 3.6 Concepto de continuidad en un punto")
    
    st.markdown("**Definición:** $f$ es continua en $a$ si:")
    st.markdown("""
    1. $f(a)$ está definida
    2. $\\lim_{x \\to a} f(x)$ existe
    3. $\\lim_{x \\to a} f(x) = f(a)$
    """)
    
    # Sección 3.7
    st.markdown("## 3.7 Teoremas sobre continuidad")
    
    st.markdown("""
    - Si $f$ y $g$ son continuas en $a$, entonces $f+g$, $f-g$, $f \\cdot g$, y $f/g$ (si $g(a) \\neq 0$) son continuas en $a$
    - Las funciones polinomiales son continuas en todo $\\mathbb{R}$
    - Las funciones racionales son continuas en su dominio
    """)
    
    # Sección 3.8
    st.markdown("## 3.8 Continuidad en un intervalo")
    
    st.markdown("**Continua en un intervalo abierto:** Continua en todo punto del intervalo")
    
    st.markdown("**Continua en un intervalo cerrado $[a,b]$:**")
    st.markdown("""
    - Continua en $(a,b)$
    - $\\lim_{x \\to a^+} f(x) = f(a)$
    - $\\lim_{x \\to b^-} f(x) = f(b)$
    """)
    
    # Sección 3.9-3.10
    st.markdown("## 3.9-3.10 Tipos de discontinuidad")
    
    st.markdown("""
    - **Evitable:** $\\lim_{x \\to a} f(x)$ existe pero $f(a)$ no existe o $\\lim_{x \\to a} f(x) \\neq f(a)$
    - **Esencial:** $\\lim_{x \\to a} f(x)$ no existe
      - Salto finito: Límites laterales existen pero son diferentes
      - Infinita: Límites laterales son infinitos
    """)
    
    # Sección 3.11
    st.markdown("## 3.11 Discontinuidad en funciones elementales")
    
    st.markdown("""
    - **Racionales:** Discontinuidades en ceros del denominador
    - **Tangente:** Discontinuidades en $x = \\frac{\\pi}{2} + n\\pi$
    - **Logaritmo:** Discontinuidad en $x = 0$
    - **Función parte entera:** Discontinuidades en todos los enteros
    """)
    
    # Sección Límites importantes
    st.markdown("## Límites importantes")
    
    st.latex(r"""
    \begin{align*}
    \lim_{x \to 0} \frac{\sin x}{x} &= 1 \\
    \lim_{x \to 0} \frac{1 - \cos x}{x} &= 0 \\
    \lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x &= e \\
    e &= \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = \sum_{n=0}^{\infty} \frac{1}{n!}
    \end{align*}
    """)
    
    # Sección Técnicas
    st.markdown("## Técnicas para calcular límites")
    
    st.markdown("""
    - Factorización y simplificación
    - Racionalización
    - División por la mayor potencia (límites en infinito)
    - Teorema del sándwich
    - Sustitución directa cuando es posible
    """)

if __name__ == "__main__":
    app()