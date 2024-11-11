def alldivisor(num):
    print(1)
    for i in range(2,(num//2)+1):
        if num%i==0:
            print(i)
    print(num)


num = int(input("Enter  your number: "))
alldivisor(num)
