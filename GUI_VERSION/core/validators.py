"""
Input validators with error messages for user feedback.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.calculator import validate_ip, subnet_mask_to_cidr, cidr_to_subnet_mask


def validate_ip_with_error(ip):
    """
    Validates IP address and returns detailed error message.
    
    Args:
        ip (str): The IP address to validate.
    
    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    ip = ip.strip()
    if not ip:
        return False, "IP address cannot be empty"
    
    if not validate_ip(ip):
        return False, f"'{ip}' is not a valid IPv4 address (e.g., 192.168.1.100)"
    
    return True, ""


def validate_cidr_with_error(cidr_str):
    """
    Validates CIDR notation and returns error message.
    
    Args:
        cidr_str (str): The CIDR notation to validate.
    
    Returns:
        tuple: (is_valid: bool, error_message: str, cidr_value: int or None)
    """
    cidr_str = cidr_str.strip()
    if not cidr_str:
        return False, "CIDR cannot be empty", None
    
    try:
        cidr = int(cidr_str)
    except ValueError:
        return False, "CIDR must be a number (e.g., 24)", None
    
    if not (0 <= cidr <= 32):
        return False, "CIDR must be between 0 and 32", None
    
    return True, "", cidr


def validate_subnet_mask_with_error(mask_str):
    """
    Validates subnet mask and returns error message.
    
    Args:
        mask_str (str): The subnet mask to validate.
    
    Returns:
        tuple: (is_valid: bool, error_message: str, cidr_value: int or None)
    """
    mask_str = mask_str.strip()
    if not mask_str:
        return False, "Subnet mask cannot be empty", None
    
    try:
        cidr = subnet_mask_to_cidr(mask_str)
        return True, "", cidr
    except ValueError:
        return False, f"'{mask_str}' is not a valid subnet mask (e.g., 255.255.255.0)", None


def validate_subnet_input(ip, method, value):
    """
    Validates complete subnet input and returns errors if any.
    
    Args:
        ip (str): IP address.
        method (str): 'cidr' or 'mask'.
        value (str): CIDR or mask value.
    
    Returns:
        tuple: (is_valid: bool, errors: dict with 'ip', 'subnet' keys)
    """
    errors = {}
    
    # Validate IP
    ip_valid, ip_error = validate_ip_with_error(ip)
    if not ip_valid:
        errors['ip'] = ip_error
    
    # Validate subnet
    if method == 'cidr':
        subnet_valid, subnet_error, _ = validate_cidr_with_error(value)
    elif method == 'mask':
        subnet_valid, subnet_error, _ = validate_subnet_mask_with_error(value)
    else:
        subnet_valid = False
        subnet_error = "Invalid subnet method"
    
    if not subnet_valid:
        errors['subnet'] = subnet_error
    
    return len(errors) == 0, errors
