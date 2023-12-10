'''
Created to make module folders faster for the classes I take
'''

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def create_folders(directory, folder_base_name, num_folders):
    for i in range(1, num_folders + 1):
        folder_name = f"{folder_base_name} {str(i).zfill(2)}"
        folder_path = os.path.join(directory, folder_name)

        # check if folder exists and is not empty
        if os.path.exists(folder_path) and os.listdir(folder_path):
            response = messagebox.askyesno("Confirm Overwrite", 
                f"The folder '{folder_name}' already exists and is not empty. Do you want to overwrite it?")
            if response:
                try:
                    # delete and recreate folder
                    for file in os.listdir(folder_path):
                        file_path = os.path.join(folder_path, file)
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    os.makedirs(folder_path, exist_ok=True)
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")
                    return False
            else:
                # skip this folder
                continue  
        else:
            try:
                os.makedirs(folder_path, exist_ok=True)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                return False
    return True

def on_submit():
    directory = dir_entry.get()
    folder_base_name = name_entry.get().title()
    num_folders = int(count_entry.get())

    if create_folders(directory, folder_base_name, num_folders):
        messagebox.showinfo("Success", "Folders created successfully")

def browse_directory():
    # clear the existing content
    dir_entry.delete(0, tk.END)  
    directory = filedialog.askdirectory()
    # only insert if a directory was selected
    if directory:  
        dir_entry.insert(0, directory)

def open_directory_dialog():
    # clear the existing content
    dir_entry.delete(0, tk.END)  
    directory = filedialog.askdirectory()
    # only insert if a directory was selected
    if directory:  
        dir_entry.insert(0, directory)

def clear_entries():
    dir_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    count_entry.delete(0, tk.END)

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

# GUI
root = tk.Tk()
root.title("New Folder Creator")

# sets the window size and locks it from being adjusted by user
root.geometry("475x140")  
root.resizable(False, False)

tk.Label(root, text="Directory:").grid(row=0, column=0, sticky="w")
dir_entry = tk.Entry(root, width=50)
dir_entry.grid(row=0, column=1)
# binds left mouse click to open directory dialog
dir_entry.bind("<Button-1>", lambda event: open_directory_dialog())  
browse_button = tk.Button(root, text="Browse", command=open_directory_dialog)
browse_button.grid(row=0, column=2)

# folder base name
tk.Label(root, text="Folder Base Name:").grid(row=1, column=0, sticky="w")
name_entry = tk.Entry(root, width=50)
name_entry.grid(row=1, column=1)
# binds Enter key to tab to next widget
name_entry.bind("<Return>", focus_next_widget)  

# number of folders row
tk.Label(root, text="Number of Folders:").grid(row=2, column=0, sticky="w")
count_entry = tk.Entry(root, width=50)
count_entry.grid(row=2, column=1)
# binds enter key to submit
count_entry.bind("<Return>", lambda event: on_submit())  

# buttons row
submit_button = tk.Button(root, text="Create Folders", command=on_submit)
submit_button.grid(row=3, column=1, sticky="e")
clear_button = tk.Button(root, text="Clear Entries", command=clear_entries)
clear_button.grid(row=3, column=1, sticky="w")

# disclaimer
disclaimer = tk.Label(root, text="Created by Joshua Baca, Dec. 2023", fg="grey")
disclaimer.grid(row=4, column=0, columnspan=3, sticky="w")

root.mainloop()

'''
Joshua Baca
'''