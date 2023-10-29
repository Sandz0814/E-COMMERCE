import requests
import json

ss_url = "C:\\Users\\Sandz\\PycharmProjects\\E-COMMERCE_TESTING\\screenshot\\"
url = "https://www.saucedemo.com/"
username = "user-name"
passwords = "password"
login = "login-button"

# pull username and password to the nodejs server
uri = "http://localhost:3000/posts"
# Send GET request
response = requests.get(uri)

# Parse response to json format
item = json.loads(response.text)

for data in item:
    user = data['user_name']
    passw = data['pass_word']













