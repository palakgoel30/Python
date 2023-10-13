numbers = [1,3,5]
double = [num *2 for num in numbers]
print(double)

names = ['pushpa','pari','sam','panjari','som','payal']
StartLetterP = []
for x in names:
    if(x.startswith('p')):
        StartLetterP.append(x)
print(StartLetterP)

##### Modified above query

names = ['pushpa','pari','sam','panjari','som','payal']
StartLetterP = [x for x in names if x.startswith('p')]
print(StartLetterP)

List1 = [2,9,7,8,6]
for i in range(len(List1)):
    max_value = max(List1[i::len(List1)])

    print(max_value)
print(List1[1:3])
print(List1[1::])
