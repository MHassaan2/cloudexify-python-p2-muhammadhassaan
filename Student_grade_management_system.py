import csv

students=[]
subjects=[
    "Maths",
    "Physics",
    "Computer",
    "Urdu",
    "English"
]
#---------------------Display Menu---------------------
def menu_display():
    print("""-------------------------------
Student Grade Management System
-------------------------------""")
    print("Menu:")
    print("1. Add Student")
    print("2. View Student")
    print("3. Class report & ranking")
    print("4. Search student")
    print("5. Update student")
    print("6. Delete student")
    print("7. Exit")
    print("--------------------------------")
    while True:
        try:
            choice=int(input("Select option(1-7):"))
            if choice<1 or choice>8:
                print("Invalid Input")
                continue
            else:
                return choice
        except ValueError:
            print("Invalid Input")

#----------------------ID-Generator---------------------
def id_generator():
    if len(students) == 0:
        return 1
    else:
        highest_ID = 0
        for student in students:
            if student['id'] > highest_ID:
                highest_ID = student['id']
        return highest_ID + 1
#----------------------Add-Student---------------------
def add_student():
    grades={}
    student_id=id_generator()
    while True:
        name = str(input("Enter student name:")).strip()
        if name =="":
            print("Name cannot be empty.")
            continue
        duplicate=False
        for student in students:
            if student['name'].lower()==name.lower():
                duplicate=True
                break
        if duplicate:
            print("Student name already exists.")
            continue
        else:
            break
    grade_list=[]
    for subject in subjects:
        while True:
            try:
                grade=int(input(f"Enter {subject} grade:"))
                if grade<0 or grade>100:
                    print('Enter grade between 0 and 100.')
                    continue
                grade_list.append(grade)
                break
            except ValueError:
                print("Invalid Input")
    grades=dict(zip(subjects,grade_list))
    average = sum(grades.values())/len(grades)
                    
    student={
        'id':student_id,
        'name':name,
        'grades':grades,
        'average' : average
    }
    students.append(student)
    save_csv()
    print("Student added successfully.")

#----------------------Grade-Letters---------------------
def grade_letter(grade):
    if grade >= 80:
        return "(A)"
    elif grade >= 70:
        return "(B)"
    elif grade >= 60:
        return "(C)"
    elif grade >= 50:
        return "(D)"
    else:
        return "(F)"

#----------------------View-Student---------------------
def view_student():
    if not students:
        print("No students found.")
        return
    print("-"*93)
    print(f'{"ID":<5}{"Name":<20}{"Maths":<10}{"Physics":<10}'
          f'{"Computer":<10}{"Urdu":<10}{"English":<10}{"Average":<10}{"Grade":<10}')
    print("-"*93)
    for student in students:
        print(f"{student['id']:<5}{student['name']:<20}{student['grades']['Maths']:<10}"
              f"{student['grades']['Physics']:<10}{student['grades']['Computer']:<10}"
              f"{student['grades']['Urdu']:<10}{student['grades']['English']:<10}"
              f"{student['average']:<10}{grade_letter(student['average']):<10}")
    print("-"*93)

#----------------------Update-Student---------------------
def update_student():
    print("---------- Update Student ----------")
    view_student()
    try:
        student=search_student()
        if student==None:
            return
        print("Select the field to update:")
        print("1. Name")
        print("2. Grades")
        print("3. Cancel")
        choice=int(input("Enter your choice(1-3):"))
        if choice==1:
            while True:
                new_name=str(input("Enter new name:")).strip()
                if new_name=="":
                    print("Name cannot be empty.")
                    continue
                duplicate=False
                for student in students:
                    if student['name'].lower()==new_name.lower():
                        duplicate=True
                        break
                if duplicate:
                        print("Student name already exists.")
                        continue
                else:
                    student['name']=new_name
                    save_csv()
                    print("Student name updated successfully.")
                    return
        if choice==2:
            new_grades={}
            for subject in subjects:
                while True:
                    try:
                        grade=int(input(f"Enter {subject} grade:"))
                        if grade<0 or grade>100:
                            print('Enter grade between 0 and 100.')
                            continue
                        new_grades[subject]=grade
                        break
                    except ValueError:
                        print("Invalid Input")
            average = sum(new_grades.values())/len(new_grades)
            student['grades']=new_grades
            student['average']=average
            save_csv()
            print("Student grades updated successfully.")
        if choice==3:
            return
    except ValueError:
        print("Invalid Input")

#----------------------Delete-Student---------------------                    
def delete_student():
    print("---------- Delete Student ----------")
    view_student()
    student = search_student()
    if student:
        students.remove(student)
        save_csv()
        print("Student deleted successfully.")

#----------------------Search-Student---------------------
def search_student():
    while True:
        try:
            print("---------- Search Student ----------")
            student_id=int(input("Enter student ID:"))
            break
        except ValueError:
            print("Invalid Input")
    for student in students:
        if student['id']==student_id:
            print(f"Name: {student['name']:<20}")
            for subject, grade in student['grades'].items():
                print(f"{subject}: {grade}")
            print(f"Average: {student['average']}")
            print(f"Grade: {grade_letter(student['average'])}")
            return student
    print("Student not found.")
    return None
    
#----------------------Save_to_CSV---------------------
def save_csv():
    with open('students.csv','w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(['ID','Name','Maths','Physics','Computer','Urdu','English','Average'])
        for student in students:
            row=[student['id'],student['name'],student['grades']['Maths'],student['grades']['Physics'],
                 student['grades']['Computer'],student['grades']['Urdu'],student['grades']['English'],
                 student['average']]
            writer.writerow(row)

#----------------------Load_CSV---------------------
def load_csv():
    try:
        with open("students.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for line in file:
                line = line
                if line == '':
                    continue
                parts = line.split(',')
                student = {
        "id": int(parts[0]),
        "name": parts[1],
        "grades": {
        "Maths": int(parts[2]),
        "Physics": int(parts[3]),
        "Computer": int(parts[4]),
        "Urdu": int(parts[5]),
        "English": int(parts[6])
    },
    "average": float(parts[7])
}
                students.append(student)
    except FileNotFoundError:
        print('No student data found. Starting fresh.')
    except Exception as e:
        print(f'Error occurred while loading data: {e}')

#----------------------Class-Report-and-Ranking---------------------
def class_report_and_ranking():
    if not students:
        print("No students found.")
        return
    print("--------------Ranking by Average--------------")
    print(f'{"Rank":<5}{"Name":<20}{"Average":<10}{"Grade":<10}')
    print("-"*46)
    sorted_student=sorted(students,key=lambda student:student['average'],reverse=True)
    for rank, student in enumerate(sorted_student,1):
        print(f"{rank:<5}. {student['name']:<20}: {student['average']:<10}{grade_letter(student['average']):<10}")
    print("-"*46)
    print("----------Class Report----------")
    class_average=sum(student['average'] for student in students)/len(students)
    print(f"Class Average: {class_average}")
    highest_average=max(student['average'] for student in students)
    lowest_average=min(student['average'] for student in students)
    print(f"Highest Average: {highest_average}{grade_letter(highest_average)}")
    print(f"Lowest Average: {lowest_average}{grade_letter(lowest_average)}")
    print("-"*32)



##----------------------Main-Function---------------------
def main():
    load_csv()
    while True:
        choice=menu_display()
        if choice==1:
            add_student()
        elif choice==2:
            view_student()
        elif choice==3:
            class_report_and_ranking()
        elif choice==4:
            search_student()
        elif choice==5:
            update_student()
        elif choice==6:
            delete_student()
        elif choice==7:
            save_csv()
            print("Exiting the program.")
            break
if __name__=="__main__":
    main()