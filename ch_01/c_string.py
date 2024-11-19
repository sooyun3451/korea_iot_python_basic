name = '홍길동'

print(name)

# 문자열 사이에 문자열 추가(join: 홍,길,동)
print(",".join(name))

# f포멧, 표현식(홍길동 입니다.)
print(f"{name}입니다.")

# 문자열 안에서 찾고자하는 문자열의 위치(인덱스) 반환
print(name.find('이')) # -1
# print(name.index('이')) # error(예외처리)

# 문자열 안에서 찾고자 하는 문자열의 갯수 반환
print(name.count('홍')) # 1

# 문자열의 길이 구하기
print(name.__len__()) # 3
print(len(name)) # 3

# 문자열 양끝 공백제거
print(" 이름 ".strip())#이름
print(" 이름 ".lstrip()) #이름
print(" 이름 ".rstrip()) #  이름

# 문자열 특정 부분 변경 
print("010-1234/5678".replace("-", "").replace("/", "")) # 01012345678

# 토큰으로 문자열 리스트화 하기
print("홍길동,홍길서,홍길남".split(",")) # ['홍길동', '홍길서', '홍길남']

address = "부산광역시 동래구 사직동 아파트 201동 201호"
print("address")
addressList = address.split(" ")
address1 = addressList[0]
address2 = addressList[1]
address3 = "".join(addressList[2:])

print(f"주소1: {address1}, 주소2: {address2}, 주소3: {address3}") # 주소1: 부산광역시, 주소2: 동래구, 주소3: 사직동아파트201동201호
print(f"주소1: {address1}\n주소2: {address2}\n주소3: {address3}") 
# 주소1: 부산광역시
# 주소2: 동래구
# 주소3: 사직동아파트201동201호

print(f"""주소1: {address1}
주소2: {address2}
주소3: {address3}""") 
# """ """ 사용 시에 줄바꿈 후 무조건 붙여주기

# 인덱싱, 슬라이싱
print(address[0]) # 부
print(address[0:3]) # 부산광(0에서 3전까지)
print(address[2:3]) # 광(2에서 3전까지)
print(address[:3]) # 부산광(0부터 3까지)
print(address[4:]) # 시 동래구 사직동(4부터 끝까지)
print(address[-1:]) # 동(-: 뒤에서부터) * -는 끝까지 or -로 가야한다
print(address[4:-3]) # 시 동래구(앞에서 4 뒤에서 3)

print(address[:address.find('시 ') + 1]) # 부산광역시(시로 끝나는 곳에서 자르기)

print(address[address.find('시') + 2: address.find('구 ') + 1]) # 동래구


print("*" * 20)
print("1. 회원가입")
print("2, 로그인")
print("*" * 20)
# ********************
# 1. 회원가입
# 2, 로그인
# ********************