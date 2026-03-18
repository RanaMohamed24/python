import lab3 as fo

def main():
    fo.create_files()
    fo.show_students()
    fo.show_python_grades()

    student_id = input("Enter student ID: ")
    fo.show_student_details(student_id)

  


if __name__ == "__main__":
    main()