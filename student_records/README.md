# Student Records Management System

## Overview
This Python application manages student records through a menu-driven interface. Users can add, view, and delete student records, with data persistence handled via a text file (`student_records.txt`).

## Features
- **Add Student:** Add a new student's first name, last name, and course.
- **View All Students:** Display all saved student records.
- **Delete Student:** Remove a student record by name.
- **Data Persistence:** Automatically saves and loads data from a text file.

## How It Works
1. When the application starts, it reads student records from `student_records.txt`. If the file does not exist, it initializes an empty list.
2. The main menu is displayed with the following options:
   - **1. Add Student**: Prompt the user to enter first name, last name, and course.
   - **2. View All Students**: Display all students in the format `FirstName LastName - Course`.
   - **3. Delete Student**: Prompt the user for the student's first and last name and remove the matching record.
   - **4. Quit**: Exit the application, saving all changes back to the text file.

## Requirements
- **Python Version:** Python 3.x

## How to Run
1. Clone or download the repository.
2. Ensure Python 3.x is installed.
3. Run the application using the following command:
   ```bash
   python3 main.py
   ```

## File Structure
- `main.py` - Main application file.
- `student_records.txt` - Data storage file (created automatically if missing).

## Example Interaction
```
1. Add student
2. View all students
3. Delete student
4. Quit

Enter your choice: 1
Enter student's first name: John
Enter student's last name: Doe
Enter student's course: Computer Science

1. Add student
2. View all students
3. Delete student
4. Quit

Enter your choice: 2
John Doe - Computer Science

Enter your choice: 4
Goodbye
```

## Notes
- Ensure correct file permissions for `student_records.txt`.
- The program expects correct input formats and does minimal input validation.

## License
This project is open-source and available under the MIT License.

