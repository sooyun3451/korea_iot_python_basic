nums = [10, 20, 30, 40]

for num in nums:
  print(num)

nums = range(10)
print(nums) # range(0, 10)
print(list(nums)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
  print(i)

nums = range(10, 20)
print(list(nums)) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

nums = range(10, 20, 2)
print(list(nums)) # [10, 12, 14, 16, 18]

# for(int i = 0; i < 10; i++) {

# } >> 밑과 같은 의미

# for i in range(10):
#   for j in range(5):
#     print(f'i: {i}, j: {j}')

'''
*     *****
**    ****
***   ***
****  **
***** *
'''

#? 별 하나씩 증가
print("\n")
for i in range(5):
  print("*" * (i + 1))

print("\n")
for i in range(1, 6):
  print('*' * i)

#? 별 하나씩 감소
print("\n")
for i in range(5):
  print('*' * (5 - i))

print("\n")
for i in range(5, 0, -1):
  print("*" * i)

#? 별 오른쪽으로 붙이기
print("\n")
for i in range(5):
    print(" " * (5 - (i + 1)), end="")
    print('*' * (i + 1))

#? 별 탭해서 옆으로 붙이기
print("\n")
for i in range(1, 6):
  # print("*" * i, end="\t\t\t")
  # print("*" * (6 - i))
  print(f'{"*" * i}\t\t\t{"*" * (6 - i)}')

print("\n")
print("aaaaa", end="")
print("bbbbb", end="")



