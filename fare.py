"""
@author: DHRUVIL
"""

import geopy

from geopy.geocoders import Nominatim

from geopy.distance import geodesic 

geolocator = Nominatim()
loc1 = input("Enter The pickup location :")
loc2 = input("Enter The drop location :")
location = geolocator.geocode(loc1)
location1 = geolocator.geocode(loc2) 
a=((location.latitude, location.longitude))
b=((location1.latitude, location1.longitude))

distance=round((geodesic(a, b).km))

#print(distance)

    

def RickPrice(dist):
    
    intial_distance = 1.5
    price = 18

    if dist == intial_distance:
    
        print("Your Fare will be :"+ str(price))

    elif dist > intial_distance:
        fare = (intial_distance + 12 * dist)
        price = round(fare-1)
        print("Your Fare will be : " + str(price+1))
        
        
def TaxiPrice(dist):
    
    intial_distance = 1.5
    price = 22

    if dist == intial_distance:
    
        print("Your Fare will be :"+ str(price))

    elif dist > intial_distance:
        fare = (intial_distance + 14 * dist)
        price = round(fare)
        print("Your Fare will be : " + str(price+1))

        
def BusPrice(dist):
    
    price = 5
    
    if dist<=5 :
    
        print("Your Fare will be :"+ str(price))

    elif dist>5 and dist<=10 :
        print("Your Fare will be : " + str(price+5))
        
    elif dist>10 and dist<=15 :
        print("Your Fare will be : " + str(price+10))
        
    elif dist>15 :
        print("Your Fare will be : " + str(price+15))
        
#print(TaxiPrice(distance))
 
ride = input("How you want to ride ? Rickshaw or Taxi or Bus.")

if ride=="Rickshaw" or ride=="rickshaw":
    print(RickPrice(distance))
    
elif ride=="Taxi" or ride=="taxi":
    print(TaxiPrice(distance))
    
elif ride=="Bus" or ride=="bus":
    print(BusPrice(distance))       
