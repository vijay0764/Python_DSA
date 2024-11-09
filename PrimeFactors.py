import math
def prime(num):
    if num<=1:
        return False
    if num==2 or num==3:
        return True
    if num%2==0 or num%3==0:
        return False
    i,last=5,math.isqrt(num)
    while(i<=last):
        if(num%i==0 or num % (i + 2)==0):
            return False
        i+=6
    return True
    
# for i in range(2,55):
#     print(i,"is prime: ", prime(i))

def primeFactor(num):
    Factors = []
    i=2
    while(i<=num):
        if prime(i) and num%i==0:
            Factors.append(i)
            num//=i
        else:
            i+=1 
    return Factors
    
    
for i in range(2,55):
    print(i,"Prime Factors: ", primeFactor(i))
    
    
    
    
    
    
    
    
    
    
