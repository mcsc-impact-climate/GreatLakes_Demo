# Great Lakes Demo
This repository contains sample locations and data for return-to-base logistics facilities in the Great Lakes region to demo the use of the [Geo-TIDE tool's](https://danikam16.wixsite.com/mysite/post/accessing-and-using-the-mcsc-s-interactive-geospatial-decision-support-tool-for-trucking-fleet-decar) data upload and overlay feature. 

Instructions on how to use this demo data on the Geo-TIDE tool can be found in [this blog post](zzz).

# How to download the files

To download the contents of the repository as a ZIP file, you can use the following URL in your browser: https://github.com/mcsc-impact-climate/GreatLakes_Demo/archive/refs/heads/main.zip 

# How to create a shapefile from the GeoJSON file

In case changes need to be made to the GeoJSON file [logistics_facilities.geojson](./GeoJSON/logistics_facilities.geojson), the corresponding shapefile can be re-created by execute the `convert_geojson_to_shapefile.py`[./convert_geojson_to_shapefile.py] script:

First, make sure your python installation includes the geopandas module:

```bash
pip install geopandas
```

Then execute the python script from the top level of this repository:

```bash
python convert_geojson_to_shapefile.py 
```
