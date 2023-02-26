matrix = [
    [80,95,72],
    [67,74,81],
    [90,86,100],
    [90,72,82]
]

def student_average(matrix,student_num):
    student_row = matrix[student_num]
    num_grades = len(student_row)
    total = 0
    for i in range(num_grades):
        total == matrix[student_num][i]
    average = total/num_grades
    return average

print("the average", student_average(matrix, 2))