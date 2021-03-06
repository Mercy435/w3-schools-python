'''fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
print()


  print(x)
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print()
#0 to 5
#1 to 6
for x in range(6): #this prints six numbers starting from 0
  print(x+2)  # 2,3,4,5,6,7
  print(x * 3)
print()

for x in range(2, 6):
  print(x)
print()

for x in range(2, 30, 3):
  print(x)
print()

for x in range(6):
  print(x)
else:
  print("Finally finished!")
print()

for x in range(6):#this doesnt allow the else statement due to the break
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
print()

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj: #nested for loop
  for y in fruits:
    print(x, y)
print()

for x in [0, 1, 2]:
  pass
'''
word= 'banana'
for x in range(0,len(word)-1,2):
    print(word[x])