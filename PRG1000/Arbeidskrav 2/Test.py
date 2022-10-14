student=open('student.txt','r')
test=student.readline()
while test!='':
    print(test.rstrip('\n'))
    test=student.readline()
student.close()
