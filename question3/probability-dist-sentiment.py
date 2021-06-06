import matplotlib

# 'courier' : [positivity, negativity]
couriers = {'DHL': [0.661, 0.339],
             'Pos Laju': [0.61, 0.39], 
             'Ninja-Van': [0.804, 0.196], 
             'J&T': [0.636, 0.364], 
             'GDEX': [0.711, 0.289]}

distances = {
            "Customer 1":{"DHL":53.944, "GDEX":61.078, "Pos Laju":63.230, "Ninja-Van":99.022, "J&T":124.942},
            "Customer 2":{"DHL":47.523, "Pos Laju":56.006, "Ninja-Van":70.249, "GDEX":77.009, "J&T":105.959},
            "Customer 3":{"J&T":52.392, "Pos Laju":54.168, "GDEX":72.422, "DHL":83.508, "Ninja-Van":111.776}
            }

print("Weighted score = (1 - dist_x/dist_sum) * positvity")

pd = {
    "Customer 1":{},
    "Customer 2":{},
    "Customer 3":{}
    }

for cust in distances:
    sum = 0
    for cour in distances.get(cust):
        sum+=distances.get(cust).get(cour)

    for cour in distances.get(cust):
        pd[cust][cour] = [round(1 - distances.get(cust).get(cour)/sum, 4), round((1 - distances.get(cust).get(cour)/sum) * couriers.get(cour)[0],4)]
        ## stores for each courier for each customer an array with 2 values: 
        # [0] is the distance score 
        # [1] is the weighted score


for cust in pd:
    best_score = 0
    best_hub = ""
    print(cust)
    for cour in pd.get(cust):
        print("  %s \n  - Distance Score: %.4f\n  - Weighted Score: %.4f"%(cour, pd.get(cust).get(cour)[0], pd.get(cust).get(cour)[1] ))
        if(pd.get(cust).get(cour)[1] > best_score):
            best_score = pd.get(cust).get(cour)[1]
            best_hub = cour


    print("\n-Best Weighted Score: %.4f via %s" % (best_score, best_hub))
    print("-Best Distance Score: %.4f via %s\n" % (list(pd.get(cust).values())[0][0], list(pd.get(cust).keys())[0]))


    
