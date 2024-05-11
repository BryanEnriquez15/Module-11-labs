def read_grades_from_file(filename):
    with open(filename, 'r') as file:
        grades = [float(line.strip()) for line in file]
        return grades

def calculate_stats(grades):
    total = sum(grades)
    count = len(grades)
    average = total / count if count > 0 else 0
    return total, count, average

def main():
    filename = 'grades.txt'
    grades = read_grades_from_file(filename)

    if not grades:
        print("No grades found in the file.")
        return

    print("Individual grades:")
    for grade in grades:
        print(grade)

    total, count, average = calculate_stats(grades)

    print("\nTotal:", total)
    print("Count:", count)
    print("Average:", average)

if __name__ == "__main__":
    main()
