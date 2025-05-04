# Simplest possible example using maplibre
# Install required packages:
# pip install py-maplibre geojson shapely

import os
from maplibre import Map, MapOptions
from maplibre.sources import GeoJSONSource
from maplibre.basemaps import Carto
from maplibre import Layer, LayerType
import geojson
from shapely.geometry import Point

# 1. Create a single point feature
point_geometry = Point(-74.0060, 40.7128)  # NYC coordinates (longitude, latitude)
feature = geojson.Feature(
    geometry=point_geometry,
    properties={"name": "New York City"}
)
feature_collection = geojson.FeatureCollection([feature])

# 2. Create a simple map centered on the point
map_options = MapOptions(
    style=Carto.POSITRON,  # Simple basemap style
    center=(-74.0060, 40.7128),  # Center on NYC
    zoom=12,  # City level zoom
)
m = Map(map_options)

# 3. Add the point to the map
m.add_source("point-source", GeoJSONSource(data=feature_collection))

# 4. Create a simple circle layer to display the point
point_layer = Layer(
    type=LayerType.CIRCLE,
    id="point-layer",
    source="point-source",
    paint={
        "circle-radius": 8,
        "circle-color": "#ff0000",  # Red circle
        "circle-stroke-width": 1,
        "circle-stroke-color": "#ffffff"  # White border
    }
)
m.add_layer(point_layer)

# 5. Add a tooltip
m.add_tooltip("point-layer", "name")

# 6. Save the map to HTML
output_file = "simple_map.html"
m.to_html(output_file)
#m.save(preview=True)

print(f"Map saved to: {os.path.abspath(output_file)}")
print("Open the HTML file in your browser to view the map.")