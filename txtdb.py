import os.path

from exceptions import TableAlreadyCreated
from exceptions import DatabaseFileAlreadyCreated
import config


class TxtDB():

	def __init__(self,source = None):
		self.source = source
		self.db_colums = []

		if source != None:
			with open(source,'r',encoding='utf-8') as file:
				colums = file.readlines(1)[0].split('|')[1::]

				for colum in colums:
					self.db_colums.append(colum[1:-1].replace('',''))
			self.count_colums = len(self.db_colums)


	def create_table(self,name,fields):
		if self.source != None:
			raise TableAlreadyCreated('Таблица была передана аргументом в класс!')
		
		self.source = name
		self.count_colums = len(fields.split(' '))
		
		if os.path.exists(name):
			return

		fields = fields.split(' ')
		with open(name,'w',encoding='utf-8') as db:
			final_field = ''
			for field in fields:
				final_field += ' | ' + field.replace('|','')
			final_field += '\n' + '―' * len(final_field)
			db.write(final_field)

		

	def insert(self,values : list):
		with open(self.source,'a',encoding="utf-8") as db:
			final_line = '\n'
			for element in values:
				final_line += ' | ' + str(element)
			db.write(final_line)

	def select_all(self,column):
		try:
			all_line_db = self.get_all_db()

			index_column = self.get_colums_db().index(column) + 1
			all_values = []

			for line in all_line_db:
				all_values.append(line.split('|')[index_column][1:-1])
			
			return all_values
			
		except ValueError:
			print('Такого столбца нет!')


	def select(self,**kwargs):
		select = kwargs['select']
		where = kwargs['where']

		with open(self.source,encoding='utf-8'):
			pass

	def get_count_colums(self):
		return self.count_colums

	def get_all_db(self):
		with open(self.source,encoding='utf-8') as all_line:
			return all_line.readlines()[2::]

	def get_colums_db(self):
		with open(self.source,encoding='utf-8') as line:
			all_colums = line.readline().replace(' ','').replace('\n','').split('|')
			return all_colums[1::]
		

		 


				

		


Db = TxtDB('users.txt')

print(Db.select_all('username'))





