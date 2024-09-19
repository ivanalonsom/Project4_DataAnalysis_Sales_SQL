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

    # Mostrar DataFrame seleccionado
    df_selected = dataframes[option]
    st.write(f"## {option}")
    st.write(df_selected)

    # Visualización de gráficos según el DataFrame seleccionado
    if option == "Dataset 1":
        st.write("### Bar Chart")
        fig, ax = plt.subplots()
        df_selected['A'].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

        st.write("### Scatter Plot")
        fig, ax = plt.subplots()
        ax.scatter(df_selected['A'], df_selected['B'])
        ax.set_xlabel('A')
        ax.set_ylabel('B')
        st.pyplot(fig)

    elif option == "Dataset 2":
        st.write("### Histogram")
        fig, ax = plt.subplots()
        ax.hist(df_selected['X'], bins=20)
        ax.set_xlabel('X')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

        st.write("### Boxplot")
        fig, ax = plt.subplots()
        ax.boxplot(df_selected['Y'].dropna())
        ax.set_xlabel('Y')
        st.pyplot(fig)

    elif option == "Dataset 3":
        st.write("### Line Chart")
        fig, ax = plt.subplots()
        ax.plot(df_selected['M'], df_selected['N'])
        ax.set_xlabel('M')
        ax.set_ylabel('N')
        st.pyplot(fig)

    # Conclusión
    st.write("""
    # Conclusion
    This concludes the data analysis presentation. Use the selector to switch between different datasets and visualize their respective analyses.
    """)


    st.write(f"## {option}")
    st.write(dataframes[option])


st.sidebar.title("Navegation")
page = st.sidebar.selectbox("Select a page", ["Introduction", "Datasets showcase", "Database creation and queries", "Graphics from advanced queries"]) 

if page == "Introduction":
    intro()
elif page == "Datasets showcase":
    datasets()




