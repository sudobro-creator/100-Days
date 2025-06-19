# Simple Student Grade Management System
# This project allows a user to:
#     Add students and their scores
#     Calculate and store grades
#     View all students with their scores and grades
#     Exit the system

# Dictionary to store student data
students = {}

# Function to calculate grade
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Function to add a student
def add_student(name, score):
    grade = calculate_grade(score)
    students[name] = {"score": score, "grade": grade}
    print(f"{name} added with score {score} and grade {grade}.")

# Function to display all students
def display_students():
    if not students:
        print("No student data available.")
    else:
        print("\nStudent List:")
        for name, data in students.items():
            print(f"{name} - Score: {data['score']}, Grade: {data['grade']}")
        print()

# Main loop
while True:
    print("\n--- Student Grade Manager ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        score_input = input("Enter student score (0–100): ")
        
        if score_input.isdigit():
            score = int(score_input)
            if 0 <= score <= 100:
                add_student(name, score)
            else:
                print("Score must be between 0 and 100.")
        else:
            print("Invalid input. Please enter a number.") 
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")