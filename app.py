import streamlit as st
import pandas as pd
import json
import os

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

    # crear nuevo id
    new_id = max([c["id"] for c in conceptos], default=0) + 1

    # insertar
    conceptos.append({
        "id": new_id,
        "termino": termino,
        "definicion": definicion
    })

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
# Importar vistas
# ========================
from parcial_uno import parcial_uno
from parcial_dos import parcial_dos
from parcial_tres import parcial_tres

# ========================
# Configuración
# ========================
st.set_page_config(page_title="Diccionario Cálculo III", layout="centered")

# ========================
# Menú lateral
# ========================
menu = st.sidebar.radio(
    "Selecciona una vista:",
    ["Diccionario", "Cálculo III Parcial I", "Cálculo III Parcial II", "Cálculo III Parcial III"]
)

# ===========================================================
# VISTA DICCIONARIO
# ===========================================================
if menu == "Diccionario":
    st.title("📘 Diccionario interactivo de Cálculo III")

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
                registro_id = st.session_state["edit_id"]
                update_definicion_by_id(registro_id, word, definition)
                st.success(f"Actualizado correctamente: {word}")

                del st.session_state["edit_word"]
                del st.session_state["edit_def"]
                del st.session_state["edit_id"]

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
# OTRAS VISTAS
# ===========================================================
elif menu == "Cálculo III Parcial I":
    parcial_uno.app()

elif menu == "Cálculo III Parcial II":
    parcial_dos.app()

elif menu == "Cálculo III Parcial III":
    parcial_tres.app()
