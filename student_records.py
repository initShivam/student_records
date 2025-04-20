# This program keeps records of students' roll numbers, names, and marks.
# It then categorizes them based on their marks.

# Dictionary to store student data in the format: {roll_no: [name, marks]}
result = {}

# Ask user for the number of students
CHOICE = int(input("How many students are there? "))

# Collect data for each student
for i in range(CHOICE):
    print(f"\nEnter details for student No. {i + 1}")
    
    roll_no = int(input("Roll No: "))
    std_name = input("Student Name: ")
    
    # Validate marks input
    while True:
        try:
            marks = int(input("Marks (out of 100): "))
            if 0 <= marks <= 100:
                break
            else:
                print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Store data in the dictionary
    result[roll_no] = [std_name, marks]

# Print the full dictionary (raw data)
print("\nAll student records:")
print(result)

# Display categorized results
print("\n--- Result Summary ---")
for roll_no, data in result.items():
    name, marks = data

    if marks > 75:
        print(f"{name} scored more than 75 marks.")
    elif marks >= 35:
        print(f"{name} passed with more than 35 marks.")
    else:
        print(f"{name} has FAILED with less than 35 marks.")
