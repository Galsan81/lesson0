grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
summ=sum(grades[0])/len(grades[0])
print(summ)
grades[0]=(sum(grades[0])/len(grades[0]))
grades[1]=(sum(grades[1])/len(grades[1]))
grades[2]=(sum(grades[2])/len(grades[2]))
grades[3]=(sum(grades[3])/len(grades[3]))
grades[4]=sum(grades[4])/len(grades[4])
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(grades), type(students))
students_list=list(students) # сделал из множества в список(пока не знаю зачем)
print(students_list)
sort_students=sorted(students) #упорядочивает множество students
print(sort_students)
slovar=dict()
slovar[sort_students[0]]=grades[0]
slovar[sort_students[1]]=grades[1]
slovar[sort_students[2]]=grades[2]
slovar[sort_students[3]]=grades[3]
slovar[sort_students[4]]=grades[4]
print(slovar) # ручная работа, наверное проще можно сделать
