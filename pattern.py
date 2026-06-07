print("\n ##################### Pattern  Practice 1 ############################## \n")
#pattern practice 1

n=5
for i in range (2*n):
    if i<n:
        for j in range(n-i):
            print("*",end=" ")
        for j in range(2*i):
            print(" ",end=" ")
        for j in range(n-i):
            print("*",end=" ")
    else:
        for j in range(i-n+1):
            print("*",end=" ")
        for j in range((2*n-i-1)*2):
            print(" ",end=" ")
        for j in range(i-n+1):
            print("*",end=" ")

    print()

print("\n ##################### Pattern  Practice 2 ############################## \n")
#Pattern Practice 2

n=5
for i in range(2*n):
    if i<n:
        for j in range(i+1):
            print("*",end=" ")
        for j in range(2*n-2*i-2):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
    else:
        for j in range(2*n-i-1):
            print("*",end=" ")
        for j in range(2*i-2*n+2):
            print(" ",end=" ")
        for j in range(2*n-i-1):
            print("*",end=" ")
    print()



print("\n ##################### Pattern  Practice 3 ############################## \n")

n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
              print("*" ,end=" ")
        else:
            print(" " ,end=" ")
    print()






    
        