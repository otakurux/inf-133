import requests
import json
url = "http://localhost:8000"

def in_line_post():
    response = requests.get(f"{url}/posts")
    print(response.text)
    # for date in response.text:
    #     print(date)
        # print(date["content"])

in_line_post()
# print(response.text)

