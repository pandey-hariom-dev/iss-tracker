import requests
import folium
import webbrowser
import time


def position():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json", timeout=10)
        data = response.json()
        latitude = float(data['iss_position']['latitude'])
        longitude = float(data['iss_position']['longitude'])
        print(f"🛸 ISS is at: {latitude}, {longitude}")
        return latitude, longitude
    except:
        print("⚠️ Connection failed, retrying...")
        time.sleep(5)
        return position()


def place(latitude, longitude):
    location = requests.get(f"https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}&api_key=6a1bb36c325c0697848568huqd5bf0b&accept-language=en")
    data = location.json()
    try:
        state = data['address'].get('state', '')
        country = data['address'].get('country', 'Ocean/Unknown')
        return f"{state}, {country}"
    except:
        return "Ocean/Unknown"





position()
webbrowser.open("iss_map.html")






while True:
    latitude, longitude = position() 
    map = folium.Map(location=[latitude, longitude], zoom_start=3, tile="Esri.WorldImagery")
    on_earth = place(latitude, longitude)

    folium.Marker(location=[latitude, longitude],popup=f"🛸ISS is passing from {on_earth}",tooltip="International Space Station").add_to(map)

    map.save("iss_map.html")

    with open("iss_map.html", "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("<head>", "<head><meta http-equiv='refresh' content='10'>")

    with open("iss_map.html", "w", encoding="utf-8") as f:
        f.write(content)

    time.sleep(30)








