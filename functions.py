def convert_to_dateTime(df_col):
    import pandas as pd

    return pd.to_datetime(df_col, format='%Y-%m-%d %H:%M:%S')
    

def replace_values_df(df_col, map_val):
    import pandas as pd

    return df_col.map(lambda x : map_val.get(x, x))


def drop_na_df(df, col):
    import pandas as pd

    return df.dropna(subset=[col])


def outlier_slayer(data): # automatically removes outliers based on Q1, Q3
    import numpy as np
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