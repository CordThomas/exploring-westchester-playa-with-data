############################################################################
# Script to extract various statistics about the number of people in 
# each neighborhood council that rent, own and then 

from qgis.core import *

nc_layer = QgsProject.instance().mapLayersByName('NC_Neighborhoods')[0]
features = nc_layer.getFeatures()
centroidLayer = QgsProject.instance().mapLayersByName('block_centroids_westchester_playa')[0]
centroids = centroidLayer.getFeatures()

neighborhoods = dict()

current_owners = 0
current_renters = 0

current_owner_1 = 0
current_owner_2 = 0
current_owner_3 = 0
current_owner_4 = 0
current_owner_5 = 0
current_owner_6 = 0
current_renter_1 = 0
current_renter_2 = 0
current_renter_3 = 0
current_renter_4 = 0
current_renter_5 = 0
current_renter_6 = 0

for feature in features:
    districtGeometry = feature.geometry()
    district = feature['District']
#    print("our district is {} and di is {}".format(str(district), str(district_index)))
        
    centroids = centroidLayer.getFeatures()
    for centroid in centroids:
        centroidGeometry = centroid.geometry()
        if centroidGeometry.intersects(districtGeometry):
            owner_1 = centroid['DEC10_HD01_S06']
            owner_2 = centroid['DEC10_HD01_S07']
            owner_3 = centroid['DEC10_HD01_S08']
            owner_4 = centroid['DEC10_HD01_S09']
            owner_5 = centroid['DEC10_HD01_S10']
            owner_6 = centroid['DEC10_HD01_S11']
            owner_7 = centroid['DEC10_HD01_S12']
            
            renter_1 = centroid['DEC10_HD01_S14']
            renter_2 = centroid['DEC10_HD01_S15']
            renter_3 = centroid['DEC10_HD01_S16']
            renter_4 = centroid['DEC10_HD01_S17']
            renter_5 = centroid['DEC10_HD01_S18']
            renter_6 = centroid['DEC10_HD01_S19']
            renter_7 = centroid['DEC10_HD01_S20']
            
            current_owners = (owner_1 * 1) + (owner_2 * 2) + 
                             (owner_3 * 3) + (owner_4 * 4) + 
                             (owner_5 * 5) + (owner_6 * 6) + 
                             (owner_7 * 7)
            current_renters = (renters_1 * 1) + (renters_2 * 2) + 
                             (renters_3 * 3) + (renters_4 * 4) + 
                             (renters_5 * 5) + (renters_6 * 6) + 
                             (renters_7 * 7)

    neighborhoods.update({district : {'owned_residents': current_under, 'rented_residents': current_over}})
    current_owners = 0
    current_renters = 0
            
print(neighborhoods)
    
    