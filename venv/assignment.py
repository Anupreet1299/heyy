N = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
m = 4
#print(N, len(N))
i=0
while  i < i+m:
    N[i] = 0
    i+= 1
    if i>= i+m:
       i =(i+m)*N
       N[i] = 0
    

num = N.count(i,0,len(N))
print(num)



