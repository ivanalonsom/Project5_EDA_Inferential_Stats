def control_test_rate(df_control, df_test, return_type="rates"):
    import pandas as pd

    # Supongamos que df_control y df_test son tus DataFrames
    # Contar el número de clientes que completaron la compra (step 4)
    control_complete = df_control[df_control["process_step"] == 4].shape[0]
    test_complete = df_test[df_test["process_step"] == 4].shape[0]

    # Contar el número total de clientes en cada grupo
    control_total = df_control.shape[0]
    test_total = df_test.shape[0]

    control_rate = control_complete / control_total
    test_rate = test_complete / test_total

    if return_type == "rates":
        return control_rate, test_rate
    elif return_type == "counts":
        return control_complete, test_complete, control_total, test_total 
    

def get_z_test_values(df_control, df_test, hypothesis):
    from statsmodels.stats.proportion import proportions_ztest

    control_complete, test_complete, control_total, test_total  = control_test_rate(df_control, df_test, "counts")
    control_rate = control_complete / control_total
    test_rate = test_complete / test_total

    # Calcular las tasas de completación


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



def umbral_aumento(df_control, df_test):

    control_rate, test_rate = control_test_rate(df_control, df_test)

    # Calcular el aumento relativo
    increase_observed = (test_rate - control_rate) / control_rate * 100

    threshold = 5  # 5%

    if increase_observed >= threshold:
        print(f"El aumento observado es de {increase_observed:.2f}%, con lo que cumple con el umbral del 5%.")
    else:
        print(f"El aumento observado es de {increase_observed:.2f}%, con lo que no cumple con el umbral del 5%.")


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
