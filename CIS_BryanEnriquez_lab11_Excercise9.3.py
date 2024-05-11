import csv

def write_grades_to_csv(filename, student_data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_data)

def main():
    filename = 'grades.csv'

    print("Enter student information. Type 'done' to exit.")
    while True:
        first_name = input("Enter student's first name: ")
        if first_name.lower() == 'done':
            break
        last_name = input("Enter student's last name: ")
        exam1 = int(input("Enter exam 1 grade: "))
        exam2 = int(input("Enter exam 2 grade: "))
        exam3 = int(input("Enter exam 3 grade: "))

        student_data = [first_name, last_name, exam1, exam2, exam3]
        write_grades_to_csv(filename, student_data)

    print("Student information has been saved and stored to", filename)

if __name__ == "__main__":
    main()
