import streamlit as st






def pagina_ecoReview():
      #Imagen de fondo
    background_image = """
    <style>
    body {
        background-image: url("https://images.unsplash.com/photo-1618022325802-7e5e732d97a1?q=80&w=3896&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        width: 100vw;
        height: 100vh;
    }

    .stApp {
        background-color: rgba(255, 255, 255, 0.1);
    }
    </style>
    """
    st.markdown(background_image, unsafe_allow_html=True)
    #Fin de imagen de fondo

    texto = """
        <div style='text-align: center;'>
        <span style='color: cyan; font-weight: bold; font-size: 40px;'>
        Clases de Vehículo
        </span>
        </div>
        """

        # Mostrar el texto alineado al centro
    st.markdown(texto, unsafe_allow_html=True)     
    for i in range(1,4):
            st.markdown(" ")
    col1,col2 = st.columns(2)
    with col1:
        
        st.write("""


       <p <h1 style='text-align:center;'><strong> </p> ¡Descubre las Clases de Vehículos y sus Categorías!</h1>""", unsafe_allow_html=True)
        
        
        
        st.markdown("""
        
        La clasificación de los vehículos es como un mapa que nos guía a través de sus diferentes características: tamaño, peso, capacidad y más. Es como organizar un armario: nos ayuda a entender mejor lo que tenemos y cómo podemos usarlo mejor. ¿Alguna vez te has preguntado cuáles son las clases de vehículo más comunes? ¡No te preocupes! Aquí te lo explicamos todo.
        """)
        st.write("""


       <p <h1 style='text-align:center;'><strong> </p> ¿Te has preguntado alguna vez cuáles son las clases de vehículo más comunes?</h1>""", unsafe_allow_html=True)
        
        
        st.markdown("""
        
        Categorías de Vehículos Eléctricos y no Eléctricos:

        Categorías "L" (L3e, L5e, L6e, L7e): ¿Te suenan esas letras "L"? ¡Claro que sí! Son como los pequeños del barrio, ideales para moverse ágilmente por la ciudad. Hablamos de motocicletas y cuadriciclos, perfectos para ir de un lado a otro sin complicaciones.

        Categorías "M" (M1, M2, M3): Ahora vamos con los más grandes, los reyes del asfalto. Si ves un "M1", prepárate para un viaje cómodo y espacioso. Estamos hablando de automóviles diseñados para llevar personas y todas sus cosas. Ideal para tus aventuras por carretera y escapadas familiares.

        Categorías "N" (N1, N2, N3): ¿Y qué hay de los gigantes del camino? ¡Aquí entramos en terreno pesado! Nos referimos a los camiones y vehículos industriales, diseñados para llevar cargas pesadas y hacer que el negocio siga adelante. Un "N1" es como una oficina móvil, lista para llevar todo lo que necesitas para triunfar en el mundo empresarial.
        """)

        



        
       

       
        with col2:
            for i in range(1,2):
                st.markdown(" ")
            
            # Ruta de la imagen
            ruta_imagen = "https://images.unsplash.com/photo-1565043666747-69f6646db940?q=80&w=3774&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

            # Mostrar la imagen
            st.image(ruta_imagen, caption='Clases de vehiculo', use_column_width=True)

    for i in range(1,4):
            st.markdown(" ")
    texto = """
        <div style='text-align: center;'>
        <span style='color: cyan; font-weight: bold; font-size: 40px;'>
        ¡Descubre las Clasificaciones Energéticas de los Vehículos!
        </span>
        </div>
        """

        # Mostrar el texto alineado al centro
    st.markdown(texto, unsafe_allow_html=True)    

    col3,col4 = st.columns(2)


    with col3:
        texto_html = """

<p style='font-size: 16px;'>¿Sabías que los vehículos se clasifican no solo por su tamaño o forma, sino también por su eficiencia energética? 
Sí, has oído bien. La eficiencia energética de un vehículo es una medida de cuánta energía utiliza en relación con su rendimiento. 
Es como comparar dos lámparas: una puede iluminar una habitación con menos energía que la otra. En el mundo de los vehículos, 
esto se traduce en menos combustible o electricidad necesarios para recorrer la misma distancia. ¡Una gran noticia para tu bolsillo 
y para el medio ambiente!</p>
<p style='font-size: 16px;'>Pero, ¿cómo se clasifican exactamente los vehículos según su eficiencia energética? ¡Vamos a averiguarlo juntos!</p>
"""

        st.markdown(texto_html, unsafe_allow_html=True)
        texto_html = """

<ul style='font-size: 16px;'>
<li><strong>Eficiencia energética A:</strong> -25% (o menos)</li>
<li><strong>Eficiencia energética B:</strong> -15% a -25%</li>
<li><strong>Eficiencia energética C:</strong> -5% a -15%</li>
<li><strong>Eficiencia energética D:</strong> -5% a +5%</li>
<li><strong>Eficiencia energética E:</strong> +5 a +15%</li>
<li><strong>Eficiencia energética F:</strong> +15% a +25%</li>
<li><strong>Eficiencia energética G:</strong> +25% o más</li>
</ul>
"""

        st.markdown(texto_html, unsafe_allow_html=True)
    

    with col4:
            for i in range(1,2):
                st.markdown(" ")
            
            # Ruta de la imagen
            ruta_imagen = "https://images.unsplash.com/photo-1617704548623-340376564e68?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

            # Mostrar la imagen
            st.image(ruta_imagen, caption='Clasificacion energetica', use_column_width=True)
    

    titulo_html = """
    <h2 style='color: cyan;'>Descubre Cómo se Clasifican los Vehículos según su Eficiencia Energética</h2>

    """
    for i in range(1,4):
            st.markdown(" ")

    texto_html = """
    <p style='font-size: 16px;'>Echando un vistazo a la eficiencia energética, la mayoría de los coches eléctricos sacan matrícula de honor (A). Los que no tienen clasificación específica son los coches eléctricos puros. Por otro lado, los que se llevan el suspenso (G) son los híbridos enchufables, seguidos por los híbridos de gasolina y, en menor medida, los de gasóleo.</p>

    <p style='font-size: 16px;'>En el mundo de los coches de gasolina y diésel, los que se llevan la medalla de bronce son los de etiqueta C, seguidos de cerca por las categorías B y D. Y si nos ponemos a investigar un poco más, vemos que la mayoría de los que se llevan el suspenso son coches de gasolina, seguidos de los de gasóleo.</p>
    """

    st.markdown(titulo_html, unsafe_allow_html=True)
    st.markdown(texto_html, unsafe_allow_html=True)
    for i in range(1,4):
            st.markdown(" ")
            
    texto = """
        <div style='text-align: center;'>
        <span style='color: cyan; font-weight: bold; font-size: 40px;'>
        Descubre la Conexión entre 'Cuántos Kilómetros Puedes Recorrer' y 'Lo Grande de la Batería' en los Coches Eléctricos"
        </span>
        </div>
        """

        # Mostrar el texto alineado al centro
    st.markdown(texto, unsafe_allow_html=True)
    for i in range(1,4):
            st.markdown(" ")

    col5,col6 = st.columns(2)
    with col5:
        for i in range(1,4):
            st.markdown(" ")

        texto_html = """
        
        <p style='font-size: 16px;'>En resumen, mientras más grande sea la batería, más lejos podrás llegar sin tener que parar a cargar. Es como tener un depósito más grande para almacenar energía. Y sabes qué, ¡los coches eléctricos puros son los que más lejos pueden llegar! Luego vienen los híbridos enchufables y los híbridos de gasolina, en ese orden.</p>

        <p style='font-size: 16px;'>Si hablamos de coches eléctricos puros, su autonomía varía entre 100 y 600 kilómetros, dependiendo de cuánta energía pueda almacenar su batería. Mientras tanto, los híbridos enchufables pueden recorrer entre 20 y 80 kilómetros solo con electricidad, y los híbridos de gasolina apenas pueden hacer unos pocos kilómetros en modo eléctrico.</p>

        <p style='font-size: 16px;'>Claro, hay otros factores que influyen en cuánto puedes viajar sin recargar, como tu estilo de conducción, el clima y el estado de la batería. Pero la capacidad de la batería es definitivamente uno de los factores más importantes que afecta tu autonomía eléctrica.</p>
        """

        st.markdown(texto_html, unsafe_allow_html=True)

    with col6:
          
            
            # Ruta de la imagen
          ruta_imagen = "https://images.unsplash.com/photo-1625998259975-b243bf480751?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

            # Mostrar la imagen
          st.image(ruta_imagen, caption='Clasificacion energetica', use_column_width=True)
         
            







