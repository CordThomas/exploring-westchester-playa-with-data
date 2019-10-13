from qgis.core import *

nc_layer = QgsProject.instance().mapLayersByName('NC_Neighborhoods')[0]
features = nc_layer.getFeatures()
centroidLayer = QgsProject.instance().mapLayersByName('block_centroids_westchester_playa')[0]
centroids = centroidLayer.getFeatures()

neighborhoods = dict()

district_index = 0

current_under = 0
current_over = 0
for feature in features:
    districtGeometry = feature.geometry()
    district = feature['District']
    print("our district is {}".format(str(district)))
    if district_index != 0 and district_index != district:
        neighborhoods[district] = {'under': under_18, 'over': over_18}
        current_under = 0
        current_over = 0
        
    for centroid in centroids:
        centroidGeometry = centroid.geometry()
        if centroidGeometry.intersects(districtGeometry):
            under_18 = centroid['DEC_10_S_3']
            over_18 = centroid['DEC_10_S_4']
            current_under += under_18
            current_over += over_18
            
            print("For District {} we found under {} and over {}".format(str(district), str(under_18), str(over_18)))
            
neighborhoods[district] = {'under': current_under, 'over': current_over}

print(neighborhoods)
    
    