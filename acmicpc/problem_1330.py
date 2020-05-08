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
    
