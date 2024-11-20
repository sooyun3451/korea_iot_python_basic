#  list 선언 및 초기화 방법
list1 = [1, 5, 3, 4, 4]
# list1 = list()

print(list1[0])
print(list1[0:2]) # [1, 2]

print(list1.index(3)) # 2

list2 = list1[:] # 깊은복사(javascript: [...])
list2.sort()
list2.reverse()
print(list2) # [5, 4, 4, 3, 1]

# pop: 리턴이 있고 인덱스를 넣어야 한다
print(list2.pop(0)) 
print(list2) # [4, 4, 3, 1]

# remove: 리턴이 없고 값을 넣어야 한다
list2.remove(4)
print(list2) # [4, 3, 1]

print(list1) # [1, 5, 3, 4, 4]

# insert(인덱스번호, 넣고자하는 값): 리턴이 없다
list1.insert(1, 10)
print(list1) # [1, 10, 5, 3, 4, 4]

# copy: 복사 
list3 = list1.copy()
print(list3) # [1, 10, 5, 3, 4, 4]

# extend: 확장 
list1.extend(list3)
print(list1) # [1, 10, 5, 3, 4, 4, 1, 10, 5, 3, 4, 4]

print(list3 + [1, 2, 3, 4]) # [1, 10, 5, 3, 4, 4, 1, 2, 3, 4] 
#? (variable) list3: list[int]

print(list3 * 3) # [1, 10, 5, 3, 4, 4, 1, 10, 5, 3, 4, 4, 1, 10, 5, 3, 4, 4]

list4 = [1, "홍길동", [10, 20], 3.14, [30, 40]]
#? (variable) list4: list(안에 자료형이 다르면 []안에 자료형 X)
print(list4) # [1, '홍길동', [10, 20], 3.14]

print(list4[2::2]) # [[10, 20], [30, 40]]
#? ::(스텝): 2칸씩 건너 뛴다

list5 = list4[2:]
list5.remove(3.14)
print(list5) # [[10, 20], [30, 40]]
