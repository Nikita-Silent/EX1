print('''Выберите один из предложенных типов машины:
1. Drag car (250 л.с.; 0-100 за 9 сек.; 14 л на 100 км)
2. Drift car (200 л.с.; 0-100 за 11 сек.; 9 л на 100 км)
3. Veg car (150 л.с.; 0-100 за 17 сек.; 7 л на 100 км)
P.s. В качестве ответа напишите НОМЕР (цифрой) выбранного вами типа''')
car = int(input('Введите номер:'))
if (car == 1):
print('''Выберите один из предложенных вам наборов тюнинга машины
0. Stage 0 (Стоковая машина)
1. Stage 1 (Перепрошивка системы машины) + 100 л.с.; - 1.5 сек.; + 2 л на 100 км
2. Stage 2 (Замена топливной системы, распил цилиндра, перебор двигателя) +150 л.с.; -3 сек.; + 4 л на 100 км
3. Stage 3 (Замена каркаса машины, замена сцепления, замена тормозов) +200 л.с.; -4.5 сек.; + 6 л на 100 км
P.s. В качестве ответа напишите НОМЕР (цифрой) выбранного вами типа''')
stage = int(input())
if stage == 0:
print('Ваша машина: 250 л.с.; 0-100 за 9 сек.; 14 л на 100 км')
if stage == 1:
print('Ваша машина: '+ 250 + 100 + " л.с.; 0-100 за "+ 9 - 1.5 +' сек.; '+ 14 + 2 +' л на 100 км')
if stage == 2:
print('Ваша машина: '+ 250 + 150 + " л.с.; 0-100 за "+ 9 - 3 +' сек.; '+ 14 + 4 +' л на 100 км')
if stage == 3:
print('Ваша машина: '+ 250 + 200 + " л.с.; 0-100 за "+ 9 - 4.5 +' сек.; '+ 14 + 6 +' л на 100 км')
elif car == 2:
print('''Выберите один из предложенных вам наборов тюнинга машины
0. Stage 0 (Стоковая машина)
1. Stage 1 (Перепрошивка системы машины) + 100 л.с.; - 1.5 сек.; + 2 л на 100 км
2. Stage 2 (Замена топливной системы, распил цилиндра, перебор двигателя) +150 л.с.; -3 сек.; + 4 л на 100 км
3. Stage 3 (Замена каркаса машины, замена сцепления, замена тормозов) +200 л.с.; -4.5 сек.; + 6 л на 100 км
P.s. В качестве ответа напишите НОМЕР (цифрой) выбранного вами типа''')
stage = input()
if stage == 0:
print('Ваша машина: 250 л.с.; 0-100 за 9 сек.; 14 л на 100 км')
if stage == 1:
print('Ваша машина: ' + 200 + 100 + " л.с.; 0-100 за " + 11 - 1.5 + ' сек.; ' + 9 + 2 + ' л на 100 км')
if stage == 2:
print('Ваша машина: ' + 200 + 150 + " л.с.; 0-100 за " + 11 - 3 + ' сек.; ' + 9 + 4 + ' л на 100 км')
if stage == 3:
print('Ваша машина: ' + 200 + 200 + " л.с.; 0-100 за " + 11 - 4.5 + ' сек.; ' + 9 + 6 + ' л на 100 км')
elif car == 3:
print('''Выберите один из предложенных вам наборов тюнинга машины
0. Stage 0 (Стоковая машина)
1. Stage 1 (Перепрошивка системы машины) + 100 л.с.; - 1.5 сек.; + 2 л на 100 км
2. Stage 2 (Замена топливной системы, распил цилиндра, перебор двигателя) +150 л.с.; -3 сек.; + 4 л на 100 км
3. Stage 3 (Замена каркаса машины, замена сцепления, замена тормозов) +200 л.с.; -4.5 сек.; + 6 л на 100 км
P.s. В качестве ответа напишите НОМЕР (цифрой) выбранного вами типа''')
stage = input()
if stage == 0:
print('Ваша машина: 250 л.с.; 0-100 за 9 сек.; 14 л на 100 км')
if stage == 1:
print('Ваша машина: ' + 150 + 100 + " л.с.; 0-100 за " + 11 - 1.5 + ' сек.; ' + 7 + 2 + ' л на 100 км')
if stage == 2:
print('Ваша машина: ' + 150 + 150 + " л.с.; 0-100 за " + 11 - 3 + ' сек.; ' + 7 + 4 + ' л на 100 км')
if stage == 3:
print('Ваша машина: ' + 150 + 200 + " л.с.; 0-100 за " + 11 - 4.5 + ' сек.; ' + 7 + 6 + ' л на 100 км')
else:
print('ОШИБКА. ПЕРЕЗАПУСТИТЕ ПРОГРАММУ И СЛЕДУЙТЕ ИНСТРУКЦИЯМ!')