'''Calculates the overall grade for a course with three equally weighted exams (graded out of 100) that account for 60% of the overall grade and four equally weighted programming assignments (graded out of 50) that account for 40% of the overall grade. Hint: The overall grade can be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.'''

exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))
prog1_grade = float(input('Enter score on Program 1 (out of 50):\n'))
prog2_grade = float(input('Enter score on Program 2 (out of 50):\n'))
prog3_grade = float(input('Enter score on Program 3 (out of 50):\n'))
prog4_grade = float(input('Enter score on Program 4 (out of 50):\n'))

averageExamScore = ((exam1_grade/100)+(exam2_grade/100)+(exam3_grade/100))/3*100
averageProgScore = ((prog1_grade/50)+(prog2_grade/50)+(prog3_grade/50)+(prog4_grade/50))/4*100

overall_grade = (averageExamScore * 0.6)+(averageProgScore * 0.4)

print('Your overall grade is:', overall_grade)
