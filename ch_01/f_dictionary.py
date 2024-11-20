# Map 자료형 
# key, value
# key 종복x, 순서x

dict1 = dict()
dict1 = {
  "name": "홍길동",
  "age": 22
}

print(dict1) # {'name': '홍길동', 'age': 22}

list1 = ['a', 'b', 'c', 'd']
print(list1[0]) # a

tuple1 = ('a', 'b', 'c')
print(tuple1[0]) # a

dict1 = { '10': 'a', '20': 'b', '30': 'c'}
print(dict1['10']) # a

dict2 = { '10': [1, 2, 3], '20': 'b', '30': 'c'}
print(dict2['10']) # [1, 2, 3]

dict1['40'] = 'd'
print(dict1) # {'10': 'a', '20': 'b', '30': 'c', '40': 'd'}