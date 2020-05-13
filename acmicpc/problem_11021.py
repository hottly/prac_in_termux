#enter number of cases and enter values to add
#print result as "Case #x: reulst"


c = int(input())
lst = []

for i in range(0,c):
    lst.append(input())


for i in range(len(lst)):
    str = lst[i].split(" ")
    a = int(str[0])
    b = int(str[1])
    print("Case #%d: %d"%(i, a+b))
