#enter a point(x,y) and print what quardrant it is


x = int(input("enter x: "))
y = int(input("enter y: "))

result = 0

if x > 0:
    if y > 0:
        result = 1
    else:
        result = 4
else:
    if y > 0:
        result = 2
    else:
        result = 3


print(result)
