import requests
from datetime import datetime as dt

"""
Finds the next 5 times the International Space Station will fly over a location. 
Visible 10 degrees above the horizon. 
"""

mb = {"name": "Moses Brown School", "arguments": {"lat": 41.8334, "lon": -71.3985, "alt": 43, "n": 5}}
mb_parameters = mb["arguments"]

iss_response = requests.get("http://api.open-notify.org/iss-pass.json", params=mb_parameters)
iss = iss_response.json()

print("****** ISS Flyover Times ******")
print("Current Time:")
print(dt.today().strftime("%Y-%m-%d %H:%M:%S"))

# Neat printout of response.
for key in ['message', 'request']:
    print("{}: {}".format(key, iss[key]))
for response in iss['response']:
    print(response)

# Summary of response.
print("Next 5 ISS flyover times for {}:".format(mb["name"]))
for response in iss["response"]:
    flyover = str(dt.fromtimestamp(response["risetime"])) + " for " + str(response["duration"]) + " seconds."
    print(flyover)

print("****** Finished ******")
