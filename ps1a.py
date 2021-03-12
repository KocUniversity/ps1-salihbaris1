n, B = list(map(int, input().strip().split()))
T = 0

# your code here

i=1
i++1
i=n
if i%2==0:
    pi=2^i+1 
elif i%2==1:
  pi=3^i+1
  

    
while ((pi^(n-1)*T + (pi^(n-2)*T + ... + (pi^0)+T)) < B):
  T++1
  T=10000
  if T>10000:
    print(-1)
    break
 
  



# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)




  














# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)