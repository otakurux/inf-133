import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

mi_pizza = {
    "size": "Grande",
    "mass": "Delgada",
    "toppings": ["Jamon", "Queso"]
}

response = requests.post(url, json=mi_pizza, headers=headers)
print(response.json())