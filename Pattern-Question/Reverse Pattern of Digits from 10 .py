start=1
stop=2
currentNum=stop
for i in range(2,6):
    for j in range(start,stop):
        currentNum -=1
        print(currentNum,end='')
    print('')
    start=stop
    stop=i+stop
    currentNum=stop