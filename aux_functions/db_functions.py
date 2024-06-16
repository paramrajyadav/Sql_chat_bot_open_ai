import pandas as pd
import csv
import os
def read_query_from_file(proj_dir=r"C:\Users\pcraj\OneDrive\Desktop\projects\new_test"):
    file_path = 'aux_data/query.txt'
    file_name=os.path.join(proj_dir,file_path)
    try:
        with open(file_name, 'r') as file:
            CreateTable = file.read()
            return CreateTable
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    
def file_name_from_file(proj_dir=r"C:\Users\pcraj\OneDrive\Desktop\projects\new_test"):
    file_path = 'aux_data/file_name.txt'
    file_name=os.path.join(proj_dir,file_path)
    try:
        with open(file_name, 'r') as file:
            return file.read().strip()  # Remove leading/trailing whitespaces
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    

import sqlite3

def drop_sqlite_database():
    """
    Deletes the SQLite database file at the specified path.

    Parameters:
    db_path (str): Path to the SQLite database file.

    Returns:
    None
    """

    db_path = 'db.db'
    try:
        if os.path.exists(db_path):
            os.remove(db_path)
            print(f"Database at {db_path} has been deleted.")
        else:
            print(f"No database file found at {db_path}.")
    except Exception as e:
        print(f"An error occurred while deleting the database: {e}")



    


def setup_database(proj_dir=r"C:\Users\pcraj\OneDrive\Desktop\projects\new_test")):

    import sqlite3
    create_table_query=read_query_from_file(proj_dir)
    # create_table_query_2 =create_table_querry

    # print(create_table_query_2)
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()

    
    cursor.execute(str(create_table_query))
    connection.commit()
    connection.close()
   

import sqlite3
import csv

def import_csv(proj_dir=r"C:\Users\pcraj\OneDrive\Desktop\projects\new_test"):
    try:
        connection = sqlite3.connect('db.db')
        c = connection.cursor()
        
        file = file_name_from_file(proj_dir)  # Assuming this function is defined elsewhere
        print("File to be imported:", file)
        folder_name=os.path.join(proj_dir,"data")
        
        with open(f"{folder_name}/{file}.csv", 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            print("Opened CSV file")
            next(reader)  # Skip the header row if present
            
            # Dynamically determine the number of columns in the CSV
            first_row = next(reader)
            num_columns = len(first_row)
            placeholders = ','.join(['?'] * num_columns)
            
            # Re-insert the first row into the reader
            reader = csv.reader(f)
            next(reader)  # Skip the header row again
            
            for row in reader:
                print("Inserting row:", row)
                c.execute(f"INSERT INTO {file} VALUES ({placeholders})", row)
            
            connection.commit()
            print("Data imported successfully")
    except sqlite3.Error as e:
        print("SQLite error:", e)
    except Exception as e:
        print("Error:", e)
    finally:
        if connection:
            connection.close()
            print("Database connection closed")


    
        
    
if __name__ == "__main__":
    print("h1")
    print(file_name_from_file())
    print("h2")
    drop_sqlite_database()
    print("h3")
    setup_database()
    print("h4")
    import_csv()