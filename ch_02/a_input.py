# num1 = int(input("숫자1: "))
# num2 = int(input("숫자2: "))

#? 숫자1, 숫자2 받아서 숫자 리스트로 만들기
num1AndNum2Input = input("숫자1, 숫자2: ").replace(",", "").split(" ")
num1AndNum2 = list(map(int, num1AndNum2Input))
print(num1AndNum2) # [10, 20]

#? 구조분해할당
num1, num2 = num1AndNum2
print(num1) # 10
print(num2) # 20

#? 문자열리스트 >> 숫자리스트 변환
nums = ['1', '2', '3', '4']
num2 = list(map(int, nums))
print(num2) # [1, 2, 3, 4]: 숫자가 들어있는 리스트로 변환

#? int변환하는 함수 만들기
def parseInt(strNum):
  return int(strNum)

nums3 = list(map(parseInt, nums))
print(nums3) # [1, 2, 3, 4]

#? 람다식으로 사용
nums4 = list(map(lambda strNum: int(strNum), nums))
print(nums4) # [1, 2, 3, 4]