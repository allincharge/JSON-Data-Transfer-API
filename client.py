import requests
import json

url = 'http://sending-raspberry-pi:5000/data'
data = {'key1': 'value1', 'key2': 'value2'}

response = requests.post(url, json=data)
if response.status_code == 200:
    print('Data sent successfully')
else:
    print('Error sending data')
