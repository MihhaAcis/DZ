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

##Dict
#filename='D:\\Работа\\DataS\\code\\01 Подготовка\\zdf.txt'
##rus_dict=['Рост','кот','жопа','рост','скелет']
#word=set(list('Ростелеком'.lower()))
#rw=[]
#dict_my={'р':1,'о':2,'с':1,'т':1,'е':2,'л':1,'к':1,'м':1}
#print(word)



#with open(filename, 'r') as f:
#	for line in f:
## убираем символ переноса строки для каждой читаемой строчки
#		line = line.strip()
#		#rw.append(line)
#		if set(line.lower()) <=word:
#			rw.append(line)



#set_new=set(rw)
#print(len(set_new))


#import itertools

#import time #библиотека для замеров времени

#start_time = time.time() #время начала работы кода


#filename='D:\\Работа\\DataS\\code\\01 Подготовка\\zdf.txt'
#dict_my={}
#list_my=[]
#rw=[]
#wr=[]

#with open(filename, 'r') as f:
#	for line in f:
#		line = line.strip()
#		rw.append(line)
#my_set_dict=set(rw)



#for i in range(2,11):
#	for x in itertools.permutations('ростелеком',i):
#		wr.append(''.join(x))
			
#my_set_word=set(wr)

#print(len(my_set_word.intersection(my_set_dict)))

#print("--- %s seconds ---" % (time.time() - start_time)) #расчитываем прошедшее время