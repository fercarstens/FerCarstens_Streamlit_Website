import sqlite3
import pandas as pd
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="FerCarstens", page_icon=":100:", layout="wide")

# Conexión a la base de datos SQLite
def connect_to_db(db_file):
    """Crea la conexión a la base de datos SQLite."""
    conn = sqlite3.connect(db_file)
    return conn

# Ejecutar consulta SQL y devolver resultados como DataFrame
def run_query(query, db_file):
    """Ejecuta una consulta SQL en la base de datos y devuelve un DataFrame."""
    conn = connect_to_db(db_file)
    try:
        result_df = pd.read_sql_query(query, conn)
    except Exception as e:
        st.error(f"Error al ejecutar la consulta: {e}")
        result_df = pd.DataFrame()  # Retorna un DataFrame vacío si falla
    conn.close()
    return result_df

# Ruta a la base de datos
db_file = "data/BD_BI.sqlite3"

# Encabezado
st.title("¡Hola! Aquí FerCarstens")
st.subheader("Desarrollador | Analista de Datos | Científico de Datos")
st.write("Bienvenido(a) a mi página interactiva. Aquí puedes encontrar información sobre mí y sobre los proyectos y avances que hago para mi Master en el CEI. ¡Gracias por visitar!")
# Divider para separar bloques
st.divider()
# Sobre mí
st.header("Sobre mí")
st.write("""
Apasionado por la tecnología y en plena transición hacia el campo de Big Data y Business Intelligence, con un enfoque destacado en Python para análisis y desarrollo de soluciones. Actualmente estoy cursando un máster en Big Data y BI, donde estoy perfeccionando mis habilidades en gestión de bases de datos SQL, creación de dashboards interactivos con Power BI y desarrollo backend con Python.

Mi formación se centra en transformar datos en información estratégica, ayudando a empresas a tomar decisiones basadas en insights claros y visualizaciones efectivas. Además, tengo experiencia práctica en automatización de procesos y generación de notificaciones dinámicas mediante programación, lo que optimiza flujos de trabajo y mejora la productividad.
""")

# Divider para separar bloques
st.divider()

# Encabezado
st.title("Resolución de ejercicios de SQL")
st.write("Ejercicios prácticos sobre una consulta a una base de datos de estudiantes aplicando a distintas carreras y universidades")

# Opciones de consulta (en el cuerpo principal)
st.subheader("Opciones de Consulta")
consulta = st.selectbox(
    "Selecciona una consulta:",
    [
        "Seleccione una opción...",  
        "Ver todos los datos de una tabla",
        "Consulta 1",
        "Consulta 2",
        "Consulta 3",
        "Consulta 4",
        "Consulta 6",
        "Consulta 7",
        "Consulta 8",
        "Consulta 9",
        "Consulta 10"
    ]
)

if consulta == "Seleccione una opción...":
    st.info("Por favor, selecciona una consulta del menú desplegable para continuar.")

# Opción 1: Mostrar todos los datos de una tabla
elif consulta == "Ver todos los datos de una tabla":
    st.subheader("Ver todos los datos de una tabla")
    # Obtener nombres de tablas en la base de datos
    try:
        conn = connect_to_db(db_file)
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tablas = pd.read_sql_query(query, conn)["name"].tolist()
        conn.close()

        if tablas:
            tabla_seleccionada = st.selectbox("Selecciona una tabla:", tablas)
            if st.button("Ejecutar consulta"):
                query = f"SELECT * FROM {tabla_seleccionada} LIMIT 100;"
                datos = run_query(query, db_file)
                st.write(f"Mostrando los primeros 100 registros de la tabla `{tabla_seleccionada}`:")
                st.dataframe(datos)
        else:
            st.warning("No se encontraron tablas en la base de datos.")
    except Exception as e:
        st.error(f"No se pudo conectar a la base de datos: {e}")

# Consulta 1
elif consulta == "Consulta 1":
    st.subheader("Obtener los nombres y notas de los estudiantes, así como el resultado de su solicitud de manera que tengan un valor de corrección menor que 1000 y hayan solicitado la carrera de Informática en la Universidad Complutense de Madrid.")
    # Botón para ejecutar la consulta
    if st.button("Ejecutar consulta"):
        query = """
        SELECT es.Nombre_Est, es.Nota, so.Carrera, so.Nombre_Univ, so.Decision, es.Valor
        FROM Estudiantes es
        JOIN Solicitudes so on es.ID=so.ID
        WHERE es.Valor < 1000 AND so.Carrera='Informatica' AND so.Nombre_Univ='Universidad Complutense de Madrid';

        """
        datos = run_query(query, db_file)
        st.write("Resultados de la consulta:")
        st.dataframe(datos)

# Consulta 2
elif consulta == "Consulta 2":
    st.subheader("Obtener la información sobre todas las solicitudes: ID y nombre del estudiante, nombre de la universidad, nota y plazas, ordenadas de forma decreciente por las notas y en orden creciente de plazas.")
    # Botón para ejecutar la consulta
    if st.button("Ejecutar consulta"):
        query = """
        SELECT es.ID, es.Nombre_Est, un.Nombre_Univ, es.Nota, un.Plazas
        FROM Estudiantes es
        LEFT JOIN Solicitudes so on es.ID=so.ID
        LEFT JOIN Universidades un on so.Nombre_Univ=un.Nombre_Univ
        ORDER BY es.Nota DESC, un.Plazas;
                """
        datos = run_query(query, db_file)
        st.write("Resultados de la consulta:")
        st.dataframe(datos)

# Consulta 3
elif consulta == "Consulta 3":
    st.subheader("Obtener todas las solicitudes a carreras que tengan relación con la biología.")
    # Botón para ejecutar la consulta
    if st.button("Ejecutar consulta"):
        query = """
        SELECT es.Nombre_Est, so.Carrera, so.Nombre_Univ
        FROM Solicitudes so
        JOIN Estudiantes es on so.ID = es.ID
        WHERE so.Carrera LIKE "Bio%";
        """
        datos = run_query(query, db_file)
        st.write("Resultados de la consulta:")
        st.dataframe(datos)

# Consulta 6
elif consulta == "Consulta 6":
    st.subheader("Admitir en la “Universidad de Jaén” a todos los estudiantes de Económicas quienes no fueron admitidos en dicha carrera en otras universidades.")
    # Botón para ejecutar la consulta
    if st.button("Ejecutar consulta"):
        query = """
        SELECT es.ID, es.Nombre_Est, "Universidad de Jaén" AS Nombre_Univ, "Economia" AS Carrera,"Si" AS Decision
        FROM Estudiantes es
        WHERE es.ID IN (
                SELECT sol.ID
                FROM Solicitudes sol
                WHERE sol.Carrera = "Economia" AND sol.Decision != "Si" AND sol.Nombre_Univ != "Universidad de Jaén"
                GROUP BY sol.ID
                );
        """
        datos = run_query(query, db_file)
        st.write("Resultados de la consulta:")
        st.dataframe(datos)

# Consulta 7
elif consulta == "Consulta 7":
    st.subheader("Borrar a todos los estudiantes que solicitaron más de 2 carreras diferentes. Sin embargo para esta web solo haremos la consulta")
    # Botón para ejecutar la consulta
    if st.button("Ejecutar consulta"):
        query = """
        SELECT es.ID, es.Nombre_Est, so.Carrera
        FROM Estudiantes es
        JOIN Solicitudes so on es.ID = so.ID
        GROUP BY so.ID
        HAVING COUNT(DISTINCT so.Carrera) >= 2
        ; --AQUI CONSULTO LOS ESTUDIANTES QUE VOY A ELIMINAR
        """
        datos = run_query(query, db_file)
        st.write("Resultados de la consulta:")
        st.dataframe(datos)

# Consulta 8
elif consulta == "Consulta 8":
    st.subheader("Obtener las carreras con nota máxima por debajo de la media")
    # Botón para ejecutar la consulta
    if st.button("Ejecutar consulta"):
        query = """
        WITH PromedioGeneral AS (
            SELECT AVG(es.Nota) AS MediaNota
            FROM Solicitudes so
            JOIN Estudiantes es ON so.ID = es.ID
        ),
        MaximaNotaPorCarrera AS (
            SELECT so.Carrera, MAX(es.Nota) AS MaxNota
            FROM Solicitudes so
            JOIN Estudiantes es ON so.ID = es.ID
            GROUP BY so.Carrera
        )
        SELECT Carrera
        FROM MaximaNotaPorCarrera, PromedioGeneral
        WHERE MaxNota < MediaNota;
        """
        datos = run_query(query, db_file)
        st.write("Resultados de la consulta:")
        st.dataframe(datos)

# Consulta 9
elif consulta == "Consulta 9":
    st.subheader("Obtener los nombres de los estudiantes y las carreras que han solicitado.")
    # Botón para ejecutar la consulta
    if st.button("Ejecutar consulta"):
        query = """
        SELECT DISTINCT es.Nombre_Est, so.Carrera, es.Nota
        FROM Estudiantes es
        JOIN Solicitudes so on es.ID = so.ID
        ;
        """
        datos = run_query(query, db_file)
        st.write("Resultados de la consulta:")
        st.dataframe(datos)

# Consulta 10
elif consulta == "Consulta 10":
    st.subheader("Obtener el nombre de las notas de los estudiantes con valor de ponderación mayor de 1000 que hayan solicitado Informática en la “Universidad de Valencia”.")
    # Botón para ejecutar la consulta
    if st.button("Ejecutar consulta"):
        query = """
        SELECT es.Nombre_Est, es.Nota, so.Carrera, so.Nombre_Univ, so.Decision, es.Valor
        FROM Estudiantes es
        JOIN Solicitudes so on es.ID=so.ID
        WHERE es.Valor > 1000 AND so.Carrera='Informatica' AND so.Nombre_Univ='Universidad de Valencia';
        """
        datos = run_query(query, db_file)
        st.write("Resultados de la consulta:")
        st.dataframe(datos)

# Divider para separar bloques
st.write("---")

# Redes sociales
st.header("Conéctate Conmigo :handshake::handshake:")
st.write("""
- [GitHub](https://github.com/fercarstens)
- [LinkedIn](https://www.linkedin.com/in/fercarstens/)
- [Correo Electrónico](mailto:fercarstens7@gmail.com)
""")
# Footer
st.write("---")
st.write("Gracias por visitar")
