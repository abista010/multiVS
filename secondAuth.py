import requests
import json
Headers = {'x-hydra-api-key':'51586fdcbd214feb84b0e475b130fce0','x-hydra-user-agent':'Hydra-Cpp/1.132.0','Content-Type':'application/json','x-hydra-client-id':'47201f31-a35f-498a-ae5b-e9915ecb411e'}
Body = { "auth": { "fail_on_missing": 1, "steam": "080110b4bdc0cf071800203a2a70c6f422ada50b0c9b35cc973c9d3a26e1986282d3c8ba04659bf6e569d9a7fc5e557ce6baa0ada0111596686d0a8e66d8f5affa7a310da4cc417f8de729eaedb7af4180977f005d27f143b1d6fd31bb7facae7e9b5316450ba55ca45fdc1351c47ab833e0ebe865e7a52432b81da20d68" }, "options": [ "wb_network" ] }
req = requests.post("https://dokken-api.wbagora.com/access", json=Body, headers=Headers).json()
print(req)