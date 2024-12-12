#program to take out prime numbers
inputNumber = int(input("enter a number:"))
primeNumber = []


for jonty in range(2,inputNumber+1):
    num = jonty
    isPrime = 1
    for aditya in range(2, num):
        if (num % aditya ==0):
            isPrime=0
            break
      
            
    if (isPrime == 1):
        primeNumber.append(num)
       

print(primeNumber) 


       

        
