from src import User, UserDatabase, concat
#? __init__안에 import 하면 src(폴더이름)으로 가져올 수 있다

def main():
  print("user project start!!!")
  newUser = User(username="aaa", password='1234', name='홍길동', email='aaa@gmail.com')
  UserDatabase().insert(newUser)
  concat(1, 10)


if __name__ == "__main__":
  main()
