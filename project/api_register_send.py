# api register and send

import requests

ip = "192.168.6.153"
username = "testing"
password = input("Please enter your password: ")

#only need this once
request = requests.post(f'http://{ip}/register', json={"username": username, "password": password})

answer = request.json()


#login into the server
request = requests.post(f'http://{ip}/login', json={"username": username, "password": password})
#print(request.json())
token = request.json()["access_token"]

new_sensor = {"type": "Temperature", "location": "Asama25", "name": "bob_temp_1", "unit": "C"}
header = {'Authorization': f"Bearer {token}"}
request = requests.post(f'http://{ip}/sensor/new', json=new_sensor, headers=header)
print(request.json())
