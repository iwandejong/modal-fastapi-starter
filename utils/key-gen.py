import secrets

def generate_api_key(length=32):
  return secrets.token_hex(length)

api_key = generate_api_key()
print("Generated API Key:", api_key)