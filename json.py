import requests

# GraphHopper API URLs
geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"

# Locations
loc1 = "Rome, Italy"
loc2 = "Frascati, Italy"

# Your GraphHopper API key
key = "9914f136-63a3-4712-a624-5e0d4dd506b6"

# Geocode the origin (Washington, D.C.)
geocode_params_1 = {
    "key": key,
    "q": loc1
}
geocode_response_1 = requests.get(geocode_url, params=geocode_params_1)
geocode_data_1 = geocode_response_1.json()

# Geocode the destination (Baltimore, Maryland)
geocode_params_2 = {
    "key": key,
    "q": loc2
}
geocode_response_2 = requests.get(geocode_url, params=geocode_params_2)
geocode_data_2 = geocode_response_2.json()

# Check if geocoding was successful
if geocode_data_1['hits'] and geocode_data_2['hits']:
    # Get coordinates from the geocoding response
    orig_lat = geocode_data_1['hits'][0]['point']['lat']
    orig_lon = geocode_data_1['hits'][0]['point']['lng']
    
    dest_lat = geocode_data_2['hits'][0]['point']['lat']
    dest_lon = geocode_data_2['hits'][0]['point']['lng']
    
    # Now, use these coordinates to get the route
    route_params = {
        "key": key,
        "point": [f"{orig_lat},{orig_lon}", f"{dest_lat},{dest_lon}"],  # Use a list for multiple points
        "type": "json",
        "vehicle": "car",
        "locale": "en"
    }
    
    # Make the route request
    route_response = requests.get(route_url, params=route_params)
    route_data = route_response.json()
    
    # Print the route data
    print(route_data)
else:
    print("Geocoding failed. Could not find coordinates for one or both locations.")
