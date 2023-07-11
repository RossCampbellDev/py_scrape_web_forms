import requests
import json
from bs4 import BeautifulSoup

target_url = "https://test-url.com"
headers = {}
page_response = requests.get(target_url, headers)

useful_types = ["text", "password", "date", "hidden", "url", "file", "email", "image", "search"]

if page_response.status_code != 200:
    print(f'Invalid response from {target_url}')
    exit(1)

soup = BeautifulSoup(page_response.content, "html.parser")

inputs = soup.find_all("input")

all_inputs = []

for input in inputs:
    if input.get("type") in useful_types:
        this_input = {}
        this_input[input.get("name")] = [
            input.get("id"),
            input.get("type")
        ]
        all_inputs.append(this_input)
    
inputs_json = json.loads(json.dumps(all_inputs))
print(inputs_json)
