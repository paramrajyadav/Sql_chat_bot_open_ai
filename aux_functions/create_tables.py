import streamlit as st
import os
import pandas as pd

def read_aux_data():
    """
    Reads the file name and column names from separate files within the aux_data directory.

    Returns:
    column_names (str): The column names read from column_names.txt.
    file_name (str): The file name read from file_name.txt.

    """
    column_names_filename = 'aux_data/column_names.txt'
    file_name_filename = 'aux_data/file_name.txt'
    with open(column_names_filename, 'r') as column_file:
        column_names = [line.strip() for line in column_file.readlines()]

    # Read file name
    with open(file_name_filename, 'r') as file_file:
        file_name = file_file.read().strip()

    return column_names, file_name

def built_table():
    st.title("File Upload, Data Preview, and SQL Schema Creation")

    column_names, file_name = read_aux_data()

    st.write("## Load and Display Saved Column Data")
    st.write(column_names)

    st.write("## Load and Display Sample Data")
    file_path = os.path.join('data', file_name)

    if os.path.exists(f"{file_path}.csv"):
        df = pd.read_csv(f"{file_path}.csv")
        st.write(df.head(20))
    else:
        st.write("Sample data not found.")

    st.write("## Create SQL Schema")
    sql_schema = {}
    data_types = ['VARCHAR(250)', 'INT', 'FLOAT', 'DATE', 'DOUBLE']

    for col in column_names:
        selectbox_key = f"{col}_selectbox"
        data_type = st.selectbox(f"Select data type for column '{col}'", [''] + data_types, key=selectbox_key)
    
        if data_type == '':
            st.warning(f"Please select a data type for column '{col}'.")
            st.stop()  # Stop execution if a data type is not selected
        sql_schema[col] = data_type

    st.write("### Generated SQL Schema")
    create_table_query = f"CREATE TABLE {file_name} (\n"
    create_table_query += ",\n".join([f"    {col} {dtype}" for col, dtype in sql_schema.items()])
    create_table_query += "\n);"

    st.code(create_table_query, language='sql')

    if st.button("Schema is correct"):
        # Store the query in a file
        query_filename = 'aux_data/query.txt'
        with open(query_filename, 'w') as query_file:
            query_file.write(create_table_query)
        st.success("Query has been saved.")

    return None
