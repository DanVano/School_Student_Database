##This Python program serves as a comprehensive school database management system. It is designed to efficiently handle and manipulate student data. 
import tkinter as tk
import pandas as pd

from tkinter import messagebox, simpledialog
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

from functions import *

#Import the student information from a CSV file
def gather_student_info():
    with open('schools.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    schools_db = {row['ID']: {'Name': row['Name'], 'Birthday': row['Birthday'], 'Classes': json.loads(row['Classes'])} for row in data}
    return schools_db

schools_db = gather_student_info()

# The Main Menu choices for the User
def menu_selection(user_choice):
    result_text.delete(1.0, tk.END)
    if user_choice == 1:
        result = search_student(schools_db)
        if result == "Cancelled":
            return
    elif user_choice == 2:
        result = multiple_student_averages(schools_db)
    elif user_choice == 3:
        result = class_average(schools_db)
        if result == "Cancelled":
            return
    elif user_choice == 4:
        result = total_average(schools_db)
    elif user_choice == 5:
        result = new_student(schools_db)
        if result == "Cancelled":
            return
    elif user_choice == 6:
        result = delete_student(schools_db)
        if result == "Cancelled":
            return
    elif user_choice == 7:
        result = add_class_and_grade(schools_db)
        if result == "Cancelled":
            return
    elif user_choice == 8:
        result = students_greater_less_grade(schools_db)
        if result == "Cancelled":
            return
    elif user_choice == 9:
        result = print_all_students(schools_db)
    elif user_choice == 10:
        root.destroy()
        return
    else:
        result = 'Invalid choice. Please choose a valid option'
    result_text.insert(tk.END, f"{result}")

#The GUI for the Main Menu Options
root = tk.Tk()
root.title("Schools Student Database")
database_label = tk.Label(root, text="Student Database", font=("Arial", 22))
database_label.pack()
main_menu_label = tk.Label(root, text="Main Menu\n", font=("Arial", 18))
main_menu_label.pack()
menu_options = [
    "Search for an individual student",
    "Print the average of each student",
    "Print the average of a given class",
    "Print the total average of all the students in all the classes",
    "Add a student to the database",
    "Delete a student from the database",
    "Add a class and grade to a pre-existing student",
    "Print all students from a class with greater than or less than a grade (1-100)",
    "Print every student with their corresponding classes",
    "Save and Quit"
    ]
for i, option in enumerate(menu_options, start=1):
    tk.Button(root, text=f"{i}. {option}", command=lambda value=i: menu_selection(value)).pack()

# Print results in GUI
result_label = tk.Label(root, text="\nResults", font=("Arial", 12))
result_label.pack()
result_text = tk.Text(root, height=22, width=70)
result_text.pack()
root.mainloop()
    
save_excel(schools_db)
