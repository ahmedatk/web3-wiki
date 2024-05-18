import json
from django.conf import settings
from web3 import Web3

abi_path = settings.ABI_FILE_PATH

try:
    with open(abi_path) as f:
        abi = json.load(f)
except FileNotFoundError:
    print(f"File not found: {abi_path}")
    raise
except json.JSONDecodeError:
    print(f"Invalid JSON in file: {abi_path}")
    raise

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
contract_address = '0x194B2D9DD3172a87138Bcf50F4C1453a27896Bc6'
contract = w3.eth.contract(address=contract_address, abi=abi)

def create_content(ipfs_hash, author_address):
    pass

# def upvote_content(content_id, user_address):
#     pass

# def downvote_content(content_id, user_address):
#     pass