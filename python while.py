i = 1
while i < 6:
    print(i)
    i += 1  # this prints i as long as it is less than 6
    # while loop needs a break else it continues forever
print()

i = 1
while i < 6:  # this prints from 1 till 3
    print(i)
    if (i == 3):
        break
    i += 1
print()

i = 0  # this prints 1 till 5 but omits the number 3
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print()

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
print()

i = 1
while i < 11:  # this prints from 1 till 10
    print(i)
    if (i == 10):
        break
    i += 1
print()

i = 1
while i < 11:  # this prints from 1 till 10
    print(i)
    i += 1  # i=i + 1
print()

i = 1
while i < 11:  # this prints from 1 till 10
    print(i)

count = 1
if count <= 10:
    print(count)
    print('yes')
else:
    print('no')

count = 1
while count <= 10:
    print(count)
    print('yes')
    count += 1

print('no')



def digit10():
    print('digit10')
    count = 1
    while count <= 10:
        print(count)
        count += 1


#digit10()


def digit():
    number = int(input('enter a number of your dreams:'))
    count = 1
    while count <= number:
        print(count)
        count += 1


#digit()


def digit_function(number):
    count = 1
    while count <= number:
        print(count)
        count += 1


digit_function(9)
