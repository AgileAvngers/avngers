import urllib.parse
import requests
 
geocode_url = "https://graphhopper.com/api/1/geocode?" 
route_url = "https://graphhopper.com/api/1/route?" 
loc1 = "Washington, D.C." 
loc2 = "Baltimore, Maryland" 
key = "9914f136-63a3-4712-a624-5e0d4dd506b6"
url = geocode_url + urllib.parse.urlencode({"q":loc1, "limit": "1", "key":key})
 
replydata = requests.get(url) 
json_data = replydata.json() 
json_status = replydata.status_code 
print(json_data)