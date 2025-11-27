import streamlit as st
import pandas as pd
import json
import os
import sys

# ========================
# Helpers para JSON
# ========================
DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"conceptos": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_definicions():
    data = load_data()
    return [(c["id"], c["termino"], c["definicion"]) for c in data["conceptos"]]

def insert_definicion(termino, definicion):
    data = load_data()
    conceptos = data["conceptos"]
    new_id = max([c["id"] for c in conceptos], default=0) + 1
    conceptos.append({"id": new_id, "termino": termino, "definicion": definicion})
    save_data(data)

def update_definicion_by_id(registro_id, termino, definicion):
    data = load_data()
    for c in data["conceptos"]:
        if c["id"] == registro_id:
            c["termino"] = termino
            c["definicion"] = definicion
            break
    save_data(data)

def delete_definicion(termino):
    data = load_data()
    data["conceptos"] = [c for c in data["conceptos"] if c["termino"] != termino]
    save_data(data)

# ========================
# Importar vistas de las unidades CON MÁS DEPURACIÓN
# ========================
def importar_unidad(nombre_unidad):
    """Función robusta para importar unidades con mejor manejo de errores"""
    try:
        # Verificar si la carpeta existe
        if not os.path.exists(nombre_unidad):
            return None, False, f"Carpeta '{nombre_unidad}' no existe"
        
        # Verificar si el archivo existe
        archivo_py = os.path.join(nombre_unidad, f"{nombre_unidad}.py")
        if not os.path.exists(archivo_py):
            return None, False, f"Archivo '{archivo_py}' no existe"
        
        # Intentar importar
        modulo = __import__(f"{nombre_unidad}.{nombre_unidad}", fromlist=['app'])
        
        # Verificar que tenga la función app
        if hasattr(modulo, 'app'):
            return modulo.app, True, "OK"
        else:
            return None, False, f"Falta función app() en {nombre_unidad}.py"
            
    except ImportError as e:
        return None, False, f"Error de importación: {e}"
    except Exception as e:
        return None, False, f"Error inesperado: {e}"

# Importar cada unidad con más información
unidades = {}
for i, nombre in enumerate(["unidad_uno", "unidad_dos", "unidad_tres", "unidad_cuatro", "unidad_cinco"], 1):
    funcion_app, disponible, mensaje = importar_unidad(nombre)
    unidades[nombre] = {
        'funcion': funcion_app, 
        'disponible': disponible,
        'mensaje': mensaje
    }
    
    # Mostrar estado en consola para depuración
    print(f"{nombre}: {mensaje}")

# ========================
# Configuración
# ========================
st.set_page_config(page_title="Diccionario Cálculo I", layout="centered")

# ========================
# Menú lateral
# ========================
menu = st.sidebar.radio(
    "Selecciona una vista:",
    ["Diccionario", "Unidad I", "Unidad II", "Unidad III", "Unidad IV", "Unidad V"]
)

# Mostrar estado de las unidades en el sidebar para depuración
with st.sidebar.expander("🔧 Estado de Unidades"):
    for i, nombre in enumerate(["unidad_uno", "unidad_dos", "unidad_tres", "unidad_cuatro", "unidad_cinco"], 1):
        estado = "✅" if unidades[nombre]['disponible'] else "❌"
        st.write(f"{estado} Unidad {i}: {unidades[nombre]['mensaje']}")

# ===========================================================
# VISTA DICCIONARIO
# ===========================================================
if menu == "Diccionario":
    st.title("📘 Diccionario interactivo de Cálculo I")

    # BUSCADOR
    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input("Buscar término", value="", placeholder="Escribe una palabra...")
    with col2:
        exact = st.checkbox("Búsqueda exacta", value=False)

    # Cargar datos
    rows = get_definicions()
    data = {r[1]: r[2] for r in rows}
    id_map = {r[1]: r[0] for r in rows}

    def search(q, exact_match):
        q = q.strip().lower()
        if not q:
            return sorted(data.items())
        if exact_match:
            return [(k, v) for k, v in data.items() if k.lower() == q]
        return [(k, v) for k, v in data.items() if q in k.lower() or q in v.lower()]

    results = search(query, exact)

    # RESULTADOS
    st.markdown("---")
    st.subheader(f"Resultados ({len(results)})")
    for palabra, defin in results:
        with st.expander(palabra):
            st.write(defin)
            colA, colB = st.columns(2)
            with colA:
                if st.button("✏️ Editar", key=f"edit_{palabra}"):
                    st.session_state["edit_word"] = palabra
                    st.session_state["edit_def"] = defin
                    st.session_state["edit_id"] = id_map[palabra]
                    st.rerun()
            with colB:
                if st.button("🗑️ Eliminar", key=f"del_{palabra}"):
                    delete_definicion(palabra)
                    st.success(f"'{palabra}' eliminado correctamente.")
                    st.rerun()

    st.markdown("---")
    
    # FORMULARIO AGREGAR / EDITAR
    st.subheader("Añadir o editar término")
    default_word = st.session_state.get("edit_word", "")
    default_def = st.session_state.get("edit_def", "")

    with st.form("form_add"):
        word = st.text_input("Término", value=default_word)
        definition = st.text_area("Definición", value=default_def, height=150)
        submitted = st.form_submit_button("Guardar")

    if submitted:
        word = word.strip()
        definition = definition.strip()
        if not word:
            st.error("El término no puede estar vacío.")
        else:
            if "edit_id" in st.session_state:
                update_definicion_by_id(st.session_state["edit_id"], word, definition)
                st.success(f"Actualizado correctamente: {word}")
                for key in ["edit_word", "edit_def", "edit_id"]:
                    if key in st.session_state:
                        del st.session_state[key]
            else:
                insert_definicion(word, definition)
                st.success(f"Guardado: {word}")
            st.rerun()

    # TABLA COMPLETA
    if st.checkbox("Mostrar tabla completa"):
        if rows:
            df = pd.DataFrame(rows, columns=["ID", "Término", "Definición"])
            st.dataframe(df, use_container_width=True)

# ===========================================================
# VISTAS DE LAS UNIDADES
# ===========================================================
elif menu == "Unidad I":
    if unidades['unidad_uno']['disponible']:
        unidades['unidad_uno']['funcion']()
    else:
        st.error(f"❌ Unidad I no disponible: {unidades['unidad_uno']['mensaje']}")
        mostrar_solucion_unidad("unidad_uno")

elif menu == "Unidad II":
    if unidades['unidad_dos']['disponible']:
        unidades['unidad_dos']['funcion']()
    else:
        st.error(f"❌ Unidad II no disponible: {unidades['unidad_dos']['mensaje']}")
        mostrar_solucion_unidad("unidad_dos")

elif menu == "Unidad III":
    if unidades['unidad_tres']['disponible']:
        unidades['unidad_tres']['funcion']()
    else:
        st.error(f"❌ Unidad III no disponible: {unidades['unidad_tres']['mensaje']}")
        mostrar_solucion_unidad("unidad_tres")

elif menu == "Unidad IV":
    if unidades['unidad_cuatro']['disponible']:
        unidades['unidad_cuatro']['funcion']()
    else:
        st.error(f"❌ Unidad IV no disponible: {unidades['unidad_cuatro']['mensaje']}")
        mostrar_solucion_unidad("unidad_cuatro")

elif menu == "Unidad V":
    if unidades['unidad_cinco']['disponible']:
        unidades['unidad_cinco']['funcion']()
    else:
        st.error(f"❌ Unidad V no disponible: {unidades['unidad_cinco']['mensaje']}")
        mostrar_solucion_unidad("unidad_cinco")

def mostrar_solucion_unidad(nombre_unidad):
    """Muestra información de solución para unidades no disponibles"""
    st.info(f"""
    **Solución para {nombre_unidad}:**
    
    1. **Verificar estructura de carpetas:**
       ```
       {nombre_unidad}/
       ├── __init__.py
       └── {nombre_unidad}.py
       ```
    
    2. **Verificar que {nombre_unidad}.py tenga:**
    ```python
    import streamlit as st
    
    def app():
        st.title("Unidad ...")
        # Tu contenido aquí...
    ```
    
    3. **Ejecutar verificación en terminal:**
    ```bash
    python -c "from {nombre_unidad}.{nombre_unidad} import app; print('✅ OK')"
    ```
    """)
    
    # Mostrar estructura actual del directorio
    if st.checkbox(f"Mostrar estructura de {nombre_unidad}"):
        if os.path.exists(nombre_unidad):
            st.write(f"**Contenido de {nombre_unidad}/:**")
            for item in os.listdir(nombre_unidad):
                st.write(f"- {item}")
        else:
            st.error(f"La carpeta '{nombre_unidad}' no existe")