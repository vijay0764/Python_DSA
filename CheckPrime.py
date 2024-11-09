import math
def CheckPrime(num):
    i,last=2,abs(math.sqrt(num))
    
    while(i<=last):
        if(num%i==0):
            return False
        i+=1
    return True
    
num = int(input("Enter Prime:"))
print(CheckPrime(num))
        
