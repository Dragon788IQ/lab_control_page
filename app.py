import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

#Set de la configuracion de la pagina
st.set_page_config(page_title="Reconocimiento app Lab de Control", page_icon=":penguin:", layout="wide")

#Declaracion de las funciones de carga de assets
def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#Assets
correo_animation_url = "https://assets10.lottiefiles.com/packages/lf20_4Ox5W3dL45.json"
laptop_animation_url = "https://assets8.lottiefiles.com/packages/lf20_w51pcehl.json"

#Json
laptop_animation_json = load_lottie(laptop_animation_url)

with st.container():
    st.subheader("Laboratorio de Control Automatico de Procesos")
    st.title("Programa de reconocimiento automatico de paneles")
    st.write(
        "Este programa esta diseñado para apoyar a los alumnos y docentes en el registro de informacion procedente de paneles, Esto con ayuda de reconociemiento en tiempo real, graficacion de la informacion y posterior registro en un documento de excel."
    )
    st.write("[Informacion de referencia >](https://github.com/JaidedAI/EasyOCR)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Requisitos para el funcionamiento:")
        #st.write("#")
        st.write(
            """
            - Equipo de computo con sistema operativo Windows. \n
            - Minimo 4Gb de memoria RAM. \n
            - X espacio de almacenamiento en el disco duro. \n
            - Webcam (En caso de no contar con una solicitar una prestada en el laboratorio) \n
            - Tener instalado MS Office Excel ó Libre Office para poder abrir el documento de registro generado\n
                [Link de descarga de libre Office >](https://es.libreoffice.org/)

            """
        )
    
    with right_column:
        st.write("\n")
        st_lottie(laptop_animation_json, height=400, key="coding")

with st.container():
    st.write("---")
    st.write("##")
    st.header("Guia de instalación:")
    img_column, text_column = st.columns((1,2))
    with img_column:
        st.write("Insertar Imagen")

    with text_column:
        st.write("Insertar guia de instalacion prrona")


with st.container():
    st.write("---")
    st.write("##")
    st.header("Guia de instalación:")
    img_column, text_column = st.columns((1,2))
    with img_column:
        st.write("Insertar Imagen")

    with text_column:
        st.write("Insertar guia de instalacion prrona")

