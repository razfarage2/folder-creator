import os
import tkinter as tk
from tkinter import messagebox, filedialog
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from tkinter import ttk

def select_directory():
    selected_dir = filedialog.askdirectory()
    if selected_dir:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, selected_dir)

def create_entries():
    try:
        num_subfolders = int(num_entry.get().strip())

        # Clear existing subfolder entry fields
        for widget in frame.winfo_children():
            widget.destroy()

        # Create entry fields for subfolder names
        for i in range(num_subfolders):
            sub_label = ttk.Label(frame, text=f"Subfolder {i + 1}:")
            sub_label.grid(row=i, column=0, padx=5, pady=5)

            sub_entry = ttk.Entry(frame)
            sub_entry.grid(row=i, column=1, padx=5, pady=5)

        feedback_label.config(text=f"{num_subfolders} entry fields created!", foreground="green")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def create_folders():
    main_folder_name = main_entry.get().strip()
    base_path = path_entry.get().strip()

    if not base_path or not main_folder_name:
        messagebox.showerror("Error", "Both path and main folder name are required.")
        return

    # Create the main folder
    main_folder_path = os.path.join(base_path, main_folder_name)

    try:
        os.mkdir(main_folder_path)
        messagebox.showinfo("Success", f"Main folder '{main_folder_name}' created successfully!")

        # Create subfolders
        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Entry):
                subfolder_name = widget.get().strip()
                if subfolder_name:
                    os.mkdir(os.path.join(main_folder_path, subfolder_name))

        messagebox.showinfo("Success", "All subfolders created successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main application window setup
app = tk.Tk()
app.title("Folder Creator")
app.geometry("500x400")

# Apply a dark theme
style = Style(theme='darkly')  # You can choose 'darkly', 'cyborg', etc.

# Path label and entry
path_label = ttk.Label(app, text="Select Path:")
path_label.grid(row=0, column=0, pady=10, padx=5)

path_entry = ttk.Entry(app, width=30)
path_entry.grid(row=0, column=1, pady=10, padx=5)

select_button = ttk.Button(app, text="Select Directory", command=select_directory)
select_button.grid(row=0, column=2, pady=10, padx=5)

# Main folder name label and entry
main_label = ttk.Label(app, text="Main Folder Name:")
main_label.grid(row=1, column=0, pady=10, padx=5)

main_entry = ttk.Entry(app)
main_entry.grid(row=1, column=1, pady=10, padx=5)

# Number of subfolders label and entry
num_label = ttk.Label(app, text="Number of Subfolders:")
num_label.grid(row=2, column=0, pady=10, padx=5)

num_entry = ttk.Entry(app)
num_entry.grid(row=2, column=1, pady=10, padx=5)

# Button to create entry fields for subfolder names
create_entries_button = ttk.Button(app, text="Create Subfolder Entries", command=create_entries)
create_entries_button.grid(row=3, column=0, columnspan=3, pady=10)

# Frame for dynamic subfolder entry fields
frame = ttk.Frame(app)
frame.grid(row=4, column=0, columnspan=3, pady=10)

# Create folders button
create_folders_button = ttk.Button(app, text="Create Folders", command=create_folders)
create_folders_button.grid(row=5, column=0, columnspan=3, pady=10)

# Feedback label
feedback_label = ttk.Label(app, text="", font=("Arial", 12))
feedback_label.grid(row=6, column=0, columnspan=3, pady=10)

# Start the main loop
app.mainloop()
