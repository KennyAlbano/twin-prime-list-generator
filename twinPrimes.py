i=0
n=1000
primes=[2]
currentVal=3
while(len(primes)<n):
    if(currentVal%primes[i]==0):
        currentVal=currentVal+2
        i=0
    if(len(primes)==(i+1)):
        primes.append(currentVal)
    if(currentVal%primes[i]!=0):
        i+=1
i=0
while(i<n):
    if(primes[i]-primes[i-1]==2):
        print(primes[i-1],primes[i])
    i+=1

#Prints all twin primes up to the value of the nth prime number
#only tests odd numbers because 2 is the only even prime

