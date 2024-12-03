def get_user_input(prompt, input_type=str):
    """Gets user input with validation for strings and integers"""
    while True: 
        try: 
            value = input(prompt)
            if input_type == str:
                return value.strip()
            elif input_type == int:
                return int(value)
            else : 
                print('Input value unknown.')
        except ValueError:
            print('Invalid value. Re enter value')

def create_student(student_system):
    """create a new student record in the student_system dictionary"""
    student_id = get_user_input('Enter new student_id:')
    if student_id in student_system:
        print('Student already exists')
        return
    student_name = get_user_input('Enter student name:')
    student_surname = get_user_input('Enter student surname:')
    student_class = get_user_input('Enter student class:')
    student_grades = generate_course_grades()
    #student_fees = generate_fee()
    student_system[student_id] = {
        'name' : student_name,
        'surname' : student_surname,
        'class' : student_class,
        'course_grades' : student_grades,
        #'fees': student_fees
    }
    
def generate_course_grades():
    course_grades = {}
    while True:
        course_name = get_user_input('Enter course name:')
        score_str = input(f'Enter {course_name} score :')
        score = int(score_str)
        if 0 <= score <= 100 :
            course_grades[course_name] = score
        else: 
            print('Enter correct score!')
        return course_grades

def generate_fee():
    fees = {}
    pass

def read_student_info():
    pass

def update_student():
    pass

def highest_performer_student():
    pass

def display_students():
    pass 

def main_menu():
    while True:
        print('Student System Dashboard')
        print('1. Create Student')
        print('2. Read Student Info')
        print('3. Update Student')
        print('4. Find Highest Performing Student')
        print('5. Display All Student')
        print('6. Exit')
        
        choice = get_user_input('Enter your choice:', input_type=int)
        if choice == 1: 
            create_student(student_system)
        elif choice == 2: 
            read_student_info()
        elif choice == 3:
            update_student()
        elif choice == 4: 
            highest_performer_student()
        elif choice == 5: 
            display_students()
        else:
            print('Program Exit.')
            break

student_system ={}
main_menu()