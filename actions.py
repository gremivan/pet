


def test_add_pet():
    result = actions.Pet.add_pet()
    print(result)
    if result is 200:
        print('Pet added')
    else:
        print('Pet did not add')

def test_find_pet_by_id(id=10):
    result = actions.Pet.get_pet_by_id(id)
    print(result)

def test_pet_update():
    result=actions.Pet.update_pet()
    print(result)

def test_remove_pet():
    pet_id = 6
    result = actions.Pet.remove_pet(pet_id)
    print(result)
    result = actions.Pet.get_pet_by_id(pet_id)
    if result is not 200:
        print('Ok',result )
