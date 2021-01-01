js1 = '''{
	"1":"A",
	"2":"B",
	"3":"C"
}'''
js2 = '''{
	"4":"D",
	"5":"E",
	"6":"F"
}'''
js3 = '''{
	"7":"G",
	"8":"H",
	"9":"I"
}'''
js4 = '''{
	"10":"J",
	"11":"K",
	"12":"L"
}'''

from freshworks import Freshworks
obj = Freshworks()

obj.create("Key1", js1)
obj.create("Key2", js2)
obj.create("Key3", js3)
obj.create("Key4", js4)
obj.delete("Key3")
print(obj.read("Key2"))
