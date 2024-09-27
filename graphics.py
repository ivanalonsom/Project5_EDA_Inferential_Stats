def graph_box_plot(df_col):
    import seaborn as sns
    
    sns.boxplot(data = df_col)


def graph_bar_plot_control_v_test(df_control, df_test):
    import pandas as pd
    import matplotlib.pyplot as plt

    # Contar y normalizar las ocurrencias de process_step en cada DataFrame
    control_counts = df_control['process_step'].value_counts(normalize=True).sort_index() * 100  
    # normalize=True me permite obtener la proporcion. Si no, obtengo datos absolutos y al ser los dos df con distintos número de valores no puedo compararlos 
    test_counts = df_test['process_step'].value_counts(normalize=True).sort_index() * 100  

    # Crear un DataFrame para facilitar la comparación
    counts_df = pd.DataFrame({'Control (%)': control_counts, 'Test (%)': test_counts})

    # Graficar
    counts_df.plot(kind='bar', figsize=(10, 6))
    plt.title('Comparación Proporcional de process_step entre Control y Test')
    plt.xlabel('Process Step')
    plt.ylabel('Porcentaje de Ocurrencias (%)')
    plt.xticks(rotation=0)
    plt.legend(title='Grupo')
    plt.grid(axis='y')
    plt.show()


def graph_process_step_controlVtest(df_control, df_test):
    import pandas as pd
    import matplotlib.pyplot as plt

    # Supongamos que df_control y df_test son tus DataFrames con los datos

    # Contar y normalizar las ocurrencias de process_step en cada DataFrame
    control_counts = df_control['process_step'].value_counts(normalize=True).sort_index() * 100
    test_counts = df_test['process_step'].value_counts(normalize=True).sort_index() * 100

    # Crear un DataFrame para facilitar la comparación
    counts_df = pd.DataFrame({'Control (%)': control_counts, 'Test (%)': test_counts})

    # Invertir el orden de los índices para calcular correctamente la probabilidad acumulada desde el paso 0
    counts_df = counts_df[::-1]

    # Calcular la probabilidad acumulada
    counts_df['Control Acumulado (%)'] = counts_df['Control (%)'].cumsum()
    counts_df['Test Acumulado (%)'] = counts_df['Test (%)'].cumsum()

    # Invertir de nuevo para graficar correctamente
    counts_df = counts_df[::-1]

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(counts_df.index, counts_df['Control Acumulado (%)'], marker='o', label='Control Acumulado (%)', color='blue')
    plt.plot(counts_df.index, counts_df['Test Acumulado (%)'], marker='o', label='Test Acumulado (%)', color='orange')
    plt.title('Probabilidad Acumulada de process_step entre Control y Test')
    plt.xlabel('Process Step')
    plt.ylabel('Probabilidad Acumulada (%)')
    plt.xticks(rotation=0)
    plt.legend(title='Grupo')
    plt.grid(axis='y')
    plt.show()


