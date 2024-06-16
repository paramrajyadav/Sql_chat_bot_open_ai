import os
import pandas as pd
import streamlit as st
import csv
from aux_functions import *

def handle_file_upload(upload_dir='data', aux_data_folder='aux_data'):
    """
    Handles the file upload, storage, and extraction of column names.
    Stores the file name and column names in an auxiliary text file.
    
    Parameters:
    upload_dir (str): The directory to store uploaded files.
    aux_file (str): The name of the auxiliary text file to store file name and column names.
    
    Returns:
    file_name (str): The name of the uploaded file.
    column_names (list): The list of column names in the uploaded file.
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # File uploader
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        # Store file in the specified directory
        # clean_data_folder()
        file_name = uploaded_file.name
        file_path = os.path.join(upload_dir, file_name)

        for filename in os.listdir(upload_dir):
            file_path_existing = os.path.join(upload_dir, filename)
            if os.path.isfile(file_path_existing) and filename != file_name:
                os.remove(file_path_existing)
                # st.write(f"Deleted: {file_path_existing}")


        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"File {file_name} saved successfully!")
        
        # Read the file and get column names
        if file_name.endswith('.csv'):
            df = pd.read_csv(file_path)

        else:
            df = pd.read_xml(file_path)

        column_names = df.columns.tolist()

        
        if not os.path.exists(aux_data_folder):
            os.makedirs(aux_data_folder)

# Define the filenames for the text files
        file_name_filename = os.path.join(aux_data_folder, "file_name.txt")
        column_names_filename = os.path.join(aux_data_folder, "column_names.txt")

# Write file name to its respective text file
        with open(file_name_filename, "w") as file_name_file:
            file_name_without_extension = file_name.rsplit('.', 1)[0]
            file_name_file.write(file_name_without_extension)

# Write column names to its respective text file
        with open(column_names_filename, "w") as column_names_file:
            for col in column_names:
                column_names_file.write(col + "\n")
        st.markdown("## File upload Successful, Click on 'Go to next Menu' to proceed forward ")

        return file_name, column_names
    else:
        st.info("Please upload a file")
        return None, None
    
    