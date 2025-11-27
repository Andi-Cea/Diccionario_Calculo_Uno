import streamlit as st

def app():
    st.title("📚 Unidad 4: La Derivada")
    
    # Sección 4.1
    st.markdown("## 4.1 Concepto de derivada")
    
    st.markdown("### Definición: Derivada en un punto")
    st.markdown("""
    La **derivada** de una función $f$ en un número $x = a$, denotada por $f'(a)$, es:
    """)
    st.latex(r"f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}")
    st.markdown("siempre que este límite exista.")
    
    st.markdown("Forma equivalente:")
    st.latex(r"f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}")
    
    st.markdown("### Definición: Función derivada")
    st.markdown("La **función derivada** de $f$ es:")
    st.latex(r"f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}")
    st.markdown("para todo $x$ donde exista el límite.")
    
    # Sección 4.2
    st.markdown("## 4.2 Interpretación geométrica. Ángulos entre curvas")
    
    st.markdown("""
    - La derivada $f'(a)$ representa la **pendiente** de la recta tangente a la curva $y = f(x)$ en el punto $(a, f(a))$.
    - La ecuación de la recta tangente es:
    """)
    st.latex(r"y - f(a) = f'(a)(x - a)")
    
    st.markdown("""
    - La pendiente de la recta secante que pasa por $(a, f(a))$ y $(a + h, f(a + h))$ es:
    """)
    st.latex(r"m_{sec} = \frac{f(a + h) - f(a)}{h}")
    
    # Sección 4.3
    st.markdown("## 4.3 Teoremas sobre la derivación de funciones elementales")
    
    st.markdown("### Derivadas de funciones algebraicas")
    
    st.markdown("#### Teorema: Reglas básicas")
    st.markdown("""
    - $\\dfrac{d}{dx}(c) = 0$
    - $\\dfrac{d}{dx}(x) = 1$
    - $\\dfrac{d}{dx}(x^n) = nx^{n-1}$
    - $\\dfrac{d}{dx}(cf(x)) = cf'(x)$
    - $\\dfrac{d}{dx}(f(x) + g(x)) = f'(x) + g'(x)$
    """)
    
    st.markdown("#### Teorema: Regla del producto")
    st.markdown("Si $f$ y $g$ son derivables en $a$, entonces:")
    st.latex(r"(fg)'(a) = f'(a)g(a) + f(a)g'(a)")
    
    st.markdown("#### Teorema: Regla del cociente")
    st.markdown("Si $f$ y $g$ son derivables en $a$ y $g(a) \\neq 0$, entonces:")
    st.latex(r"\left(\frac{f}{g}\right)'(a) = \frac{f'(a)g(a) - f(a)g'(a)}{(g(a))^2}")
    
    st.markdown("### Derivadas de funciones trascendentes")
    
    st.markdown("#### Teorema: Funciones trigonométricas")
    st.markdown("""
    - $\\dfrac{d}{dx}(\\sin x) = \\cos x$
    - $\\dfrac{d}{dx}(\\cos x) = -\\sin x$
    - $\\dfrac{d}{dx}(\\tan x) = \\sec^2 x$
    - $\\dfrac{d}{dx}(\\cot x) = -\\csc^2 x$
    - $\\dfrac{d}{dx}(\\sec x) = \\sec x \\tan x$
    - $\\dfrac{d}{dx}(\\csc x) = -\\csc x \\cot x$
    """)
    
    st.markdown("#### Teorema: Funciones trigonométricas inversas")
    st.markdown("""
    - $\\dfrac{d}{dx}(\\arcsin x) = \\dfrac{1}{\\sqrt{1 - x^2}}$
    - $\\dfrac{d}{dx}(\\arccos x) = -\\dfrac{1}{\\sqrt{1 - x^2}}$
    - $\\dfrac{d}{dx}(\\arctan x) = \\dfrac{1}{1 + x^2}$
    - $\\dfrac{d}{dx}(\\mathrm{arcsec}\\, x) = \\dfrac{1}{|x|\\sqrt{x^2 - 1}}$
    """)
    
    st.markdown("#### Teorema: Regla de la cadena")
    st.markdown("Si $g$ es derivable en $a$ y $f$ es derivable en $g(a)$, entonces:")
    st.latex(r"(f \circ g)'(a) = f'(g(a)) \cdot g'(a)")
    
    # Sección 4.4
    st.markdown("## 4.4 Diferenciabilidad de funciones elementales y no elementales")
    
    st.markdown("### Definición: Diferenciabilidad")
    st.markdown("""
    Una función $f$ es **diferenciable** en $x = a$ si $f'(a)$ existe. 
    Es diferenciable sobre un intervalo abierto si es diferenciable en todo número del intervalo.
    """)
    
    st.markdown("### Teorema: Diferenciabilidad implica continuidad")
    st.markdown("Si $f$ es diferenciable en $x = a$, entonces $f$ es continua en $x = a$.")
    
    st.markdown("**NOTA:** El recíproco es falso. Por ejemplo, $f(x) = |x|$ es continua en $x = 0$ pero no es diferenciable allí.")
    
    st.markdown("### Casos donde una función no es diferenciable:")
    st.markdown("""
    - Puntos con \"esquinas\" o \"picos\" (ej: $f(x) = |x|$ en $x = 0$)
    - Discontinuidades
    - Tangentes verticales
    """)
    
    # Sección 4.5
    st.markdown("## 4.5 Diferenciación implícita")
    
    st.markdown("### Definición: Diferenciación implícita")
    st.markdown("""
    Técnica para encontrar la derivada de una función definida implícitamente por una ecuación que relaciona $x$ e $y$.
    """)
    
    st.markdown("### Procedimiento:")
    st.markdown("""
    1. Derivar ambos lados de la ecuación respecto a $x$
    2. Tratar $y$ como función de $x$ y aplicar la regla de la cadena
    3. Agrupar términos con $\\dfrac{dy}{dx}$
    4. Despejar $\\dfrac{dy}{dx}$
    """)
    
    st.markdown("### Ejemplo:")
    st.markdown("Para $x^2 + y^2 = 25$:")
    st.latex(r"2x + 2y\frac{dy}{dx} = 0 \quad \Rightarrow \quad \frac{dy}{dx} = -\frac{x}{y}")
    
    # Sección 4.6
    st.markdown("## 4.6 Derivadas de orden superior")
    
    st.markdown("### Definición: Derivadas de orden superior")
    st.markdown("""
    - Primera derivada: $f'(x) = \\dfrac{d}{dx}f(x)$
    - Segunda derivada: $f''(x) = \\dfrac{d}{dx}f'(x)$
    - Tercera derivada: $f'''(x) = \\dfrac{d}{dx}f''(x)$
    - $n$-ésima derivada: $f^{(n)}(x) = \\dfrac{d}{dx}f^{(n-1)}(x)$
    """)
    
    st.markdown("### Notaciones:")
    st.latex(r"f''(x) = \frac{d^2y}{dx^2}, \quad f'''(x) = \frac{d^3y}{dx^3}, \quad f^{(n)}(x) = \frac{d^ny}{dx^n}")
    
    # Sección 4.7
    st.markdown("## 4.7 Regla de L'Hôpital. Formas indeterminadas")
    
    st.markdown("### Teorema: Regla de L'Hôpital")
    st.markdown("""
    Si $\\lim_{x \\to a} f(x) = 0$ y $\\lim_{x \\to a} g(x) = 0$, o ambos límites son $\\pm\\infty$, 
    y existe $\\lim_{x \\to a} \\frac{f'(x)}{g'(x)}$, entonces:
    """)
    st.latex(r"\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}")
    
    st.markdown("### Formas indeterminadas:")
    st.markdown("""
    - $\\dfrac{0}{0}$ y $\\dfrac{\\infty}{\\infty}$: Aplicar directamente L'Hôpital
    - $0 \\cdot \\infty$: Convertir a $\\dfrac{0}{1/\\infty}$ o $\\dfrac{\\infty}{1/0}$
    - $\\infty - \\infty$: Combinar en una sola fracción
    - $0^0$, $\\infty^0$, $1^\\infty$: Usar logaritmos
    """)
    
    st.markdown("### Ejemplo:")
    st.latex(r"\lim_{x \to 0} \frac{\sin x}{x} = \lim_{x \to 0} \frac{\cos x}{1} = 1")

if __name__ == "__main__":
    app()