import requests
USER_NAME = "krishna27"
TOKEN = "krishnasharma@27"
GRAPH_ID = "graph1"
from datetime import date


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "krishnasharma@27",
    "username": "krishna27",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Masturbation Graph",
    "unit": "commit",
    "type": "int",
    "color": "kuro"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}"

today = date.today().strftime("%Y%m%d")

quantity = input("How many times today did u shake ur PP? ")
post_config = {
    "date": today,
    "quantity": quantity
}
response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)

# update_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{'20230725'}"

# update_config = {
#     "quantity": "1"
# }
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)

# delete_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{today}"
# response = requests.delete(url=delete_endpoint, headers=headers)