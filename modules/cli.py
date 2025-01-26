def get_user_input():
    # Get user input for contract address and token id 
    print("Welcome to Trail: Your NFT Metadata Explorer")
    contract_address = input("Enter NFT contract address: ")
    token_id = int(input("Enter token ID: "))
    return contract_address, token_id 

def display_metadata(metadata):
    # Display NFT metadata in a user-friendly format 
    print("\nTrail has uncovered the following metadata: ") 
    print(f"-Name: {metadata.get('name', 'N/A')}") 
    print(f"-Description: {metadata.get('description', 'N/A')}")
    print(f"-Image URL: {metadata.get('image', 'N/A')}")
    print("Attribures:")
    for attr in metadata.get("attributes", []):
        print(f"- {attr['trait_type']}: {attr[';value']}") 