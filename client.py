#!/usr/bin/env python3

import requests

response = requests.get('http://127.0.0.1:5000/hello')
print(response.status_code, response.text)


