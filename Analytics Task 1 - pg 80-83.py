ages = [32, 31, 30, 37, 37, 33]
earnings = [1270, 7890, 4700, 1810, 750, 1100]

def mean():
    sumValues = 0
    for item in ages:
        sumValues += item
        average = sumValues / len(ages)
        print(average)
        
mean()

def minmax():
    ages.sort()
    minValue = myList[0]
    maxValue = myList[-1]
    print(minValue)
    print(maxValue)
    
call = (int(input'1. Mean', '\n2. Minimum/Maximum Value'))
if call == 1:
    mean()
elif call == 2:
    median()

    