import requests 
import urllib.parse
 
# Base URL for the GraphHopper routing API
route_url = "https://graphhopper.com/api/1/route?" 
# Default locations for testing
loc1 = "Washington, D.C." 
loc2 = "Baltimore, Maryland"
# Your GraphHopper API key
key = "9914f136-63a3-4712-a624-5e0d4dd506b6"
 
def geocoding(location, key): 
    """
    Geocode a given location using the GraphHopper Geocoding API.
 
    Parameters:
    location (str): The location to geocode.
    key (str): The API key for authentication.
 
    Returns:
    tuple: A tuple containing the status code, latitude, longitude, and formatted location name.
    """
    # Ensure the location is not empty
    while location == "": 
        location = input("Enter the location again: ") 
    # Construct the geocoding API URL
    geocode_url = "https://graphhopper.com/api/1/geocode?" 
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})
    # Make the API request
    replydata = requests.get(url) 
    json_data = replydata.json() 
    json_status = replydata.status_code 
    # Print the geocoding API URL
    print("Geocoding API URL for " + location + ":\n" + url) 
    # Check if the request was successful
    if json_status == 200 and len(json_data["hits"]) != 0:
        # Extract latitude, longitude, and other details
        lat = json_data["hits"][0]["point"]["lat"] 
        lng = json_data["hits"][0]["point"]["lng"] 
        name = json_data["hits"][0]["name"] 
        value = json_data["hits"][0]["osm_value"]
 
        # Extract country and state if available
        country = json_data["hits"][0].get("country", "")
        state = json_data["hits"][0].get("state", "")
        # Format the new location string
        if len(state) != 0 and len(country) != 0: 
            new_loc = name + ", " + state + ", " + country 
        elif len(state) != 0:
            new_loc = name + ", " + country 
        else: 
            new_loc = name
 
        # Print the formatted location
        print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n" + url) 
    else:
        # Handle errors
        lat = "null" 
        lng = "null" 
        new_loc = location 
        print("Geocode API status: " + str(json_status) + "\nError message: " + json_data["message"]) 
    return json_status, lat, lng, new_loc
 
# Main loop for user interaction
while True:
    print("\n+++++++++++++++++++++++++++++++++++++++++++++") 
    print("Vehicle profiles available on Graphhopper:") 
    print("+++++++++++++++++++++++++++++++++++++++++++++") 
    print("car, bike, foot") 
    print("+++++++++++++++++++++++++++++++++++++++++++++")
 
    # List of available vehicle profiles
    profile = ["car", "bike", "foot"] 
    vehicle = input("Enter a vehicle profile from the list above: ")
 
    # Exit conditions
    if vehicle == "quit" or vehicle == "q": 
        break 
    elif vehicle in profile: 
        vehicle = vehicle 
    else: 
        vehicle = "car" 
        print("No valid vehicle profile was entered. Using the car profile.")
 
    # Get starting location from user
    loc1 = input("Starting Location: ") 
    if loc1 == "quit" or loc1 == "q": 
        break 
    orig = geocoding(loc1, key) 
    print(orig)
 
    # Get destination from user
    loc2 = input("Destination: ") 
    if loc2 == "quit" or loc2 == "q": 
        break 
    dest = geocoding(loc2, key)
 
    print("=================================================") 
    # Check if both locations were successfully geocoded
    if orig[0] == 200 and dest[0] == 200:
        # Construct the routing API URL
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2]) 
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2]) 
        paths_url = route_url