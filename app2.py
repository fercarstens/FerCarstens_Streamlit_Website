import sqlite3
import pandas as pd
import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Mi Portafolio", page_icon=":briefcase:", layout="wide")
# Encabezado
st.title("¡Hola! Aquí FerCarstens 👋")
st.subheader("Desarrollador | Analista de Datos | Científico de Datos")
st.write("Bienvenido(a) a mi portafolio interactivo. Aquí puedes encontrar información sobre mí y contactarme. ¡Gracias por visitar!")
# Sobre mí
st.header("Sobre mí")
st.write("""
Hola, soy FerCarstens. Me apasiona el mundo de la programación y los datos. Actualmente estoy desarrollando mis habilidades 
en Python, análisis de datos y desarrollo web. Siempre estoy en busca de nuevos desafíos y oportunidades para crecer profesionalmente.
""")
# Habilidades
st.header("Habilidades")
st.write("""
- **Lenguajes de Programación:** Python, SQL.
- **Herramientas y Frameworks:** Streamlit, Pandas, NumPy, Matplotlib.
- **Idiomas:** Español (Nativo), Inglés (Intermedio).
""")
# Base de datos
st.header("Explorar la base de datos 📂")
st.write("Aquí puedes visualizar los datos de mi base de datos SQLite.")
# Archivo de base de datos SQLite
db_file = "BD_BI.sqlite3"
# Conexión a la base de datos
def connect_to_db(db_file):
    """Crea la conexión a la base de datos SQLite."""
    conn = sqlite3.connect(db_file)
    return conn


# Ejecutar consulta SQL y devolver resultados como DataFrame
def run_query(query, db_file):
    conn = connect_to_db(db_file)
    try:
        result_df = pd.read_sql_query(query, conn)
    except Exception as e:
        st.error(f"Error al ejecutar la consulta: {e}")
        result_df = pd.DataFrame()  # Retorna un DataFrame vacío si falla
    conn.close()
    return result_df
# Encabezado
st.title("Consultas Dinámicas con Streamlit")
st.write("Explora y filtra datos de tu base de datos SQLite utilizando consultas SQL.")

# Opciones de consulta
st.header("Opciones de Consulta")
consulta = st.selectbox(
    "Selecciona una consulta:",
    [
        "Ver todos los datos de una tabla",
        "Filtrar por valor en una columna",
        "Obtener datos por rango de fechas"
    ]
)

# Opción 1: Mostrar todos los datos de una tabla
if consulta == "Ver todos los datos de una tabla":
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

# Opción 2: Filtrar por valor en una columna
elif consulta == "Filtrar por valor en una columna":
    st.subheader("Filtrar por valor en una columna")
    tabla_seleccionada = st.text_input("Ingresa el nombre de la tabla:")
    columna_seleccionada = st.text_input("Ingresa el nombre de la columna:")
    valor_filtrar = st.text_input("Ingresa el valor para filtrar:")
    
    if st.button("Ejecutar consulta"):
        if tabla_seleccionada and columna_seleccionada and valor_filtrar:
            query = f"SELECT * FROM {tabla_seleccionada} WHERE {columna_seleccionada} = '{valor_filtrar}' LIMIT 100;"
            datos = run_query(query, db_file)
            st.write(f"Mostrando resultados para `{columna_seleccionada} = {valor_filtrar}` en la tabla `{tabla_seleccionada}`:")
            st.dataframe(datos)
        else:
            st.warning("Por favor, completa todos los campos.")

# Opción 3: Filtrar por rango de fechas
elif consulta == "Obtener datos por rango de fechas":
    st.subheader("Obtener datos por rango de fechas")
    tabla_seleccionada = st.text_input("Ingresa el nombre de la tabla:")
    columna_fecha = st.text_input("Ingresa el nombre de la columna de fechas:")
    fecha_inicio = st.date_input("Selecciona la fecha de inicio:")
    fecha_fin = st.date_input("Selecciona la fecha de fin:")

    if st.button("Ejecutar consulta"):
        if tabla_seleccionada and columna_fecha:
            query = f"""
            SELECT * FROM {tabla_seleccionada}
            WHERE {columna_fecha} BETWEEN '{fecha_inicio}' AND '{fecha_fin}' LIMIT 100;
            """
            datos = run_query(query, db_file)
            st.write(f"Mostrando resultados entre `{fecha_inicio}` y `{fecha_fin}` en la tabla `{tabla_seleccionada}`:")
            st.dataframe(datos)
        else:
            st.warning("Por favor, completa todos los campos.")

# Redes sociales
st.header("Conéctate conmigo")
st.write("""
- [GitHub](https://github.com/fercarstens)
- [LinkedIn](https://www.linkedin.com/in/fercarstens/)
- [Correo Electrónico](mailto:fercarstens7@gmail.com)
""")

# Formulario de contacto
st.header("Formulario de Contacto")
st.write("¿Te interesa trabajar conmigo o tienes alguna pregunta? Llena el siguiente formulario y me pondré en contacto contigo.")

# Widgets del formulario
with st.form(key="contact_form"):
    name = st.text_input("Tu nombre", placeholder="Escribe tu nombre aquí...")
    email = st.text_input("Tu correo electrónico", placeholder="ejemplo@email.com")
    message = st.text_area("Tu mensaje", placeholder="Escribe tu mensaje aquí...")
    
    # Botón de enviar
    submit_button = st.form_submit_button("Enviar")

    # Procesar la información al enviar
    if submit_button:
        if name and email and message:
            st.success(f"¡Gracias por contactarme, {name}! Me pondré en contacto contigo pronto.")
            # Aquí podrías guardar los datos o enviarlos a un servicio externo
            print(f"Nuevo mensaje de contacto:\nNombre: {name}\nCorreo: {email}\nMensaje: {message}")
        else:
            st.error("Por favor, completa todos los campos antes de enviar el formulario.")

# Imagen de perfil
# st.image("images/20220521-IMG_4478.jpg", width=100, caption="FerCarstens", use_column_width=False)

# Footer
st.write("---")
st.write("Gracias por visitar")
