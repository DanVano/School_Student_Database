##This Python program serves as a comprehensive school database management system. It is designed to efficiently handle and manipulate student data. 

from schoolsdatabase import schools_db

#Import the schools_db from a csv file or delete the above code and use the schools_db found below

#schools_db = {'ID0001': {'Name': 'John Doe', 'Birthday': '2005-01-01', 'Classes': {'Math': 85, 'English': 90, 'Science': 95}},
#    'ID0002': {'Name': 'Jane Smith', 'Birthday': '2005-02-02', 'Classes': {'Math': 90, 'English': 85, 'Science': 88}},
#    'ID0003': {'Name': 'Alice Cooper', 'Birthday': '1960-04-05', 'Classes': {'Math': 85, 'English': 78, 'Science': 92}},
#    'ID0004': {'Name': 'Bob Barker', 'Birthday': '1970-08-21', 'Classes': {'Math': 79, 'English': 95, 'Science': 88}},
#    'ID0006': {'Name': 'Charlie Richardson', 'Birthday': '2006-11-28', 'Classes': {'Math': 82, 'English': 98, 'Science': 94}},
#    'ID0007': {'Name': 'Nikhil Kwell', 'Birthday': '2002-06-22', 'Classes': {'Math': 90, 'English': 82, 'Science': 92}},
#    'ID0008': {'Name': 'Chris Tran', 'Birthday': '1992-09-05', 'Classes': {'Math': 81, 'English': 94, 'Science': 86}},
#    'ID0009': {'Name': 'Tim Tech', 'Birthday': '2001-06-30', 'Classes': {'English': 76, 'Physical Education': 20, 'History': 89, 'Comp Sci': 99}}, 
#    'ID0010': {'Name': 'Bob Marley', 'Birthday': '2005-03-03', 'Classes': {'Math': 88, 'English': 92, 'Science': 85}}
#            }

#Sort the student database by ID
schools_db = dict(sorted(schools_db.items()))

#Calculate the average grade of a student.
def student_average(student_db, student_id):
    grades = student_db[student_id]['Classes'].values()
    return round(sum(grades) / len(grades), 2)

def multiple_student_averages(schools_db):
    print('The GPA of each student given below')
    for student_id, student_info in schools_db.items():
        total = 0
        num_classes = 0
        for class_name, grade in student_info['Classes'].items():
            total += grade
            num_classes += 1
        average = total / num_classes
        print(f"{student_info['Name']} (ID: {student_id[2:]}) has an average grade of {average:.2f}")

#Calculate the average grade of a class.
def class_average(schools_db):
    total = 0
    count = 0
    class_input = input('Which class would you like the average of? (ex: Math): ')
    for student in schools_db.values():
        if class_input in student['Classes']:
            total += student['Classes'][class_input]
            count += 1
    avg = round((total / count), 2)
    print(f"The total average of the students in {class_input} is {avg}")

#Calculate the average grade of all students and all classes.
def total_average(schools_db):
    total = 0
    count = 0
    for student in schools_db.values():
        for grade in student['Classes'].values():
            total += grade
            count += 1
    avg = round((total / count), 2)
    print(f'The Total Average of all students in all classes is {avg}')

# Print all students from a class with >= grade (is grade between 1-100)
def students_with_grade(schools_db):
    while True:
        class_name = input("Please enter the class name (ex. 'Math' to search or 'done' to finish): ")
        if class_name.lower() == 'done':
            break
        min_grade = int(input("Please enter the minimum grade (1-100): "))
        for student_id, student_info in schools_db.items():
            if class_name in student_info['Classes'] and student_info['Classes'][class_name] >= min_grade:
                print(f"{student_info['Name']} has a grade equal to or above {min_grade} with {student_info['Classes'][class_name]} in {class_name}")

# Generate a unique ID for a new student.
# ID0005, ID0012, ID0025 and ID0026 are not used in the orginal DB. New students will be given those first
def generate_unique_id(schools_db):
    highest_id = max(schools_db.keys())
    highest_number = int(highest_id[2:])
    new_number = highest_number + 1
    new_id = 'ID' + str(new_number).zfill(4)
    return new_id

# Input a new student with classes and grades
def add_new_student(schools_db):
    print("Add a student to the school's database")
    new_id = generate_unique_id(schools_db)
    new_name = input("Please enter the new student's name: ")
    new_student_birthday = input("Please enter the new student's birthday (YYYY-MM-DD): ")
    if ' ' in new_student_birthday:
            new_student_birthday = '-'.join(new_student_birthday.split())
    if len(new_student_birthday) == 8:
            new_student_birthday = new_student_birthday[:4] + "-" + new_student_birthday[4:6] + "-" + new_student_birthday[6:]
    new_classes = {}
    while True:
        new_class = input("Please enter a class for the new student (or 'done' to finish): ")
        if new_class.lower() == 'done':
            break
        new_grade = int(input(f"Please enter the new student's grade for {new_class}: "))
        new_classes[new_class] = new_grade
    schools_db[new_id] = {'Name': new_name, 'Birthday': new_birthday, 'Classes': new_classes}
    
# Delete an existing student
def delete_student(schools_db):
    student_id = input("Please enter the ID of the student to delete: ")
    if not student_id.startswith('ID'):
        student_id = 'ID' + student_id
    if student_id in schools_db:
        del schools_db[student_id]
        print(f"Student {student_id} has been deleted.")
    else:
        print("No student found with this ID.")
        
# Add a class and grade to a pre-existing student    
def add_class_and_grade(schools_db):
    student_id = input("Enter the student ID you would like to add a class and grade: ")
    if not student_id.startswith('ID'):
        student_id = 'ID' + student_id
    if student_id not in schools_db:
        print("Student ID not found in the database.")
        return
    class_name = input("Enter the class name: ")
    while True:
        try:
            grade = int(input("Enter the grade (0-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")   
    schools_db[student_id]['Classes'][class_name] = grade
    print(f"Added {class_name} with grade {grade} to {schools_db[student_id]['Name']}'s record.")


#########################################################################

#Prints an individual students main Info 
def print_student_info(student_info):
    print(f"Name: {student_info['Name']}")
    print(f"Birthday: {student_info['Birthday']}")
    print("Classes:")
    for class_name, grade in student_info['Classes'].items():
        print(f"- {class_name}: {grade}")   
        
#Prints all students info in the database        
def print_all_students(schools_db):
    print('Print each student with their corresponding classes')
    for student_id, student_info in schools_db.items():
        print('-' * 70)
        print(f'ID: {student_id}')
        print_student_info(student_info)
        print('Avg', student_average(schools_db, student_id))
        print()

#Search for an individual student
def search_student(schools_db):
    print('Individual student search')
    search_by_id = input('Do you want to search by ID? (Yes/No) ')
    if search_by_id.lower() == 'yes':
        student_id = input("Please enter the student's ID: ")
        if not student_id.startswith('ID'):
            student_id = 'ID' + student_id
        if student_id in schools_db:
            print_student_info(schools_db[student_id])
        else:
            print('No student found with this ID.')
    else:
        student_name = input("Please enter the student's name: ")
        student_birthday = input("Please enter the student's birthday (YYYY-MM-DD): ")
        if ' ' in student_birthday:
            student_birthday = '-'.join(student_birthday.split())
        if len(student_birthday) == 8:
            student_birthday = student_birthday[:4] + "-" + student_birthday[4:6] + "-" + student_birthday[6:]
        found_students = [info for info in schools_db.values() if info['Name'] == student_name and info['Birthday'] == student_birthday]
        if found_students:
            for student in found_students:
                print(student)
        else:
            print("No student found with this name and birthday.")

#Main Menu
def print_menu():
    print('-' * 70)
    print('1. Search for an individual student')
    print('2. Print the average of each student')
    print('3. Print the average of a given class')
    print('4. Print the total average of all the students in all the classes')
    print('5. Add a student to the database')
    print('6. Delete a student from the database')
    print('7. Add a class and grade to a pre-existing student')
    print('8. Print all students from a class with >= grade (1-100)')
    print('9. Print every student with their corresponding classes')
    print('10. Quit')
    print()

def main_menu(schools_db):
    while True:
        print_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            search_student(schools_db)
        elif choice == '2':
            multiple_student_averages(schools_db)
        elif choice == '3':
            class_average(schools_db)
        elif choice == '4':
            total_average(schools_db)
        elif choice == '5':
            add_new_student(schools_db)
        elif choice == '6':
            delete_student(schools_db)
        elif choice == '7':
            add_class_and_grade(schools_db)   
        elif choice == '8':
            students_with_grade(schools_db)
        elif choice == '9':
            print_all_students(schools_db)
        elif choice == "10":
            print("Quitting the program...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
        print()

print('Welcome to the Student information database')
print()
main_menu(schools_db)
