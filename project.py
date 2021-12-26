import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import csv
import math

splash_root = tk.Tk()
splash_root.title("Splash Screen")
splash_root.geometry("300x300")
splash_label = tk.Label(splash_root, text="Welcome !", font='times 20 bold')
splash_label.pack(pady=100)

data_header = None
data_rows = None


def read_data():
    file_name = simpledialog.askstring("Input", "What is file name?", parent=main_root)
    if file_name is not None:
        try:
            file = open(file_name)
            csvreader = csv.reader(file)
            global data_header
            global data_rows
            data_header = next(csvreader)
            data_rows = []
            for row in csvreader:
                data_rows.append(row)
            file.close()
            messagebox.showinfo("Successful", "The data has been read successfully")
        except:
            messagebox.showerror("Error", "File is not exist.")


def compute_show_grade():
    if data_header is not None and data_rows is not None:
        data_header.append('grade')
        for row in data_rows:
            score = int(row[3])
            if 100 >= score >= 90:
                row.append('A')
            elif 90 > score >= 75:
                row.append('B')
            elif 75 > score >= 60:
                row.append('C')
            elif 60 > score >= 50:
                row.append('D')
            else:
                row.append('F')
        table_screen(data_header, data_rows)
    else:
        messagebox.showerror("Error", "Read data first and try again.")


def calc_mean(num_list):
    return sum(num_list) / len(num_list)


def calc_variance(num_list):
    mean = calc_mean(num_list)
    x_from_mean = 0
    for x in num_list:
        x_from_mean += math.pow((x - mean), 2)
    return x_from_mean / (len(num_list) - 1)


def descriptive_statistics():
    if data_header is not None and data_rows is not None:
        hours = []
        scores = []
        for row in data_rows:
            hours.append(int(row[2]))
            scores.append(int(row[3]))
        messagebox.showinfo("Hours Statistics",
                            f"\tMean = {calc_mean(hours).__round__(2)} \n\tStandard Deviation= {math.sqrt(calc_variance(hours)).__round__(2)}\n\tVariance= {calc_variance(hours).__round__(2)}")
        messagebox.showinfo("Score Statistics",
                            f"\tMean = {calc_mean(scores).__round__(2)} \n\tStandard Deviation= {math.sqrt(calc_variance(scores)).__round__(2)}\n\tVariance= {calc_variance(scores).__round__(2)}")
    else:
        messagebox.showerror("Error", "Read data first and try again.")


def sum_multiple_2_list(list1, list2):
    _sum = 0
    for i, val in enumerate(list1):
        _sum += list1[i] * list2[i]
    return _sum


def estimate_coef(x, y):
    n = len(x)
    mean_x = calc_mean(x)
    mean_y = calc_mean(y)

    # calculating cross-deviation and deviation about x
    ss_xy = sum_multiple_2_list(y, x) - n * mean_y * mean_x
    ss_xx = sum_multiple_2_list(x, x) - n * mean_x * mean_x

    # calculating regression coefficients
    b1 = ss_xy / ss_xx
    b0 = mean_y - b1 * mean_x

    return (b0, b1)


def regression_analysis():
    if data_header is not None and data_rows is not None:
        hours = []
        scores = []
        for row in data_rows:
            hours.append(int(row[2]))
            scores.append(int(row[3]))
        b0, b1 = estimate_coef(hours, scores)
        messagebox.showinfo("The Regression Equation", f"Y = {b0.__round__(3)} + {b1.__round__(3)} X")
    else:
        messagebox.showerror("Error", "Read data first and try again.")


def prediction():
    if data_header is not None and data_rows is not None:
        hours = []
        scores = []
        for row in data_rows:
            hours.append(int(row[2]))
            scores.append(int(row[3]))
        b0, b1 = estimate_coef(hours, scores)
        num_hours = simpledialog.askfloat("Predict Score", "What is the number of hours", parent=main_root)
        if num_hours is not None:
            predict_score = b0 + b1 * num_hours
            messagebox.showinfo("Predict Score", f"The Predict Score is: {predict_score.__round__(1)}")
    else:
        messagebox.showerror("Error", "Read data first and try again.")


def search_by_name():
    if data_header is not None and data_rows is not None:
        name = simpledialog.askstring("Search", "Enter the student name", parent=main_root)
        if name is not None:
            result_search = []
            for row in data_rows:
                if name.lower() in row[1].lower():
                    result_search.append(row)
            if len(result_search) > 0:
                table_screen(data_header, result_search)
            else:
                messagebox.showinfo("Result", "No data with this name")
    else:
        messagebox.showerror("Error", "Read data first and try again.")


def table_screen(tree_header, tree_rows):
    if tree_header is not None and tree_rows is not None:
        tree_root = tk.Tk()
        tree_root.title('Data Viewer')
        tree_root.geometry('500x500')
        tree_view = ttk.Treeview(tree_root, selectmode='browse')
        tree_view.pack(expand=tk.YES, fill=tk.BOTH, side='left')

        vsb = ttk.Scrollbar(tree_root, orient="vertical", command=tree_view.yview)
        vsb.pack(side='right', fill='y')
        tree_view.configure(yscrollcommand=vsb.set)

        tree_view['columns'] = tree_header  # ['ID', 'Name', 'Hours', 'Score']
        tree_view.column("#0", width=0, stretch=tk.NO)
        tree_view.heading("#0", text="", anchor=tk.CENTER)

        for x in tree_header:
            tree_view.column(x, anchor=tk.CENTER, width=80)
            tree_view.heading(x, text=x, anchor=tk.CENTER)

        for x in tree_rows:
            tree_view.insert(parent='', index='end', iid=x[0], text='', values=x)

        tree_root.mainloop()
    else:
        messagebox.showerror("Error", "Read data first and try again.")


def exit_():
    messagebox.showinfo("Good Bye", "Good Bye..")
    main_root.quit()


def main_screen():
    splash_root.destroy()
    global main_root
    global data_header
    global data_rows
    main_root = tk.Tk()
    main_root.title("Main Screen")
    main_root.geometry("400x400")
    tk.Label(main_root, text="Menu", font='times 16 bold').pack()
    tk.Button(main_root, text="Read Data", bg="#e0e0e0", command=read_data).pack(fill=tk.X, padx=20, pady=10)
    tk.Button(main_root, text="List Data", bg="#e0e0e0", command=lambda: table_screen(data_header, data_rows)).pack(
        fill=tk.X, padx=20,
        pady=10)
    tk.Button(main_root, text="Compute and Show Grades", bg="#e0e0e0", command=compute_show_grade).pack(fill=tk.X,
                                                                                                        padx=20,
                                                                                                        pady=10)
    tk.Button(main_root, text="Search by Name", bg="#e0e0e0", command=search_by_name).pack(fill=tk.X, padx=20, pady=10)
    tk.Button(main_root, text="Descriptive Statistics", bg="#e0e0e0", command=descriptive_statistics).pack(fill=tk.X,
                                                                                                           padx=20,
                                                                                                           pady=10)
    tk.Button(main_root, text="Regression Analysis", bg="#e0e0e0", command=regression_analysis).pack(fill=tk.X, padx=20,
                                                                                                     pady=10)
    tk.Button(main_root, text="Prediction", bg="#e0e0e0", command=prediction).pack(fill=tk.X, padx=20, pady=10)
    tk.Button(main_root, text="Exit", bg="#b86363", command=exit_).pack(fill=tk.X, padx=20, pady=10)


splash_root.after(100, main_screen)
tk.mainloop()
