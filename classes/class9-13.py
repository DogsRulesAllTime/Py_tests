from collections import OrderedDict
dict = OrderedDict()

dict['one'] = 1
dict['two'] = 2

print(dict)
for k,v in dict.items():
	print(k,' ',v)

dict = {}

dict['one'] = 1
dict['two'] = 2

print(dict)

for k,v in dict.items():
	print(k,' ',v)