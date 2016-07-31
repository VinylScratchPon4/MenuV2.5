import base64

encoded = base64.b64encode(b'password')

print(encoded)

decoded = base64.b64decode(b'cGFzc3dvcmQ=')

print(decoded.decode('utf-8'))
