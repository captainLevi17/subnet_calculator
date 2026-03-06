import ipaddress  # For IP address validation and manipulation
from time import sleep  # Optional: For adding delays in user prompts

def validate_ip(ip):
    """
    Validates if the given string is a valid IPv4 address.
    Returns True if valid, False otherwise.
    """
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False

def cidr_to_subnet_mask(cidr):
    """
    Converts a CIDR notation (e.g., 24) to a subnet mask string (e.g., '255.255.255.0').
    """
    if not (0 <= cidr <= 32):
        raise ValueError("CIDR must be between 0 and 32")
    subnet_mask = []
    for i in range(4):
        if cidr >= 8:
            subnet_mask.append(255)
            cidr -= 8
        else:
            subnet_mask.append(256 - (2 ** (8 - cidr)))
            cidr = 0
    return '.'.join(map(str, subnet_mask))

def subnet_mask_to_cidr(mask):
    """
    Converts a subnet mask string (e.g., '255.255.255.0') to CIDR notation (e.g., 24).
    """
    try:
        mask_obj = ipaddress.IPv4Network(f'0.0.0.0/{mask}', strict=False)
        return mask_obj.prefixlen
    except ValueError:
        raise ValueError("Invalid subnet mask")

def calculate_network_address(ip, mask):
    """
    Calculates the network address from IP and subnet mask.
    Returns the network address as a string.
    """
    ip_int = int(ipaddress.IPv4Address(ip))
    mask_int = int(ipaddress.IPv4Address(mask))
    network_int = ip_int & mask_int
    return str(ipaddress.IPv4Address(network_int))

def calculate_broadcast_address(ip, mask):
    """
    Calculates the broadcast address from IP and subnet mask.
    Returns the broadcast address as a string.
    """
    ip_int = int(ipaddress.IPv4Address(ip))
    mask_int = int(ipaddress.IPv4Address(mask))
    broadcast_int = ip_int | (~mask_int & 0xFFFFFFFF)
    return str(ipaddress.IPv4Address(broadcast_int))

def calculate_usable_hosts(cidr):
    """
    Calculates the number of usable hosts for a given CIDR.
    Formula: 2^(32 - CIDR) - 2
    """
    return (2 ** (32 - cidr)) - 2

def get_usable_ip_range(network, broadcast):
    """
    Returns the first and last usable IP addresses as a tuple (first, last).
    Excludes network and broadcast addresses.
    """
    network_addr = ipaddress.IPv4Address(network)
    broadcast_addr = ipaddress.IPv4Address(broadcast)
    first = str(network_addr + 1)
    last = str(broadcast_addr - 1)
    return first, last

def main():
    """
    Main function to handle user input, validation, calculations, and output.
    """
    print("=================" * 3)
    print("\t\tMLSG's Subnet Calculator")
    print("=================" * 3)

    print("\nWelcome to the Subnet Calculator! This tool helps you \n calculate network information based on an IPv4 address and subnet mask.\n")
    sleep(2)
    print("You can enter the host IP or network IP, and the subnet mask \n in either CIDR notation or traditional format \n to get the network address, broadcast address, number of usable hosts, and the usable IP range.")
    sleep(2)

    while True:
        ip = input("\nEnter an IPv4 address: ").strip()
        if validate_ip(ip):
            break
        print("Invalid IP address. Try again.") 
    
    while True:
        print("\nChoose input method for subnet mask:")
        print("a) CIDR notation (e.g., 24)")
        print("b) Subnet mask (e.g., 255.255.255.0)\n")
    
        choice = input("Choice: ").strip().lower()
        if choice in ['a', 'b']:
            break
        sleep(1)  # Optional: Add a small delay before re-prompting
        print("\nInvalid choice. Try again.")
        sleep(2)
    
    if choice == 'a':
        while True:
            cidr_str = input("Enter CIDR (e.g., 24): ").strip()
            try:
                cidr = int(cidr_str)
                if 0 <= cidr <= 32:
                    mask = cidr_to_subnet_mask(cidr)
                    break
                else:
                    print("CIDR must be between 0 and 32. Try again.")
            except ValueError:
                print("Invalid CIDR. Please enter a number between 0 and 32.")
        
            
    if choice == 'b':
        while True:
            mask = input("Enter subnet mask (e.g., 255.255.255.0): ").strip()
            try:
                cidr = subnet_mask_to_cidr(mask)
                break
            except ValueError:
                print("Invalid subnet mask. Try again.")

        
    
    network = calculate_network_address(ip, mask)
    broadcast = calculate_broadcast_address(ip, mask)
    usable_hosts = calculate_usable_hosts(cidr)
    first_usable, last_usable = get_usable_ip_range(network, broadcast)
    
    print("\nResults:")
    print(f"Network Address: {network}")
    print(f"Subnet Mask: {mask}(/{cidr})")
    print(f"Broadcast Address: {broadcast}")
    print(f"Number of Usable Hosts: {usable_hosts}")
    print(f"Usable IP Range: {first_usable} - {last_usable}\n")

if __name__ == "__main__":
    main()