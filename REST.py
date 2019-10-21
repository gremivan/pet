import requests


api_url = 'https://petstore.swagger.io/v2/pet/'
headers = {'accept': 'application/json', 'Content-type': 'application/json'}


def get_pet_by_id(pet_id):
    response = requests.get(api_url + str(pet_id))
    return response.json()


def add_pet(new_pet):
    response = requests.post(api_url, data=new_pet, headers=headers)
    return response.status_code


print(get_pet_by_id(10))

