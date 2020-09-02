from exceptions import TableAlreadyCreated
import config


class TxtDB():

	def __init__(self,source = None):
		self.source = source

	def create_table(self,name,fields):
		if self.source != None:
			raise TableAlreadyCreated('Таблица была передана аргументом в класс!')
		fields = fields.split(' ')
		with open(f'{name}.txt','w',encoding='utf-8') as db:
			final_field = ''
			for field in fields:
				final_field += ' | ' + field
			final_field += '\n'
			for len_field in fields:
				for el in range(len(len_field) + len(fields)):
					final_field += '―'
			db.write(final_field)
		print('База была создана!')

	def execute():
		pass

		 


				

		


Db = TxtDB()
Db.create_table('xyi','id nick password')