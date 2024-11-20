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

#! dict 쌍 추가
dict1['40'] = 'd'
print(dict1) # {'10': 'a', '20': 'b', '30': 'c', '40': 'd'}

dict1.update({'40': 'e', '50': 'f'})
print(dict1) # {'10': 'a', '20': 'b', '30': 'c', '40': 'e', '50': 'f'}

dict1['40'] = 'g'
print(dict1) # {'10': 'a', '20': 'b', '30': 'c', '40': 'g', '50': 'f'}
#? 있으면 업데이트 없으면 추가 

#! value 가져오기 
print(dict1.get('20')) # b
print(dict1['20']) # b

#! 쌍 삭제
print(dict1.pop('30')) # c
print(dict1) # {'10': 'a', '20': 'b', '40': 'g', '50': 'f'}

print(dict1.items()) # dict_items([('10', 'a'), ('20', 'b'), ('40', 'g'), ('50', 'f')])

for item in dict1.items():
  print(item)
# ('10', 'a')
# ('20', 'b')
# ('40', 'g')
# ('50', 'f')

for key in dict1.keys():
  print(key)
# 10
# 20
# 40
# 50

for value in dict1.values():
  print(value)
# a
# b
# g
# f

#? (method) def keys() -> dict_keys[str, str]: 튜플처럼 리스트로 들고오지만 append, remove같은 함수 x
keys1 = dict1.keys()
print(keys1) # dict_keys(['10', '20', '40', '50'])

#? ['10', '20', '40', '50']: list로 변환해서 사용
keys2 = list(dict1.keys())
print(keys2) 