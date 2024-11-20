print()
# 리스트랑 동일한 구조(값의 추가, 수정, 삭제 불가능)
tuple1 = ()
tuple1 = tuple()

tuple1 = (1, 2, 3)
print(tuple1[1:]) # (2, 3)

tuple1 = tuple1 * 3 # tuple은 값 추가 X: tuple1 * 3해서 새로운 튜플을 만들어 tuple1에 덮어쓰기한 것
print(tuple1) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

tuple2 = (10, ) # tuple에 값을 하나만 넣을때는 ,사용

tuple3 = 1, 2, 3 # ()소괄호 생략 가능 

#? python 함수(:후 밑에 들여쓰기하면 함수 안)
def add(n1, n2, n3):
  return n1 + n2, n2 + n3, n1 + n3 # ()소괄호가 생략된 튜플

print(add(10, 20, 30)) # (30, 50, 40): tuple의 형태