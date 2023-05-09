from py_filecoin_api_client import FilecoinAPI

# Create a new wallet
wallet = FilecoinAPI.create_wallet()

# Get the wallet address and private key
address = wallet['address']
private_key = wallet['private_key']

print(f"Wallet Address: {address}")
print(f"Private Key: {private_key}")
