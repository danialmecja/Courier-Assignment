import gmplot
import requests
from requests.exceptions import HTTPError

# Create the map plotter:
apikey = 'AIzaSyAEmwryz_HN3i80CoDeHu_oCuv_91vIIkI'  # (your API key here)

map_style = {
    "featureType": "administrative.locality",
    "stylers": [
        {"visibility": "off"}
    ]
}

gmap = gmplot.GoogleMapPlotter(3.139, 101.6869, 14, title="courier-q1", map_styles=map_style, apikey=apikey)

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


hubs = [[3.0319924887507144, 101.37344116244806, "City-Link Express", "Port Klang"],
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




print("Orgin to Destinations Distanaces\n")
for i in range(3):
    print(" Customer {} - {} to {}".format(i+1, origin_cord[i][2], dest_cord[i][2]))
    print("     -Distance : {} KM\n".format(getDistance(origin_cord[i], dest_cord[i])/1000))
    gmap.marker(origin_cord[i][0], origin_cord[i][1], label=i+1, color='green', title=origin_cord[i][2])
    #gmap.text(origin_cord[i][0], origin_cord[i][1], origin_cord[i][2], color='black')
    gmap.marker(dest_cord[i][0], dest_cord[i][1], label=i+1, color='red', title=dest_cord[i][2])
    #gmap.text(dest_cord[i][0], dest_cord[i][1], dest_cord[i][2], color='black')

print("Nearest Hub for Given Customer")
for i in range(3):
    print("\n    For customer {}, delivering from {} to {}\n".format(i+1, origin_cord[i][2], dest_cord[i][2]))
    min = 99999     # stores the minimum distance through a hub
    hub = 0         # stores the index of the nearest hub
    for j in range(5):
        distance = getDistance(origin_cord[i], hubs[j]) + getDistance(hubs[j], dest_cord[i])
        print("         Customer {} via {} hub : {} KM".format(i+1, hubs[j][2], distance/1000))
        if distance<min:
            min = distance
            hub = j


    print("\n     -Nearest hub : {} located at {}".format(hubs[hub][2], hubs[hub][3]))
    origin_to_hub = getDistance(origin_cord[i], hubs[hub])/1000
    hub_to_target = getDistance(hubs[hub], dest_cord[i])/1000
    print("         Distance: {} KM (Origin to Hub: {} KM, Hub to Destination {} KM)".format(origin_to_hub + hub_to_target, origin_to_hub, hub_to_target))
    gmap.directions(
        (origin_cord[i][0], origin_cord[i][1]),
        (dest_cord[i][0], dest_cord[i][1]),
        waypoints=[(hubs[hub][0], hubs[hub][1])]
    )
    print("     ")

# Draw the map:
gmap.draw('courier-q1.html')




