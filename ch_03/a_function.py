def fx01():
  pass

def fx02():
  print("fx02 출력")

fx02()

class A:
  pass

#? python의 오버로딩은 매개변수의 갯수가 다를 경우
#? 오버로딩 시 방법을 나눠서: 인터프리터 언어라 함수 호출이 다른 오버로딩 밑으로 오면 error
#? =None 사용하면 값이 들어오지 않았을때 default값 None으로
#! python에서 new가 없고 클래스명() >> 객체 생성

def fx03(a: int, b:A | None=A(), c=None): 
  print(a)
  print(b)
  print(c)

fx03(10, A())
fx03(1, "문자열", True)

#? 가변 매개변수(*는 매개변수를 여러개 넣으면 그 매개변수를 tuple로 만들어준다.)
def fx04(*args):
  print(args)

fx04(1, 2, 3, 4, 5) # (1, 2, 3, 4, 5)


#? 호출 시 두번째가 None이면 세번째가 당겨져서 담기니 3번째 매개변수에도 None 달아주기
def requestGet(
    url:str | None="http://localhost", 
    port:int | None = 8080, 
    params:dict | None=dict()):
  print(url) # https://localhost
  print(port) # 8080
  print(params) # {'name': '홍길동', 'age': 22}
  return "Response"

responseData = requestGet(url="https://localhost", params={"name": "홍길동", "age": 22})
print(responseData) # Response

req = lambda url="http://localhost", port=8080, params={}: {"url": url, "port": port, "params": params}

print(req("http://localhost", 8080, {"name": "홍길동", "age": 22})) # {'url': 'http://localhost', 'port': 8080, 'params': {'name': '홍길동', 'age': 22}}