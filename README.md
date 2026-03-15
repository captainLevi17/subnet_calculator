# MLSG's subnet calculator

A simple and efficient IPv4 subnet calculator that helps you quickly determine subnet information such as network address, broadcast address, subnet mask, usable hosts, and CIDR notation.

## Features

- Convert between **CIDR notation** and **subnet masks**
- Calculate:
  - Network address
  - Broadcast address
  - First usable host
  - Last usable host
  - Usable IP range
  - Total number of hosts
- Supports all IPv4 subnet ranges
- Fast and lightweight
- Easy to integrate or run as a standalone tool

## Installation

Clone the repository:

- git clone https://github.com/captainLevi17/subnet_calculator.git

## How it works

The calculator uses bitwise operations on IPv4 addresses to determine subnet boundaries.

Steps:

Convert the IPv4 address into a 32-bit binary number.

Apply the subnet mask using a bitwise AND operation.

Determine:

Network address

Broadcast address

Host range

Convert results back into dotted-decimal format.


## Use Cases

Network planning

Subnetting practice for certifications

Infrastructure design

DevOps and cloud networking

Roadmap
 GUI version

 IPv6 subnet support

 Web interface

 API endpoint

 Visualization of subnet ranges

## Contributing

Contributions are welcome!

Fork the repository

Create a feature branch

Commit your changes

Open a pull request

## License

This project is licensed under the MIT License.

## Author

Created by MLSG

Feel free to open issues or suggestions!

