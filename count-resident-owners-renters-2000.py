############################################################################
# Script to extract various statistics about the number of people in 
# each neighborhood council that rent, own.  For 2000

from qgis.core import *

nc_layer = QgsProject.instance().mapLayersByName('NC_Neighborhoods')[0]
features = nc_layer.getFeatures()
centroidLayer = QgsProject.instance().mapLayersByName('block_centroids_westchester_playa_2000')[0]
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
            owner_1 = centroid['DEC00_HC01_VC07']
            owner_2 = centroid['DEC00_HC01_VC08']
            owner_3 = centroid['DEC00_HC01_VC09']
            owner_4 = centroid['DEC00_HC01_VC10']
            owner_5 = centroid['DEC00_HC01_VC11']
            owner_6 = centroid['DEC00_HC01_VC12']
            owner_7 = centroid['DEC00_HC01_VC13']
            
            renter_1 = centroid['DEC00_HC01_VC15']
            renter_2 = centroid['DEC00_HC01_VC16']
            renter_3 = centroid['DEC00_HC01_VC17']
            renter_4 = centroid['DEC00_HC01_VC18']
            renter_5 = centroid['DEC00_HC01_VC19']
            renter_6 = centroid['DEC00_HC01_VC20']
            renter_7 = centroid['DEC00_HC01_VC21']
            
            current_owners += (owner_1 * 1) + (owner_2 * 2) + \
                             (owner_3 * 3) + (owner_4 * 4) + \
                             (owner_5 * 5) + (owner_6 * 6) + \
                             (owner_7 * 7)
            current_renters += (renter_1 * 1) + (renter_2 * 2) + \
                             (renter_3 * 3) + (renter_4 * 4) + \
                             (renter_5 * 5) + (renter_6 * 6) + \
                             (renter_7 * 7)

    neighborhoods.update({district : {'owned_residents': current_owners, 'rented_residents': current_renters}})
    current_owners = 0
    current_renters = 0
            
print(neighborhoods)
    
    