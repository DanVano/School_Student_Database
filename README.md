# School_Student_Database
### About

This Python program is a comprehensive school database management system. It allows the Admin to manage and analyze the student directory. Key features include student search, class averages calculation, student management, database overview, and grade filtering. It’s a valuable tool for educational institutions, simplifying administrative tasks and providing insights into student performance. The program accepts a CSV file of student information and saves the database into an Excel file.

### How to use the program

pip install pandas and pip install openpyxl

Files main.py functions.py are required

In the same directory place the CSV student info database file (default: schools). Edit the function gather_student_info() at the top of main.py file to change the filename

Run the main.py file for the Main Menu GUI prompt

### Project Status

Core development completed.
Bug fixes development.

### Known Bugs

After the intial input pop-up box occurs the precending pop-ups dont load into focus. The following code is placed into each function --> root = tk.Tk(), root.withdraw(), root.destroy() and parent = root to bypass the issuse. A cleaner universial fix would be ideal.
 
dvanovcan@gmail.com
