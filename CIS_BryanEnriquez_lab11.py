def save_grades(filename, grades):
    with open(filename, 'w') as file:
        for grade in grades:
            file.write(str(grade) + '\n')
            

def main():
    filename = 'grades.txt'
    grades = []


    print("Enter your grades. Type 'done' when you want to quit.")
    while True:
        grade = input("Enter grade: ")
        if grade.lower() == 'done':
            break
        try:
            grade = float(grade)
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a grade or type 'done' to exit.")

    save_grades(filename, grades)
    print("your grades have been saved and stored to", filename)


if __name__ == "__main__":
    main()
