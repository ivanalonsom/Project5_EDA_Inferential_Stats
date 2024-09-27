import numpy as np
from scipy import stats

def convert_to_dateTime(df_col):
    import pandas as pd
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
    import pandas as pd
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


def get_final_demo_df():
    import pandas as pd
    df_final_demo = pd.read_csv("df_final_demo.csv")

    df_final_demo.dropna(inplace=True)

    mapGenre = {'X' : 'U'}
    df_final_demo["gendr"] = replace_values_df(df_final_demo["gendr"], mapGenre)

    return df_final_demo


def get_web_data_df():
    import pandas as pd

    df_web_data1 = pd.read_csv("df_final_web_data_pt_1.csv")
    df_web_data2 = pd.read_csv("df_final_web_data_pt_2.csv")

    df_web_data_concat = pd.concat([df_web_data1, df_web_data2], axis=0, join='inner')
    # Convert type object into datetime 

    df_web_data_concat['date_time'] = convert_to_dateTime(df_web_data_concat['date_time'])

    # I turn 'step' into a discrete numeric df

    map_values = {'start' : 0, 'step_1' : 1, 'step_2' : 2, 'step_3' : 3, 'confirm' : 4}

    df_web_data_concat["process_step"] = replace_values_df(df_web_data_concat["process_step"], map_values)

    return df_web_data_concat


def get_final_exp_df():
    import pandas as pd

    df_final_exp = pd.read_csv("df_final_experiment_clients.csv")
    df_final_exp.rename(columns={"Variation" : "variation"}, inplace=True)
    df_final_exp = drop_na_df(df_final_exp, "variation")
    map_values2 = {'Control': 0, 'Test': 1}

    df_final_exp["variation"] = replace_values_df(df_final_exp["variation"], map_values2)

    return df_final_exp


def get_df_all():
    import pandas as pd

    df_1 = get_final_demo_df()
    df_2 = get_web_data_df()
    df_3 = get_final_exp_df()

    df_temp = pd.merge(df_1, df_2, on='client_id', how='inner')
    df_all = pd.merge(df_temp, df_3, on='client_id', how='inner')

    return df_all


def get_df_all_no_duplicates():
    import pandas as pd

    df_all = get_df_all().copy()
    df_all_no_duplicates = df_all.drop_duplicates(subset="client_id")

    return df_all_no_duplicates


def print_stats(df_col):
    """
    Prints descriptive statistics and mode of a DataFrame column.
    
    Parameters:
    df_col (pd.Series): Column of a DataFrame.
    
    Returns:
    pd.Series, str: Descriptive statistics and mode of the column.
    """
    # Descriptive statistics
    description = df_col.describe()
    
    # Calculate mode
    mode = df_col.mode()
    if len(mode) == 1:
        mode_str = f"Mode: {mode.iloc[0]}"
    else:
        mode_str = f"Mode: {list(mode)}"
    
    return description, mode_str


def get_limits(df_col):
    """
    Calculate lower and upper limits of a DataFrame column.
    
    Parameters:
    df_col (pd.Series): Column of a DataFrame.
    
    Returns:
    tuple: Lower and upper limits of the column.
    """
    # Calculate lower and upper limits
    q1 = df_col.quantile(0.25)
    q3 = df_col.quantile(0.75)
    iqr = q3 - q1
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr
    return lower_limit, upper_limit


def get_last_step(df, variation):

    df = df[df["variation"] == variation]

    df_step_0 = df[df["process_step"] == 0]
    df_step_1 = df[df["process_step"] == 1]
    df_step_2 = df[df["process_step"] == 2]
    df_step_3 = df[df["process_step"] == 3]
    df_step_4 = df[df["process_step"] == 4]

    perc_step0 = 100 * df_step_0.shape[0] / df.shape[0]
    perc_step1 = 100 * df_step_1.shape[0] / df.shape[0]
    perc_step2 = 100 * df_step_2.shape[0] / df.shape[0]
    perc_step3 = 100 * df_step_3.shape[0] / df.shape[0]

    perc_confirms = 100 * df_step_4.shape[0] / df.shape[0]

    print(f"""
    El % de gente que se quedó en el INICIO en la web de {'CONTROL' if variation == 0 else 'TEST'} es de {perc_step0}
    El % de gente que se quedó en el PASO 1 en la web de {'CONTROL' if variation == 0 else 'TEST'} es de {perc_step1}
    El % de gente que se quedó en el PASO 2 en la web de {'CONTROL' if variation == 0 else 'TEST'} es de {perc_step2}
    El % de gente que se quedó en el PASO 3 en la web de {'CONTROL' if variation == 0 else 'TEST'} es de {perc_step3}
    El % de gente que CONFIRMÓ la compra en la web de {'CONTROL' if variation == 0 else 'TEST'} es de {perc_confirms}
      """)