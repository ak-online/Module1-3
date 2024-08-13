grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)

students_list = {}
students_list = dict(zip(students, grades))

students_list['Aaron'] = round(sum(grades[0])/len(grades[0]),2)
students_list['Bilbo'] = round(sum(grades[1])/len(grades[1]),2)
students_list['Johnny'] = round(sum(grades[2])/len(grades[2]),2)
students_list['Khendrik'] = round(sum(grades[3])/len(grades[3]),2)
students_list['Steve'] = round(sum(grades[4])/len(grades[4]),2)

print(students_list)



