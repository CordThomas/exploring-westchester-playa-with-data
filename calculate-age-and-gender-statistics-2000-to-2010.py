############################################################################
# Script to extract data about the age characteristics of each neighborhood.
# Demographic data is from the American FactFinder where I selected:
#    Topics - Year - 2010 (and then 2000)
#    geographics - Block - 100 under Census Tract 140 (this is not one of
#       the most requested geographic types, so you have select the "all geographic
#       types" radio button to see it in the selection list)
#    Topics - People - Basic Count / Estimate - Population Total
#    Downloaded the "SEX BY AGE" table
#  For 2000 data, the data was in Topics - People - Age & Sex
from qgis.core import *
import numpy as np

nc_layer = QgsProject.instance().mapLayersByName('NC_Neighborhoods')[0]
features = nc_layer.getFeatures()
centroidLayer = QgsProject.instance().mapLayersByName('block_centroids_westchester_playa_2000')[0]
centroids = centroidLayer.getFeatures()

neighborhoods = dict()

males = dict()
femails = dict()

for feature in features:
    districtGeometry = feature.geometry()
    district = feature['District']
#    print("our district is {} and di is {}".format(str(district), str(district_index)))
        
    centroids = centroidLayer.getFeatures()
    for centroid in centroids:
        centroidGeometry = centroid.geometry()
        if centroidGeometry.intersects(districtGeometry):
            district_dict = dict()
            for i in range(22):
                key = "D00_VD" + str(i+3).zfill(2)
                print("key {} had centroid value {}".format(key, centroid[key]))
                district_dict.update({key, centroid[key]})

    neighborhoods.update({district :  district_dict})
            
print(neighborhoods)
    
    