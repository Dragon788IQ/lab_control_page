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
imagen_1 = Image.open("imagenes/recorte 1.PNG")
imagen_2 = Image.open("imagenes/recorte 2.PNG")

local_css("Estilos/estilos.css")

#Json
laptop_animation_json = load_lottie(laptop_animation_url)

with st.container():
    st.subheader("Laboratorio de Control Automático de Procesos")
    st.title("Programa de reconocimiento automático de paneles")
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
            Equipo de cómputo con sistema operativo Windows 64bits. \n
            - Mínimo 4Gb de memoria RAM. \n
            - 1.4Gb de espacio de almacenamiento en el disco duro. \n
            - Webcam (En caso de no contar con una solicitar una prestada en el laboratorio) \n
            - Tener instalado MS Office Excel o Libreoffice para poder abrir el documento de registro generado\n

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
    st.header("Guia de uso:")
    img_column, text_column = st.columns((1,2))
    with img_column:
        st.image(imagen_1)
    with text_column:
        st.write(
            """
            Una vez instalado el programa de reconocimiento y conectada la webcam al equipo, se procede a abrir el programa, el cual mostrará el video captado de la webcam.

            Como primer paso será cuadrar la imagen con el panel el cual se querrá utilizar para hacer la lectura del mismo, se recomienda que se coloque la cámara mirando de forma directa a  la webcam con la distancia suficiente para un correcto enfoque, además de mantener un iluminación óptima para que se visualicen los dígitos de la forma mas clara posible.

            """
        )

with st.container():
    img_column, text_column = st.columns((1,2))
    with img_column:
        st.image(imagen_2)
    with text_column:
        st.write(
            """
            Una vez enfocado el panel a leer se selecciona con el raton el area especifica que se quiere leer, esta se marcara con una recuadro de color verde, como se muestra en la imagen de referencia.
            """
        )