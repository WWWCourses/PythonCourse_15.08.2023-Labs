# 3. Трябва да се напълни цистерна с вода. Имате 2 кофи с вместимост 2 и 3 литра
# и ги ползвате едновременно. Да се състави програма, която по въведен обем извежда
# как ще прелеете течността с тези кофи, т.е. по-колко пъти ще се пълни всяка от кофите.
# Входни данни: естествено число от интервала [10..9999].
# Използвайте проверка на логическо условие - оператор if.
# Пример: 107 Изход: 21 пъти 2-те кофи, допълнително кофа от 2 литра

bucket1_volume = 2
bucket2_volume = 3
both_bucket_volume = bucket1_volume + bucket2_volume

bucket1_count = 0
bucket2_count = 0

target_volume = 16


fill_count_both = target_volume//both_bucket_volume
reminder = target_volume%both_bucket_volume

if reminder == 0:
	 print(f'{fill_count_both} пъти 2-те кофи')
elif reminder<bucket1_volume:
	# не може да прелеем остатъка =намаляваме курсовете
	fill_count_both -= 1
	reminder = target_volume-(fill_count_both*both_bucket_volume)


print(f'fill_count_both: {fill_count_both}, reminder: {reminder}')
# exit()
while reminder:
	print(f'reminder = {reminder}')
	if reminder%bucket2_volume==0:
		bucket2_count=reminder//bucket2_volume
		break
	elif reminder%bucket1_volume==0:
		bucket1_count=reminder//bucket1_volume
		break
	else:
		reminder = reminder%bucket2_volume



print(f'''{fill_count_both} пъти 2-те кофи
кофа от {bucket2_volume} литра - {bucket2_count} пъти;
кофа от {bucket1_volume} литра - {bucket1_count} пъти.''')