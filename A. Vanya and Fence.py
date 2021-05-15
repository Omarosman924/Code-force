n,h = list(map(int,input().split()))
tall = list(map(int,input().split()))
r = 0
for i in range(n):
    if tall[i] <= h:
        r+=1
    else:
        r+=2
print(r)
