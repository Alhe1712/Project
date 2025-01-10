import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de precios de vehículos') 

st.write('Selecciona las casillas para mostrar el gráfico correspondiente.')

# Casilla de verificación para el histograma
show_histogram = st.checkbox('Mostrar histograma')
if show_histogram:
    st.write('Histograma para el odómetro')
    fig = px.histogram(car_data, x="odometer", color_discrete_sequence=["orange"], barmode="overlay", nbins=100, range_x=[0, 1000000])
    fig.update_layout( xaxis_title="Odómetro (millas)", yaxis_title="Frecuencia")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para el diagrama de dispersión
show_scatter = st.checkbox('Mostrar diagrama de dispersión')
if show_scatter:
    st.write('Distribución precio vs. odómetro')
    fig = px.scatter(car_data, x="odometer", y="price", color_discrete_sequence=["pink"])
    fig.update_layout( xaxis_title="Odómetro (millas)", yaxis_title="Precio (USD)")
    st.plotly_chart(fig, use_container_width=True)
