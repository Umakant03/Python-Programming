#Inverted Pyramid of Numbers
rows=int(input("Enter the rows"))
b=0
for i in range(rows,0,-1):
    b=b+1
    for j in range(i):
        print(b,end='')
    print('')


    

