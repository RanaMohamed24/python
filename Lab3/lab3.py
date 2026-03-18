def create_files():
    try:
        with open("students.txt", "w") as f:
            f.write("1,Rana Mohamed\n")
            f.write("2,Salma yasser\n")
            f.write("3,Amira Samy\n")

        with open("grades.txt", "w") as f:
            f.write("1,Python,85\n")
            f.write("1,Math,90\n")
            f.write("2,Python,78\n")
            f.write("3,Math,88\n")

        print("Files created successfully!\n")

    except Exception as e:
        print("Error while creating files:", e)


def show_students():
    try:
        with open("students.txt", "r") as f:
            print("Student Names:")
            for line in f:
                data = line.strip().split(",")
                print(data[1])
        print()

    except FileNotFoundError:
        print("students.txt not found!\n")


def show_python_grades():
    try:
        with open("grades.txt", "r") as f:
            print("Python Grades:")
            for line in f:
                data = line.strip().split(",")
                if data[1] == "Python":
                    print(f"Student ID: {data[0]}, Grade: {data[2]}")
        print()

    except FileNotFoundError:
        print("grades.txt not found!\n")


def show_student_details(student_id):
    try:
        name = None

        with open("students.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == student_id:
                    name = data[1]
                    break

        if not name:
            print("Student not found!\n")
            return

        print("Name:", name)

        with open("grades.txt", "r") as f:
            print("Grades:")
            for line in f:
                data = line.strip().split(",")
                if data[0] == student_id:
                    print(f"{data[1]}: {data[2]}")
        print()

    except Exception as e:
        print("Error:", e)

