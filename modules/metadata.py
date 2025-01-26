import requests
from modules.ipfs import resolve_ipfs_url

def fetch_metadata(token_uri):
    # Fetch and parse NFT metadata for TRAIL
    resolved_url = resolve_ipfs_url(token_uri)
    response = requests.get(resolved_url)
    response.raise_for_status()
    return response.json() 