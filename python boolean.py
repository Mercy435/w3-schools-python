print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33
print('b>a', b > a)
print('b>a', 10+10)
if 10+10==20:
  print("kelvin")
else:
  print("mercy")

  print(bool("Hello"))
  print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

print('mercy')
print(bool(False))
print(bool(None))
print(bool(1))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return False
print(myFunction())


def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

x= 200
print(isinstance(x, int))
