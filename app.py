import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def intro():
    st.title("Project 4 - Data Analysis Oriented to Sales Strategies from a SQL perspective")

    st.write("""
    # Introduction
    This presentation demonstrates data analysis using Streamlit. Use the selector below to choose different datasets and visualize their respective analyses.
    """)


def datasets():
    # Diccionario de DataFrames
    dataframes = {
        "Games Dataset": pd.read_csv('data/games_register.csv'),
        "Shops Dataset": pd.read_csv('data/shops_register.csv'),
        "Game units Dataset": pd.read_csv('data/units_register.csv'),
        "Genres Dataset": pd.read_csv('data/genres_register.csv'),
    }

    # Selector de DataFrame
    option = st.radio(
        "Select a dataset to display",
        list(dataframes.keys())
    )

    st.write(f"# {option}")

    df_selected = dataframes[option]

    if option == 'Games Dataset':
        st.write("""
        The `games` dataset stores information about video games, including a unique identifier for each game (`gameID`), its title (`title`), release date (`release_date`), and a numerical score (`scores`) which represent the mean rating from users .
        """)
    elif option == 'Shops Dataset':
        st.write("""
        The `shops` dataset contains data about the stores where the games are sold. It includes a store identifier (`store_id`) and the store name (`store_name`).         
        """)
    elif option == 'Game units Dataset':
        st.write("""
        The `units` dataset appears to be related to the units of games available in different stores. 
        It includes the number of units (`num_unit`), the associated game identifier (`gameID`), the identifier of the store where it is sold (`store_id`), the original price (`original_price`), and the discounted price (`discount_price`).         
        """)
    elif option == 'Genres Dataset':
        st.write("""
        The `genres` dataset keeps track of different video game genres. It contains the genre name (`genre_name`) and an optional description (`description`).      
        """)

    # Mostrar DataFrame seleccionado
    
    st.write(df_selected)


def database():

    sql_files = {
        "Entity - Relation" : 'ER.png',
        "Tables": 'data/tables.sql',
        "Queries": 'queries.sql'
    }

    # Selector de DataFrame
    option = st.radio(
        "## Select an option to display",
        list(sql_files.keys())
    )

    if option == 'Entity - Relation':
        st.write("## Entity - Relation Diagram")
        st.image("data/ER.png")
        st.write("## Entity - Relational Model Diagram")
        st.image("data/relational.png")
    elif option == 'Tables':
        st.title("Table creation")

        with open('data/tables.sql', 'r', encoding='utf-8') as file:
            sql_tables = file.read()

        st.code(sql_tables, language='sql')

    elif option == 'Queries':
            
        selected_query = {
            'Query_1' : ["data/Queries/simple1.sql","data/Queries/result1.csv"] ,
            'Query_2' : ["data/Queries/simple2.sql","data/Queries/result2.csv"],
            'Query_3' : ["data/Queries/simple3.sql","data/Queries/result3.csv"]
        }

        query_opt = st.radio(
            "## Select a query to display",
            list(selected_query.keys()), horizontal = True
        )

        selected_value = selected_query[query_opt][0]

        with open(selected_value, 'r', encoding='utf-8') as file:
            sql_tables = file.read()

        st.code(sql_tables, language='sql')

        result_sel = selected_query[query_opt][1]

        st.write(pd.read_csv(result_sel))


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
page = st.sidebar.selectbox("Select a page", ["Introduction", "Datasets showcase", "Database creation and queries", "Graphics from advanced queries"]) 
st.sidebar.markdown("<br>" * 20, unsafe_allow_html=True)
st.sidebar.markdown("""  
                ## This project has been developed by:
                Iván Alonso - https://github.com/ivanalonsom  
                Mario Jimenez - https://github.com/mjimcode
                """)

if page == "Introduction":
    intro()
elif page == "Datasets showcase":
    datasets()
elif page == 'Database creation and queries':
    database()
elif page == 'Graphics from advanced queries':
    adv_queries_graphics()




