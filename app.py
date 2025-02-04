import pandas as pd
import plotly.express as px
import streamlit as st
import os

#print(os.getcwd())

#importancion del archivo CSV
car_data = pd.read_csv('/Users/leonnic/Documents/project_7/Data/vehicles_us.csv')

st.header('Web App de Análisis de Datos de Vehículos')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creando un histograma para la columna Odometer...')
    
    # Crear el histograma usando Plotly Express
    fig = px.histogram(car_data, x="odometer", nbins=50, title="Histograma de Odometer")
    
    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de Dispersión')
if disp_button:
    st.write('Creando gráfico de dispersión para la columna Odometer...')

    fig1 = px.scatter(car_data, x='odometer', y='price', title='Dispersión Precio vs. Odometer')
    st.plotly_chart(fig1, use_container_width=True)

