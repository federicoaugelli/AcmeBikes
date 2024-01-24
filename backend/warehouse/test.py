from zeep import Client

# Create a Zeep client
client = Client(wsdl='myWsdl.wsdl')

# Create a request payload
request_payload = {
    'test': 'your_test_value'
}

# Make the SOAP call
response = client.service.getStatus(**request_payload)

# Print the response
print(response)