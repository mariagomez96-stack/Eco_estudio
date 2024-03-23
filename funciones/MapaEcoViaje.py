import pandas as pd
import streamlit as st

# Visualizaciones de mapas
import folium
from geopy.distance import geodesic
from geopy.geocoders import Nominatim


df_cargadores = pd.read_csv("./data/df_cargadores.csv")

def funcion_folium_cp_radio(cp=None, radio=None):
    if cp and radio:
        # Define el nombre de tu aplicación o proyecto
        nombre_app = "Mi Aplicación de Geolocalización"
        
        # Crea una instancia del geolocalizador y proporciona el nombre de tu aplicación como user_agent
        geolocator = Nominatim(user_agent=nombre_app)
        
        direccion = f"{str(cp)}, España"
        # Obtener las coordenadas de la dirección
        location = geolocator.geocode(direccion)
        
        # Imprimir las coordenadas
        if location:
            localizacion_inicial = [location.latitude, location.longitude]
        else:
            print("La dirección no se encontró.")

        # Crear un mapa centrado en las coordenadas iniciales
        mapa = folium.Map(location=localizacion_inicial, zoom_start=7)
        
        lista_indices = []
        # Iterar sobre las filas del DataFrame y agregar marcadores al mapa
        for index, row in df_cargadores.iterrows():
            coordenadas_punto = (row['latitude'], row['longitude'])
            distancia = geodesic(localizacion_inicial, coordenadas_punto).kilometers
            
            tiene_carga_rapida = False
            for valor in row['isfastChargeCapable']:
                if valor == "Sí": 
                    tiene_carga_rapida = True
                    break  
            
            html_popup = f'''
                    <div style="min-width: 300px; max-width: 300px; font-size: 7px;">
                        <p><strong>Dirección:</strong> {str(row["addressLine1"])}</p>
                        <p><strong>Tipo de cargadores:</strong> {str(row["title"]).replace("[", "").replace("]", "").replace("'", "")}</p>
                        <p><strong>Energía de cada cargador:</strong> {str(row["energia"]).replace("[", "").replace("]", "").replace("'", "")}</p>
                        <p><strong>¿Tiene carga rápida?:</strong> {str(row["isfastChargeCapable"]).replace("[", "").replace("]", "").replace("'", "")}</p>
                        <p><strong>Distancia a tu ubicación:</strong> {distancia:.2f} km</p>
                        <p><strong>Indice del cargador :</strong> {index}<p>
                    </div>
                '''
            
            if tiene_carga_rapida:
                # Agregar marcador solo si la distancia es menor o igual a radio
                if distancia <= radio:
                    folium.Marker(location=coordenadas_punto, popup=folium.Popup(html=html_popup), icon=folium.Icon(icon='flash')).add_to(mapa)
                    lista_indices.append(index)
            else:        
                if distancia <= radio:
                    folium.Marker(location=coordenadas_punto, popup=folium.Popup(html=html_popup)).add_to(mapa)
                    lista_indices.append(index)

        # Generar el HTML del mapa
        mapa_html = mapa._repr_html_()

        return mapa_html, lista_indices
    
    else:
        # Crear un mapa centrado en las coordenadas iniciales
        mapa = folium.Map(location=["40.2085", "-3.7130"], zoom_start=5) 
        mapa_html = mapa._repr_html_()
        return mapa_html
