import requests
import json
Headers = {'x-hydra-api-key':'15189024601c48fa94e7dfe62a6a3cb6','x-hydra-user-agent':'Hydra-Cpp/1.132.0','Content-Type':'application/json'}
Body = { "code": "I+MPokHx/JkCFmuHpcEiaiJmCYbyeDHQaj10VwxkbYbr6p2eGAE9cLkva9kUG3Uy7KTHiRJVXw0+oFHMwDtsiUs6DefsGFTJneEkwQYDQGc=","grant_type":"authorization_code" }
req = requests.post("https://prod-network-api.wbagora.com/sessions/auth/token", json=Body, headers=Headers).json()
print(req)