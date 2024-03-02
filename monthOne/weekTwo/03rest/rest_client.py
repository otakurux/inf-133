import requests

def get_names_starting_with_initial(initial):
    url = f"http://localhost:8000/buscar_nombre/{initial}"
    response = requests.get(url)
    name_initial = response.json()
    return name_initial

initial = 'p'
name_initial = get_names_starting_with_initial(initial)
print("\n   Names that start with the initial '{}':".format(initial))
for name in name_initial:
    print(name)


def get_student_count_per_major():
    url = "http://localhost:8000/contar_carreras"
    response = requests.get(url)
    count_per_major = response.json()
    return count_per_major

student_count_per_major = get_student_count_per_major()
print("\n   Student count per major:")
for major, count in student_count_per_major.items():
    print("{}: {}".format(major, count))
