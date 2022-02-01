import json

with open('output.json') as json_file:
    data = json.load(json_file)
    import base64
    decoded_string = base64.b64decode(data['printData'][0])
    with open('test.pdf', 'wb') as f:
        f.write(decoded_string)
        