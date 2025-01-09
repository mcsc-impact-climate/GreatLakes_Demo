import geopandas as gpd

# Read the GeoJSON file into a GeoDataFrame
geojson_data = gpd.read_file("GeoJSON/logistics_facilities.geojson")

# Save the GeoDataFrame directly to a Shapefile
shapefile_path = "shapefile/logistics_facilities.shp"
geojson_data.to_file(shapefile_path, driver="ESRI Shapefile")

print(f"Shapefile saved as: {shapefile_path}")
