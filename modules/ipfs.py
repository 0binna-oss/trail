from config import IPFS_GATEWAY

def resolve_ipfs_url(url):
    # Resolve an IPFS URL to a HTTP gateway URL for TRAIL 
    if url.startswith("ipfs://"):
        return url.replace("ipfs://", IPFS_GATEWAY)
    return url 