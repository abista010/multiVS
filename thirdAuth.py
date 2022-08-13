import requests
import json
Headers = {'x-hydra-api-key':'15189024601c48fa94e7dfe62a6a3cb6','x-hydra-user-agent':'Hydra-Cpp/1.132.0','Content-Type':'application/json'}
Body = { "code": "I+MPokHx/JkCFmuHpcEiaqyzIV/BJGsRHnFwTEiKxk6TdlwIaolu4wyL6h5q3C62Ljs3DvzZRN8+oFHMwDtsifmzQftbOxFJUVS9c9ijMO0=","grant_type":"authorization_code" }
req = requests.post("https://prod-network-api.wbagora.com/sessions/auth/token", json=Body, headers=Headers).json()
print(req)