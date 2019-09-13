import requests
baseurl="https://www.metaweather.com/api/location/search/?query="
endpointurl="Bangalore"
findurll=baseurl+endpointurl
resp=requests.get(findurll)
print(resp.json())

""" In this above program i searching the Bangalore "worid":"""
"""so i got banglore "woeid" is :2295420.   like below"""

''' [{'title': 'Bangalore', 'location_type': 'City', 'woeid': 2295420, 'latt_long': '12.955800,77.620979'}]'''