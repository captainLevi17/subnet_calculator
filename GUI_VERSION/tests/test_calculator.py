"""
Unit tests for the Subnet Calculator core functions.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.calculator import (
    validate_ip,
    cidr_to_subnet_mask,
    subnet_mask_to_cidr,
    calculate_network_address,
    calculate_broadcast_address,
    calculate_usable_hosts,
    get_usable_ip_range,
    perform_subnet_calculation
)


class TestValidateIP:
    """Tests for IP validation."""
    
    def test_valid_ips(self):
        assert validate_ip("192.168.1.1") == True
        assert validate_ip("10.0.0.0") == True
        assert validate_ip("255.255.255.255") == True
        assert validate_ip("0.0.0.0") == True
    
    def test_invalid_ips(self):
        assert validate_ip("256.1.1.1") == False
        assert validate_ip("192.168.1") == False
        assert validate_ip("192.168.1.1.1") == False
        assert validate_ip("abc.def.ghi.jkl") == False
        assert validate_ip("") == False


class TestCIDRToSubnetMask:
    """Tests for CIDR to subnet mask conversion."""
    
    def test_common_cidrs(self):
        assert cidr_to_subnet_mask(24) == "255.255.255.0"
        assert cidr_to_subnet_mask(16) == "255.255.0.0"
        assert cidr_to_subnet_mask(8) == "255.0.0.0"
        assert cidr_to_subnet_mask(32) == "255.255.255.255"
        assert cidr_to_subnet_mask(0) == "0.0.0.0"
    
    def test_edge_cases(self):
        assert cidr_to_subnet_mask(25) == "255.255.255.128"
        assert cidr_to_subnet_mask(30) == "255.255.255.252"
        assert cidr_to_subnet_mask(31) == "255.255.255.254"


class TestSubnetMaskToCIDR:
    """Tests for subnet mask to CIDR conversion."""
    
    def test_common_masks(self):
        assert subnet_mask_to_cidr("255.255.255.0") == 24
        assert subnet_mask_to_cidr("255.255.0.0") == 16
        assert subnet_mask_to_cidr("255.0.0.0") == 8
        assert subnet_mask_to_cidr("255.255.255.255") == 32
        assert subnet_mask_to_cidr("0.0.0.0") == 0
    
    def test_invalid_masks(self):
        try:
            subnet_mask_to_cidr("255.255.255.256")
            assert False, "Should raise ValueError"
        except ValueError:
            pass
        
        try:
            subnet_mask_to_cidr("192.168.1.1")
            assert False, "Should raise ValueError"
        except ValueError:
            pass


class TestCalculateNetworkAddress:
    """Tests for network address calculation."""
    
    def test_class_c_networks(self):
        assert calculate_network_address("192.168.1.100", "255.255.255.0") == "192.168.1.0"
        assert calculate_network_address("192.168.1.1", "255.255.255.0") == "192.168.1.0"
        assert calculate_network_address("192.168.1.255", "255.255.255.0") == "192.168.1.0"
    
    def test_class_b_networks(self):
        assert calculate_network_address("172.16.5.130", "255.255.0.0") == "172.16.0.0"
        assert calculate_network_address("172.16.255.255", "255.255.0.0") == "172.16.0.0"
    
    def test_class_a_networks(self):
        assert calculate_network_address("10.20.30.40", "255.0.0.0") == "10.0.0.0"


class TestCalculateBroadcastAddress:
    """Tests for broadcast address calculation."""
    
    def test_class_c_networks(self):
        assert calculate_broadcast_address("192.168.1.100", "255.255.255.0") == "192.168.1.255"
        assert calculate_broadcast_address("192.168.1.1", "255.255.255.0") == "192.168.1.255"
    
    def test_class_b_networks(self):
        assert calculate_broadcast_address("172.16.5.130", "255.255.0.0") == "172.16.255.255"
    
    def test_class_a_networks(self):
        assert calculate_broadcast_address("10.20.30.40", "255.0.0.0") == "10.255.255.255"


class TestCalculateUsableHosts:
    """Tests for usable hosts calculation."""
    
    def test_common_cidrs(self):
        assert calculate_usable_hosts(24) == 254
        assert calculate_usable_hosts(16) == 65534
        assert calculate_usable_hosts(8) == 16777214
    
    def test_edge_cases(self):
        assert calculate_usable_hosts(30) == 2
        assert calculate_usable_hosts(31) == 2  # Point-to-point
        assert calculate_usable_hosts(32) == 0  # Single host


class TestGetUsableIPRange:
    """Tests for usable IP range calculation."""
    
    def test_standard_networks(self):
        first, last = get_usable_ip_range("192.168.1.0", "192.168.1.255")
        assert first == "192.168.1.1"
        assert last == "192.168.1.254"
    
    def test_small_networks(self):
        first, last = get_usable_ip_range("192.168.1.0", "192.168.1.3")
        assert first == "192.168.1.1"
        assert last == "192.168.1.2"


class TestPerformSubnetCalculation:
    """Tests for complete subnet calculation."""
    
    def test_calculation_with_cidr(self):
        result = perform_subnet_calculation("192.168.1.100", "cidr", "24")
        
        assert result['ip'] == "192.168.1.100"
        assert result['network'] == "192.168.1.0"
        assert result['broadcast'] == "192.168.1.255"
        assert result['mask'] == "255.255.255.0"
        assert result['cidr'] == 24
        assert result['usable_hosts'] == 254
        assert result['first_usable'] == "192.168.1.1"
        assert result['last_usable'] == "192.168.1.254"
    
    def test_calculation_with_subnet_mask(self):
        result = perform_subnet_calculation("10.0.0.50", "mask", "255.255.0.0")
        
        assert result['ip'] == "10.0.0.50"
        assert result['network'] == "10.0.0.0"
        assert result['broadcast'] == "10.0.255.255"
        assert result['cidr'] == 16
        assert result['usable_hosts'] == 65534
    
    def test_invalid_ip(self):
        try:
            perform_subnet_calculation("256.1.1.1", "cidr", "24")
            assert False, "Should raise ValueError"
        except ValueError as e:
            assert "Invalid IP" in str(e)
    
    def test_invalid_cidr(self):
        try:
            perform_subnet_calculation("192.168.1.1", "cidr", "33")
            assert False, "Should raise ValueError"
        except ValueError as e:
            assert "CIDR" in str(e)


# Run tests if executed directly
if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
