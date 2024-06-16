import streamlit as st

from aux_functions.aux_functions import *
from aux_functions.add_data import *
from aux_functions.create_tables import *
from aux_functions.db_functions import *
from aux_functions.chat_sql_function import *

project_dir = os.getcwd()

st.set_page_config(layout="wide")

# Define the header of the app
st.markdown("# SQL Chatbot")

# Initialize session state if not already done
if 'selected_index' not in st.session_state:
    st.session_state['selected_index'] = 0

def reset_app():
    clean_data_folder(project_dir)
    st.session_state['selected_index'] = 0


selected_index = st.session_state['selected_index']

if st.button("Reset the App", key="reset_app"):
        reset_app()

cols = st.columns(3)

# Create menu buttons dynamically
for i, label in enumerate(["Home", "Create Table", "Query"]):
    if cols[i].button(label, key=f"menu_button_{i}"):
        selected_index = i  # Select corresponding menu (Menu 1 = 1, Menu 2 = 2, etc.)
        st.session_state['selected_index'] = selected_index





if selected_index == 0:
    st.markdown("# Upload your file")
    handle_file_upload()

elif selected_index == 1:
    st.write("This is the display code for Create Table.")
    built_table()
    if st.button("Insert values in the database"):
        file_name_from_file(project_dir)
        drop_sqlite_database()
        setup_database()
        import_csv(project_dir)
    st.markdown(" # Proceed to the QA Part")

elif selected_index == 2:
    st.write("# Enter your Question.")
    query = st.text_input("Question")
    if st.button("Initiate the Chatbot"):
        x = initiate_chat(query)
        st.write(x)

button_col1, button_col2 = st.columns([1, 1])

if button_col1.button("Go to previous Menu", key="prev_menu"):
    if selected_index == 0:
        st.write("Try Reset Button")
    else:
        selected_index -= 1
        st.session_state['selected_index'] = selected_index

if button_col2.button("Go to next Menu", key="next_menu"):
    if selected_index == 2:
        st.write("Try Reset Button")
    else:
        selected_index += 1
        st.session_state['selected_index'] = selected_index
