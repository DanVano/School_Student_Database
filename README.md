# School Student Information Database Version 2
Program version 2.a     Python 3.12

### About

This Python program is a comprehensive school database management system. It allows the Admin to manage and analyze the student directory. Key features include student search, class averages calculation, student management, database overview, and grade filtering. It’s a valuable tool for educational institutions, simplifying administrative tasks and providing insights into student performance. The program accepts a CSV file of student information and saves the database into an Excel file.

### How to use the program

pip install pandas and pip install openpyxl

Files main.py, functions.py, and utilities.py are required. schools.csv can be found for a default database.

In the same directory place the CSV student info database file (default: schools). Edit the function gather_student_info() at the top of main.py file to change the filename

Run the main.py file for the Main Menu GUI prompt

the file grades.py is Version 1
### Project Status

Core development completed.
Bug fixes development.

### Known Bugs

After the intial input pop-up box occurs the precending pop-ups dont load into focus. The following code is placed into each function --> root = tk.Tk(), root.withdraw(), root.destroy() and parent = root to bypass the issuse. A cleaner universial fix would be ideal which would allow for better code readability

dvanovcan@gmail.com
