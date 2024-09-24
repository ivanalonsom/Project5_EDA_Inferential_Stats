def convert_to_dateTime(df_col):
    import pandas as pd

    return pd.to_datetime(df_col, format='%Y-%m-%d %H:%M:%S')
    

def replace_values_df(df_col, map_val):
    import pandas as pd

    return df_col.map(lambda x : map_val.get(x, x))


def drop_na_df(df, col):
    import pandas as pd

    return df.dropna(subset=[col])