import matplotlib

# 'courier' : [positivity, negativity]
couriers = {'DHL': [0.661, 0.339],
             'Pos Laju': [0.61, 0.39], 
             'NinjaVan': [0.804, 0.196], 
             'JNT': [0.636, 0.364], 
             'GDex': [0.711, 0.289]}

distances = {"Customer 1" : 
                    {'DHL' : 55.94, 
                    'Pos Laju' : 63.24,
                    'NinjaVan' : 99.03,
                    'JNT' : 124.95,
                    'GDex' : 61.01},
            "Customer 2" : 
                    {'DHL' : 47.52, 
                    'Pos Laju' : 55.02,
                    'NinjaVan' : 70.25,
                    'JNT' : 105.96,
                    'GDex' : 77.02},
            "Customer 3" : 
                    {'DHL' : 83.51, 
                    'Pos Laju' : 53.56,
                    'NinjaVan' : 111.776,
                    'JNT' : 52.39,
                    'GDex' : 72.43}
            }

pd = {}

for cust in distances:
    min = 9999
    pd[cust] = {}
    for courier in distances.get(cust):
        d = distances.get(cust).get(courier)
        pd[cust][courier] = round(d - d * couriers.get(courier)[0], 2)
        if (d < min):
            min = d
            min_courier = courier


print("Weighted score = distance - distance*positivity\n")

for cust in pd:
    min_pd = 999
    min_dist = 999
    print("For %s, weighted score of distance and positivity are:" % (cust))
    for courier in pd.get(cust):
        print(" -%s = %.2f" % (courier,  pd.get(cust).get(courier)))
        if (pd.get(cust).get(courier) < min_pd):
            min_pd = pd.get(cust).get(courier)
            min__pd_courier = courier
        if (distances.get(cust).get(courier) < min_dist):
            min_dist = distances.get(cust).get(courier)
            min__dist_courier = courier
    print("\nMinimum Probability -> %s with score of %.2f" % (min__pd_courier,min_pd))
    print("Minimum Distance    -> %s with score of %.2f\n\n" % (min__dist_courier,min_dist))

