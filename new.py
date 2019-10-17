
import actions

new_pet = '''
{
  "id": 10,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Bars",
  "photoUrls": [
    "Some nnddn"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
'''


updated_pet = '''
{
  "id": 6,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Bars_updated",
  "photoUrls": [
    "Some nnddn"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
'''

class Pet:
    def get_pet_by_id(pet_id):

        response = requests.get(url+str(pet_id))
        return response.status_code

    def add_pet():
        response = requests.post(url, data=new_pet, headers=headers)
        return response.status_code


    def update_pet():
        response = requests.put(url, data=updated_pet, headers=headers)
        return response.status_code


    def remove_pet(pet_id):
        response = requests.delete(url+str(pet_id))
        return response.status_code

#get_pet_by_id(6)
#add_pet()
#get_pet_by_id(6)
#remove_pet(6)
#update_pet()