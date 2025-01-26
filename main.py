from modules.blockchain import connect_to_ethereum, get_contract_instance, fetch_token_url
from modules.metadata import fetch_metadata
from modules.image_utils import fetch_image, display_image
from modules.cli import get_user_input, display_metadata
from utils.helpers import validate_contact_address

def main():
    print("Starting Trail: Your NFT Metadata Explorer...")

    #connect to ethereum
    web3 = connect_to_ethereum()

    #get user input
    contract_address, token_id = get_user_input()
    validate_contact_address(contract_address)

    #fetch token url 
    erc721_abi = [
        {
            "inputs": [],
            "name": "name",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "symbol",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [{"internalType": "uint256", "name": "tokenid", "type": "uimt256"}],
            "name": "tokenURL",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [{"internalType": "address", "name": "owner", "type": "address"}],
            "name": "balanaceOf",
            "outputs": [{"internalType": "uimt256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}],
            "name": "ownerOf",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {"internalType": "address", "name": "from", "type": "address"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "tokenId", "type": "uimt256"}
            ],
            "name": "safeTransferFrom",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {"internalType": "address", "name": "from", "type": "address"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "tokenId", "type": "uint256"},
                {"internalType": "bytes", "name": "data", "type": "bytes"}
            ],
            "name": "safeTransferFrom",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {"internalType": "address", "name": "from", "type": "address"},
                {"internalType": "uint256", "name": "tokenId", "type": "uint256"}
            ],
            "name": "approve",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {"internalType": "address", "name": "operator", "type": "address"},
                {"internalType": "bool", "name": "approved", "type": "bool"}
            ],
            "name": "setApprovalForAll",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}],
            "name": "getApproved",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {"internalType": "address", "name": "owner", "type": "address"},
                {"internalType": "address", "name": "operator", "type": "address"}
            ],
            "name": "isApprovedForAll",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "statemutability": "view",
            "type": "function"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "internalType": "address", "name": "from", "type": "address"},
                {"indexed": True, "internalType": "address", "name": "to", "type": "address"},
                {"indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256"}
            ],
            "name": "Transfer",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "internalType": "address", "name": "owner", "type": "address"},
                {"indexed": True, "internalType": "address", "name": "approved", "type": "address"},
                {"indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256"}
            ],
            "name": "Approval",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "internalType": "address", "name": "owner", "type": "address"},
                {"indexed": True, "internalType": "address", "name": "operator", "type": "address"},
                {"indexed": False, "internalType": "bool", "name": "approved", "type": "bool"}
            ],
            "name": "ApprovalForAll",
            "type": "event" 
        }
    ]
    contract = get_contract_instance(web3, contract_address, erc721_abi)
    token_url = fetch_token_url(contract, token_id)

    metadata = fetch_metadata(token_url)
    display_metadata(metadata)

    image_data = fetch_image(metadata["image"])
    display_image(image_data)

if __name__ == "__main__":
    main() 