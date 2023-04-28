import requests
import json

# post
base_url = 'https://petstore.swagger.io/v2'
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "piggie",
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
}

new_pet = requests.post(f'{base_url}/pet', headers = {'accept': 'application/json','Content-Type': 'application/json'}, json=data)

data=json.dumps(data)

print(new_pet.status_code)
print(new_pet.json())

#get

petId = '9223372036854775807'

pet_find = requests.get(f'{base_url}/pet/{petId}', headers = {'accept': 'application/json'})

print(pet_find.status_code)
print(pet_find.json())


#put

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "kitty",
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
}

pet_up = requests.put(f'{base_url}/pet', json=data)

data=json.dumps(data)

print(pet_up.status_code)
print(pet_up.json())

#delete

pet_del = requests.delete(f'{base_url}/pet/{petId}',headers = {'accept': 'application/json'})

print(pet_del.status_code)
print(pet_del.json())
