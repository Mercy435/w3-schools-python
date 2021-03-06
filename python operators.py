print(10+5)
print(5-10)
print(5/2)
print(5*2)
print(5%2)
print(5**2)
print(5//2)

x = 5
print(x)

x +=3
print(x)

x = 5
x -=3
print(x)

x = 5
x *=3
print(x)

x = 5
x /=3
print(x)
print('miracle')
x= 5
x %=3
print(x)

x= 5
x **=3
print(x)

#functions as binary numbers
x=15
x &=3
print(x)

x = 5
x |=3
print(x)
print('confident')
x= 5
x ^= 3
print(x)

x = 5
x >>=3
print(x)

x = 5
x <<=3
print(x)

#not equal to
x = 5
y = 3
print(x != y)

# returns True because five is greater, or equal, to 3
x=5
y=3
print(x>=y)

x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print('banana' in x)
print('banana' not in x)