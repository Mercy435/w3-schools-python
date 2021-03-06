def my_function():
  print("Hello from a function")
my_function()
print()

def my_function(fname): #arguments
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
print()

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
print()

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", 'doc')
print()

def my_function(*kids): #if the number of arguments is unknown
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
print()

def my_function(*kids):
  print("The youngest child is " + kids[0])
my_function("Emil", "Tobias", "Linus")
print()

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print()

def my_function(**kid): #if the number of keyword arguments is unknown....kwargs-keyword argument
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
print()

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print()

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
print()

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
print()

:
def my_function(x):
  print( 5 * x)
my_function(3)
my_function(5)
my_function(9)
print()

def myfunction():
  pass #this prevents an error

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)