#!/usr/bin/env python3
import requests, pprint # import requests and pretty print
# the line below will store a PUT transaction with the key requests, the value http for humans, and the response, as the object r
r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans'})
r.status_code # return the status code associated with object r
pprint.pprint(r.json()) # pretty print the json associated with object r
print('*******************')
r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans, version 2'})
r.status_code
pprint.pprint(r.json())
print('*******************')
r = requests.get("http://127.0.0.1:2379/v2/keys/requests")
r.status_code
pprint.pprint(r.json())
