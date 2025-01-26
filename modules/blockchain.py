from web3 import Web3 
from config import INFURA_URL

def connect_to_ethereum():
    # Connect to the ethereum network for Trail
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))
    if web3.is_connected():
        print("Connected to Ethereum network")
        return web3
    else:
        raise ConnectionError("Failed to connect to Ethereum network")

def get_contract_instance(web3, contract_address, abi):
    return web3.eth.contract(address=contract_address, abi=abi)

def fetch_token_url(contract, token_id):
    return contract.functions.tokenURL(token_id).call()