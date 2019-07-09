import numpy as np 
import matplotlib.pyplot as plt  

f = open("greetings.txt", "r")
message = f.read()
print(message)
f.close()

x = np.arange(0, 3 * np.pi, 0.1) 
y = np.sin(x) 
plt.title("sine wave form") 

# Plot the points using matplotlib 
plt.plot(x, y) 
plt.savefig("data/matplot_output.png")
plt.show() 

import geopandas

path = geopandas.datasets.get_path('naturalearth_lowres')
df = geopandas.read_file(path)
# Add a column we'll use later
df['gdp_pp'] = df['gdp_md_est'] / df['pop_est']

boroughs = geopandas.read_file(geopandas.datasets.get_path('nybb')).to_crs(epsg='4326')
injurious_collisions = geopandas.read_file(
    "https://github.com/ResidentMario/geoplot-data/raw/master/nyc-injurious-collisions.geojson")

import geoplot

geoplot.polyplot(df, figsize=(8, 4))

import geoplot.crs as gcrs

ax = geoplot.kdeplot(injurious_collisions.sample(1000),
                     shade=True, shade_lowest=False,
                     clip=boroughs.geometry)
geoplot.polyplot(boroughs, ax=ax)
plt.savefig("data/geopandas_results.png", bbox_inches='tight', pad_inches=0.1)