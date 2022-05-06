# import requests
#
url = "http://localhost:8000/api/location/?active=1"
#
# payload = ""
# headers = {
#   'origin': 'https://test-for-coronavirus.service.gov.uk'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
#


import requests
import json

# url = "localhost:8000/api/location/"

payload = json.dumps({
  "city": "timisoara",
  "country": "romania"
})
headers = {
  'origin': 'https://test-for-coronavirus.service.gov.uk',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
