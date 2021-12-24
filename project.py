import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import pandas as pd

splash_root = tk.Tk()
splash_root.title("Splash Screen")
splash_root.geometry("300x300")
splash_label = tk.Label(splash_root, text="Welcome !", font='times 20 bold')
splash_label.pack(pady=100)


def read_data():
    file_name = simpledialog.askstring("Input", "What is file name?", parent=main_root)
    if file_name is not None:
        try:
            file = open(file_name + '.csv')
            csvreader = csv.reader(file)
            global header,rows
            header = next(csvreader)
            print(header)
            rows = []
            for row in csvreader:
                rows.append(row)
            print(rows)
            file.close()
            messagebox.showinfo("Successful", "The data has been read successfully")
        except:
            messagebox.showerror("Error", "File is not exist.")


def exit_():
    messagebox.showinfo("Good Bye", "Good Bye..")
    main_root.quit()


def main_screen():
    splash_root.destroy()
    global main_root
    main_root = tk.Tk()
    main_root.title("Main Screen")
    main_root.geometry("400x400")
    tk.Label(main_root, text="Menu", font='times 16 bold').pack()
    tk.Button(main_root, text="Read Data", bg="#e0e0e0", command=read_data).pack(fill=tk.X, padx=20, pady=10)
    tk.Button(main_root, text="List Data", bg="#e0e0e0").pack(fill=tk.X, padx=20, pady=10)
    tk.Button(main_root, text="Compute and Show Grades", bg="#e0e0e0").pack(fill=tk.X, padx=20, pady=10)
    tk.Button(main_root, text="Search by Name", bg="#e0e0e0").pack(fill=tk.X, padx=20, pady=10)
    tk.Button(main_root, text="Descriptive Statistics", bg="#e0e0e0").pack(fill=tk.X, padx=20, pady=10)
    tk.Button(main_root, text="Regression Analysis", bg="#e0e0e0").pack(fill=tk.X, padx=20, pady=10)
    tk.Button(main_root, text="Prediction", bg="#e0e0e0").pack(fill=tk.X, padx=20, pady=10)
    tk.Button(main_root, text="Exit", bg="#b86363", command=exit_).pack(fill=tk.X, padx=20, pady=10)


splash_root.after(100, main_screen)
tk.mainloop()
