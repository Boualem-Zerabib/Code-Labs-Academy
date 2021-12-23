file = open('./Input Output/Student_names.txt')
students = file.read()
file = open('./Input Output/Student_names.txt','w')
new_students = ["\nJeffery Garza", "\nAarron Markham", "\nKunal Lambert", "\nMusa Copeland", "\nKaylan Preston", "\nAntonia Quintero", "\nKacie Davey"]
for k in new_students:
    file.write(students)
print("the new list of student names after adding some random ones is:", students)

