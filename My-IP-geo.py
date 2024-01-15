import requests, json

api = "http://ip-api.com/json"

data = requests.get(api).json()
a = ">>"
print(a, "", data['query'])
print(a, "", data['as'])
print(a, "ISP:", data['isp'])
print(a, "Org:", data['org'])
print(a, "Pais:", data['country'])
print(a, "Region:", data['regionName'])
print(a, "City:", data['city'])
print(a, "Zip code:", data['zip'])
print(a, "Timezone:", data['timezone'])

