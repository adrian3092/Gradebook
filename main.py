import sys

# initialize dictionary to store student ids, grades from grades.txt
gradebook = {}


def read_grade_book(file):
    """
    This function reads the student ids, grades from grades.txt
    and stores the ids, grades in a dictionary called gradebook
    """
    with open(file, "r", encoding="UTF-8") as grades_file:
        for grades in grades_file:
            grades = grades.strip().split(",")
            # check if format is student id,grade, student id is six digits and grade is 3 digits
            if len(grades) == 2 and len(grades[0]) == 6 and len(grades[1].replace(".", "")) <= 4:
                try:
                    gradebook[int(grades[0])] = float(grades[1])
                except ValueError:
                    print(f"""
{file} is not in the expected format: Student ID,Grade
Example: 768654,89.5
Please verify the format of the file contents and re-run the program.
""")
                    sys.exit()
            else:
                print(f"""
{file} is not in the expected format: Student ID,Grade
Example: 768654,89.5
Please verify the format of the file contents and re-run the program.
""")
                sys.exit()
    return gradebook


def display_grade():
    """
    This function displays the grade book from the
    data in the gradebook dictionary
    """
    print("Student ID | Grade")
    for student_id, grade in gradebook.items():
        print(f"{student_id}       {grade}")


def highest_grade():
    """
    This function sorts the gradebook dictionary and displays the
    student id with the highest grade
    """
    sorted_grades = sorted(gradebook.items(), key=lambda x:x[1])
    return f"The student ID with the highest grade is {sorted_grades[-1][0]} with a grade of {sorted_grades[-1][1]}"


def add_newstudent(file):
    """
    This function adds a new student and their grade
    to the grade book
    """
    while True:
        # ask for student id, validate it can be converted to int, is equal to six digits and not in grade book
        try:
            student_id = int(input("Please enter the student's ID: "))
            if len(str(student_id)) != 6:
                print("The student ID should be six digits. Please try again.")
            elif student_id in gradebook:
                print(f"The student ID {student_id} already exists in the grade book. Please try again.")
            else:
                break
        except ValueError as error:
            error = str(error).split("'")[1]
            print(f"{error} is not a valid input. The student's ID should be six digits in length. Please try again.")
    while True:
        try:
            grade = float(input("Please enter the student's grade: "))
            break
        except ValueError as error:
            error = str(error).split("'")[1]
            print(f"{error} is not a valid input. Examples of a valid input are 67.1, 98.3, 100.0, etc. Please try again.")
    # add new student and their grade to grades.txt
    with open(file, "a", encoding="UTF-8") as grades_file:
        grades_file.write(f"\n{student_id},{grade}")


def update_grade(file):
    """
    This function will update the grade of a student
    that already exists in the grade book
    """
    while True:
        try:
            student_id = int(input("Please enter the student ID: "))
            if student_id not in gradebook:
                print(f"The student ID {student_id} does not exist in the grade book. Please try again.")
            else:
                old_grade = gradebook[student_id]
                break
        except ValueError as error:
            error = str(error).split("'")[1]
            print(f"{error} is not a valid input. The student's ID should be six digits in length. Please try again.")
    while True:
        try:
            new_grade = float(input("Please enter the student's grade: "))
            break
        except ValueError as error:
            error = str(error).split("'")[1]
            print(f"{error} is not a valid input. Examples of a valid input are 67.1, 98.3, 100.0, etc. Please try again.")
    # update grades.txt with the student's new grade
    search_text = f"{student_id},{old_grade}"
    replace_text = f"{student_id},{new_grade}"
    with open(file, "r", encoding="UTF-8") as grades_file:
        grades_data = grades_file.read()
        grades_data = grades_data.replace(search_text, replace_text)
    with open(file, "w", encoding="UTF-8") as grades_file:
        grades_file.write(grades_data)


def main():
    actions = []
    menu_options = [
        "Display the current grade book",
        "Display the student with the highest grade",
        "Add a new student to the grade book",
        "Update the grade for an existing student",
        "Quit"
    ]
    while True:
        file_path = input("Please enter the path to the file grades.txt: ")
        # verify if file exists and can be opened
        try:
            with open(file_path, encoding="UTF-8"):
                break
        except FileNotFoundError as error:
            error = str(error).split("'")[1]
            print(f"The file {error} could not be opened. Please try again.")
    while True:
        read_grade_book(file_path)
        actions.clear()
        counter = 1
        # dynamically build menu options
        for option in menu_options:
            actions.append(str(counter))
            print(f"[{counter}] {option}")
            counter += 1
        action = input("What action would you like to perform?\nPlease type the corresponding number: ")
        if action == actions[0]:
            print("\n")
            display_grade()
            print("\n")
        elif action == actions[1]:
            print("\n")
            print(highest_grade())
            print("\n")
        elif action == actions[2]:
            print("\n")
            add_newstudent(file_path)
            print("\n")
        elif action == actions[3]:
            print("\n")
            update_grade(file_path)
            print("\n")
        elif action not in actions:
            print("\n")
            print(f"{action} is not a valid option. Please select one of the options below:")
            print("\n")
        elif action == actions[-1]:
            break


if __name__ == '__main__':
    main()
