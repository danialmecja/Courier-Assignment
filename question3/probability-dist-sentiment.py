import matplotlib
import gmplot

# 'courier' : [name, positivity]

couriers = {'DHL': [0.661, 3.2127230893650065, 101.57467295692778],
             'Pos Laju': [0.61, 3.112924170027219, 101.63982650389863], 
             'Ninja-Van': [0.804, 3.0319924887507144, 101.37344116244806], 
             'J&T': [0.636, 2.9441205329488325, 101.7901521759029], 
             'GDEX': [0.711, 3.265154613796736, 101.68024844550233]}

distances = [[["DHL",53.944], ["GDEX",61.078], ["Pos Laju",63.230], ["Ninja-Van",99.022], ["J&T",124.942]],
            [["DHL",47.523], ["Pos Laju",56.006], ["Ninja-Van",70.249], ["GDEX",77.009], ["J&T",105.959]],
            [["J&T",52.392], ["Pos Laju",54.168], ["GDEX",72.422], ["DHL",83.508], ["Ninja-Van",111.776]]]

hubs = [[3.0319924887507144, 101.37344116244806, "Ninja-Van", "Port Klang"],
        [3.112924170027219, 101.63982650389863, "Pos Laju", "Petaling Jaya"],
        [3.265154613796736, 101.68024844550233, "GDEX", "Batu Caves"],
        [2.9441205329488325, 101.7901521759029, "J&T", "Kajang"],
        [3.2127230893650065, 101.57467295692778, "DHL", "Sungai Buloh"]]

origin_cord = [[3.3615395462207878, 101.56318183511695, "Rawang"],
               [3.049398375759954, 101.58546611160301, "Subang Jaya"],
               [3.141855957281073, 101.76158583424586, "Ampang"]]

dest_cord = [[3.1000170516638885, 101.53071480907951, "Bukit Jelutong"],
             [3.227994355250716, 101.42730357605375, "Puncak Alam"],
             [2.9188704151716256, 101.65251821655471, "Cyberjaya"]]

apikey = 'AIzaSyAEmwryz_HN3i80CoDeHu_oCuv_91vIIkI'  # (your API key here)

style = [
    {
        "featureType": "administrative.locality",
        "stylers": [
            {"visibility":"off"}
        ]
    }
]

gmap = gmplot.GoogleMapPlotter(3.139, 101.6869, 14, title="courier-q3", map_styles=style, apikey=apikey)

def getNextGap(gap):
    gap = (gap * 10)/13
    if gap < 1:
        return 1
    return int(gap)

def combSort(arr):
    n = len(arr)
    gap = n
    swapped = True
 
    while gap !=1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False
        for i in range(0, n-gap):
            if arr[i][1] < arr[i + gap][1]:     ##comparisons based on value[i][0] which stores the distance to be compared
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True

print("Weighted score = (1 - dist_x/dist_sum) * (weight + positvity * (1-weight)\n")

pd = [0]*3
weight = 0.5
for i in range(3):
    sum = 0
    for j in range(5):
        sum += distances[i][j][1]
    arr = [0] * 5
    for j in range(5):
        ##arr[j] = [distances[i][j][0], round( (1 - distances[i][j][1]/sum) * couriers.get(distances[i][j][0])[0] , 4) ]
        arr[j] = [distances[i][j][0], round( (1 - distances[i][j][1]/sum) * (weight + (couriers.get(distances[i][j][0])[0] * (1-weight))), 4)]
    
    combSort(arr)
    pd[i] = arr

print("Courier Weighted Score Rankings\n")
for i in range (3):
    print("  Customer "+str(i+1))
    print("   -Original Courier: "+distances[i][0][0])
    print("   -Updated Courier: "+pd[i][0][0])
    for j in range (5):
        print("    %.4f - %s" % (pd[i][j][1], pd[i][j][0]))
    print()

for i in range(5):
    gmap.marker(hubs[i][0], hubs[i][1], color='blue', title=hubs[i][2])
    gmap.text(hubs[i][0], hubs[i][1], hubs[i][2], color='black')

for i in range(3):
    gmap.text(origin_cord[i][0]-0.01, origin_cord[i][1], origin_cord[i][2], color='black')
    gmap.text(dest_cord[i][0]-0.01, dest_cord[i][1], dest_cord[i][2], color='black')
    gmap.text(origin_cord[i][0], origin_cord[i][1], "Customer "+str(i+1), color='black')
    gmap.text(dest_cord[i][0], dest_cord[i][1], "Customer "+str(i+1), color='black')

    gmap.directions(
            (origin_cord[i][0], origin_cord[i][1]),
            (dest_cord[i][0], dest_cord[i][1]),
            waypoints=[(couriers.get(pd[i][0][0])[1], couriers.get(pd[i][0][0])[2])]
        )

gmap.draw('courier_q3.html')

    
