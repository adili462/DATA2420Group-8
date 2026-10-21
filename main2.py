from classes import PatientExam

# Task 2: read the csv file into a list of PatientExam objects
exams = []
file = open('data/patient_exams.csv', 'r')
lines = file.readlines()
file.close()
for line in lines[1:]:                                      # skip header row
    parts = line.strip().split(',')
    exams.append(PatientExam(int(parts[0]), parts[1], parts[2], int(parts[3]), float(parts[4])))

# Task 3: statistics
total = 0
month_counts = {}
for exam in exams:
    total = total + exam.get_BMI()
    month = exam.get_exam_month()
    if month in month_counts:
        month_counts[month] = month_counts[month] + 1
    else:
        month_counts[month] = 1
print('Average BMI:', round(total / len(exams), 2))

busiest = 0
for month in month_counts:
    if busiest == 0 or month_counts[month] > month_counts[busiest]:
        busiest = month
print('Busiest month:', busiest)
