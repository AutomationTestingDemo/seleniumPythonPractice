data = 'All students are stupids'
f = open('student.txt', 'w')
f.write(data)
with open('student.txt', 'r+') as f:
	data= f.read()
	print(data)
	print('CurrentPosition of the cursor',f.tell())
	f.seek(17,0)
	print('CurrentPosition of the cursor',f.tell())
	f.write('Chutiyas')
	f.seek(0)
	data= f.read()
	print(data)