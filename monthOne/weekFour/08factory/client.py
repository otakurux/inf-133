import requests

url = "http://localhost:8000/delivery"

headers = {"Content-Type": "application/json"}

def create_vehicle(vehicle_type):
    data = {"vehicle_type": vehicle_type}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print("Error scheduling delivery:", response.text)

vehicle_type_one = "drone"
vehicle_type_two = "motorcycle"
vehicle_type_three = "scout"

create_vehicle(vehicle_type_one)
create_vehicle(vehicle_type_two)
create_vehicle(vehicle_type_three)

    