import requests
import folium
import webbrowser
import time

def position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    print(f"🛸 ISS is at: {latitude}, {longitude}")
    return latitude, longitude

position()
webbrowser.open("iss_map.html")

while True:
    latitude, longitude = position() 
    map = folium.Map(location=[latitude, longitude], zoom_start=3)


    folium.Marker(location=[latitude, longitude],popup="🛸 ISS is here!",tooltip="International Space Station").add_to(map)

    map.save("iss_map.html")

    with open("iss_map.html", "r") as f:
        content = f.read()
    content = content.replace("<head>", "<head><meta http-equiv='refresh' content='10'>")

    with open("iss_map.html", "w") as f:
        f.write(content)

    time.sleep(10)