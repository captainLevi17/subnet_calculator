"""
Core calculation logic for Subnet Calculator.
Pure utility functions for subnet calculations.
"""

import ipaddress


def validate_ip(ip):
    """
    Validates if the given string is a valid IPv4 address.
    
    Args:
        ip (str): The IP address to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False


def cidr_to_subnet_mask(cidr):
    """
    Converts a CIDR notation (e.g., 24) to a subnet mask string (e.g., '255.255.255.0').
    
    Args:
        cidr (int): CIDR notation between 0 and 32.
    
    Returns:
        str: Subnet mask in dotted-decimal notation.
    
    Raises:
        ValueError: If CIDR is not between 0 and 32.
    """
    if not (0 <= cidr <= 32):
        raise ValueError("CIDR must be between 0 and 32")
    subnet_mask = []
    cidr_copy = cidr
    for i in range(4):
        if cidr_copy >= 8:
            subnet_mask.append(255)
            cidr_copy -= 8
        else:
            subnet_mask.append(256 - (2 ** (8 - cidr_copy)))
            cidr_copy = 0
    return '.'.join(map(str, subnet_mask))


def subnet_mask_to_cidr(mask):
    """
    Converts a subnet mask string (e.g., '255.255.255.0') to CIDR notation (e.g., 24).
    
    Args:
        mask (str): Subnet mask in dotted-decimal notation.
    
    Returns:
        int: CIDR notation.
    
    Raises:
        ValueError: If subnet mask is invalid.
    """
    try:
        mask_obj = ipaddress.IPv4Network(f'0.0.0.0/{mask}', strict=False)
        return mask_obj.prefixlen
    except ValueError:
        raise ValueError("Invalid subnet mask")


def calculate_network_address(ip, mask):
    """
    Calculates the network address from IP and subnet mask.
    
    Args:
        ip (str): IP address.
        mask (str): Subnet mask in dotted-decimal notation.
    
    Returns:
        str: The network address.
    """
    ip_int = int(ipaddress.IPv4Address(ip))
    mask_int = int(ipaddress.IPv4Address(mask))
    network_int = ip_int & mask_int
    return str(ipaddress.IPv4Address(network_int))


def calculate_broadcast_address(ip, mask):
    """
    Calculates the broadcast address from IP and subnet mask.
    
    Args:
        ip (str): IP address.
        mask (str): Subnet mask in dotted-decimal notation.
    
    Returns:
        str: The broadcast address.
    """
    ip_int = int(ipaddress.IPv4Address(ip))
    mask_int = int(ipaddress.IPv4Address(mask))
    broadcast_int = ip_int | (~mask_int & 0xFFFFFFFF)
    return str(ipaddress.IPv4Address(broadcast_int))


def calculate_usable_hosts(cidr):
    """
    Calculates the number of usable hosts for a given CIDR.
    Formula: 2^(32 - CIDR) - 2
    
    Args:
        cidr (int): CIDR notation.
    
    Returns:
        int: Number of usable hosts. Returns 0 for /31 and /32.
    """
    num_hosts = 2 ** (32 - cidr)
    if cidr == 32:
        return 0  # Single host
    elif cidr == 31:
        return 2  # Point-to-point links (RFC 3021)
    else:
        return num_hosts - 2


def get_usable_ip_range(network, broadcast):
    """
    Returns the first and last usable IP addresses as a tuple (first, last).
    Excludes network and broadcast addresses.
    
    Args:
        network (str): Network address.
        broadcast (str): Broadcast address.
    
    Returns:
        tuple: (first_usable_ip, last_usable_ip) as strings. Returns (None, None) for /31 and /32.
    """
    network_addr = ipaddress.IPv4Address(network)
    broadcast_addr = ipaddress.IPv4Address(broadcast)
    
    # For /31 and /32, there are no traditional usable hosts
    if network_addr >= broadcast_addr - 1:
        return None, None
    
    first = str(network_addr + 1)
    last = str(broadcast_addr - 1)
    return first, last


def perform_subnet_calculation(ip, subnet_method, subnet_value):
    """
    Performs complete subnet calculation based on IP and subnet specification.
    
    Args:
        ip (str): IP address.
        subnet_method (str): Either 'cidr' or 'mask'.
        subnet_value (str): CIDR value or subnet mask string.
    
    Returns:
        dict: Dictionary containing all calculation results.
        
    Raises:
        ValueError: If inputs are invalid.
    """
    # Validate IP
    if not validate_ip(ip):
        raise ValueError("Invalid IP address")
    
    # Get mask and CIDR based on method
    if subnet_method == 'cidr':
        try:
            cidr = int(subnet_value)
            if not (0 <= cidr <= 32):
                raise ValueError("CIDR must be between 0 and 32")
            mask = cidr_to_subnet_mask(cidr)
        except ValueError as e:
            raise ValueError(f"Invalid CIDR: {str(e)}")
    elif subnet_method == 'mask':
        try:
            mask = subnet_value
            cidr = subnet_mask_to_cidr(mask)
        except ValueError as e:
            raise ValueError(f"Invalid subnet mask: {str(e)}")
    else:
        raise ValueError("Invalid subnet method")
    
    # Perform calculations
    network = calculate_network_address(ip, mask)
    broadcast = calculate_broadcast_address(ip, mask)
    usable_hosts = calculate_usable_hosts(cidr)
    first_usable, last_usable = get_usable_ip_range(network, broadcast)
    
    return {
        'ip': ip,
        'network': network,
        'broadcast': broadcast,
        'mask': mask,
        'cidr': cidr,
        'usable_hosts': usable_hosts,
        'first_usable': first_usable,
        'last_usable': last_usable
    }
