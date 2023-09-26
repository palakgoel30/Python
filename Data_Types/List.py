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
