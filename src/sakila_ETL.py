from sqlalchemy import create_engine, text
from config import *
import pandas as pd
import os

def conection_bd():
    """Establece conexión con la base de datos Sakila"""
    url_db = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(url_db)
    return engine.connect()

def test_connection():
    """Probar la conexión a la base de datos"""
    connection = conection_bd()
    try:
        with connection:
            print("✅ Conexión exitosa a Sakila.")
            result = connection.execute(text("SELECT * FROM film LIMIT 1;"))
            print(result.fetchone())
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")

def get_data_list_from_join():
    """Obtener datos y generar múltiples CSV"""
    connection = conection_bd()
    
    # Lista de consultas y nombres de archivos
    queries = [
        {
            "name": "DataFrame1",
            "query": """
                SELECT c.customer_id, LOWER(c.first_name) AS first_name, ...
                FROM customer c JOIN address a ON c.address_id = a.address_id ...
                WHERE r.rental_id IS NOT NULL AND p.amount > 0;
            """
        },
        {
            "name": "DataFrame2",
            "query": "SELECT * FROM film WHERE rental_duration > 5;"
        },
        {
            "name": "DataFrame3",
            "query": "SELECT staff_id, COUNT(*) FROM payment GROUP BY staff_id;"
        }
    ]

    # Ruta base para la carpeta data
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIR = os.path.dirname(BASE_DIR)
    DATA_DIR = os.path.join(PARENT_DIR, "output")
    os.makedirs(DATA_DIR, exist_ok=True)

    # Ejecutar cada consulta y exportar
    for query_info in queries:
        with connection:
            result = connection.execute(text(query_info["query"]))
            rows = result.fetchall()
            df = pd.DataFrame(rows, columns=result.keys())

            file_path = os.path.join(DATA_DIR, f"{query_info['name']}.csv")
            df.to_csv(file_path, index=False, encoding='utf-8')
            print(f"✅ {query_info['name']} guardado en: {file_path} | Registros: {len(df)}")
 