dist=int(input())
mcost=0
scost=0
sucost=0
#mini
if(dist>75):
    mcost=dist*8
else:
    t=dist
    if(t-3>=0):
        mcost+=50
        t-=3
    else:
        mcost=50
        t=0
    if(t>0):
        if(t-15>0):
            mcost+=15*10
            t-=15
        else:
            mcost+=t*10
            t=0
    if(t>0):
        mcost+=(t*8)
#sedan

if(dist>100):
    scost=dist*10
else:
    t=dist
    if(t-5>=0):
        scost+=80
        t-=5
    else:
        scost=80
        t=0
    if(t>0):
        if(t-15>0):
            scost+=15*12
            t-=15
        else:
            scost+=t*12
            t=0
    if(t>0):
        scost+=(t*10)
#SUV
t=dist
if(t-5>=0):
    sucost+=100
    t-=5
else:
    sucost=100
    t=0
if(t>0):
    if(t-15>=0):
        sucost+=15*15
        t-=15
    else:
        sucost+=t*15
        t=0
if(t>0):
    sucost+=(t*12)
print("Mini - Rs.",mcost,",Sedan - Rs.",scost,",SUV - Rs.",sucost)