def transform_dataset(data):
    # Your solution here

    from collections import Counter
    from itertools import chain

    qualified_students = {}  # Dictionary to store qualified students and their average grades
    qualified_subjects = []  # List to store subjects taken by qualified students

    for item in data:
        single_student_id = item['student_id']
        single_grades = item['grades']
        single_subjects = item['subjects']
 #       print("Name = {} : Grades = {} : Subjects = {}".format(item['student_id'], item['grades'], item['subjects']))

        
    # Step 1: Calculate average grade for each student and filter qualified students
    # (students with all grades above 70)
        total_of_grades = sum(single_grades)
        number_of_grades = len(single_grades)
        average_grade = total_of_grades / number_of_grades

        if average_grade > 70 and all(grade > 70 for grade in single_grades):  # Check if the average grade is above 70 and all grades are above 70
                qualified_students[single_student_id] = float("{:.2f}".format(average_grade))  # add the student id and average grade to the qualified_students dictionary

    # Step 2: Create a summary of subjects taken by qualified students

                qualified_subjects.append(single_subjects)

    subject_summary = dict(Counter(chain.from_iterable(qualified_subjects)))  # Count the occurrences of each subject in the qualified_subjects set
    
    # Step 3: Return the final dictionary with qualified_students and subject_summary

    return {
        "qualified_students": qualified_students,
        "subject_summary": subject_summary
    }

input = [{"student_id": "S123", "grades": [88, 92, 85], "subjects": ["Math", "Science", "History"]}, {"student_id": "S124", "grades": [65, 95, 80], "subjects": ["Math", "Science", "English"]}, {"student_id": "S125", "grades": [91, 89, 92], "subjects": ["Math", "Physics", "History"]}]
report =transform_dataset(input)


