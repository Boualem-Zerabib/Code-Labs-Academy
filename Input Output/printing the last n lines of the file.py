file = open('./Input Output/Student_names.txt')
for i , line in enumerate(file):
    if i in range(10,16):
        print(line)