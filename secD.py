x = input('Сколько сейчас секунд? ')
try:
	x = int(x)
except ValueError:
	print('ошибка ввода данных')
	x = input('Сколько сейчас секунд? ')
	x = int(x)
if x>=3600:
	Hours = int(x/3600)
	Minutes = int(x%3600/60)
	Sec = int(x%60)
	print('Сейчас на часах:', Hours, 'часов', Minutes , 'минут ,',Sec ,'секунд ')
else:
	Hours = 0
	Minutes = int(x/60)
	Sec = int(x%60)
	print('Сейчас на часах:',Hours, 'часов',Minut)



