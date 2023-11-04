import tkinter as tk

from tkinter import messagebox, simpledialog


# Generate a unique ID for a new student. ID0005, ID0012, ID0025 and ID0026 are not used in the orginal DB. New students will be given those first
def generate_unique_id(schools_db):
    new_number = 1
    while True:
        new_id = 'ID' + str(new_number).zfill(4)
        if new_id not in schools_db:
            return new_id
        new_number += 1

# Collects the classes within the database for the gui
def available_classes(schools_db):
    #all_classes = {}
    all_classes= set()
    for student in schools_db.values():
        all_classes.update(student['Classes'].keys())
    classes_gui = ', '.join(sorted(all_classes))
    return classes_gui       

# Prints out the total average of an inputted class
def class_average(schools_db):
    root = tk.Tk()
    root.withdraw()
    classes_gui = available_classes(schools_db)
    class_input = simpledialog.askstring("Input", "Which class would you like the average of? (ex: Math)\nAvailable classes: " + classes_gui, parent=root)
    if class_input is None:
        root.destroy()
        return "Cancelled"
    total_grades = sum(student['Classes'][class_input] for student in schools_db.values() if class_input in student['Classes'])
    num_students = sum(class_input in student['Classes'] for student in schools_db.values())
    avg = round((total_grades / num_students), 2)
    result = f"The total average of the students in {class_input} is {avg}%"
    root.destroy()
    return result
      
# Inputs a new student with corresponding classes and grades
def new_student(schools_db):
    root = tk.Tk()
    root.withdraw()
    new_id = generate_unique_id(schools_db)
    new_name = simpledialog.askstring("Input", "Please enter the new student's name: ", parent = root)
    if new_name is None:
        return "Cancelled"
    new_student_birthday = simpledialog.askstring("Input", "Please enter the new student's birthday (YYYY-MM-DD): ", parent = root)
    if new_student_birthday is None:
        return "Cancelled"
    if ' ' in new_student_birthday:
            new_student_birthday = '-'.join(new_student_birthday.split())
    if len(new_student_birthday) == 8:
            new_student_birthday = new_student_birthday[:4] + "-" + new_student_birthday[4:6] + "-" + new_student_birthday[6:]
    new_classes = {}
    while True:
        new_class = simpledialog.askstring("Input", "Please enter a class for the new student (or 'done' to finish): ", parent = root)
        if new_class.lower() == 'done':
            break
        new_grade = int(simpledialog.askstring("Input", f"Please enter the new student's grade for {new_class}: ", parent = root))
        new_classes[new_class] = new_grade
    schools_db[new_id] = {'Name': new_name, 'Birthday': new_student_birthday, 'Classes': new_classes}
    root.destroy()
    return "New student added"
    
# Deletes an existing student
def delete_student(schools_db):
    student_id = simpledialog.askstring("Input", "Please enter the ID of the student to delete: ")
    if student_id is None:
        return "Cancelled"
    if not student_id.startswith('ID'):
        student_id = 'ID' + student_id
    if student_id in schools_db:
        student_name = schools_db[student_id]['Name']
        del schools_db[student_id]
        return f"Student {student_id} has been deleted.\n{student_name}"
    return "No student found with this ID."

# Add a new class and grade to a selected student
def add_class_and_grade(schools_db):
    root = tk.Tk()
    root.withdraw()
    student_id = simpledialog.askstring("Input", "Enter the student ID you would like to add a class and grade: ", parent = root)
    if student_id is None:
        root.destroy()
        return "Cancelled"
    if not student_id.startswith('ID'):
        student_id = 'ID' + student_id
    if student_id not in schools_db:
        root.destroy()
        return "Student ID not found in the database."
    class_name = simpledialog.askstring("Input", "Enter the class name: ", parent = root)
    if class_name is None:
        root.destroy()
        return "Cancelled"
    while True:
        try:
            grade = int(simpledialog.askstring("Input", "Enter the grade (0-100): ", parent = root))
            if grade is None:
                root.destroy()
                return "Cancelled"
            if 0 <= grade <= 100:
                break
            else:
                return "Grade must be between 0 and 100. Please try again."
        except ValueError:
            return "Invalid input. Please enter a number."  
    schools_db[student_id]['Classes'][class_name] = grade
    result = f"Added {class_name} with grade {grade} to {schools_db[student_id]['Name']}'s record."
    root.destroy()
    return result

# Search for a student by ID or Name and Birthday
def search_student(schools_db):
    root = tk.Tk()
    root.withdraw()
    search_by_id = simpledialog.askstring("Input", "Do you want to search by ID? (Yes/No)", parent = root)
    if search_by_id is None:
        return "Cancelled"
    if search_by_id.lower() == 'yes':
        student_id = simpledialog.askstring("Input", "Please enter the student's ID:", parent = root)
        if student_id is None:
            root.destroy()
            return "Cancelled"
        if not student_id.startswith('ID'):
            student_id = 'ID' + student_id
        if student_id in schools_db:
            root.destroy()
            return print_student_info(schools_db[student_id])
        root.destroy()
        return 'No student found with this ID.'
    else:
        student_name = simpledialog.askstring("Input", "Please enter the student's name:", parent = root)
        if student_name is None:
            root.destroy()
            return "Cancelled"
        student_birthday = simpledialog.askstring("Input", "Please enter the student's birthday (YYYY-MM-DD):", parent = root)
        if student_birthday is None:
            root.destroy()
            return "Cancelled"
        if ' ' in student_birthday:
            student_birthday = '-'.join(student_birthday.split())
        if len(student_birthday) == 8:
            student_birthday = student_birthday[:4] + "-" + student_birthday[4:6] + "-" + student_birthday[6:]
        found_students = [info for info in schools_db.values() if info['Name'] == student_name and info['Birthday'] == student_birthday]
        if found_students:
            root.destroy()
            return '\n'.join(print_student_info(student) for student in found_students)
        else:
            root.destroy()
            return "No student found with this name and birthday."
        
# Print all students from a class with >= grade (is grade between 1-100)
def students_greater_less_grade(schools_db):
    root = tk.Tk()
    root.withdraw()
    result = ''
    classes_gui = available_classes(schools_db)
    class_input = simpledialog.askstring("Input", "Which class would you like the average of? (ex: Math)\nAvailable classes: " + classes_gui, parent=root)
    if class_input is None:
        root.destroy()
        return "Cancelled"
    grade_operator = simpledialog.askstring("Input", "Please enter the grade operator (<= or >=): ", parent = root)
    grade = int(simpledialog.askstring("Input", f"Enter the grade {grade_operator} (0-100): ", parent = root))
    total_students = 0
    students_meeting_criteria = 0
    for student_id, student_info in schools_db.items():
        if class_input in student_info['Classes']:
            total_students += 1
            if (grade_operator == ">=" and student_info['Classes'][class_input] >= grade) or (grade_operator == "<=" and student_info['Classes'][class_input] <= grade):
                students_meeting_criteria += 1
                result += f"{student_info['Name']} grade is {student_info['Classes'][class_input]} in {class_input} which is {grade_operator} {grade}\n"
    percentage = round((students_meeting_criteria / total_students) * 100 if total_students > 0 else 0, 2)
    result += f"\n{percentage}% of students fit the criteria of {grade_operator} {grade} in {class_input}."
    root.destroy()
    return result

############################################################################
#Functions that do not require user inputs

# Prints an individual students main Info 
def print_student_info(student_info):
    result = f"Name: {student_info['Name']}\n"
    result += f"Birthday: {student_info['Birthday']}\n"
    result += "Classes:\n"
    for class_name, grade in student_info['Classes'].items():
        result += f"- {class_name}: {grade}\n"
    return result  
        
# Prints all students info in the database        
def print_all_students(schools_db):
    result = 'Print each student with their corresponding classes\n'
    schools_db = dict(sorted(schools_db.items()))
    for student_id, student_info in schools_db.items():
        result += '-' * 70 + '\n'
        result += f'ID: {student_id}\n'
        result += print_student_info(student_info)
        result += 'Avg: ' + str(student_average(schools_db, student_id)) + '\n'
    return result

#Calculate the average grade of all students and all classes.
def total_average(schools_db):
    total_grades = sum(grade for student in schools_db.values() for grade in student['Classes'].values())
    num_grades = sum(len(student['Classes']) for student in schools_db.values())
    avg = round((total_grades / num_grades), 2)
    result= f'The Total Average of all students in all classes is {avg}%'
    return result

# Calculate the average grade of a student.
def student_average(student_db, student_id):
    grades = student_db[student_id]['Classes'].values()
    average = round(sum(grades) / len(grades), 2)
    return average

def multiple_student_averages(schools_db):
    result = 'The GPA of each student given below\n'
    for student_id, student_info in schools_db.items():
        total_grades = sum(student_info['Classes'].values())
        num_classes = len(student_info['Classes'])
        average = total_grades / num_classes
        result += f"{student_info['Name']} (ID: {student_id[2:]}) GPA: {average:.2f}%\n"
    return result

