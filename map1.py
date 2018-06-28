import folium
map = folium.Map(location=[-41.2562879,174.7854069], zoom_start=8,tiles="Mapbox Bright")

map.add_child(folium.Marker(location=[-41.2562879,174.7854069], popup="Hi I am a marker", icon=folium.Icon(color='green')))

map.save("Map1.html")