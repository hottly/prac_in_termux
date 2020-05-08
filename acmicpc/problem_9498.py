#enter the score and make it as grade

score = int(input())

result = ""

if score > 100: 
    result = "Wrong value please check input"
elif score > 89 and score <=100:
    result = "A"
elif score > 79 and score <=89:
    result = "B"
elif score > 69 and score <=79:
    result = "C"
elif score > 59 and score <=69:
    result = "D"
else:
    result = "F"


print(result)
