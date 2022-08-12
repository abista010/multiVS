import requests
import json
Headers={'x-hydra-api-key':'51586fdcbd214feb84b0e475b130fce0','x-hydra-user-agent':'Hydra-Cpp/1.132.0','Content-Type':'application/json','x-hydra-access-token':'I+MPokHx/JkCFmuHpcEiajXcdqDjb8SnphNob31YxyQhHf4db4niqcn86Vt3T7+fdXqqrqB4vyk+oFHMwDtsicwg9iAHOaFCaBq3SMTVCg4='}
req=requests.get("https://dokken-api.wbagora.com/matches/all/[62ee8335316e42e50e07ea8b]", headers=Headers).json()
print(req)