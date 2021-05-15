k  = int(input())
prop =  0
for i in range (k):
    x = list(map(int,input().split()))
    if x.count(1)>x.count(0):
        prop+=1
print(prop)

