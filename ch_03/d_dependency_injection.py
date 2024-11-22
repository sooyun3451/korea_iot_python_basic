# 의존성 주입
from dataclasses import dataclass

@dataclass
class Repository:

  def insert(self, entity:dict):
    print(f"{entity} -> 데이터를 추가합니다.")

class Service:
  repository: Repository

  def __init__(self, repository: Repository):
    self.repository = repository

  def addData(self, dto:dict):
    entity = dto
    self.repository.insert(entity)

# 서비스를 생성할 때 마다 Repository도 같이 생성되므로 좋지 않은 코드
# class Service:
#   repository = Repository()

#   def addData(self, dto: dict):
#     entity = dto
#     self.repository.insert(entity)
  
#   def addData2(self, dto: dict):
#     entity = dto
#     self.repository.insert(entity)
  
#   def addData3(self, dto: dict):
#     entity = dto
#     self.repository.insert(entity)

repository = Repository()
service = Service(repository)

service.addData({"name":"김준일", "age":31})