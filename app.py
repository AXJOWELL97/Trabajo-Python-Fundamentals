import streamlit as st
import pandas as pd

# 1. Definición del Menú Lateral (Aquí se crea la variable 'opcion')
st.sidebar.title("Navegación")
opcion = st.sidebar.selectbox(
    "Seleccione una sección:",
    ["Inicio", "Presupuesto mensual", "Saldo", "Notas", "Reportes"]
)

# 2. Lógica de las secciones
if opcion == "Inicio":
    st.title("Gestor de Finanzas Personales")
    st.sidebar.image("gestor.png")
    st.write("Bienvenido al proyecto de **[Bruno Pillaca]**")

elif opcion == "Reportes":
    st.title("Manejo de Dataframes")
    st.sidebar.markdown("---")
    st.sidebar.title("Herramientas")

    # file_uploader debe ir antes de intentar leer el archivo
    archivo = st.sidebar.file_uploader("Seleccione su archivo", type=["csv", "xlsx"])

    if archivo is not None:
        st.write("### Su archivo ha sido cargado")
        
        # Validación de extensión usando el atributo .name
        if archivo.name.endswith('.csv'):
            datos = pd.read_csv(archivo)
            st.dataframe(datos) # Mostramos la tabla
        elif archivo.name.endswith('.xlsx'):
            datos = pd.read_excel(archivo)
            st.dataframe(datos)
    else:
        st.warning("Por favor, cargue un archivo para visualizar los datos.")