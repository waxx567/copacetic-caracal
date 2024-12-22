def main():
    
    """
    Main function to manage student records. It reads student data from a file,
    allows the user to add, view, or delete students, and then saves updated
    records back to the file. Provides a menu-driven interface for user interaction.
    """

    studentList = []

    try:
        infile = open("student_records.txt", "r")
        line = infile.readline()
        while line != "":
            student = line.strip().split(" - ")
            studentList.append({"firstName": student[0].split(" ")[0], "lastName": student[0].split(" ")[1], "course": student[1]})
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("File not found")
        studentList = []

    choice = 0

    while choice != 4:
        print("1. Add student")
        print("2. View all students")
        print("3. Delete student")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            firstName = input("Enter student's first name: ")
            lastName = input("Enter student's last name: ")
            course = input("Enter student's course: ")
            student = {"firstName": firstName, "lastName": lastName, "course": course}
            studentList.append(student)  
        elif choice == 2:
            for student in studentList:
                print(f"{student['firstName']} {student['lastName']} - {student['course']}")
        elif choice == 3:
            firstName = input("Enter student's first name: ")
            lastName = input("Enter student's last name: ")
            for student in studentList:
                if student["firstName"] == firstName and student["lastName"] == lastName:
                    studentList.remove(student)
                    print(f"{firstName} {lastName} deleted")
                    break
                else:
                    print(f"{firstName} {lastName} not found")
        elif choice == 4:
            print("Goodbye")
        else:
            print("Invalid choice")

    outfile = open("student_records.txt", "w")
    for student in studentList:
        outfile.write(f"{student['firstName']} {student['lastName']} - {student['course']}\n")
    outfile.close()


if __name__ == "__main__":
    main()