import numpy as np
import pandas as pd

def convert_to_dateTime(df_col):
    import pandas as pd
    return pd.to_datetime(df_col, format='%Y-%m-%d %H:%M:%S')
def replace_values_df(df_col, map):
    import pandas as pd
    return df_col.map(map)
def drop_na_df(df, col):
    import pandas as pd
    return df.dropna(subset=[col])

#Función para quitar outlier
def outlier_slayer(data): # automatically removes outliers based on Q1, Q3
    """
    Automatically removes outliers based on Q1, Q3
    """
    for column in data.select_dtypes(include=[np.number]):
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
    return data


def normalizar_nombres_columnas(df):
    """
    Normaliza los nombres de las columnas de un DataFrame.

    Args:
        df (pd.DataFrame): El DataFrame cuyos nombres de columnas se van a normalizar.

    Returns:
        pd.DataFrame: El DataFrame con los nombres de columnas normalizados.
    """

    df.columns = df.columns.str.lower()  # Convertir a minúsculas
    df.columns = df.columns.str.replace('[^\w\s]', '')  # Eliminar símbolos no alfanuméricos
    df.columns = df.columns.str.replace('\s+', '_')  # Reemplazar espacios múltiples por un guion bajo

    return df