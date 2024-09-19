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
        "Tables": 'tables.sql',
        "Queries": 'queries.sql'
    }

    # Selector de DataFrame
    option = st.radio(
        "## Select an option to display",
        list(sql_files.keys())
    )

    if option == 'Tables':
        st.title("Table creation")

        with open('tables.sql', 'r', encoding='utf-8') as file:
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
            list(selected_query.keys())
        )

        selected_value = selected_query[query_opt][0]

        with open(selected_value, 'r', encoding='utf-8') as file:
            sql_tables = file.read()

        st.code(sql_tables, language='sql')

        result_sel = selected_query[query_opt][1]

        st.write(pd.read_csv(result_sel))


    


st.sidebar.title("Navegation")
page = st.sidebar.selectbox("Select a page", ["Introduction", "Datasets showcase", "Database creation and queries", "Graphics from advanced queries"]) 
st.sidebar.markdown("<br>" * 20, unsafe_allow_html=True)
st.sidebar.markdown("""  
                ## This project have been developed by:
                Iván Alonso - https://github.com/ivanalonsom  
                Mario Jimenez - https://github.com/mjimcode
                """)

if page == "Introduction":
    intro()
elif page == "Datasets showcase":
    datasets()
elif page == 'Database creation and queries':
    database()




