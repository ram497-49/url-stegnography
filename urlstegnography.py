import base64
def encode_message_in_url(message):
    # Convert message to bytes
    message_bytes = message.encode('ascii')
    # Base64 encode the message
    encoded_message = base64.b64encode(message_bytes)
    # Convert encoded message to a string
    encoded_message_str = encoded_message.decode('ascii')
    return f'https://example.com/{encoded_message_str}'
def decode_message_from_url(url):
    # Get the encoded message from the URL
    encoded_message_str = url.split('/')[-1]
    # Convert the encoded message to bytes
    encoded_message_bytes = encoded_message_str.encode('ascii')
    # Base64 decode the message
    decoded_message = base64.b64decode(encoded_message_bytes)
    decoded_message_str = decoded_message.decode('ascii')
    # Return the decoded message
    return decoded_message_str
message = 'Hello, ram pr '
encoded_url = encode_message_in_url(message)
print('Encoded URL:', encoded_url)
decoded_message = decode_message_from_url(encoded_url)
print('Decoded message:', decoded_message)