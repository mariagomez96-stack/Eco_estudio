import streamlit as st
from archivos_py.EcoMovilidad import *
from archivos_py.EcoHome import *
from archivos_py.EcoNtacto import *
from archivos_py.EcoFaqs import *
from archivos_py.EcoEncuesta import *


st.set_page_config(layout = "wide")

def main():
    
   #Barra lateral con un selectbox para que selecciones si ver el proyecto o el portfolio
    st.sidebar.markdown("<h2>Selecciona qué desea ver:</h2>" , unsafe_allow_html=True)


    #Seleccion del sidebar
    seleccion_pagina = st.sidebar.selectbox(label = " ", options = ["EcoHome","EcoMovilidad", "EcoNtacto", "EcoFaqs", "EcoEncuesta"])

    if seleccion_pagina == "EcoHome":
        paginaprincipal()
    elif seleccion_pagina == "EcoMovilidad":
        pagina_EcoMovilidad()
    elif seleccion_pagina == 'EcoNtacto':
        st.write("llamadaFuncion_conocenos")
    elif seleccion_pagina == "EcoFaqs":
        pagina_ecofaqs()
    elif seleccion_pagina == "EcoEncuesta":
        pagina_ecoencuesta()


if __name__ == "__main__":
    main()

    