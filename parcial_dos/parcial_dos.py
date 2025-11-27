import streamlit as st

def app():
    st.title("📚 Cálculo 3: Bloque II")

    # Sección 1: Derivadas parciales
    st.markdown("## 1. Derivadas parciales, definición, notación y cálculo")
    
    st.markdown("### Definición: Derivada Parcial")
    st.markdown("""
    Sea $f: D \\subset \\mathbb{R}^n \\to \\mathbb{R}$ y $\\mathbf{a} = (a_1, a_2, \\dots, a_n) \\in D$. 
    La derivada parcial de $f$ con respecto a $x_i$ en $\\mathbf{a}$ es:
    """)
    st.latex(r"""
    \frac{\partial f}{\partial x_i}(\mathbf{a}) = \lim_{h \to 0} \frac{f(a_1, \dots, a_i + h, \dots, a_n) - f(a_1, \dots, a_i, \dots, a_n)}{h}
    """)
    st.markdown("si el límite existe.")
    
    st.markdown("### Definición: Notaciones")
    st.markdown("Las derivadas parciales se denotan de varias formas:")
    st.markdown("""
    - $\\frac{\\partial f}{\\partial x_i}(\\mathbf{x})$
    - $f_{x_i}(\\mathbf{x})$
    - $D_i f(\\mathbf{x})$
    - $\\partial_{x_i} f(\\mathbf{x})$
    """)
    
    st.markdown("### Teorema: Cálculo de Derivadas Parciales")
    st.markdown("""
    Para calcular $\\frac{\\partial f}{\\partial x_i}$, se tratan todas las variables excepto $x_i$ como constantes 
    y se deriva con respecto a $x_i$ usando las reglas del cálculo univariado.
    """)

    # Sección 2: Derivadas de orden superior
    st.markdown("## 2. Derivadas de orden superior")
    
    st.markdown("### Definición: Derivadas Parciales Segundas")
    st.markdown("Las derivadas parciales de segundo orden de $f: \\mathbb{R}^2 \\to \\mathbb{R}$ son:")
    st.latex(r"""
    \begin{align*}
    \frac{\partial^2 f}{\partial x^2} &= \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) \\
    \frac{\partial^2 f}{\partial y^2} &= \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right) \\
    \frac{\partial^2 f}{\partial x \partial y} &= \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right) \\
    \frac{\partial^2 f}{\partial y \partial x} &= \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)
    \end{align*}
    """)
    
    st.markdown("### Teorema: Teorema de Clairaut (Schwarz)")
    st.markdown("""
    Si $f: D \\subset \\mathbb{R}^2 \\to \\mathbb{R}$ tiene derivadas parciales segundas mixtas continuas 
    en una bola abierta alrededor de $(a,b)$, entonces:
    """)
    st.latex(r"""
    \frac{\partial^2 f}{\partial x \partial y}(a,b) = \frac{\partial^2 f}{\partial y \partial x}(a,b)
    """)

    # Sección 3: Diferenciabilidad de funciones
    st.markdown("## 3. Diferenciabilidad de funciones")
    
    st.markdown("### Definición: Diferenciabilidad")
    st.markdown("""
    Una función $f: D \\subset \\mathbb{R}^n \\to \\mathbb{R}$ es diferenciable en $\\mathbf{a} \\in D$ 
    si existe una transformación lineal $L: \\mathbb{R}^n \\to \\mathbb{R}$ tal que:
    """)
    st.latex(r"""
    \lim_{\mathbf{h} \to \mathbf{0}} \frac{f(\mathbf{a} + \mathbf{h}) - f(\mathbf{a}) - L(\mathbf{h})}{\|\mathbf{h}\|} = 0
    """)
    st.markdown("En este caso, $L$ se llama la diferencial de $f$ en $\\mathbf{a}$.")
    
    st.markdown("### Teorema: Diferenciabilidad implica Continuidad")
    st.markdown("Si $f$ es diferenciable en $\\mathbf{a}$, entonces $f$ es continua en $\\mathbf{a}$.")
    
    st.markdown("### Teorema: Condición Suficiente para Diferenciabilidad")
    st.markdown("""
    Si todas las derivadas parciales de $f$ existen y son continuas en una bola abierta alrededor de $\\mathbf{a}$, 
    entonces $f$ es diferenciable en $\\mathbf{a}$.
    """)

    # Sección 4: Regla de la cadena
    st.markdown("## 4. Regla de la cadena")
    
    st.markdown("### Teorema: Regla de la Cadena - Caso 1")
    st.markdown("""
    Sea $f: \\mathbb{R}^n \\to \\mathbb{R}$ y $\\mathbf{g}: \\mathbb{R} \\to \\mathbb{R}^n$. 
    Si $f$ es diferenciable y $\\mathbf{g}$ es diferenciable, entonces:
    """)
    st.latex(r"""
    \frac{d}{dt} f(\mathbf{g}(t)) = \nabla f(\mathbf{g}(t)) \cdot \mathbf{g}'(t) = \sum_{i=1}^n \frac{\partial f}{\partial x_i} \frac{dx_i}{dt}
    """)
    
    st.markdown("### Teorema: Regla de la Cadena - Caso 2")
    st.markdown("""
    Sea $f: \\mathbb{R}^2 \\to \\mathbb{R}$ y $x,y: \\mathbb{R}^2 \\to \\mathbb{R}$. 
    Si $f$ es diferenciable y $x,y$ tienen derivadas parciales, entonces:
    """)
    st.latex(r"""
    \frac{\partial f}{\partial u} = \frac{\partial f}{\partial x} \frac{\partial x}{\partial u} + \frac{\partial f}{\partial y} \frac{\partial y}{\partial u}
    """)
    st.latex(r"""
    \frac{\partial f}{\partial v} = \frac{\partial f}{\partial x} \frac{\partial x}{\partial v} + \frac{\partial f}{\partial y} \frac{\partial y}{\partial v}
    """)

    # Sección 5: Derivada direccional y gradiente
    st.markdown("## 5. Derivada direccional y gradiente")
    
    st.markdown("### Definición: Derivada Direccional")
    st.markdown("""
    La derivada direccional de $f$ en $\\mathbf{a}$ en la dirección del vector unitario $\\mathbf{u}$ es:
    """)
    st.latex(r"""
    D_{\mathbf{u}} f(\mathbf{a}) = \lim_{h \to 0} \frac{f(\mathbf{a} + h\mathbf{u}) - f(\mathbf{a})}{h}
    """)
    
    st.markdown("### Definición: Gradiente")
    st.markdown("El gradiente de $f: \\mathbb{R}^n \\to \\mathbb{R}$ en $\\mathbf{a}$ es el vector:")
    st.latex(r"""
    \nabla f(\mathbf{a}) = \left(\frac{\partial f}{\partial x_1}(\mathbf{a}), \frac{\partial f}{\partial x_2}(\mathbf{a}), \dots, \frac{\partial f}{\partial x_n}(\mathbf{a})\right)
    """)
    
    st.markdown("### Teorema: Relación entre Gradiente y Derivada Direccional")
    st.markdown("Si $f$ es diferenciable en $\\mathbf{a}$, entonces:")
    st.latex(r"""
    D_{\mathbf{u}} f(\mathbf{a}) = \nabla f(\mathbf{a}) \cdot \mathbf{u}
    """)

    # Sección 6: Aplicación de la derivada direccional y gradiente
    st.markdown("## 6. Aplicación de la derivada direccional y gradiente")
    
    st.markdown("### Teorema: Propiedades del Gradiente")
    st.markdown("Sea $f$ diferenciable en $\\mathbf{a}$:")
    st.markdown("""
    1. La dirección de máximo crecimiento de $f$ es $\\nabla f(\\mathbf{a})$
    2. La tasa máxima de crecimiento es $\\|\\nabla f(\\mathbf{a})\\|$
    3. La dirección de máximo decrecimiento es $-\\nabla f(\\mathbf{a})$
    4. $\\nabla f(\\mathbf{a})$ es perpendicular a la curva de nivel que pasa por $\\mathbf{a}$
    """)
    
    st.markdown("### Corolario")
    st.markdown("Si $\\nabla f(\\mathbf{a}) = \\mathbf{0}$, entonces $D_{\\mathbf{u}} f(\\mathbf{a}) = 0$ para toda dirección $\\mathbf{u}$.")

    # Sección 7: Máximos y mínimos sin restricciones
    st.markdown("## 7. Máximos y mínimos sin restricciones")
    
    st.markdown("### Definición: Punto Crítico")
    st.markdown("""
    Un punto $\\mathbf{a} \\in D$ es punto crítico de $f$ si $\\nabla f(\\mathbf{a}) = \\mathbf{0}$ 
    o si $\\nabla f(\\mathbf{a})$ no existe.
    """)
    
    st.markdown("### Definición: Matriz Hessiana")
    st.markdown("Para $f: \\mathbb{R}^2 \\to \\mathbb{R}$, la matriz Hessiana en $(a,b)$ es:")
    st.latex(r"""
    H(a,b) = \begin{bmatrix}
    f_{xx}(a,b) & f_{xy}(a,b) \\
    f_{yx}(a,b) & f_{yy}(a,b)
    \end{bmatrix}
    """)
    
    st.markdown("### Teorema: Test de la Segunda Derivada")
    st.markdown("""
    Sea $(a,b)$ un punto crítico de $f$ y sea $D = f_{xx}(a,b)f_{yy}(a,b) - [f_{xy}(a,b)]^2$:
    - Si $D > 0$ y $f_{xx}(a,b) > 0$: mínimo local
    - Si $D > 0$ y $f_{xx}(a,b) < 0$: máximo local
    - Si $D < 0$: punto silla
    - Si $D = 0$: el test no decide
    """)

    # Sección 8: Máximos y mínimos con restricciones
    st.markdown("## 8. Máximos y mínimos con restricciones y multiplicadores de Lagrange")
    
    st.markdown("### Teorema: Multiplicadores de Lagrange - Una restricción")
    st.markdown("""
    Sean $f$ y $g$ funciones con derivadas parciales continuas. Los extremos de $f$ sujetos a $g(\\mathbf{x}) = k$ 
    ocurren en puntos $\\mathbf{a}$ donde:
    """)
    st.latex(r"""
    \nabla f(\mathbf{a}) = \lambda \nabla g(\mathbf{a})
    """)
    st.markdown("para algún $\\lambda \\in \\mathbb{R}$ (multiplicador de Lagrange).")
    
    st.markdown("### Teorema: Multiplicadores de Lagrange - Dos restricciones")
    st.markdown("Para optimizar $f$ sujeto a $g(\\mathbf{x}) = k$ y $h(\\mathbf{x}) = c$, resolvemos:")
    st.latex(r"""
    \nabla f(\mathbf{a}) = \lambda \nabla g(\mathbf{a}) + \mu \nabla h(\mathbf{a})
    """)

    # Sección 9: Serie de Taylor en dos variables
    st.markdown("## 9. Serie de Taylor en dos variables")
    
    st.markdown("### Definición: Polinomio de Taylor de Segundo Orden")
    st.markdown("Para $f: \\mathbb{R}^2 \\to \\mathbb{R}$ alrededor de $(a,b)$:")
    st.latex(r"""
    \begin{align*}
    P_2(x,y) = & f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b) \\
    & + \frac{1}{2}\left[f_{xx}(a,b)(x-a)^2 + 2f_{xy}(a,b)(x-a)(y-b) + f_{yy}(a,b)(y-b)^2\right]
    \end{align*}
    """)
    
    st.markdown("### Teorema: Fórmula de Taylor")
    st.markdown("""
    Si $f$ tiene derivadas parciales continuas hasta orden $n+1$ en una bola abierta que contiene $(a,b)$, entonces:
    """)
    st.latex(r"""
    f(x,y) = P_n(x,y) + R_n(x,y)
    """)
    st.markdown("donde $R_n(x,y)$ es el resto.")

    # Sección 10: Graficación de funciones suaves
    st.markdown("## 10. Graficación de funciones suaves en $\\mathbb{R}^3$ y visualización de máximos y mínimos")
    
    st.markdown("### Definición: Superficie Suave")
    st.markdown("Una superficie $z = f(x,y)$ es suave si $f$ tiene derivadas parciales continuas de primer orden.")
    
    st.markdown("### Teorema: Plano Tangente")
    st.markdown("""
    Si $f$ es diferenciable en $(a,b)$, el plano tangente a la superficie $z = f(x,y)$ en $(a,b,f(a,b))$ es:
    """)
    st.latex(r"""
    z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)
    """)
    
    st.markdown("### Definición: Puntos de Interés en Visualización")
    st.markdown("En la gráfica de $f: \\mathbb{R}^2 \\to \\mathbb{R}$:")
    st.markdown("""
    - **Máximos locales**: Picos en la superficie
    - **Mínimos locales**: Valles en la superficie  
    - **Puntos silla**: Puntos que son máximos en una dirección y mínimos en otra
    - **Curvas de nivel**: Proporcionan información sobre la pendiente
    """)
    
    st.markdown("### Corolario: Técnicas de Visualización con CAS")
    st.markdown("Para visualizar funciones y sus extremos:")
    st.markdown("""
    1. Graficar la superficie en 3D
    2. Superponer curvas de nivel
    3. Marcar puntos críticos con diferentes colores
    4. Dibujar vectores gradiente
    5. Mostrar planos tangentes en puntos críticos
    """)
    
    st.markdown("### Teorema: Interpretación Geométrica del Gradiente")
    st.markdown("""
    En la gráfica 3D de $f$, el vector $\\nabla f(a,b)$ apunta en la dirección de máxima pendiente 
    en el punto $(a,b,f(a,b))$, y su magnitud representa la tasa de cambio en esa dirección.
    """)

if __name__ == "__main__":
    app()