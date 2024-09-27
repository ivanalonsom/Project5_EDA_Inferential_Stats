import numpy as np
import pandas as pd
from scipy import stats
def convert_to_dateTime(df_col):
    """
    Convert column to datetime type using pandas
    """

    return pd.to_datetime(df_col, format='%Y-%m-%d %H:%M:%S')
    

def replace_values_df(df_col, map_val):
    """
    Replace values in a column with a map
    """
    return df_col.map(lambda x : map_val.get(x, x))


def drop_na_df(df, col):
    """
    Drop rows with NaN values in a specific column
    """
    return df.dropna(subset=[col])


def outlier_slayer(data):
    try:
        for column in data.select_dtypes(include=['float64', 'int64']).columns:
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
        return data
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return data


# Función para eliminar outliers usando Z-score
def outlier_slayer_zscore(data, threshold=3):
    z_scores = np.abs(stats.zscore(data.select_dtypes(include=[np.number])))
    data = data[(z_scores < threshold).all(axis=1)]
    return data