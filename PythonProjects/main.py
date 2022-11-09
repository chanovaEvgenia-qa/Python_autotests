import requests

response = requests.post("https://petstore.swagger.io/v2/pet" ,json={
  "id": 5000,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Rex",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response = requests.put("https://petstore.swagger.io/v2/pet" ,json={
  "id": 5000,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Flaffy",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response = requests.get("https://petstore.swagger.io/v2/pet/5000")
print(response.text)
print(response.status_code)