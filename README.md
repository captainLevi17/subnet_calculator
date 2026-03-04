Subnet Calculator in Python
Project Overview

This project is a simple Subnet Calculator built in Python. It allows users to input an IPv4 address and either a CIDR notation or a subnet mask, then calculates and displays key subnet information:

Network Address

Broadcast Address

Number of Usable Hosts

Range of Usable IP Addresses

This tool is useful for network engineers, students, or anyone learning IP subnetting.

Features

Accepts IPv4 addresses from the user

Lets the user choose between CIDR notation (e.g., /24) or subnet mask (e.g., 255.255.255.0)

Calculates and displays:

Network address

Broadcast address

Number of usable hosts

First and last usable IP addresses

Validates user input for correctness

How It Works

User enters an IP address.

User chooses whether to enter a CIDR or subnet mask.

User enters the chosen format.

The program performs calculations:

Converts IP and subnet to binary

Finds the network address using bitwise AND

Finds the broadcast address using the inverted subnet mask

Determines the number of usable hosts: 2^(32 - CIDR) - 2

Determines the range of usable IP addresses

Results are displayed clearly to the user.

Example Usage
Enter IP address: 192.168.1.10
Do you want to use CIDR or Subnet Mask? (Enter CIDR/Mask): CIDR
Enter CIDR notation (e.g., /24): /24

Results:
IP Address: 192.168.1.10
Subnet Mask: 255.255.255.0
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
First Usable IP: 192.168.1.1
Last Usable IP: 192.168.1.254
Number of Usable Hosts: 254

Project Structure
subnet_calculator/
│
├── subnet_calculator.py   # Main Python program
├── utils.py               # Optional: helper functions for calculations
├── README.md              # Project documentation

Future Enhancements

Support for IPv6 addresses

Add a GUI using tkinter

Subnetting: divide a network into smaller subnets

Export results to CSV or text file

Dependencies

Python

No external libraries required for the basic version

Getting Started

Clone or download the repository.

Open terminal or command prompt.

Run the program:

python subnet_calculator.py


Follow the on-screen prompts.
