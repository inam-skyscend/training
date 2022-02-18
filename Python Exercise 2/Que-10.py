car={"brand":"ford","model":"mustang","year":2018}

if "brand" in car:
    print("exist")



print(car.keys())



if car.get("orange"):
    print("exist")
else:
    print("does not exist")