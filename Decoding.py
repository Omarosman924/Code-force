input()
name = str(input())
x = name[0]

if len(name)==2:
    print(name)
else:
    if len(name)%2 != 0:
        
        
        y = name[(int(len(name)/2))]
        z = name[(int(len(name)/2)+1)]
    else:
        y = name[(int(len(name)/2)-1)]
        z =  name[(int(len(name)/2))]
    name = name.replace(z,y,1)
    name = name.replace(y,z,1)

    name = name.replace(z,x,1)
    name = name.replace(x,z,1)
    print(name)
