import streamlit as st

def app():
    st.title("📚 Unidad 5: Aplicaciones de la Derivada")
    
    # Sección 5.1
    st.markdown("## 5.1 Máximos y mínimos de una función")
    
    st.markdown("### Definición: Extremos relativos")
    st.markdown("""
    Sea $f$ una función definida en un intervalo $I$ y $c \\in I$:
    - $f(c)$ es un **máximo relativo** si existe $\\delta > 0$ tal que $f(c) \\geq f(x)$ para todo $x \\in (c-\\delta, c+\\delta) \\cap I$
    - $f(c)$ es un **mínimo relativo** si existe $\\delta > 0$ tal que $f(c) \\leq f(x)$ para todo $x \\in (c-\\delta, c+\\delta) \\cap I$
    """)
    
    st.markdown("### Definición: Puntos críticos")
    st.markdown("""
    Un número $c$ en el dominio de $f$ es un **punto crítico** si:
    """)
    st.latex(r"f'(c) = 0 \quad \text{o} \quad f'(c) \text{ no existe}")
    
    st.markdown("### Teorema: Condición necesaria para extremos relativos")
    st.markdown("""
    Si $f$ tiene un extremo relativo en $c$ y $f'(c)$ existe, entonces $f'(c) = 0$.
    """)
    
    # Sección 5.2
    st.markdown("## 5.2 Extremos relativos y absolutos en intervalos cerrados")
    
    st.markdown("### Definición: Extremos absolutos")
    st.markdown("""
    Sea $f$ definida en un intervalo $I$:
    - $f(c)$ es el **máximo absoluto** si $f(c) \\geq f(x)$ para todo $x \\in I$
    - $f(c)$ es el **mínimo absoluto** si $f(c) \\leq f(x)$ para todo $x \\in I$
    """)
    
    st.markdown("### Teorema: Teorema del valor extremo")
    st.markdown("""
    Si $f$ es continua en $[a,b]$, entonces $f$ alcanza sus valores máximo y mínimo absolutos en $[a,b]$.
    """)
    
    st.markdown("### Procedimiento para encontrar extremos absolutos en $[a,b]$:")
    st.markdown("""
    1. Encontrar los puntos críticos de $f$ en $(a,b)$
    2. Evaluar $f$ en los puntos críticos
    3. Evaluar $f$ en los extremos $a$ y $b$
    4. El mayor valor es el máximo absoluto, el menor es el mínimo absoluto
    """)
    
    # Sección 5.3
    st.markdown("## 5.3 Teorema de Rolle y del valor medio")
    
    st.markdown("### Teorema: Teorema de Rolle")
    st.markdown("""
    Sea $f$ continua en $[a,b]$ y derivable en $(a,b)$. Si $f(a) = f(b)$, entonces existe $c \\in (a,b)$ tal que $f'(c) = 0$.
    """)
    
    st.markdown("### Teorema: Teorema del Valor Medio")
    st.markdown("""
    Sea $f$ continua en $[a,b]$ y derivable en $(a,b)$. Entonces existe $c \\in (a,b)$ tal que:
    """)
    st.latex(r"f'(c) = \frac{f(b) - f(a)}{b - a}")
    
    # Sección 5.4
    st.markdown("## 5.4 Concavidad de una curva y puntos de inflexión")
    
    st.markdown("### Definición: Concavidad")
    st.markdown("""
    Sea $f$ derivable en un intervalo abierto $I$:
    - $f$ es **cóncava hacia arriba** en $I$ si $f'$ es creciente en $I$
    - $f$ es **cóncava hacia abajo** en $I$ si $f'$ es decreciente en $I$
    """)
    
    st.markdown("### Teorema: Criterio de concavidad")
    st.markdown("""
    Sea $f$ dos veces derivable en $I$:
    - Si $f''(x) > 0$ para todo $x \\in I$, entonces $f$ es cóncava hacia arriba en $I$
    - Si $f''(x) < 0$ para todo $x \\in I$, entonces $f$ es cóncava hacia abajo en $I$
    """)
    
    st.markdown("### Definición: Punto de inflexión")
    st.markdown("""
    Un punto $(c, f(c))$ es un **punto de inflexión** si la concavidad de $f$ cambia en $c$.
    """)
    
    # Sección 5.5
    st.markdown("## 5.5 Prueba de la primera derivada")
    
    st.markdown("### Teorema: Prueba de la primera derivada")
    st.markdown("""
    Sea $c$ un punto crítico de $f$:
    - Si $f'(x)$ cambia de positiva a negativa en $c$, entonces $f(c)$ es un máximo relativo
    - Si $f'(x)$ cambia de negativa a positiva en $c$, entonces $f(c)$ es un mínimo relativo
    - Si $f'(x)$ no cambia de signo en $c$, entonces $f(c)$ no es un extremo relativo
    """)
    
    st.markdown("### Procedimiento:")
    st.markdown("""
    1. Encontrar puntos críticos
    2. Dividir el dominio en intervalos usando los puntos críticos
    3. Determinar el signo de $f'$ en cada intervalo
    4. Aplicar el teorema
    """)
    
    # Sección 5.6
    st.markdown("## 5.6 Prueba de la segunda derivada")
    
    st.markdown("### Teorema: Prueba de la segunda derivada")
    st.markdown("""
    Sea $c$ un punto crítico de $f$ con $f'(c) = 0$:
    - Si $f''(c) > 0$, entonces $f(c)$ es un mínimo relativo
    - Si $f''(c) < 0$, entonces $f(c)$ es un máximo relativo
    - Si $f''(c) = 0$, la prueba no decide
    """)
    
    # Sección Aplicaciones adicionales
    st.markdown("## Aplicaciones adicionales: Rectas tangente y normal")
    
    st.markdown("### Definición: Rectas tangente y normal")
    st.markdown("""
    Sea $f$ derivable en $x_1$:
    - **Recta tangente**: pasa por $(x_1, y_1)$ con pendiente $m_T = f'(x_1)$
    - **Recta normal**: pasa por $(x_1, y_1)$ con pendiente $m_N = -\\frac{1}{f'(x_1)}$
    """)
    
    st.markdown("### Ecuaciones:")
    st.markdown("""
    - Tangente: $y - y_1 = f'(x_1)(x - x_1)$
    - Normal: $y - y_1 = -\\frac{1}{f'(x_1)}(x - x_1)$
    """)
    
    st.markdown("### Longitudes relacionadas con la tangente y normal")
    st.markdown("""
    Para una curva $y = f(x)$ en el punto $P_1(x_1, y_1)$:
    - **Subtangente**: $\\overline{AQ} = \\left|\\frac{y_1}{f'(x_1)}\\right|$
    - **Subnormal**: $\\overline{QB} = |y_1 f'(x_1)|$
    - **Tangente**: $\\overline{AP_1} = \\left|\\frac{y_1}{f'(x_1)}\\right|\\sqrt{1 + [f'(x_1)]^2}$
    - **Normal**: $\\overline{BP_1} = |y_1|\\sqrt{1 + [f'(x_1)]^2}$
    """)
    
    # Sección Ejemplos resueltos
    st.markdown("## Ejemplos resueltos")
    
    st.markdown("### Ejemplo: Prueba de la primera derivada")
    st.markdown("""
    Encontrar los extremos relativos de $f(x) = x^3 - 3x^2 + 2$

    **Solución:**
    1. $f'(x) = 3x^2 - 6x = 3x(x - 2)$
    2. Puntos críticos: $x = 0$, $x = 2$
    3. Signo de $f'$:
       - $(-\\infty, 0)$: $f'(x) > 0$ (creciente)
       - $(0, 2)$: $f'(x) < 0$ (decreciente)
       - $(2, \\infty)$: $f'(x) > 0$ (creciente)
    4. $f(0) = 2$ es máximo relativo, $f(2) = -2$ es mínimo relativo
    """)
    
    st.markdown("### Ejemplo: Prueba de la segunda derivada")
    st.markdown("""
    Encontrar los extremos relativos de $f(x) = x^4 - 4x^3$

    **Solución:**
    1. $f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3)$
    2. Puntos críticos: $x = 0$, $x = 3$
    3. $f''(x) = 12x^2 - 24x = 12x(x - 2)$
    4. $f''(0) = 0$ (prueba no decide), $f''(3) = 36 > 0$ (mínimo relativo)
    5. $f(3) = -27$ es mínimo relativo
    """)

if __name__ == "__main__":
    app()