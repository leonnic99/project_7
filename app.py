import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Obtener la ruta del directorio donde está app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta del archivo CSV de forma relativa
csv_path = os.path.join(BASE_DIR, "Data", "vehicles_us.csv")

# Verificar si el archivo existe antes de cargarlo
if os.path.exists(csv_path):
    car_data = pd.read_csv(csv_path)
else:
    st.error(f"No se encontró el archivo CSV en: {csv_path}")
    st.stop()  # Detener la ejecución si el archivo no existe

# Interfaz de Streamlit
st.header('Web App de Análisis de Datos de Vehículos')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creando un histograma para la columna Odometer...')
    fig = px.histogram(car_data, x="odometer", nbins=50, title="Histograma de Odometer")
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de Dispersión')
if disp_button:
    st.write('Creando gráfico de dispersión para la columna Odometer...')
    fig1 = px.scatter(car_data, x='odometer', y='price', title='Dispersión Precio vs. Odometer')
    st.plotly_chart(fig1, use_container_width=True)


