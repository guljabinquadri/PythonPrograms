

j = 5
while(True):#or while(1) #it will run the result continuosly
    if j<=10:
        j= j+1
        continue #The continue keyword is used to end the current iteration
                        # in a for loop (or a while loop), and continues to the next iteration.
                         # (the condtion b4 continue will not print)
    print(j, end=" ")
    if(j==44):
        break #stop the loop
    j = j+1

