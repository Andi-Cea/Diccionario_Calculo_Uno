import psycopg2
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# -----------------------------
# CONEXIÓN A POSTGRESQL
# -----------------------------
def get_connection():
    try:
        return psycopg2.connect(
            host=os.getenv("PGHOST"),
            database=os.getenv("PGDATABASE"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            port=os.getenv("PGPORT")
        )
    except psycopg2.OperationalError as e:
        raise RuntimeError(f"No se pudo conectar a la base de datos: {e}")

# -----------------------------
# CREAR TABLA
# -----------------------------
def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS conceptos (
            id SERIAL PRIMARY KEY,
            termino TEXT UNIQUE NOT NULL,
            definicion TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# -----------------------------
# INSERTAR O ACTUALIZAR
# -----------------------------
def insert_definicion(termino, definicion):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO conceptos (termino, definicion)
        VALUES (%s, %s)
        ON CONFLICT (termino) DO UPDATE SET definicion = EXCLUDED.definicion;
    """, (termino, definicion))
    conn.commit()
    cur.close()
    conn.close()

# -----------------------------
# OBTENER TODAS LAS DEFINICIONES
# -----------------------------
def get_definicions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, termino, definicion FROM conceptos ORDER BY termino ASC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# -----------------------------
# ELIMINAR DEFINICIÓN
# -----------------------------
def delete_definicion(termino):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM conceptos WHERE termino = %s;", (termino,))
    conn.commit()
    cur.close()
    conn.close()

# -----------------------------
# ACTUALIZAR DEFINICIÓN POR ID
# -----------------------------
def update_definicion_by_id(id_, termino, definicion):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE conceptos
        SET termino = %s, definicion = %s
        WHERE id = %s;
    """, (termino, definicion, id_))
    conn.commit()
    cur.close()
    conn.close()
