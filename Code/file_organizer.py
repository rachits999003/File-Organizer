import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

#defining file categories
FILE_CATEGORIES = {
    "Images": [".jpg",".jpeg",".png","gif","bmp"],
    "Documents":[".pdf",".docx",".txt",".xlsx",".pptx"],
    "Videos":[".mp4",".mkv",".avi",".mov"],
    "Music": [".mp3",".wav",".flac"],
    "Archhives":[".zip",".rar",".tar",".gz",".7z"],
    "Code":[".html",".css",".js",".c",".cpp",".java",".py"],
    "Others":[]
}

def get_category(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_by_type(directory):
    if not os.path.exists(directory):
        messagebox.showerror("Error","Invalid Directory!")
        return
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            category = get_category(file_name)
            category_path = os.path.join(directory, category)
            os.makedirs(category_path, exist_ok=True)
            shutil.move(file_path, os.path.join(category_path, file_name))
            messagebox.showinfo("Success","Files have been sorted by type!")

def organize_by_date(directory):
    if not os.path.exists(directory):
        messagebox.showerror("Error","Invalid Directory!")
        return
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            mod_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")
            date_path = os.path.join(directory, date_folder)
            os.makedirs(date_path, exist_ok=True)
            shutil.move(file_path, os.path.join(date_path, file_name))
    messagebox.showinfo("Success","Files have been sorted by date!")

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        choice = sort_var.get()
        if choice == "Type":
            organize_by_type(folder)
        elif choice == "Date":
            organize_by_date(folder)
        else:
            messagebox.showerror("Error","Select a sorting option!")

# Create the main window
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x200")
root.resizable(False,False)

sort_var = tk.StringVar(value="Type")

# Create the widgets
label = tk.Label(root, text="Choose a sorting option:")
label.pack(pady=10)

type_button = tk.Radiobutton(root, text="By Type", variable=sort_var, value="Type")
type_button.pack()

date_button = tk.Radiobutton(root, text="By Date", variable=sort_var, value="Date")
date_button.pack()

browse_button = tk.Button(root, text="Select Folder", command=select_folder)
browse_button.pack(pady=20)

root.mainloop()