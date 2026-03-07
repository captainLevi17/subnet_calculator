# GUI Subnet Calculator

A graphical user interface (GUI) version of the Subnet Calculator, built with Python's tkinter library. This application provides an intuitive interface for calculating IPv4 subnet information.

## Features

- **Real-time Input Validation**: Immediate visual feedback for IP addresses and subnet masks
- **Dual Input Methods**: Support for both CIDR notation (0-32) and dotted-decimal subnet masks
- **Live Format Conversion**: Automatically converts between CIDR and subnet mask formats
- **Comprehensive Results**: Displays network address, broadcast address, usable hosts, and IP range
- **Export Functionality**: Save results to text files with timestamp
- **Clipboard Support**: One-click copy of results to clipboard
- **User-Friendly Interface**: Clean, intuitive design with clear visual feedback

## Requirements

- Python 3.6 or higher
- tkinter (Python GUI library)

## Installation

### Step 1: Install tkinter

tkinter is included with Python but may need to be installed separately on some systems:

**Linux (Ubuntu/Debian)**:
```bash
sudo apt-get install python3-tk
```

**Linux (Fedora/RHEL)**:
```bash
sudo dnf install python3-tkinter
```

**macOS**:
tkinter usually comes with Python. If needed:
```bash
brew install python-tk@3.x
```

**Windows**:
tkinter comes built-in. If missing, reinstall Python and check "tcl/tk and IDLE" during installation.

### Step 2: Run the Application

1. Navigate to the GUI_VERSION directory:
```bash
cd GUI_VERSION
```

2. Run the application:
```bash
python3 main.py
```

## Usage

1. **Enter an IPv4 Address**: Type the IP address (e.g., `192.168.1.100`)
   - The application validates the format in real-time
   
2. **Select Subnet Input Method**: Choose between CIDR or Subnet Mask
   - **CIDR Notation**: Enter 0-32 (e.g., `24`)
   - **Subnet Mask**: Enter dotted-decimal format (e.g., `255.255.255.0`)
   - The application automatically converts and displays both formats
   
3. **Click "Calculate Results"**: View detailed subnet information
   - Network Address
   - Subnet Mask (both formats)
   - Broadcast Address
   - Number of Usable Hosts
   - Usable IP Range
   
4. **Optional Actions**:
   - **Copy Results**: Copy formatted output to clipboard
   - **Export as Text**: Save results to a text file
   - **Clear**: Reset all fields

## Project Structure

```
GUI_VERSION/
├── main.py                    # Entry point
├── requirements.txt           # Dependencies (none for MVP!)
├── README.md                  # This file
├── gui/
│   ├── __init__.py
│   ├── main_window.py         # Main GUI window and application logic
│   └── styles.py              # UI styling and themes
├── core/
│   ├── __init__.py
│   ├── calculator.py          # Core calculation functions
│   └── validators.py          # Input validation with error messages
└── tests/
    ├── __init__.py
    └── test_calculator.py     # Unit tests
```

## Module Overview

### core/calculator.py
Pure utility functions for subnet calculations:
- `validate_ip()`: Validates IPv4 address format
- `cidr_to_subnet_mask()`: Converts CIDR to subnet mask
- `subnet_mask_to_cidr()`: Converts subnet mask to CIDR
- `calculate_network_address()`: Computes network address
- `calculate_broadcast_address()`: Computes broadcast address
- `calculate_usable_hosts()`: Calculates usable host count
- `get_usable_ip_range()`: Gets first and last usable IPs
- `perform_subnet_calculation()`: Complete subnet calculation

### core/validators.py
Input validation with user-friendly error messages:
- `validate_ip_with_error()`: Validates IP with error message
- `validate_cidr_with_error()`: Validates CIDR with error message
- `validate_subnet_mask_with_error()`: Validates subnet mask with error message

### gui/main_window.py
Main application window and UI logic:
- `SubnetCalculatorGUI`: Main tkinter application class
- Input field management and validation
- Result calculation and display
- Export and clipboard functionality

### gui/styles.py
Centralized styling and theming configuration:
- Color palette
- Font definitions
- Padding and size constants
- Widget styling dictionaries

## Examples

### Example 1: Calculate Class C Network
1. **IP Address**: `192.168.1.100`
2. **Method**: CIDR
3. **CIDR**: `24`
4. **Results**:
   - Network: 192.168.1.0
   - Subnet Mask: 255.255.255.0
   - Broadcast: 192.168.1.255
   - Usable Hosts: 254
   - Range: 192.168.1.1 - 192.168.1.254

### Example 2: Calculate using Subnet Mask
1. **IP Address**: `10.0.0.50`
2. **Method**: Subnet Mask
3. **Subnet Mask**: `255.255.0.0`
4. **Results**:
   - Network: 10.0.0.0
   - CIDR: /16
   - Broadcast: 10.0.255.255
   - Usable Hosts: 65534
   - Range: 10.0.0.1 - 10.0.255.254

## Keyboard Shortcuts (Future)

- `Ctrl+C`: Clear all inputs
- `Ctrl+B`: Calculate
- `Ctrl+E`: Export results

## Future Enhancements

- **Phase 2 Features**:
  - Result history (last 10 calculations)
  - Keyboard shortcuts
  - Improved styling with themes
  - Custom preset networks
  
- **Phase 3 Features**:
  - Subnetting calculator (divide networks)
  - IPv6 support
  - Dark mode theme
  - Settings/preferences panel

## Code Style

This project follows these guidelines:
- **Functions first**: Pure utility functions before GUI logic
- **Descriptive names**: Clear function and variable names
- **Docstrings**: All functions have docstrings
- **Input validation**: Always validate before processing
- **Error handling**: Try-except with helpful error messages
- **MVC Pattern**: Separation of business logic and UI

## Testing

Run tests with pytest:
```bash
pytest tests/
```

## Troubleshooting

### Application won't start
- Ensure Python 3.6+ is installed: `python3 --version`
- Verify tkinter is available: `python3 -m tkinter` (should open a small window)

### Can't copy to clipboard
- Make sure `xclip` is installed on Linux: `sudo apt-get install xclip`
- On macOS and Windows, clipboard should work automatically

### Import errors
- Ensure you're running from the correct directory
- Check that all files are in the proper structure

## Contributing

Feel free to submit issues or improvements. Author: MLSG.

## License

MIT License (same as the CLI version)
