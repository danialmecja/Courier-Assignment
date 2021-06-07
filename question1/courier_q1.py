import gmplot
import requests
from requests.exceptions import HTTPError

results =   {
            "Customer 1":{"DHL":53.944, "GDEX":61.078, "Pos Laju":63.230, "Ninja-Van":99.022, "J&T":124.942},
            "Customer 2":{"DHL":47.523, "Pos Laju":56.006, "Ninja-Van":70.249, "GDEX":77.009, "J&T":105.959},
            "Customer 3":{"J&T":52.392, "Pos Laju":54.168, "GDEX":72.422, "DHL":83.508, "Ninja-Van":111.776}
            }

# Create the map plotter:
apikey = 'AIzaSyAEmwryz_HN3i80CoDeHu_oCuv_91vIIkI'  # (your API key here)

style = [
    {
        "featureType": "administrative.locality",
        "stylers": [
            {"visibility":"off"}
        ]
    }
]

gmap = gmplot.GoogleMapPlotter(3.139, 101.6869, 14, title="courier-q1", map_styles=style, apikey=apikey)

def getDistance(origin, destination):
    try:
        response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={},{}&destinations={},{}&key={}".
                                format(origin[0],origin[1],destination[0],destination[1],'AIzaSyAEmwryz_HN3i80CoDeHu_oCuv_91vIIkI'))
        response.raise_for_status()
        jsonResponse = response.json()['rows'][0]["elements"][0]["distance"]["value"]
        return int(jsonResponse)


    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

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
            if arr[i][0] > arr[i + gap][0]:     ##comparisons based on value[i][0] which stores the distance to be compared
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True


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


for i in range(5):
    gmap.marker(hubs[i][0], hubs[i][1], color='blue', title=hubs[i][2])
    gmap.text(hubs[i][0], hubs[i][1], hubs[i][2], color='black')


distances = [0]*3

print("Orgin to Destinations Distanaces\n")
for i in range(3):
    print(" Customer {} - {} to {}".format(i+1, origin_cord[i][2], dest_cord[i][2]))
    print("     -Distance : {} KM\n".format(getDistance(origin_cord[i], dest_cord[i])/1000))
    gmap.text(origin_cord[i][0]-0.01, origin_cord[i][1], origin_cord[i][2], color='black')
    gmap.text(dest_cord[i][0]-0.01, dest_cord[i][1], dest_cord[i][2], color='black')
    gmap.text(origin_cord[i][0], origin_cord[i][1], "Customer "+str(i+1), color='black')
    gmap.text(dest_cord[i][0], dest_cord[i][1], "Customer "+str(i+1), color='black')

print("Nearest Hub for Given Customer")
for i in range(3):
    print("\n    For customer {}, delivering from {} to {}\n".format(i+1, origin_cord[i][2], dest_cord[i][2]))
    arr = [0]*5     ## stores the distance distances for each courier for a given customer, along with courier cords, name and location
    for j in range(5):
        distance = getDistance(origin_cord[i], hubs[j]) + getDistance(hubs[j], dest_cord[i])
        arr[j] = [round(distance/1000, 3), hubs[j][0], hubs[j][1] ,hubs[j][2], hubs[j][3]]
        print("         Customer {} via {} hub : {} KM".format(i+1, hubs[j][2], distance/1000))

    combSort(arr)       ## comb sorts the array
    distances[i] = arr

    print("\n     -Nearest hub : {} located at {}".format(arr[0][3], arr[0][4]))
    print("         Distance: {} KM".format(arr[0][0]))
    gmap.directions(
        (origin_cord[i][0], origin_cord[i][1]),
        (dest_cord[i][0], dest_cord[i][1]),
        waypoints=[(arr[0][1], arr[0][2])]
    )
    print("     ")

print(distances)

# Draw the map:
gmap.draw('courier_q1.html')




