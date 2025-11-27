import streamlit as st

def app():
    st.title("📚 Cálculo 3: Bloque III")

    # Sección 1: Integrales dobles
    st.markdown("## 1. Definición y evaluación de integrales dobles. Cambio de orden de integración")
    
    st.markdown("### Definición: Integral Doble sobre un Rectángulo")
    st.markdown("""
    Sea $f: R = [a,b] \\times [c,d] \\to \\mathbb{R}$ una función acotada. La integral doble de $f$ sobre $R$ es:
    """)
    st.latex(r"""
    \iint_R f(x,y) \, dA = \lim_{m,n \to \infty} \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*) \Delta A
    """)
    st.markdown("si el límite existe.")
    
    st.markdown("### Teorema: Teorema de Fubini")
    st.markdown("Si $f$ es continua en $R = [a,b] \\times [c,d]$, entonces:")
    st.latex(r"""
    \iint_R f(x,y) \, dA = \int_a^b \int_c^d f(x,y) \, dy \, dx = \int_c^d \int_a^b f(x,y) \, dx \, dy
    """)
    
    st.markdown("### Definición: Integral Doble sobre Regiones Generalizadas")
    st.markdown("""
    1. **Región Tipo I**: $D = \\{(x,y) : a \\leq x \\leq b, g_1(x) \\leq y \\leq g_2(x)\\}$
    """)
    st.latex(r"""
    \iint_D f(x,y) \, dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) \, dy \, dx
    """)
    st.markdown("""
    2. **Región Tipo II**: $D = \\{(x,y) : c \\leq y \\leq d, h_1(y) \\leq x \\leq h_2(y)\\}$
    """)
    st.latex(r"""
    \iint_D f(x,y) \, dA = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y) \, dx \, dy
    """)
    
    st.markdown("### Teorema: Cambio de Orden de Integración")
    st.markdown("El cambio de orden de integración puede simplificar el cálculo cuando:")
    st.markdown("""
    - Los límites de integración son funciones complicadas
    - La función es más fácil de integrar en un orden específico
    - La región de integración se describe más fácilmente en el otro orden
    """)

    # Sección 2: Transformación de coordenadas
    st.markdown("## 2. Transformación de coordenadas")
    
    st.markdown("### Definición: Transformación de Coordenadas")
    st.markdown("Una transformación $T: \\mathbb{R}^2 \\to \\mathbb{R}^2$ es una función que asigna $(u,v)$ a $(x,y)$ mediante:")
    st.latex(r"""
    x = g(u,v), \quad y = h(u,v)
    """)
    
    st.markdown("### Definición: Jacobiano")
    st.markdown("El Jacobiano de la transformación $T$ es el determinante:")
    st.latex(r"""
    \frac{\partial(x,y)}{\partial(u,v)} = 
    \begin{vmatrix}
    \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
    \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
    \end{vmatrix}
    = \frac{\partial x}{\partial u} \frac{\partial y}{\partial v} - \frac{\partial x}{\partial v} \frac{\partial y}{\partial u}
    """)
    
    st.markdown("### Teorema: Cambio de Variables en Integrales Dobles")
    st.markdown("Sea $T: S \\to D$ una transformación uno-a-uno con Jacobiano no nulo. Entonces:")
    st.latex(r"""
    \iint_D f(x,y) \, dA = \iint_S f(g(u,v), h(u,v)) \left| \frac{\partial(x,y)}{\partial(u,v)} \right| \, du \, dv
    """)

    # Sección 3: Integrales dobles en coordenadas polares
    st.markdown("## 3. Integrales dobles en coordenadas polares")
    
    st.markdown("### Definición: Coordenadas Polares")
    st.markdown("La transformación a coordenadas polares está dada por:")
    st.latex(r"""
    x = r \cos \theta, \quad y = r \sin \theta
    """)
    st.markdown("donde $r \\geq 0$ y $0 \\leq \\theta \\leq 2\\pi$.")
    
    st.markdown("### Teorema: Jacobiano en Coordenadas Polares")
    st.markdown("El Jacobiano de la transformación a polares es:")
    st.latex(r"""
    \frac{\partial(x,y)}{\partial(r,\theta)} = 
    \begin{vmatrix}
    \cos \theta & -r \sin \theta \\
    \sin \theta & r \cos \theta
    \end{vmatrix}
    = r
    """)
    
    st.markdown("### Teorema: Integral Doble en Polares")
    st.latex(r"""
    \iint_D f(x,y) \, dA = \iint_S f(r \cos \theta, r \sin \theta) \, r \, dr \, d\theta
    """)
    
    st.markdown("### Corolario: Regiones Comunes en Polares")
    st.markdown("""
    - **Disco**: $0 \\leq r \\leq a$, $0 \\leq \\theta \\leq 2\\pi$
    - **Sector circular**: $0 \\leq r \\leq a$, $\\alpha \\leq \\theta \\leq \\beta$
    - **Anillo**: $a \\leq r \\leq b$, $0 \\leq \\theta \\leq 2\\pi$
    """)

    # Sección 4: Integrales triples
    st.markdown("## 4. Integrales triples en rectangulares, cilíndricas y esféricas")
    
    st.markdown("### Definición: Integral Triple en Coordenadas Rectangulares")
    st.latex(r"""
    \iiint_E f(x,y,z) \, dV = \iiint_E f(x,y,z) \, dz \, dy \, dx
    """)
    
    st.markdown("### Teorema: Fubini para Integrales Triples")
    st.markdown("Si $E = [a,b] \\times [c,d] \\times [p,q]$, entonces:")
    st.latex(r"""
    \iiint_E f(x,y,z) \, dV = \int_a^b \int_c^d \int_p^q f(x,y,z) \, dz \, dy \, dx
    """)
    
    st.markdown("### Definición: Coordenadas Cilíndricas")
    st.latex(r"""
    x = r \cos \theta, \quad y = r \sin \theta, \quad z = z
    """)
    st.markdown("donde $r \\geq 0$, $0 \\leq \\theta \\leq 2\\pi$, $z \\in \\mathbb{R}$.")
    
    st.markdown("### Teorema: Integral Triple en Cilíndricas")
    st.markdown("El elemento de volumen en cilíndricas es $dV = r \\, dz \\, dr \\, d\\theta$, luego:")
    st.latex(r"""
    \iiint_E f(x,y,z) \, dV = \iiint_S f(r \cos \theta, r \sin \theta, z) \, r \, dz \, dr \, d\theta
    """)
    
    st.markdown("### Definición: Coordenadas Esféricas")
    st.latex(r"""
    x = \rho \sin \phi \cos \theta, \quad y = \rho \sin \phi \sin \theta, \quad z = \rho \cos \phi
    """)
    st.markdown("donde $\\rho \\geq 0$, $0 \\leq \\theta \\leq 2\\pi$, $0 \\leq \\phi \\leq \\pi$.")
    
    st.markdown("### Teorema: Jacobiano en Esféricas")
    st.markdown("El elemento de volumen en esféricas es $dV = \\rho^2 \\sin \\phi \\, d\\rho \\, d\\phi \\, d\\theta$.")
    
    st.markdown("### Teorema: Integral Triple en Esféricas")
    st.latex(r"""
    \iiint_E f(x,y,z) \, dV = \iiint_S f(\rho \sin \phi \cos \theta, \rho \sin \phi \sin \theta, \rho \cos \phi) \, \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
    """)

    # Sección 5: Aplicaciones
    st.markdown("## 5. Aplicaciones")
    
    st.markdown("### Teorema: Área de una Superficie")
    st.markdown("El área de la superficie $z = f(x,y)$ sobre la región $D$ es:")
    st.latex(r"""
    S = \iint_D \sqrt{1 + \left(\frac{\partial f}{\partial x}\right)^2 + \left(\frac{\partial f}{\partial y}\right)^2} \, dA
    """)
    
    st.markdown("### Definición: Aplicaciones Físicas")
    st.markdown("""
    - **Masa**: $m = \\iiint_E \\rho(x,y,z) \\, dV$
    - **Centro de Masa**: 
    """)
    st.latex(r"""
    \bar{x} = \frac{1}{m} \iiint_E x \rho \, dV, \quad
    \bar{y} = \frac{1}{m} \iiint_E y \rho \, dV, \quad
    \bar{z} = \frac{1}{m} \iiint_E z \rho \, dV
    """)
    st.markdown("- **Momentos de Inercia**:")
    st.latex(r"""
    \begin{align*}
    I_x &= \iiint_E (y^2 + z^2) \rho \, dV \\
    I_y &= \iiint_E (x^2 + z^2) \rho \, dV \\
    I_z &= \iiint_E (x^2 + y^2) \rho \, dV
    \end{align*}
    """)
    
    st.markdown("### Teorema: Volumen usando Integrales Múltiples")
    st.latex(r"""
    V = \iiint_E dV
    """)
    
    st.markdown("### Corolario: Valor Promedio")
    st.markdown("El valor promedio de $f$ sobre la región $E$ es:")
    st.latex(r"""
    f_{\text{prom}} = \frac{1}{\text{Vol}(E)} \iiint_E f(x,y,z) \, dV
    """)

    # Sección 6: Graficación con CAS
    st.markdown("## 6. Graficación de funciones suaves en $\\mathbb{R}^3$ con el uso de CAS")
    
    st.markdown("### Definición: Superficies Paramétricas")
    st.markdown("Una superficie paramétrica en $\\mathbb{R}^3$ está dada por:")
    st.latex(r"""
    \mathbf{r}(u,v) = (x(u,v), y(u,v), z(u,v)), \quad (u,v) \in D
    """)
    
    st.markdown("### Teorema: Elemento de Área en Superficies Paramétricas")
    st.markdown("El elemento de área para una superficie paramétrica es:")
    st.latex(r"""
    dS = \|\mathbf{r}_u \times \mathbf{r}_v\| \, du \, dv
    """)
    st.markdown("donde $\\mathbf{r}_u$ y $\\mathbf{r}_v$ son las derivadas parciales.")
    
    st.markdown("### Definición: Técnicas de Visualización con CAS")
    st.markdown("""
    1. **Plot 3D**: Para funciones explícitas $z = f(x,y)$
    2. **ParametricPlot3D**: Para superficies paramétricas
    3. **ContourPlot3D**: Para superficies implícitas $F(x,y,z) = 0$
    4. **RegionPlot3D**: Para regiones sólidas
    5. **VectorPlot3D**: Para campos vectoriales
    """)
    
    st.markdown("### Teorema: Visualización de Integrales Múltiples")
    st.markdown("Con CAS podemos visualizar:")
    st.markdown("""
    - La región de integración en 3D
    - La función integrando como superficie coloreada
    - Las proyecciones en los planos coordenados
    - Las trazas y secciones transversales
    - La evolución de la integración iterada
    """)
    
    st.markdown("### Corolario: Estrategias para Elegir Sistema de Coordenadas")
    st.markdown("""
    - Usar **rectangulares** para regiones definidas por planos
    - Usar **cilíndricas** para regiones con simetría axial
    - Usar **esféricas** para regiones con simetría esférica
    - Considerar el cambio cuando el integrando se simplifica
    """)
    
    st.markdown("### Proposición: Verificación de Resultados con CAS")
    st.markdown("""
    1. Calcular la integral en diferentes órdenes de integración
    2. Usar diferentes sistemas de coordenadas
    3. Comparar con valores numéricos aproximados
    4. Verificar propiedades como linealidad y aditividad
    5. Calcular cantidades físicas conocidas (volumen, masa, etc.)
    """)

if __name__ == "__main__":
    app()