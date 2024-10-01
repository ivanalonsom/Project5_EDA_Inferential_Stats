import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Función para crear el gráfico de barras comparativo
def graph_bar_plot_control_v_test(df_control, df_test, selected_steps):
    # Filtrar los datos según los pasos seleccionados
    df_control_filtered = df_control[df_control['process_step'].isin(selected_steps)]
    df_test_filtered = df_test[df_test['process_step'].isin(selected_steps)]

    # Contar y normalizar las ocurrencias de process_step en cada DataFrame
    control_counts = df_control_filtered['process_step'].value_counts(normalize=True).sort_index() * 100  
    test_counts = df_test_filtered['process_step'].value_counts(normalize=True).sort_index() * 100  

    # Crear un DataFrame para facilitar la comparación
    counts_df = pd.DataFrame({'Control (%)': control_counts, 'Test (%)': test_counts})

    # Graficar
    plt.figure(figsize=(10, 6))
    counts_df.plot(kind='bar')
    plt.title('Comparación Proporcional de process_step entre Control y Test')
    plt.xlabel('Process Step')
    plt.ylabel('Porcentaje de Ocurrencias (%)')
    plt.xticks(rotation=0)
    plt.legend(title='Grupo')
    plt.grid(axis='y')
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)

# Leer los datos
df_control = pd.read_csv('data/df_control_propio.csv'),
df_test = pd.read_csv('data/df_test_propio.csv')

# Obtener los valores únicos de process_step
unique_steps = sorted(df_control['process_step'].unique())

# Crear un selector múltiple en Streamlit para elegir los pasos
selected_steps = st.multiselect("Select Process Steps to Include", unique_steps, default=unique_steps)

# Mostrar el gráfico en Streamlit
st.title("Gráfico Comparativo entre Control y Test")
graph_bar_plot_control_v_test(df_control, df_test, selected_steps)
