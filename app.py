import streamlit as st
import pandas as pd
from db import (
    create_table,
    insert_definicion,
    get_definicions,
    delete_definicion,
    update_definicion_by_id,
)

# ==============================
# Importar vistas Cálculo III
# ==============================
from parcial_uno import parcial_uno
from parcial_dos import parcial_dos
from parcial_tres import parcial_tres

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Diccionario Cálculo III", layout="centered")

# Crear tabla al iniciar
try:
    create_table()
except Exception as e:
    st.error(f"No se pudo crear la tabla: {e}")

# --- MENÚ LATERAL ---
menu = st.sidebar.radio(
    "Selecciona una vista:",
    [
        "Diccionario",
        "Cálculo III Parcial I",
        "Cálculo III Parcial II",
        "Cálculo III Parcial III"
    ]
)

# ===========================================================
# VISTA DICCIONARIO
# ===========================================================
if menu == "Diccionario":
    st.title("📘 Diccionario interactivo de Cálculo III")

    # --------------------------
    # BUSCADOR
    # --------------------------
    col1, col2 = st.columns([3, 1])

    with col1:
        query = st.text_input("Buscar término", value="", placeholder="Escribe una palabra...")

    with col2:
        exact = st.checkbox("Búsqueda exacta", value=False)

    # Cargar definiciones
    try:
        rows = get_definicions()  # (id, termino, definicion)
    except Exception as e:
        st.error(f"No se pudieron cargar las definiciones: {e}")
        rows = []

    # Diccionarios auxiliares
    data = {r[1]: r[2] for r in rows}
    id_map = {r[1]: r[0] for r in rows}  # término → id

    def search(q, exact_match):
        q = q.strip().lower()
        if not q:
            return sorted(data.items())

        if exact_match:
            return [(k, v) for k, v in data.items() if k.lower() == q]

        return [(k, v) for k, v in data.items() if q in k.lower() or q in v.lower()]

    results = search(query, exact)

    # --------------------------
    # RESULTADOS
    # --------------------------
    st.markdown("---")
    st.subheader(f"Resultados ({len(results)})")

    for palabra, defin in results:
        with st.expander(palabra):
            st.write(defin)

            colA, colB = st.columns(2)

            # ---- BOTÓN EDITAR ----
            with colA:
                if st.button("✏️ Editar", key=f"edit_{palabra}"):
                    st.session_state["edit_word"] = palabra
                    st.session_state["edit_def"] = defin
                    st.session_state["edit_id"] = id_map[palabra]
                    st.rerun()

            # ---- BOTÓN ELIMINAR ----
            with colB:
                if st.button("🗑️ Eliminar", key=f"del_{palabra}"):
                    try:
                        delete_definicion(palabra)
                        st.success(f"'{palabra}' eliminado correctamente.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"No se pudo eliminar: {e}")

    st.markdown("---")

    # --------------------------
    # FORMULARIO AGREGAR / EDITAR
    # --------------------------
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
            try:
                # Si estamos editando
                if "edit_id" in st.session_state:
                    registro_id = st.session_state["edit_id"]
                    update_definicion_by_id(registro_id, word, definition)
                    st.success(f"Actualizado correctamente: {word}")

                    # limpiar estado
                    del st.session_state["edit_word"]
                    del st.session_state["edit_def"]
                    del st.session_state["edit_id"]

                # Si estamos insertando
                else:
                    insert_definicion(word, definition)
                    st.success(f"Guardado: {word}")

                st.rerun()

            except Exception as e:
                st.error(f"No se pudo guardar el término: {e}")

    # --------------------------
    # TABLA COMPLETA
    # --------------------------
    if st.checkbox("Mostrar tabla completa"):
        if rows:
            df = pd.DataFrame(rows, columns=["ID", "Término", "Definición"])
            st.dataframe(df, use_container_width=True)

# ===========================================================
# VISTAS DE LOS PARCIALES
# ===========================================================
elif menu == "Cálculo III Parcial I":
    parcial_uno.app()

elif menu == "Cálculo III Parcial II":
    parcial_dos.app()

elif menu == "Cálculo III Parcial III":
    parcial_tres.app()
