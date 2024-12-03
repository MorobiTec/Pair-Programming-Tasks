def get_user_input(prompt, input_type=str):
    """Gets user input with validation for strings and integers."""
    while True:
        try:
            value = input(prompt)
            if input_type == str:
                return value.strip()  # Remove leading/trailing whitespace
            elif input_type == int:
                return int(value)
            else:
                print("Invalid input type specified.")
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def create_student(school_system):
    """Creates a new student entry in the school system dictionary."""
    student_id = get_user_input("Enter student ID: ")
    if student_id in school_system:
        print(f"Student with ID {student_id} already exists.")
        return
    student_name = get_user_input("Enter student name: ")
    student_surname = get_user_input("Enter student surname: ")
    student_class = get_user_input("Enter student class: ")
    course_grades = {}
    while True:
        course_name = get_user_input("Enter course name (or 'done' to finish): ")
        if course_name.lower() == "done":
            break
        scores = []
        while True:
            score_str = get_user_input(f"Enter score for {course_name} (or 'done' to finish): ")
            if score_str.lower() == "done":
                break
            try:
                score = int(score_str)
                if 0 <= score <= 100:
                    scores.append(score)
                else:
                    print("Invalid score. Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid score. Please enter an integer.")
        if scores:
            course_grades[course_name] = scores
    fees = get_user_input("Enter student fees: ", input_type=int)
    school_system[student_id] = {
        "name": student_name,
        "surname": student_surname,
        "class": student_class,
        "course_grades": course_grades,
        "fees": fees,
    }
    print(f"Student {student_name} {student_surname} added successfully.")

def read_student(school_system):
    """Reads student information based on student ID."""
    student_id = get_user_input("Enter student ID: ")
    if student_id not in school_system:
        print(f"Student with ID {student_id} not found.")
        return
    student = school_system[student_id]
    print(f"\nStudent ID: {student_id}")
    print(f"Name: {student['name']} {student['surname']}")
    print(f"Class: {student['class']}")
    print("Course Grades:")
    for course, scores in student["course_grades"].items():
        print(f"- {course}: {', '.join(str(score) for score in scores)}")
    print(f"Fees: {student['fees']}")

def update_student(school_system):
    """Updates student information based on student ID."""
    student_id = get_user_input("Enter student ID: ")
    if student_id not in school_system:
        print(f"Student with ID {student_id} not found.")
        return
    student = school_system[student_id]

    while True:
        print("\nUpdate Menu:")
        print("1. Update name")
        print("2. Update surname")
        print("3. Update class")
        print("4. Update course grades")
        print("5. Update fees")
        print("6. Go back")
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            new_name = get_user_input("Enter new name: ")
            student["name"] = new_name
            print(f"Name updated to {new_name}.")
        elif choice == "2":
            new_surname = get_user_input("Enter new surname: ")
            student["surname"] = new_surname
            print(f"Surname updated to {new_surname}.")
        elif choice == "3":
            new_class = get_user_input("Enter new class: ")
            student["class"] = new_class
            print(f"Class updated to {new_class}.")
        elif choice == "4":
            while True:
                course_name = get_user_input("Enter course name to update (or 'done' to finish): ")
                if course_name.lower() == "done":
                    break
                if course_name in student["course_grades"]:
                    scores = []
                    while True:
                        score_str = get_user_input(f"Enter new score for {course_name} (or 'done' to finish): ")
                        if score_str.lower() == "done":
                            break
                        try:
                            score = int(score_str)
                            if 0 <= score <= 100:
                                scores.append(score)
                            else:
                                print("Invalid score. Please enter a value between 0 and 100.")
                        except ValueError:
                            print("Invalid score. Please enter an integer.")
                    if scores:
                        student["course_grades"][course_name] = scores
                        print(f"Scores for {course_name} updated.")
                else:
                    print(f"Course {course_name} not found.")
        elif choice == "5":
            new_fees = get_user_input("Enter new fees: ", input_type=int)
            student["fees"] = new_fees
            print(f"Fees updated to {new_fees}.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def find_highest_performing_student(school_system):
    """Calculates the highest average score across all courses for a student
       in a different class than the provided student (if any).

       Args:
           school_system: The dictionary containing student information.

       Returns:
           A dictionary containing the information of the highest performing
           student in a different class, or None if no students are found
           in different classes.
    """

    if len(school_system) <= 1:
        return None  # Not enough students to compare across classes

    current_student_class = None
    highest_performer = None
    highest_average = 0.0

    for student_id, student_data in school_system.items():
        if current_student_class is None:
            current_student_class = student_data["class"]
            continue  # Skip the first iteration to avoid self-comparison

        if student_data["class"] != current_student_class:
            # Calculate average score for this student
            total_score = 0
            course_count = 0
            for course, scores in student_data["course_grades"].items():
                total_score += sum(scores)
                course_count += len(scores)
            if course_count > 0:
                average_score = total_score / course_count
                if average_score > highest_average:
                    highest_average = average_score
                    highest_performer = student_data

    return highest_performer

def display_all_students(school_system):
    """Displays all students without showing their course grades and fees."""
    print("\nAll Students:")
    for student_id, student in school_system.items():
        print(f"ID: {student_id}, Name: {student['name']} {student['surname']}, Class: {student['class']}")

def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        print("\nMain Menu:")
        print("1. Create student")
        print("2. Read student information")
        print("3. Update student information")
        print("4. Find highest performing student")
        print("5. Display all students")
        print("6. Exit")
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            create_student(school_system)
        elif choice == "2":
            read_student(school_system)
        elif choice == "3":
            update_student(school_system)
        elif choice == "4":
            highest_performer = find_highest_performing_student(school_system)
            if highest_performer:
                print(f"Highest Performing Student: {highest_performer['name']} {highest_performer['surname']} from class {highest_performer['class']}")
            else:
                print("No students found in different classes.")
        elif choice == "5":
            display_all_students(school_system)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main program execution
school_system = {}  # Empty dictionary to store student data
main_menu()
