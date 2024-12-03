"""import math 
print(dir(math))
print('Paper Coding Q1')
print()

student_tup = (
    ('211101', 'David Doe', '010-1234-4500'),
    ('211102', ' John Smith', '010-2230-6540'),
    ('211103', ' Jane Carter', '010-3232-7788'),
)
student_dic = {}
for student in student_tup:
    student_dic[student[0]] = [student[1], student[2]]

print(student_dic)
for key, value in student_dic.items():
    print("{ " + '{} : {}'.format(key, value) + " }")

print('*******************')
print('Paper Coding Q2')
print()
student_tup = (
    ('211101', 'David Doe', '010-1234-4500'),
    ('211102', ' John Smith', '010-2230-6540'),
    ('211103', ' Jane Carter', '010-3232-7788'),
)
student_dic = {}
for student in student_tup:
    student_dic[student[0]] = [student[1], student[2]]
search_id = input('Enter student ID: ')
if search_id in student_dic:
    student_details = student_dic[search_id]
    print('Name:', student_details[0])
    print('Phone Number:', student_details[1])
else :
    print('Student not found!')

"""

print('*******************')
print('Pair Programming Q1')
# Define the list of tuples
student_tup = (
    ('211101', 'David Doe', '010-123-1111'),
    ('211102', 'John Smith', '010-123-2222'),
    ('211103', 'Jane Carter', '010-123-3333')
)

# Convert list of tuples into a dictionary
student_dic = {}
for student in student_tup:
    student_dic[student[0]] = [student[1], student[2]]

# Main program loop
while True:
    print("\nMenu")
    print("1. Create student")
    print("2. Read student")
    print("3. Update student")
    print("4. Delete student")
    print("5. View all students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        student_id = input("Enter student ID: ")
        if student_id in student_dic:
            print("Student ID already exists.")
        else:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            student_dic[student_id] = [name, phone]
            print("Student added successfully.")
    
    elif choice == 2:
        student_id = input("Enter student ID: ")
        if student_id in student_dic:
            student_info = student_dic[student_id]
            print(f'Student ID: {student_id}, Name: {student_info[0]}, Phone Number: {student_info[1]}')
        else:
            print("Student ID not found.")
    
    elif choice == 3:
        student_id = input("Enter student ID: ")
        if student_id in student_dic:
            name = input("Enter new name (leave blank if no change): ")
            phone = input("Enter new phone number (leave blank if no change): ")
            if name:
                student_dic[student_id][0] = name
            if phone:
                student_dic[student_id][1] = phone
            print("Student updated successfully.")
        else:
            print("Student ID not found.")
    
    elif choice == 4:
        student_id = input("Enter student ID: ")
        if student_id in student_dic:
            del student_dic[student_id]
            print("Student deleted successfully.")
        else:
            print("Student ID not found.")
    
    elif choice == 5:
        if student_dic:
            print("All students:")
            for student_id, details in student_dic.items():
                print(f'Student ID: {student_id}, Name: {details[0]}, Phone Number: {details[1]}')
        else:
            print("No students found.")
    
    elif choice == 6:
        print("Program exited.")
        break
    
    else:
        print("Invalid choice. Please try again.")
