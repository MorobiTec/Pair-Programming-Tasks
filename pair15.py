student_tup = [('211101', 'David Doe', '010-123-1111'),
               ('211102', 'John Smith', '010-123-2222'),
               ('211103', 'Jane Carter', '010-123-3333')]
student_dic = {}
for stu in student_tup:
    student_dic[stu[0]] = [stu[1], stu[2]]
while True:
    print("Menu\n")
    print("1) Create Student\n")
    print("2) View Student\n")
    print("3) Update Student\n")
    print("4) Delete Student\n")
    print("5) View all Students\n")
    print("6) Exit the program\n")

    choice = int(input(" Enter your choice:\n"))
    if choice == 1:
        stu_id = input("Enter student ID number :\n")
        if stu_id in student_dic:
            print("Student already exist.")
        else:
            name = input("Enter name :")
            phone_num = input("Enter phone number :")
            student_dic[stu_id] = [name, phone_num]
            print("Student added.")
    elif choice == 2:
        search_id = input("Enter student ID number :\n")
        if search_id in student_dic:
            student_info = student_dic[search_id]
            print(search_id, "Student is", student_info[0], "and phone number is", student_info[1])
        else:
            print("Student ID not found.")
    elif choice == 3:
        stu_id = input("Enter student ID number :\n")
        if stu_id in student_dic:
            name = input("Enter new name :")
            phone_num = input("Enter new phone number :")
            if name:
                student_dic[stu_id][0] = name
            if phone_num:
                student_dic[stu_id][1] = phone_num
            print("Student updated.")
        else:
            print("Student ID not found.")
    elif choice == 4:
        stu_id = input("Enter student ID number :\n")
        if stu_id in student_dic:
            del student_dic[stu_id]
            print("Student Deleted.")
        else:
            print("Student ID not found.")
    elif choice == 5:
        if student_dic:
            print("All Students")
            for stu_id, details in student_dic.items():
                print(f"Student ID: {stu_id}, Name: {details[0]}, Phone Number: {details[1]}")
        else:
            print("No Students Found.")
    elif choice == 6:
        print("Program exit.")
        break
    else:
        print("Try again.")



















