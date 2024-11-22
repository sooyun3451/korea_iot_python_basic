def moduleTest():
  print("메소드 모듈")

def moduleTest2():
  print("메소드 모듈2")

from dataclasses import dataclass

@dataclass
class StudentModule:
  name: str
  age: int

print(__name__)

if __name__ == "__main__":
  moduleTest()
  moduleTest2()