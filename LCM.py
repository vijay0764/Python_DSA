def LCM(a,b):
    maximum=max(a,b)
    minimum=min(a,b)
    i=maximum 
    while(i<=(a*b)):
        if(i%minimum==0):
            return i 
        i+=maximum

a=int(input("A: "))
b=int(input("B: "))

print("LCM->",LCM(a,b))
