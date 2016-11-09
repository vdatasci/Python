import folium

map_2 = folium.Map(location=[40.7128, -74.0059], tiles='Stamen Toner',
                   zoom_start=13)
folium.Marker(location=[40.7128, -74.0059], popup='The Waterfront').add_to(map_2)
folium.CircleMarker(location=[40.7128, -74.0059], radius=500,
                    popup='Laurelhurst Park', color='#3186cc',
                    fill_color='#3186cc').add_to(map_2)
map_2.save('NewYorkCity.html')
