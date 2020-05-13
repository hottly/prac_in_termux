#enter an integer between 1 to 4000
#print number is leap year or not


year =  int(input())

if year <1 or year>4000:
    print("not valid nubmer.")

result = ""

if year%4==0:
    if year%100!=0:
        result = "leap year"
    elif year%400==0:
        result = "leap year"
else:
    result = "not leap year"

print(result)
