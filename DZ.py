import itertools

import time #библиотека для замеров времени

start_time = time.time() #время начала работы кода


filename='D:\\Работа\\DataS\\code\\01 Подготовка\\zdf.txt'
dict_my={}
list_my=[]

with open(filename, 'r') as f:
	for line in f:
		line = line.strip()
		dict_my[line]=True

for i in range(2,11):
	for x in itertools.permutations('ростелеком',i):
		if dict_my.get(''.join(x),False):
			list_my.append(''.join(x))

print(len(set(list_my)))

print("--- %s seconds ---" % (time.time() - start_time))#расчитываем прошедшее время

