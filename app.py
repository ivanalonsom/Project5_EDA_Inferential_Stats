import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def show_boxplot(df_col):
    # Cargar datos
    df_outliers = pd.read_csv('data/df_all_outliers.csv')

    # Verificar si la columna 'clnt_tenure_mnth' existe
    if df_col.name in df_outliers.columns:
        # Crear el gráfico de cajas y bigotes
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df_col)
        plt.title(f'Gráfico de Cajas y Bigotes para {df_col.name}')
        plt.ylabel('Valores')
        plt.grid(True)
        st.pyplot(plt)
        
        # Mostrar outliers si existen
        desc = df_outliers['clnt_tenure_mnth'].describe()
        q1 = desc['25%']
        q3 = desc['75%']
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        outliers = df_outliers[(df_outliers[df_col.name].notna()) & (df_col < lower_bound) | (df_col > upper_bound)]
        if not outliers.empty:
            st.write(f"Outliers encontrados: {outliers.count()[0]}")
        else:
            st.write("No se encontraron outliers.")
    else:
        st.write("La columna no se encuentra en el DataFrame.")


def graph_bar_plot_control_v_test(df_control, df_test):
    # Contar y normalizar las ocurrencias de process_step en cada DataFrame
    control_counts = df_control['process_step'].value_counts(normalize=True).sort_index() * 100  
    test_counts = df_test['process_step'].value_counts(normalize=True).sort_index() * 100  

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
 

def intro():
    st.image("https://ceblog.s3.amazonaws.com/wp-content/uploads/2018/06/29173427/ab-testing-2.jpg", use_column_width=True)
    st.markdown("<p style='text-align: right; font-size: 10px; padding: 0'>Image source: <em><a href=https://www.crazyegg.com/blog/ab-testing/'>https://www.crazyegg.com/blog/ab-testing/</em></a></p>", unsafe_allow_html=True)


    st.markdown("<style>h1 {text-align: justify;}</style>", unsafe_allow_html=True)
    st.title("Project 5 - Evaluation of Website Efficiency through Data Analysis using A/B Testing") 

    st.markdown("""<p style='font-size: 18px; text-align: justify'>
                 In this project, we will analyze the efficiency of a website through data analysis using A/B Testing.
                Our goal is to evaluate the performance and user engagement between two variations of the website: the original version (control) and a new version (test).</p>
        """, unsafe_allow_html=True)
    
    
    st.markdown("<h3 style='color:gray; font-size: 18px'>Below is an example of the original dataframes, prior to the treatment performed.</h3>", unsafe_allow_html=True)
        

    if 'show_df' not in st.session_state:
        st.session_state.show_df = False    
    
    if 'show_boxplots' not in st.session_state:
        st.session_state.show_boxplots = False

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Show/Hide Dataframes"):
            st.session_state.show_df = not st.session_state.show_df

    with col2:
        if st.button("Show/Hide Boxplots"):
            st.session_state.show_boxplots = not st.session_state.show_boxplots

    
    if st.session_state.show_df:
        df_no_treatment_demo = pd.read_csv('original_data/df_final_demo.csv')
        df_no_treatment_experiment = pd.read_csv('original_data/df_final_experiment_clients.csv')
        df_no_treatment_webdataConcat = pd.read_csv('original_data/df_web_data_concat.csv')

        st.markdown("<p style='color:gray'>Clients data .</p>", unsafe_allow_html=True)
        st.write(df_no_treatment_demo)

        st.markdown("<p style='color:gray'>Webdata.</p>", unsafe_allow_html=True)
        st.write(df_no_treatment_webdataConcat)

        st.markdown("<p style='color:gray'>Final experiment.</p>", unsafe_allow_html=True)
        st.write(df_no_treatment_experiment)

    
    if st.session_state.show_boxplots:

        df_outliers = pd.read_csv('data/df_all_outliers.csv')
        show_boxplot(df_outliers["clnt_tenure_mnth"])

        df_no_outliers = pd.read_csv('data/df_all_cleaned.csv')
        show_boxplot(df_no_outliers["clnt_tenure_mnth"])


def datasets():
    # Diccionario de DataFrames
    dataframes = {
        "Total": pd.read_csv('data/df_all.csv'),
        "No Duplicates": pd.read_csv('data/df_all_no_duplicates.csv'),
        "Test": pd.read_csv('data/df_test_propio.csv'),
        "Control": pd.read_csv('data/df_control_propio.csv'),
    }

    # Selector de DataFrame
    option = st.radio(
        "Select a dataset to display",
        list(dataframes.keys())
    )

    st.write(f"# {option}")

    df_selected = dataframes[option]

    if option == 'Total':
        st.write("""
        This df contains all the data from the three initial datasets, merged together and cleaned. 
        """)
    elif option == 'No Duplicates':
        st.write("""
        This df contains the data deleting duplicate entries of client ID in order to analyse client data such as average age.      
        """)
    elif option == 'Control':
        st.write("""
        This df contains the data from the old version of the website.      
        """)
    elif option == 'Test':
        st.write("""
        This df contains the data from the new version of the website.       
        """)

    st.write(df_selected)


def statistics():
    df_all = pd.read_csv('data/df_all.csv')
    df_control = pd.read_csv('data/df_control_propio.csv')
    df_test = pd.read_csv('data/df_test_propio.csv')

    df_num = df_all.select_dtypes(include=['int64', 'float64'])
    df_num.drop(['client_id', 'num_accts', 'lastOp', 'variation', 'process_step', 'num_compras'], axis=1, inplace=True)
    df_cat = df_all.select_dtypes(include=['object'])

    st.write("Numerical variables statistics:")
    st.write(df_num.describe() )

    st.write("Categorical variables statistics:")
    st.write(df_cat.describe() )

    graph_bar_plot_control_v_test(df_control, df_test)


# def database():

#     sql_files = {
#         "Entity - Relation" : 'ER.png',
#         "Tables": 'data/tables.sql',
#         "Queries": 'queries.sql'
#     }

#     # Selector de DataFrame
#     option = st.radio(
#         "## Select an option to display",
#         list(sql_files.keys())
#     )

#     if option == 'Entity - Relation':
#         st.write("## Entity - Relation Diagram")
#         st.image("data/ER.png")
#         st.write("## Entity - Relational Model Diagram")
#         st.image("data/relational.png")
#     elif option == 'Tables':
#         st.title("Table creation")

#         with open('data/tables.sql', 'r', encoding='utf-8') as file:
#             sql_tables = file.read()

#         st.code(sql_tables, language='sql')

#     elif option == 'Queries':
            
#         selected_query = {
#             'Query_1' : ["data/Queries/simple1.sql","data/Queries/result1.csv"] ,
#             'Query_2' : ["data/Queries/simple2.sql","data/Queries/result2.csv"],
#             'Query_3' : ["data/Queries/simple3.sql","data/Queries/result3.csv"]
#         }

#         query_opt = st.radio(
#             "## Select a query to display",
#             list(selected_query.keys()), horizontal = True
#         )

#         selected_value = selected_query[query_opt][0]

#         with open(selected_value, 'r', encoding='utf-8') as file:
#             sql_tables = file.read()

#         st.code(sql_tables, language='sql')

#         result_sel = selected_query[query_opt][1]

#         st.write(pd.read_csv(result_sel))


def adv_queries_graphics():
    import pandas as pd
    import plotly.express as px
    
    selected_query = {
            'Query_A' : ["data/Queries/advanced1.sql","data/Queries/adv_res1.csv"],
            'Query_B' : ["data/Queries/advanced2.sql","data/Queries/adv_res2.csv"],
            'Query_C' : ["data/Queries/advanced3.sql","data/Queries/adv_res3.csv"],
            'Query_D' : ["data/Queries/advanced4.sql","data/Queries/adv_res4.csv"]
    }

    query_opt = st.radio(
        "## Select a query to display",
        list(selected_query.keys() ), horizontal = True
    )

    selected_value = selected_query[query_opt][0]

    with open(selected_value, 'r', encoding='utf-8') as file:
        sql_tables = file.read()

    st.code(sql_tables, language='sql')

    result_sel = selected_query[query_opt][1]

    st.write(pd.read_csv(result_sel))

    df_res = pd.read_csv(result_sel)
    
    st.title("Gráfico interactivo")
    if df_res is not None:
        st.write("Elija una columna para el eje X")
        ejeX = st.selectbox("Eje X", df_res.columns)
        st.write("Elija una columna para el eje Y")
        ejeY = st.selectbox("Eje Y", df_res.columns)

        col1, col2, col3 = st.columns(3)
        graph_container = st.container()


        with col1:
            if st.button("Create bar chart"):
                with graph_container:
                    fig = px.bar(df_res, x=ejeX, y=ejeY, title=f"{ejeY} per {ejeX}")
                    st.plotly_chart(fig)

        with col2:
            if st.button("Create dot chart"):
                with graph_container:
                    fig = px.line(df_res, x=ejeX, y=ejeY, title=f"{ejeY} per {ejeX}")
                    st.plotly_chart(fig)

        with col3:
            if st.button("Create pie chart"):
                with graph_container:
                    fig = px.pie(df_res, values= ejeX, names=ejeY, title=f"{ejeY} per {ejeX}")
                    st.plotly_chart(fig)


    


st.sidebar.title("Navegation")
page = st.sidebar.selectbox("Select a page", ["Introduction", "Datasets showcase", "Statistics", "Graphics from advanced queries"]) 
st.sidebar.markdown("<br>" * 20, unsafe_allow_html=True)
st.sidebar.markdown("""  
                ## This project has been developed by:
                Iván Alonso - https://github.com/ivanalonsom  
                Danny Rodas - https://github.com/cohet3
                """)

if page == "Introduction":
    intro()
elif page == "Datasets showcase":
    datasets()
elif page == 'Statistics':
    statistics()
elif page == 'Graphics from advanced queries':
    adv_queries_graphics()




