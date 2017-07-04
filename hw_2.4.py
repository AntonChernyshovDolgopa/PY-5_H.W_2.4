import os
import io

os.chdir(r'C:\Python\Задание 10\Python_course-master (2)\Python_course-master\homework\2.3-paths\Migrations')
files_list = []
for name in os.listdir("."):
    if name.endswith(".sql"):
    	files_list.append(name)

list_with_word = []
word  = input ()
for file in files_list:
	with io.open(file) as f:
		for line in f:
			if word in line:
				list_with_word.append(file)
				
print (set(list_with_word))
