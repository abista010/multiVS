import requests
import json
Headers = {'x-hydra-api-key':'51586fdcbd214feb84b0e475b130fce0','x-hydra-user-agent':'Hydra-Cpp/1.132.0','Content-Type':'application/json','x-hydra-client-id':'47201f31-a35f-498a-ae5b-e9915ecb411e'}
Body = { "auth": { "fail_on_missing": 1, "steam": "080110f092bac30e1800203a2a70b6b924aeb378209fa80f5092c0fe867332e93a5836048859711aae5e7e44ed047c0de268d252bd7828fb9e8f34e43944c700e2c580ca2afc0e8ef4ac454cb9ed87db6a6a7ff2696866018c0b8e11942d153b809126fe9301db7658a0fb2a15359e6110c6629a4eb07f72f4b90e2b3560" }, "options": [ "wb_network" ] }
req = requests.post("https://dokken-api.wbagora.com/access", json=Body, headers=Headers).json()
print(req)