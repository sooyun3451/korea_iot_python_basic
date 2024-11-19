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