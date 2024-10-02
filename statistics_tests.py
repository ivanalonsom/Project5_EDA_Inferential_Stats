
def control_test_rate(df, return_type="rates"):
    import pandas as pd

    # Verifica si df es un DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("El argumento df debe ser un DataFrame de pandas.")
    
    # Filtrar los grupos de control y test utilizando la columna 'variation'
    df_control = df[df["variation"] == 0]
    df_test = df[df["variation"] == 1]

    # Contar el número de clientes que completaron la compra (step 4)
    control_complete = df_control[df_control["process_step"] == 4].shape[0]
    test_complete = df_test[df_test["process_step"] == 4].shape[0]

    # Contar el número total de clientes en cada grupo
    control_total = df_control.shape[0]
    test_total = df_test.shape[0]

    # Calcular las tasas de conversión
    control_rate = control_complete / control_total if control_total > 0 else 0
    test_rate = test_complete / test_total if test_total > 0 else 0

    # Devolver tasas o conteos
    if return_type == "rates":
        return control_rate, test_rate
    elif return_type == "counts":
        return control_complete, test_complete, control_total, test_total

def get_z_test_values(df, hypothesis): 
    from statsmodels.stats.proportion import proportions_ztest

    # Filtrar los grupos de control y test utilizando la columna 'variation'
    df_control = df[df["variation"] == 0]
    df_test = df[df["variation"] == 1]

    # Contar el número de clientes que completaron la compra (step 4)
    control_complete = df_control[df_control["process_step"] == 4].shape[0]
    test_complete = df_test[df_test["process_step"] == 4].shape[0]

    # Contar el número total de clientes en cada grupo
    control_total = df_control.shape[0]
    test_total = df_test.shape[0]

    # Calcular las tasas de completación
    control_rate = control_complete / control_total if control_total > 0 else 0
    test_rate = test_complete / test_total if test_total > 0 else 0

    # Imprimir las tasas de completación
    print(f"Tasa de completación del grupo de control: {control_rate:.2%}")
    print(f"Tasa de completación del grupo de test: {test_rate:.2%}")

    # Realizar el test de dos proporciones (Z-test)
    count = [control_complete, test_complete]
    nobs = [control_total, test_total]
    stat, p_value = proportions_ztest(count, nobs, alternative=hypothesis)

    # Imprimir los resultados del test
    print(f"Estadístico Z: {stat:.4f}")
    print(f"P-valor: {p_value}")

    # Interpretar el resultado
    alpha = 0.05
    if p_value < alpha:
        print("Podemos afirmar con un 95% de confianza que la diferencia en la tasa de completación es estadísticamente significativa (rechazamos H0).")
    else:
        print("La diferencia en la tasa de completación no es estadísticamente significativa (no podemos rechazar H0).")


def umbral_aumento(df, threshold=5):
    import pandas as pd

    # Verifica si df es un DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("El argumento df debe ser un DataFrame de pandas.")

    # Filtrar los grupos de control y test utilizando la columna 'variation'
    df_control = df[df["variation"] == 0]
    df_test = df[df["variation"] == 1]

    # Calcular las tasas de conversión utilizando la función control_test_rate
    control_rate, test_rate = control_test_rate(df, return_type="rates")

    # Calcular el aumento relativo
    increase_observed = (test_rate - control_rate) / control_rate * 100
    if increase_observed >= threshold:
        print(f"El aumento observado es de {increase_observed:.2f}%, cumpliendo con el umbral del {threshold}%.")
    else:
        print(f"El aumento observado es de {increase_observed:.2f}%, no cumpliendo con el umbral del {threshold}%.")

def chi_cuadrado_test(df_control, df_test):
    import pandas as pd
    from scipy.stats import chi2_contingency

    # Contar el número de clientes que completaron la compra (step 4)
    control_complete = df_control[df_control["process_step"] == 4].shape[0]
    test_complete = df_test[df_test["process_step"] == 4].shape[0]

    # Contar el número de clientes que no completaron la compra
    control_incomplete = df_control.shape[0] - control_complete
    test_incomplete = df_test.shape[0] - test_complete

    # Crear la tabla de contingencia
    contingency_table = pd.DataFrame({
        'Complete': [control_complete, test_complete],
        'Incomplete': [control_incomplete, test_incomplete]
    }, index=['Control', 'Test'])

    # Aplicar el test chi-cuadrado
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Imprimir los resultados del test
    print(f"Chi-cuadrado: {chi2:.4f}")
    print(f"P-valor: {p}")

    # Interpretar el resultado
    alpha = 0.05
    if p < alpha:
        print("La diferencia en la tasa de completación es estadísticamente significativa (rechazamos H0).")
    else:
        print("La diferencia en la tasa de completación no es estadísticamente significativa (no podemos rechazar H0).")
def chi_cuadrado_test_dos(df):
    import pandas as pd
    from scipy.stats import chi2_contingency

    # Verifica si df es un DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("El argumento df debe ser un DataFrame de pandas.")

    # Filtrar los grupos de control y test utilizando la columna 'variation'
    df_control = df[df["variation"] == 0]
    df_test = df[df["variation"] == 1]

    # Contar el número de clientes que completaron la compra (step 4)
    control_complete = df_control[df_control["process_step"] == 4].shape[0]
    test_complete = df_test[df_test["process_step"] == 4].shape[0]

    # Contar el número de clientes que no completaron la compra
    control_incomplete = df_control.shape[0] - control_complete
    test_incomplete = df_test.shape[0] - test_complete

    # Crear la tabla de contingencia
    contingency_table = pd.DataFrame({
        'Complete': [control_complete, test_complete],
        'Incomplete': [control_incomplete, test_incomplete]
    }, index=['Control', 'Test'])

    # Aplicar el test chi-cuadrado
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Imprimir los resultados del test
    print(f"Chi-cuadrado: {chi2:.4f}")
    print(f"P-valor: {p}")

    # Interpretar el resultado
    alpha = 0.05
    if p < alpha:
        print("La diferencia en la tasa de completación es estadísticamente significativa (rechazamos H0).")
    else:
        print("La diferencia en la tasa de completación no es estadísticamente significativa (no podemos rechazar H0).")


