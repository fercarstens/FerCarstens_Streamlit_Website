import sqlite3

db_file = "BD_BI.sqlite3"

try:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()

    if tables:
        print("Tablas encontradas:")
        for table in tables:
            print(table[0])  # Imprime los nombres de las tablas
    else:
        print("No se encontraron tablas en la base de datos.")
except Exception as e:
    print(f"Error al conectarse a la base de datos: {e}")
