import streamlit as st

from Paginas.EcoEstudio import *
from Paginas.EcoHistorico import *
from Paginas.EcoViaje import *
from funciones import FuncionesEcoMovilidad

import pandas as pd




def pagina_EcoMovilidad():
    #Barra lateral con un selectbox para que selecciones si ver el proyecto o el portfolio
    st.sidebar.markdown("<h2>Aqui podrás encontrar:</h2>" , unsafe_allow_html=True)
    #Seleccion del sidebar
    seleccion_pestaña = st.sidebar.radio(label = " ", options = ["EcoEstudio","EcoHistórico","EcoViaje"])

    
    if seleccion_pestaña == "EcoEstudio":
        EcoEstudio()
    elif seleccion_pestaña == "EcoHistórico":
        pagina_historico()
    elif seleccion_pestaña == "EcoViaje":
        pagina_ecoviaje()
    





       
            
           
           
            

                                        























