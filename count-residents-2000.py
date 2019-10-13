from qgis.core import *

nc_layer = QgsProject.instance().mapLayersByName('NC_Neighborhoods')[0]
features = nc_layer.getFeatures()
centroidLayer = QgsProject.instance().mapLayersByName('block_centroids_westchester_playa_2010')[0]
centroids = centroidLayer.getFeatures()

neighborhoods = dict()


total_population = 0

for feature in features:
    districtGeometry = feature.geometry()
    district = feature['District']
#    print("our district is {} and di is {}".format(str(district), str(district_index)))
        
    centroids = centroidLayer.getFeatures()
    for centroid in centroids:
        centroidGeometry = centroid.geometry()
        if centroidGeometry.intersects(districtGeometry):
            total = centroid['TotalPopulation']
            if (isinstance(under_18, int)):
                total_population += total

    neighborhoods.update({district : {'total': total_population}})
    total_population = 0
            
print(neighborhoods)