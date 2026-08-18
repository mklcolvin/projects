student_records = {}

def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
        return
    student_records[name] = {"age": age, "grades": set(), "courses": set(courses)}
    print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return
    student_records[name]["grades"].add(grade)
    print(f"Grade {grade} added for student '{name}'.") 

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    return course in student_records[name]["courses"]

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    grades = student_records[name]["grades"]
    if not grades:
        print(f"No grades available for student '{name}'.")
        return None
    average = sum(grades) / len(grades)
    return average

def list_students_by_course(course):
    if not any(course in info["courses"] for info in student_records.values()):
        return []
    enrolled_students = [name for name, info in student_records.items() if course in info["courses"]]
    return enrolled_students

def filter_top_students(threshold):
    top_students = []
    for name, info in student_records.items():
#        if threshold in info["grades"]:
        average_grade = calculate_average_grade(name)
        if average_grade is not None and average_grade >= threshold:
            top_students.append(name)
    return top_students 

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list