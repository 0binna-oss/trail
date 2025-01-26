def validate_contact_address(address):
    # Validate Ethereum contract address
    if not address.startswith("0x") or len(address) != 42:
        raise ValueError("Invalid contract address.") 