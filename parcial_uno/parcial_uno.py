import streamlit as st

def app():
    st.title("📚 Cálculo 3: Bloque I")

    # Sección 1: Topología de los espacios cartesianos
    st.markdown("## 1. Topología de los espacios cartesianos")
    
    st.markdown("### Definición: Espacio Cartesiano $\mathbb{R}^n$")
    st.markdown("El espacio cartesiano $\mathbb{R}^n$ es el conjunto de todas las n-tuplas ordenadas de números reales:")
    st.latex(r"\mathbb{R}^n = \{(x_1, x_2, \dots, x_n) : x_i \in \mathbb{R}, i = 1, 2, \dots, n\}")
    
    st.markdown("### Definición: Norma Euclidiana")
    st.markdown("La norma euclidiana de un vector $\\mathbf{x} = (x_1, x_2, \\dots, x_n) \\in \\mathbb{R}^n$ se define como:")
    st.latex(r"\|\mathbf{x}\| = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}")
    
    st.markdown("### Definición: Bola Abierta")
    st.markdown("Dado un punto $\\mathbf{a} \\in \\mathbb{R}^n$ y $r > 0$, la bola abierta de centro $\\mathbf{a}$ y radio $r$ es:")
    st.latex(r"B(\mathbf{a}, r) = \{\mathbf{x} \in \mathbb{R}^n : \|\mathbf{x} - \mathbf{a}\| < r\}")
    
    st.markdown("### Definición: Conjunto Abierto")
    st.markdown("Un conjunto $U \\subset \\mathbb{R}^n$ es abierto si para cada $\\mathbf{a} \\in U$, existe $r > 0$ tal que $B(\\mathbf{a}, r) \\subset U$")
    
    st.markdown("### Definición: Conjunto Cerrado")
    st.markdown("Un conjunto $C \\subset \\mathbb{R}^n$ es cerrado si su complemento $\\mathbb{R}^n \\setminus C$ es abierto.")

    # Sección 2: Conceptos de funciones
    st.markdown("## 2. Conceptos de funciones")
    
    st.markdown("### Definición: Función Real de un Vector")
    st.markdown("Una función $f: D \\subset \\mathbb{R}^n \\to \\mathbb{R}$ se llama función real de un vector:")
    st.latex(r"f(\mathbf{x}) = f(x_1, x_2, \dots, x_n)")
    
    st.markdown("### Definición: Función Vectorial de un Real")
    st.markdown("Una función $\\mathbf{f}: I \\subset \\mathbb{R} \\to \\mathbb{R}^m$ se llama función vectorial de un real:")
    st.latex(r"\mathbf{f}(t) = (f_1(t), f_2(t), \dots, f_m(t))")
    
    st.markdown("### Definición: Función Vectorial de un Vector")
    st.markdown("Una función $\\mathbf{F}: D \\subset \\mathbb{R}^n \\to \\mathbb{R}^m$ se llama función vectorial de un vector:")
    st.latex(r"\mathbf{F}(\mathbf{x}) = (F_1(\mathbf{x}), F_2(\mathbf{x}), \dots, F_m(\mathbf{x}))")

    # Sección 3: Dominio
    st.markdown("## 3. Dominio de una función real de un vector")
    
    st.markdown("### Definición: Dominio")
    st.markdown("El dominio de una función $f: D \\subset \\mathbb{R}^n \\to \\mathbb{R}$ es el conjunto:")
    st.latex(r"\text{Dom}(f) = \{\mathbf{x} \in \mathbb{R}^n : f(\mathbf{x}) \text{ está definida}\}")
    
    st.markdown("### Teorema: Caracterización del Dominio")
    st.markdown("""
    El dominio está determinado por las restricciones que evitan:
    1. División por cero  
    2. Raíces pares de números negativos  
    3. Logaritmos de números no positivos  
    4. Operaciones no definidas en $\mathbb{R}$
    """)

    # Sección 4: Límites
    st.markdown("## 4. Límites de funciones reales de un vector")
    
    st.markdown("### Definición: Límite")
    st.latex(r"\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = L")
    
    st.markdown("### Condición ε–δ")
    st.latex(r"0 < \|\mathbf{x} - \mathbf{a}\| < \delta \ \Rightarrow \ |f(\mathbf{x}) - L| < \epsilon")
    
    st.markdown("### Teorema: Unicidad y propiedades de límites")
    st.markdown("""
    1. $\\lim (f+g) = L+M$  
    2. $\\lim (cf) = cL$  
    3. $\\lim (fg) = LM$  
    4. $\\lim (f/g) = L/M$ si $M \\neq 0$
    """)

    st.markdown("### Teorema: Límites por trayectorias")
    st.markdown("Si dos trayectorias dan límites distintos, el límite no existe.")

    # Sección 5: Continuidad
    st.markdown("## 5. Continuidad de funciones reales de un vector")
    
    st.markdown("### Definición")
    st.latex(r"\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})")
    
    st.markdown("### Teorema: Funciones continuas")
    st.markdown("""
    1. Polinomios  
    2. Racionales  
    3. Trigonométricas  
    4. Exponenciales y logarítmicas
    """)

    st.markdown("### Teorema del Valor Intermedio")
    st.markdown("""
    Si $f$ es continua en un conjunto conexo y $f(a)<k<f(b)$,  
    entonces existe $c$ tal que $f(c)=k$.
    """)

    # Sección 6: Gráficas
    st.markdown("## 6. Graficación de funciones reales con CAS")
    
    st.markdown("### Gráfica")
    st.latex(r"\text{Gráfica}(f)=\{(\mathbf{x},f(\mathbf{x}))\in\mathbb{R}^{n+1}\}")
    
    st.markdown("### Curvas y superficies de nivel")
    st.latex(r"C_c=\{(x,y) : f(x,y)=c\}")
    st.latex(r"S_c=\{(x,y,z) : f(x,y,z)=c\}")

if __name__ == "__main__":
    app()
