import ipaddress  # For IP address validation and manipulation

def validate_ip(ip):
    """
    Validates if the given string is a valid IPv4 address.
    Returns True if valid, False otherwise.
    """
    pass  # TODO: Implement IP validation using ipaddress.IPv4Address

def cidr_to_subnet_mask(cidr):
    """
    Converts a CIDR notation (e.g., 24) to a subnet mask string (e.g., '255.255.255.0').
    """
    pass  # TODO: Calculate subnet mask from CIDR

def subnet_mask_to_cidr(mask):
    """
    Converts a subnet mask string (e.g., '255.255.255.0') to CIDR notation (e.g., 24).
    """
    pass  # TODO: Calculate CIDR from subnet mask

def calculate_network_address(ip, mask):
    """
    Calculates the network address from IP and subnet mask.
    Returns the network address as a string.
    """
    pass  # TODO: Use bitwise AND to find network address

def calculate_broadcast_address(ip, mask):
    """
    Calculates the broadcast address from IP and subnet mask.
    Returns the broadcast address as a string.
    """
    pass  # TODO: Use bitwise OR with inverted mask to find broadcast address

def calculate_usable_hosts(cidr):
    """
    Calculates the number of usable hosts for a given CIDR.
    Formula: 2^(32 - CIDR) - 2
    """
    pass  # TODO: Implement the formula

def get_usable_ip_range(network, broadcast):
    """
    Returns the first and last usable IP addresses as a tuple (first, last).
    Excludes network and broadcast addresses.
    """
    pass  # TODO: Increment network by 1 and decrement broadcast by 1

def main():
    """
    Main function to handle user input, validation, calculations, and output.
    """
    print("Subnet Calculator")
    print("=================")
    
    # TODO: Get IP address from user and validate it
    
    # TODO: Ask user to choose CIDR or subnet mask
    
    # TODO: Get the chosen input and convert if necessary
    
    # TODO: Perform calculations
    
    # TODO: Display results

if __name__ == "__main__":
    main()