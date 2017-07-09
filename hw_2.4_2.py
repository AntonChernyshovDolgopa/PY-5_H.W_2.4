import os, sys
import io

#поиск файлов расщирения sql
def find_sql_files():
	dirs = os.listdir ()
	files_sql = []
	for file in dirs:
		if file.endswith('.sql'):
			files_sql.append(file)
	return files_sql

#поиск файлов в которые входят указанные слова
def find_in_files():
	files_list = find_sql_files()
	key_word = None
	while key_word != 'exit':
		new_list = []
		key_word = input ()
		for file in files_list:
			with io.open(file) as f:
				for line in f:
					if key_word in line:
						new_list.append(file)
						if key_word == 'exit':
							break
		new_list_without_repeats = list(set(new_list))
		for element in new_list_without_repeats:
			print (element)
		print ('Всего:', len(new_list_without_repeats))
		files_list = new_list_without_repeats

find_in_files()
