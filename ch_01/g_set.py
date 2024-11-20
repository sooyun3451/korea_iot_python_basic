set1 = set()
set1 = {'a', 'b', 'c'}

print(set1) # {'a', 'b', 'c'}
print(list(set1)) # ['a', 'b', 'c']
print(set1.pop()) # 제일 앞에있는거

for data in set1: 
  if data == 'b':
    print(data) # b

set2 = {1, 2, 3, 4, 'a'}
set3 = set1.union(set2)
print(set3) # {1, 2, 3, 4, 'a', 'b'}

print(set1 & set2) # {'a'}: 교집합

set4 = {1, 1, 1, 2, 3, 4, 5, 5, 5}
print(set4) # {1, 2, 3, 4, 5}

set4 = set([1, 1, 1, 2, 3, 4, 5, 5, 5])
print(set4) # {1, 2, 3, 4, 5}

print(set1 - set2) # {'c', 'b'}: 차집합