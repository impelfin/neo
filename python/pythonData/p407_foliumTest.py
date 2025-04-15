import folium 

latitude = 37.566345
longitude = 126.977893

map_osm = folium.Map(location=[latitude, longitude])
map_osm.save('xx_map1.html')
print(type(map_osm))

map_osm = folium.Map(location=[latitude, longitude], zoom_start=16)
map_osm.save('xx_map2.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17)
folium.TileLayer('OpenTopoMap').add_to(map_osm)
# tiles preview site : https://leaflet-extras.github.io/leaflet-providers/preview
map_osm.save('xx_map3.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17)
folium.Marker([latitude, longitude], popup='서울특별시청').add_to(map_osm)
map_osm.save('xx_map4.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17)
folium.Marker([latitude, longitude], popup='서울특별시청', icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)

folium.CircleMarker([37.5658859, 126.9754788], radius=150, color='blue', fill_color='red', fill=False, popup='덕수궁').add_to(map_osm)
map_osm.save('xx_map5.html')
print('file saved..')

