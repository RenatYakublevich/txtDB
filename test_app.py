from txtdb import TxtDB

db = TxtDB()

db.create_table('users.txt','user password')


print('Привет!\nЭто тестовое приложения на TxtDB\n')
login_menu = input('Вы хотите войти или зарегистрироваться?\n 1 - Войти\n 2 - Зарегистрироваться ')

if login_menu == '1':
	login = input('Ввдети логин ')
	password = input('Введите пароль ')

	if password == db.select_where('password','user',login)[0]:
		print('Вход успешно завершён!')

else:
	login = input('Введите логин ')
	password = input('Введите пароль ')
	db.insert([login,password])
	print('Регистрация прошла успешна!')
