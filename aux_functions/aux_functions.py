import os
import shutil

def clean_data_folder(proj_dir=r"C:\Users\pcraj\OneDrive\Desktop\projects\new_test"):
    try:
        # Get the current working directory
        


        # Define the folder name to clean
        folder_name = 'data'
        folder_name2 = 'aux_data'

        # Construct the full path to the folder
        folder_path = os.path.join(proj_dir, folder_name)

        # print(folder_name)

        # Check if the folder exists
        if os.path.exists(folder_path):
            try:
                # Delete the folder and its contents
                shutil.rmtree(folder_path)
                print(f"Successfully deleted the folder: {folder_path}")
            except OSError as e:
                print(f"Error: {folder_path} : {e.strerror}")
            except PermissionError:
                print(f"Permission error occurred while trying to delete contents of '{folder_name}'.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"The folder '{folder_path}' does not exist.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
clean_data_folder()
