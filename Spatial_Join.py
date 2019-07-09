# import necessary modules
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from geopandas import GeoSeries, GeoDataFrame
import os

# Change Working Directory
path_wd = "C:/Users/tan.m.14/OneDrive - Procter and Gamble/SD Science (Sharing)/13.Vietnam Distribution/VN Distribution Maximisation/Workflow/"
os.chdir(path_wd)

# Read Store Locations from MESA
path_store_loc = "Workflow2-Append NH Polygon/VN_MESA_WF2_input.csv"
df_store_loc = pd.read_csv(path_store_loc)

# Convert to geopandas df
store_loc = GeoDataFrame(df_store_loc, geometry=geopandas.points_from_xy(df_store_loc.Longitude, df_store_loc.Latitude))

path_commune_shp = "C:/Users/tan.m.14/Procter and Gamble/APAC Data Science Team - Documents/Vietnam NAS/1. DataFiles/1.VNShapeFiles/gadm36_VNM_shp/gadm36_VNM_3.shp"
communes = GeoDataFrame.from_file(path_commune_shp)

def Count_Points(gdf_point, gdf_polygon):
    polygon_with_points = geopandas.sjoin(gdf_point, gdf_polygon,  op='within')
    points_count = polygon_with_points.groupby("GID_3").count()["Legacy Store (ID)"]
    
    return polygon_with_points, points_count 
    



# Count stores in each commune
communes_with_stores, commune_storecnt = Count_Points(store_loc, communes)
