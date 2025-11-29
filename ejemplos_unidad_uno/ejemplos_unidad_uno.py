# En app.py
import streamlit as st
from ejemplos_unidad_uno import app_ejemplos_unidad_uno

# Configuración
ejemplos_unidad_uno_disponible = True

# Menú principal
menu = st.sidebar.selectbox(
    "Navegación",
    ["Inicio", "Ejercicios", "Ejemplos Unidad I", "Teoría"]
)

if menu == "Ejemplos Unidad I":
    if ejemplos_unidad_uno_disponible:
        app_ejemplos_unidad_uno()
    else:
        st.error("❌ Módulo de Ejemplos Unidad I no disponible")