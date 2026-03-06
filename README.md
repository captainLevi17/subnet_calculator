# Subnet Calculator in Python

A simple, interactive command-line tool for calculating IPv4 subnet information. Enter an IP address and subnet mask (in CIDR or dotted-decimal format), and get the network address, broadcast address, usable hosts, and IP range instantly.

## Features

- **Input Flexibility**: Accepts IPv4 addresses with CIDR notation (e.g., /24) or traditional subnet masks (e.g., 255.255.255.0).
- **Comprehensive Calculations**:
  - Network address
  - Broadcast address
  - Number of usable hosts (2^(32 - CIDR) - 2)
  - Range of usable IP addresses
- **Input Validation**: Ensures valid IPs, CIDRs (0-32), and subnet masks.
- **User-Friendly Interface**: Interactive prompts with examples and error handling.

Useful for network engineers, students, or anyone learning IP subnetting.

## Requirements

- Python 3.6 or higher (uses built-in `ipaddress` module—no external dependencies).

## Installation

1. Clone or download the repository.
2. Ensure Python 3 is installed: `python3 --version`.
3. Run the script: `python3 subnet_calculator.py`.

## Usage

1. Run the program: `python3 subnet_calculator.py`.
2. Enter an IPv4 address (e.g., `192.168.1.100`).
3. Choose input method: CIDR (e.g., `24`) or subnet mask (e.g., `255.255.255.0`).
4. View the results!

### Example

```
Enter an IPv4 address: 192.168.1.100

Choose input method for subnet mask:
a) CIDR notation (e.g., 24)
b) Subnet mask (e.g., 255.255.255.0)

Choice: a
Enter CIDR (e.g., 24): 24

Results:
Network Address: 192.168.1.0
Subnet Mask: 255.255.255.0(/24)
Broadcast Address: 192.168.1.255
Number of Usable Hosts: 254
Usable IP Range: 192.168.1.1 - 192.168.1.254
```

## How It Works

1. **Input**: User provides an IP and subnet info.
2. **Validation**: Checks for valid IPv4 and subnet formats.
3. **Calculations**:
   - **Network Address**: IP & subnet mask (bitwise AND).
   - **Broadcast Address**: IP | (~subnet mask & 0xFFFFFFFF) (bitwise OR with inverted mask).
   - **Usable Hosts**: 2^(32 - CIDR) - 2 (excludes network and broadcast).
   - **IP Range**: Network + 1 to Broadcast - 1.
4. **Output**: Displays all results clearly.

## Contributing

Feel free to submit issues or pull requests. Author: MLSG.

## License

MIT License

## Future Enhancements

Support for IPv6 addresses

Add a GUI using tkinter

Subnetting: divide a network into smaller subnets

Export results to CSV or text file

