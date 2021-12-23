
file = open('./Input Output/Student_names.txt')
students = file.read()
file = open('./Input Output/Student_names.txt','w')
students = students + "\nJeffery Garza" "\nAarron Markham" "\nKunal Lambert" "\nMusa Copeland" "\nKaylan Preston" "\nAntonia Quintero" "\nKacie Davey"
file.write(students)
print("the new list of student names after adding some random ones is:", students)

