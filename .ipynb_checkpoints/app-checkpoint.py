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
st.image("images/20220521-IMG_4478.jpg", width=100, caption="FerCarstens", use_column_width=False)

# Footer
st.write("---")
st.write("Gracias por visitar")
