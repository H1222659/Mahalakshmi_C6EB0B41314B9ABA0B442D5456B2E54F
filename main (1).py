# 1.1 Implement a recursive function to calculate the factorial of a give number

def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)

n=int(input("Enter a number:"))
a=fact(n)

print("The factorial of {} is {}.".format(n,a))


      
      


    
  



