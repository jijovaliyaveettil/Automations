def isPrime(n):
  if(n==1 or n==0):
    return False
   
  for i in range(2,n):
    if(n%i==0):
      return False
  return True

    
def Main():
    n = int(input ("Enter the value n: "))
    
    isPrime(n)
    
    for j in range(1,n+1):
      if(isPrime(j)):
        print(j,end=" ")
    
Main()
    
    
        
