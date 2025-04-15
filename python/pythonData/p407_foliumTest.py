import folium 

latitude = 37.566345
longitude = 126.977893

map_osm = folium.Map(location=[latitude, longitude])
map_osm.save('xx_map1.html')
print(type(map_osm))