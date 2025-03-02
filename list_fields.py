import arcpy

# Set workspace (change the path to your local GIS data folder)
arcpy.env.workspace = r"E:\Git"

# Input shapefile (Replace 'YourShapefile.shp' with an actual file in your workspace)
shapefile = "surrey-latest-free.shp"

# Print all field names in the shapefile
fields = arcpy.ListFields(shapefile)
print("Fields in the shapefile:")
for field in fields:
    print(field.name)
