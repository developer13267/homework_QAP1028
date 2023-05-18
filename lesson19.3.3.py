import requests
import json

base_url = 'https://petstore.swagger.io/v2'

#получение списка питомцев по статусу
get_url = '/pet/findByStatus'
params_get = {'status': 'available'}
headers_get = {'accept': 'application/json'}

r = requests.get(base_url + get_url, params=params_get, headers=headers_get)
try:
    result = r.json()
except:
    result = r.text
finally:
    print(result)

#создание нового питомца
post_url = '/pet'
headers_post = {'accept': 'application/json', 'Content-Type': 'application/json'}
new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name": "Cat",
  "photoUrls": [
    "cat_foto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "cat"
    }
  ],
  "status": "available"
}
data_post = json.dumps(new_pet)

r = requests.post(base_url + post_url, headers=headers_post, data=data_post)
try:
    result = r.json()
    id_new_pet = result.get('id')
except:
    result = r.text
    id_new_pet = int(result.split(':')[1].split(',')[0])
finally:
    print(result)


#изменение даных питомца
put_url = '/pet'
headers_put = {'accept': 'application/json', 'Content-Type': 'application/json'}
change_pet = {
  "id": id_new_pet,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name": "Catty",
  "photoUrls": [
    "cat_foto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "cat"
    }
  ],
  "status": "available"
}
data_put = json.dumps(change_pet)

r = requests.put(base_url + put_url, headers=headers_put, data=data_put)
try:
    result = r.json()
except:
    result = r.text
finally:
    print(result)

#удаление питомца
del_url = f'/pet/{id_new_pet}'
params_del = {'petId': id_new_pet}

r = requests.delete(base_url + del_url, params=params_del)
try:
    result = r.json()
except:
    result = r.text
finally:
    print(result)

#проверка удалённого питомца по id
get_url = f'/pet/{id_new_pet}'
params_get = {'petId': id_new_pet}
headers_get = {'accept': 'application/json'}

r = requests.get(base_url + get_url, params=params_get, headers=headers_get)
if r:
    try:
        result = r.json()
    except:
        result = r.text
    finally:
        print(result)
else:
    print('Питомец не найден.')
