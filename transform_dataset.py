def transform_dataset(data):
    # Your solution here
    
    for item in data:
        single_student_id = item['student_id']
        single_grades = item['grades']
        single_subjects = item['subjects']
        print("Name = {} : Grades = {} : Subjects = {}".format(item['student_id'], item['grades'], item['subjects']))

        
    # Step 1: Calculate average grade for each student and filter qualified students
    # (students with all grades above 70)
        total_of_grades = sum(single_grades)
        number_of_grades = len(single_grades)
        average_grade = total_of_grades / number_of_grades

    
    # Step 2: Create a summary of subjects taken by qualified students
    
    # Step 3: Return the final dictionary with qualified_students and subject_summary

input = [{"student_id": "S123", "grades": [88, 92, 85], "subjects": ["Math", "Science", "History"]}, {"student_id": "S124", "grades": [65, 95, 80], "subjects": ["Math", "Science", "English"]}, {"student_id": "S125", "grades": [91, 89, 92], "subjects": ["Math", "Physics", "History"]}]
transform_dataset(input)
