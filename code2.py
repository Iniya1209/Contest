dist=int(input())
def base(vehicle_type,dist):
    if(vehicle_type=="mini"):
        base_charge=50
    if(vehicle_type=="sedan"):
        base_charge=80
    if(vehicle_type=="suv"):
        base_charge=100
    return base_charge
def charges(vehicle_type,dist):
    if(dist>0):
        if(vehicle_type=="mini"):
            if(dist-15>0):
                extra_charge=15*10
            else:
                extra_charge=dist*10
        if(vehicle_type=="sedan"):
            if(dist-15>0):
                extra_charge=15*12
            else:
                extra_charge=dist*12
        if(vehicle_type=="suv"):
            if(dist-15>0):
                extra_charge=15*15
            else:
                extra_charge=dist*15
        return extra_charge
    return 0
def add_charge(vehicle_type,dist):
    if(dist>0):
        if(vehicle_type=="mini"):
            add_charge=dist*8
        if(vehicle_type=="sedan"):
            add_charge=dist*10
        if(vehicle_type=="suv"):
            add_charge=dist*12
        return add_charge
    return 0
def greater_dist(vehicle_type,dist):
    if(vehicle_type=="mini"):
        cost=dist*8
    if(vehicle_type=="sedan"):
        cost=dist*10
    return cost
if(dist>75):
    mcost=greater_dist("mini",dist)
else:
    mcost=base("mini",dist)+charges("mini",dist-3)+add_charge("mini",dist-18)
if(dist>100):
    scost=greater_dist("sedan",dist)
else:
    scost=base("sedan",dist)+charges("sedan",dist-5)+add_charge("sedan",dist-20)
sucost=base("suv",dist)+charges("suv",dist-5)+add_charge("suv",dist-20)
print("Mini - Rs.",mcost,",Sedan - Rs.",scost,",SUV - Rs.",sucost)
   
