from dataclasses import dataclasses

@dataclasses
class User:
  username: str
  password: str
  name:str
  email: str

class UserDatabase:
  def insert(self, user:User):
    print(f"insert Data -> {user}")

  def select(self, username:User):
    print(f"select Data -> search username: {username}")

  def update(self, user:User):
    print(f"update Data -> {user}")

  def insert(self, username:User):
    print(f"delete Data -> search username: {username}")

if __name__ == "__main__":
  userDatabase = UserDatabase()
  userDatabase.insert(User('aaa', '1234', '홍길동', 'aaa@gmail.com'))

  newUser = User(name='홍길서', password='5678', username='bbb', email='bbb@gmail.com')
  userDatabase.insert(newUser)