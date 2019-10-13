############################################################################
# Script to extract data about the age characteristics of each neighborhood.

from qgis.core import *

nc_layer = QgsProject.instance().mapLayersByName('NC_Neighborhoods')[0]
features = nc_layer.getFeatures()
centroidLayer = QgsProject.instance().mapLayersByName('block_centroids_westchester_playa_2000')[0]
centroids = centroidLayer.getFeatures()

neighborhoods = dict()

count_own = 0
count_rent = 0

count_u15_own = 0
count_u25_own = 0
count_u35_own = 0
count_u45_own = 0
count_u55_own = 0
count_u65_own = 0
count_u75_own = 0
count_u85_own = 0
count_o85_own = 0

count_u15_rent = 0
count_u25_rent = 0
count_u35_rent = 0
count_u45_rent = 0
count_u55_rent = 0
count_u65_rent = 0
count_u75_rent = 0
count_u85_rent = 0
count_o85_rent = 0

for feature in features:
    districtGeometry = feature.geometry()
    district = feature['District']
#    print("our district is {} and di is {}".format(str(district), str(district_index)))
        
    centroids = centroidLayer.getFeatures()
    for centroid in centroids:
        centroidGeometry = centroid.geometry()
        if centroidGeometry.intersects(districtGeometry):
            count_own = centroid['DEC00_HC01_VC23']
            count_u25_own = centroid['DEC00_HC01_VC24']
            count_u35_own = centroid['DEC00_HC01_VC24']
            count_u45_own = centroid['DEC00_HC01_VC24']
            count_u55_own = centroid['DEC00_HC01_VC24']
            count_u65_own = centroid['DEC00_HC01_VC24']
            count_u75_own = centroid['DEC00_HC01_VC24']
            count_u85_own = centroid['DEC00_HC01_VC24']
            count_o85_own = centroid['DEC00_HC01_VC24']
\            
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
    
    