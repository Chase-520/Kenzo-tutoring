


# our input            len(x)-1 len(x)  
x = [2,4,6,1,14,1,1,9,1,10] # 
# len(x) = 10

# setting up counter
i = 0
result = 0


while (i <= len(x)-2):

  if(x[i] < x[i+1]):
    result += 1
  i = i + 1

print(result)






