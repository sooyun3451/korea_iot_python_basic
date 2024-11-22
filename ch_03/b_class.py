# class: 변수, 메서드
class User:
  username="hgd"
  password="qwe123"
  name="홍길동"
  email="gildong@gmail.com"
  
  def getUserInfo(self, address): # self = java에서의 this
    return f'''
username: {self.username} 
password: {self.password} 
name: {self.name}
email: {self.email}
address: {address}
'''
  
user1 = User()
print(user1.getUserInfo("부산"))