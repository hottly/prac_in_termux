#enter two numbers and print that first number is lesser, greater or equal

a, b = input().split(' ')

a = int(a)
b = int(b)
result =  ""

if a > b:
    result =  ">"
elif a < b:
    result = "<"
else:
    result =  "="


print(result)
