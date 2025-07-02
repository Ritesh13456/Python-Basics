students = []

def add_student():
    name = input("Enter student name: ")
    marks = []
    for i in range(5):
        mark = int(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)
    students.append([name] + marks)
    print("Student added successfully!\n")

def display_students():
    print("\nAll Student Records:")
    for student in students:
        print("Name:", student[0], "Marks:", student[1:])
    print()

def average_marks():
    print("\nAverage Marks of Students:")
    for student in students:
        total = sum(student[1:])
        avg = total / 5
        print(f"{student[0]} - Average: {avg:.2f}")
    print()

def find_topper():
    if not students:
        print("No students available.")
        return
    topper = students[0]
    highest_total = sum(topper[1:])
    for student in students[1:]:
        total = sum(student[1:])
        if total > highest_total:
            topper = student
            highest_total = total
    print(f"\nTopper: {topper[0]} with total marks {highest_total}\n")

def remove_student():
    name = input("Enter the name of the student to remove: ")
    found = False
    for student in students:
        if student[0].lower() == name.lower():
            students.remove(student)
            found = True
            print("Student removed successfully!\n")
            break
    if not found:
        print("Student not found.\n")

def main():
    while True:
        print("----- Student Marks Manager -----")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Show Average Marks")
        print("4. Show Topper")
        print("5. Remove Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            average_marks()
        elif choice == '4':
            find_topper()
        elif choice == '5':
            remove_student()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.\n")

# Start the program
main()
