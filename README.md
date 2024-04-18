# JSON Data Transfer API

This API allows you to transfer JSON data from a microprocessor like a Raspberry Pi to another Raspberry Pi with a WiFi or Ethernet connection.

## Table of Contents
- [API Documentation](#api-documentation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## API Documentation

### POST /data

#### Description
Receives JSON data from the client and processes it.

#### Request
- **Method**: POST
- **URL**: /data
- **Headers**:
  - Content-Type: application/json
- **Body**: JSON data to be transferred

#### Response
- **Status Code**: 200 (on success)
- **Body**:
  ```json
  {
    "status": "success"
  }


## Example Usage

### Python (Client):
```python
import requests
import json

url = 'http://sending-raspberry-pi:5000/data'
data = {'key1': 'value1', 'key2': 'value2'}

response = requests.post(url, json=data)
if response.status_code == 200:
    print('Data sent successfully')
else:
    print('Error sending data')
```

### Python (Server):
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    # Process the received JSON data
    print(data)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

## Error Handling

If there are any issues with the request or the server, the API will return an appropriate HTTP status code and error message in the response body.

## Security Considerations

This API does not include any authentication or authorization mechanisms.

## Limitations

- The maximum size of the JSON data that can be transferred is limited by the memory and processing capabilities of the Raspberry Pis involved.
- The API does not provide any error handling or retry mechanisms for failed data transfers.

## Future Improvements

- Implement support for more robust error handling and retries.
- Add authentication and authorization mechanisms to secure the API.
- Explore the use of message queues or other asynchronous communication patterns to improve scalability and reliability.

## License
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-yellow.svg)](https://github.com/dvlab-research/MiniGemini/blob/main/LICENSE)
