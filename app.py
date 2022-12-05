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
imagen_1 = Image.open("Imagenes/recorte_1.png")
imagen_2 = Image.open("Imagenes/recorte_2.png")
imagen_5 = Image.open("Imagenes/recorte_5.png")
grafica_img = Image.open("imagenes/Grafica.png")
instrucciones_img = Image.open("imagenes/instrucciones.png")
#Imagenes de la guia de instalcion
descarga_img = Image.open("Imagenes/descarga.PNG")
componentev2 = Image.open("Imagenes/componente_v2.PNG")
archivo_exe = Image.open("Imagenes/erchivo_exe.PNG")

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
            - Un programa para descomprimir archivos (ej. Winrar, 7zip)\n
            - 1.4Gb de espacio de almacenamiento en el disco duro. \n
            - Webcam (En caso de no contar con una solicitar una prestada en el laboratorio) \n
            - Tener instalado MS Office Excel o Libreoffice para poder abrir el documento de registro generado\n

            [> Link de descarga de libre Office](https://es.libreoffice.org/)\n
            [> Link de descarga de 7zip](https://www.7-zip.org/download.html)\n
            [> Link de descarga de Winrar](https://www.winrar.es/descargas)\n


            """
        )
    
    with right_column:
        st.write("\n")
        st_lottie(laptop_animation_json, height=400, key="coding")

#----------------------Sección de instlación -------------------------------------------

with st.container():
    st.write("---")
    st.write("##")
    st.header("Guia de instalación:")
    st.write(
        """
        link de drive [Descarga](https://drive.google.com/file/d/1oCZ2-IOUoSqrUgh6lm36Q9UR4sXTSR4Z/view?usp=share_link), Una vez ingresado en el link se tiene que dar click en el botón de descarga como el que se marca en la imagen de referencia de abajo.\n

        [> Link de Descarga programa de reconocimiento](https://drive.google.com/file/d/1oCZ2-IOUoSqrUgh6lm36Q9UR4sXTSR4Z/view?usp=share_link)
        """)
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.empty()

        with col2:
            st.image(descarga_img)

        with col3:
            st.empty()

    st.write(
        """
        Una vez presionado el botón se deberá comenzar la descarga automática del documento con extensión “.rar”.
        """)

    st.write(
        """
        Ya que el documento .rar se haya descargado por completo se procede a descomprimirlo con el programa de descompresión que se tenga a la mano.
        """)
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.empty()

        with col2:
            st.image(componentev2)

        with col3:
            st.empty()

    st.write(
        """
        Cuando se descomprima el documento dejara una carpeta llamada “Componente_v2”, la cual al abrirla nos permitirá ver todos los archivos que componen el programa de reconocimiento, de los cuales el que nos permitirá ejecutar el programa sera el archivo llamado “Componente_v2.exe” el cual tiene por icono un pingüino para una referencia más clara.
        """)
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.empty()

        with col2:
            st.image(archivo_exe)

        with col3:
            st.empty()

#st.image(descarga_img)

#----------------------Sección de la guia de uso -------------------------------------------
with st.container():
    st.write("---")
    st.write("##")
    st.header("Guia de uso:")
    img_column, text_column = st.columns((1,2))
    with img_column:
        st.image(imagen_1, width=300)
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
        st.image(imagen_2, width=300)
        st.image(imagen_5, width=300)

    with text_column:
        st.write(
            """
            Después de que quedo enfocado el panel a leer se selecciona con el raton el area especifica que se quiere leer, esta se marcara con una recuadro de color verde, como se muestra en la imagen de referencia.

            Ya seleccionada el área presionamos la  **Tecla “Q”** para pasar el modo de la lectura donde se aplicara un par de filtro  negativo ademas de otro en  blanco y negro para optimizar la lectura.

            Cuando se despliegue una ventana con los filtros que se pueden observar como en la imagen de la izquierda, estaremos listos para continuar.

            Estando en este modo podemos hacer los últimos ajustes a la posición de la cámara y a la iluminación requerida para que nuestra lecturas sean lo mas correctas posibles, las lecturas no comenzaron de forma automática hasta que se presione un par de veces la **Tecla “C”** al momento de realizar esta acción se desplegará una alerta de windows que nos avisara que la toma de lecturas comenzará.

            La forma en la que trabaja las lecturas será cada que se cumpla un ciclo de 5 segundos aproximadamente esto tomando en cuenta que si llegara a cambiar la posición de la cámara por algún motivo este intervalo permite reacomodar la posición sin perder información del experimento.
            """
        )

with st.container():
    img_column, text_column = st.columns((1,2))
    with img_column:
        st.image(grafica_img, width=300)

    with text_column:
        st.write(
            """
            Las gráficas  plestánanteadas para tener en el eje vertical las medidas de la temperatura medida mientras que el eje horizontal estará el tiempo que se calculará automáticamente conforme avance el experimento.

            En la imagen de ejemplo se pueden observar unos puntos que se miden en temperaturas muy inferiores a las de la tendencia, esto se puede dar si hay un error en la medición y si la cámara no registra ningún dato por que se desplazó del punto de lectura este se marcará automáticamente como un cero.
            """
        )





with st.container():
    st.write("---")
    st.write("##")
    st.write(
        """
        ****Nota:**** Al ejecutar el programa mostrara una ventana con un version resumida de las instrucciones en dado caso de que sea necesario repasar los controles de uso.
        """
    )
    comlumn_1, comlumn_2, comlumn_3 = st.columns(3)
    with comlumn_1:
        st.empty()
    with comlumn_2:
        st.image(instrucciones_img, width=300)
    with comlumn_3:
        st.empty()