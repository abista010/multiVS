import requests
import json
Headers = {'x-hydra-api-key':'51586fdcbd214feb84b0e475b130fce0','x-hydra-user-agent':'Hydra-Cpp/1.132.0','Content       Type':'application/json','x-hydra-client-id':'47201f31-a35f-498a-ae5b-e9915ecb411e'}
Body = { "auth": { "fail_on_missing": 1, "steam": "080110baf4b0dd0c1800203a2a707346143ef51649d56511937f3a6d67d1a0e1575b704138c7ec7639ca9a79632015317d5d3fe33423658c4ae96badad6cfcac6496e0414ed8e4ba9f2f261bd16acd04266aef884ee67718038cd715b7594e924e3e8bece911f70d8bac32f5b5ab4cc9bd03ff394ec8378f33ddeec9a0a9" }, "options": [ "wb_network" ] }
req = requests.post("https://dokken-api.wbagora.com/access", json=Body, headers=Headers).json()
print(req)