a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

"""
come over to the house
its urgent..... note that this is different from the multi line string.. 
this is a comment
"""
#this is a comment

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


a='howva'
print(a[0])

#this prints all the letters in a single file
for x in "baby":
  print(x)

x='father'
print(len(x))

txt = "The best things in life are free!"
print("free" in txt)
print("Free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  if "Free" not in txt:
      print("No, 'Free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

  b = "Hello, World!"
  print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])



b = "Hello, World!"
print(b[2:])
print(b[2:6])

b = "Hello, World!"
print(b[-5:-2])
print(b[-12:])
#modifying strings
a = "Hello, World!"
print(a.upper())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print(a.replace(' ',''))

a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace("H","J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#concatenating strings
a = "Hello"
b = "World"
c = a +  b
print(c)
#to give space between words
a= "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#formating strings
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

txt = "\110\145\154\154\157"
print(txt)

txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

a='this is my time'
x = a.capitalize()
print(x)
x=a.center(1)
print(x)

txt = "banana"
x = txt.center(20)
print(x)
