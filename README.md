# Project Database
import folium
from folium.plugins import MarkerCluster

map = folium.Map(location=[37.5007, 126.8677],
                 zoom_start=15,
                 zoom_control=False,
                 control_scale=True)

folium.Marker(
    [37.5007, 126.8677],
    popup=folium.Popup("동양미래대학교", max_width=100)
).add_to(map)

folium.Marker(
    [37.5000, 126.8670],
    tooltip='위치1'
).add_to(map)

folium.Marker(
    [37.5001, 126.8672],
    popup='위치2',
    icon=folium.Icon()
).add_to(map)

mk3 = folium.Marker(
    [37.5002, 126.8674],
    popup='위치3',
    icon=folium.Icon(color='red', icon='pen-nib', prefix='fa')
)
mk3.add_to(map)

folium.Circle(
    [37.5003, 126.8676],
    popup='위치4',
    color='green'
).add_to(map)

folium.Circle(
    [37.5004, 126.8678],
    popup='위치5',
    color='green',
    radius=100
).add_to(map)

folium.Circle(
    [37.5005, 126.8680],
    popup='위치6',
    color='red',
    radius=300,
    fill=True
).add_to(map)

mc = MarkerCluster().add_to(map)

folium.Marker([37.4009,