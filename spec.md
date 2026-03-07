# GUI Subnet Calculator - Specification

## Overview
This document outlines the design and implementation specifications for a graphical user interface (GUI) version of the Subnet Calculator. The GUI version will provide a user-friendly interface using Python's tkinter library, making subnet calculations more accessible to users who prefer visual interactions over command-line interfaces.

## Project Scope

### Current CLI Features to Preserve
- IPv4 address validation
- CIDR notation support (0-32 range)
- Subnet mask format support (dotted-decimal notation)
- Network address calculation
- Broadcast address calculation
- Usable host count calculation
- Usable IP range calculation

### GUI-Specific Enhancements
- Real-time input validation with visual feedback
- Tab-based interface for different calculation modes
- Result history/clipboard copy functionality
- Visual indicators for valid/invalid inputs
- Preset subnet scenarios (common network sizes)
- Export functionality for results

## Architecture

### Module Organization
```
subnet_calculator_gui/
├── main.py                    # Entry point; instantiates GUI
├── gui/
│   ├── __init__.py
│   ├── main_window.py         # Main application window
│   ├── widgets.py             # Custom widget definitions
│   └── styles.py              # UI styling and themes
├── core/
│   ├── __init__.py
│   ├── calculator.py          # Core calculation logic (refactored from CLI)
│   └── validators.py          # Input validation functions
└── tests/
    ├── __init__.py
    └── test_gui.py            # GUI unit tests
```

### Design Pattern
- **Model-View-Controller (MVC)**: Separate business logic (calculator) from UI rendering (tkinter)
- **Reusability**: Core calculation functions remain pure and testable; no tkinter dependencies
- **Separation of Concerns**: GUI logic separate from calculation logic

## User Interface Design

### Main Window Layout (800x600 minimum)

#### Section 1: Input Fields (Top Panel)
```
┌─ IPv4 Address Input ────────────────────┐
│ Label: "Host IP or Network IP"          │
│ Entry Field: [192.168.1.100           ] │
│ Status: ✓ Valid / ✗ Invalid            │
└─────────────────────────────────────────┘

┌─ Subnet Mask Selection ─────────────────┐
│ ○ CIDR Notation    ● Subnet Mask        │
│                                         │
│ CIDR: [24  ] ↔ Subnet: [255.255.255.0]│
│ Status: ✓ Valid / ✗ Invalid            │
└─────────────────────────────────────────┘

```

#### Section 2: Calculate Button
```
┌─────────────────────────────────────────┐
│        [Calculate Results]              │
└─────────────────────────────────────────┘
```

#### Section 3: Results Display Panel (Bottom)
```
┌─ Calculation Results ───────────────────┐
│ Network Address:      192.168.1.0       │
│ Subnet Mask:          255.255.255.0 (/24)│
│ Broadcast Address:    192.168.1.255     │
│ Number of Hosts:      254               │
│ Usable IP Range:      192.168.1.1 -     │
│                       192.168.1.254      │
│                                         │
│ [Copy Results] [Clear] [Export as TXT] │
└─────────────────────────────────────────┘
```

### UI Components

#### 1. Input Validation Display
- **Real-time validation**: Check input as user types (with debouncing)
- **Color-coded status**: Green checkmark for valid, red X for invalid
- **Error messages**: Display below input field explaining validation error
- **Tooltips**: Hover hints for input formats (e.g., "e.g., 192.168.1.100")

#### 2. Radio Button Selection
- Toggle between CIDR and Subnet Mask input methods
- Dynamically convert between formats when toggled
- Swappable entry fields based on selection

#### 3. Results Display
- **Read-only text widget**: Displays calculation results
- **Line-separated**: Clear formatting with labels
- **Copy-to-clipboard button**: One-click result copying
- **Export button**: Save results to text file with timestamp

#### 4. Button Actions
- **Calculate**: Perform validation and calculations
- **Clear**: Reset all fields and results
- **Copy Results**: Copy formatted results to clipboard
- **Export**: Save results to file dialog

## Features

### Core Features
1. **IP Address Input**
   - Text entry with real-time validation
   - Error messages for invalid IPs
   - Placeholder text with format hints

2. **Subnet Mask Selection**
   - Toggle between CIDR (/0-32) and dotted-decimal (255.255.255.0) formats
   - Bi-directional conversion when toggled
   - Live format conversion display

3. **Calculation Results**
   - Network Address
   - Broadcast Address
   - Subnet Mask (both formats)
   - Number of usable hosts
   - First usable IP
   - Last usable IP

4. **Input Validation**
   - IPv4 address format validation
   - CIDR range validation (0-32)
   - Subnet mask validity validation
   - Visual feedback (color + icons)
   - Helpful error messages

### Enhanced Features (Phase 2)
1. **Result History**
   - Store last 10 calculations
   - Click to reload previous calculations
   - Clear history option

2. **Preset Networks**
   - Class A/B/C quick buttons
   - Custom preset buttons for common networks
   - Editable presets in settings

3. **Export/Import**
   - Export results to .txt file with formatting
   - Export results to .csv for bulk calculations
   - Copy to clipboard with custom formatting

4. **Subnetting Calculator**
   - Divide network into N subnets
   - Display subnet table with ranges
   - Export subnet breakdown

## Implementation Details

### Core Calculator Module (`core/calculator.py`)
Refactor existing CLI functions into pure utility functions:
```python
def validate_ip(ip: str) -> bool
def validate_cidr(cidr: int) -> bool
def validate_subnet_mask(mask: str) -> bool
def cidr_to_subnet_mask(cidr: int) -> str
def subnet_mask_to_cidr(mask: str) -> int
def calculate_network_address(ip: str, mask: str) -> str
def calculate_broadcast_address(ip: str, mask: str) -> str
def calculate_usable_hosts(cidr: int) -> int
def get_usable_ip_range(network: str, broadcast: str) -> tuple[str, str]
def perform_subnet_calculation(ip: str, subnet_method: str, subnet_value: str) -> dict
```

### Validators Module (`core/validators.py`)
Wrapper functions for user input with detailed error messages:
```python
def validate_ip_with_error(ip: str) -> tuple[bool, str]
def validate_cidr_with_error(cidr: str) -> tuple[bool, str]
def validate_subnet_mask_with_error(mask: str) -> tuple[bool, str]
def validate_subnet_input(ip: str, method: str, value: str) -> tuple[bool, dict]
```

### Main Window Class (`gui/main_window.py`)
```python
class SubnetCalculatorGUI(tk.Tk):
    def __init__(self):
        self.setup_ui()
        self.setup_styles()
        self.bind_events()
    
    def setup_ui(self):
        # Create input frame, results frame, button frame
        pass
    
    def on_ip_input_change(self, event):
        # Real-time IP validation
        pass
    
    def on_subnet_input_change(self, event):
        # Real-time subnet validation
        pass
    
    def toggle_subnet_method(self):
        # Switch between CIDR and subnet mask
        pass
    
    def convert_subnet_formats(self):
        # Live conversion between formats
        pass
    
    def calculate(self):
        # Validate and calculate
        pass
    
    def display_results(self, results: dict):
        # Format and display calculations
        pass
    
    def copy_results(self):
        # Copy to clipboard
        pass
    
    def export_results(self):
        # Save to file
        pass
    
    def clear_all(self):
        # Reset fields
        pass
```

### Styling Module (`gui/styles.py`)
```python
COLORS = {
    'bg': '#f0f0f0',
    'fg': '#333333',
    'valid': '#28a745',
    'invalid': '#dc3545',
    'neutral': '#007bff',
    'button_bg': '#007bff',
    'button_fg': '#ffffff'
}

FONTS = {
    'title': ('Arial', 14, 'bold'),
    'label': ('Arial', 10),
    'input': ('Arial', 10),
    'results': ('Courier New', 9)
}

STYLES = {
    'entry': {...},
    'button': {...},
    'label': {...}
}
```

## Technology Stack

### Core Dependencies
- **Python 3.6+**: Language requirement
- **tkinter**: Built-in GUI framework (included with Python)
- **ipaddress**: Built-in IP validation module (already used in CLI)

### Optional Dependencies (Future)
- **pillow**: For custom icons/images
- **ttkbootstrap**: For modern themes (alternative to tkinter)
- **pytest**: For unit testing

## File Structure (Phase 1)

```
subnet_calculator/
├── LICENSE
├── README.md
├── spec.md                              # This file
├── subnet_calculator.py                 # Original CLI version
├── subnet_calculator_gui.py             # Main GUI entry point
└── GUI_VERSION/
    ├── __init__.py
    ├── main.py                          # Application launcher
    ├── requirements.txt                 # Dependencies (empty for tkinter)
    ├── gui/
    │   ├── __init__.py
    │   ├── main_window.py               # Main window class
    │   ├── styles.py                    # Theme and styling
    │   └── widgets.py                   # Custom widgets (future)
    ├── core/
    │   ├── __init__.py
    │   ├── calculator.py                # Refactored calculation logic
    │   └── validators.py                # Input validation with errors
    └── tests/
        ├── __init__.py
        ├── test_calculator.py           # Unit tests for core logic
        └── test_validators.py           # Unit tests for validators
```

## Development Phases

### Phase 1: MVP (Minimum Viable Product)
**Timeline**: 2-3 weeks
- Basic tkinter window with input fields
- IPv4 and subnet input validation
- CIDR/subnet mask toggle and conversion
- Basic calculation and result display
- Clear and Calculate buttons
- Simple styling

**Deliverables**:
- `gui/main_window.py` with basic UI
- `core/calculator.py` (refactored from CLI)
- `core/validators.py` with error messages
- Working GUI version matching CLI functionality

### Phase 2: Enhanced Features
**Timeline**: 2-3 weeks
- Copy-to-clipboard functionality
- Export to text file
- Result history (last 10 calculations)
- Preset network buttons
- Improved styling and layout
- Input field tooltips

**Deliverables**:
- Enhanced main_window.py with new features
- gui/widgets.py for custom widgets
- Export/clipboard utilities
- History management

### Phase 3: Advanced Features (Optional)
**Timeline**: 3-4 weeks
- Subnetting calculator (divide network into N subnets)
- Subnet table display with calculation details
- Custom themes/dark mode
- Keyboard shortcuts
- Settings/preferences panel
- Tabbed interface for multiple tools

**Deliverables**:
- Multi-tab interface
- Subnetting logic and UI
- Settings persistence
- Theme switcher

## Testing Strategy

### Unit Tests
- Test all calculator functions with edge cases (/0, /32, invalid inputs)
- Test validators independently
- Mock tkinter widgets where necessary

### GUI Tests
- Verify input validation triggers correctly
- Test calculation accuracy with various inputs
- Test button actions and state management
- Test result display formatting

### Integration Tests
- End-to-end workflow tests
- Export file generation validation
- Clipboard copy verification

## Success Criteria

### Phase 1 (MVP)
- ✓ All CLI features functional in GUI
- ✓ Real-time input validation working
- ✓ Results display accurately
- ✓ Cross-platform compatibility (Windows, macOS, Linux)
- ✓ Application runs without external dependencies

### Phase 2
- ✓ Copy-to-clipboard on all platforms
- ✓ File export generates valid text files
- ✓ History feature stores and retrieves calculations
- ✓ UI is responsive and user-friendly

### Phase 3
- ✓ Subnetting calculator produces correct subnet lists
- ✓ Multiple themes available and switchable
- ✓ Keyboard shortcuts functional
- ✓ Settings persist across sessions

## Future Enhancements

1. **IPv6 Support**: Extend calculator for IPv6 address handling
2. **VLSM Calculator**: Variable Length Subnet Masking calculations
3. **Network Simulation**: Visualize subnets and host assignments
4. **CLI Integration**: Accept command-line arguments for batch processing
5. **Web Version**: Flask/Django web interface for browser access
6. **Mobile App**: Cross-platform mobile application wrapper
7. **Advanced Filtering**: Filter IP ranges by criteria
8. **Routing Table**: Display routing information for subnets

## Notes

- The core calculator logic can remain unchanged; GUI wraps it without modifying CLI behavior
- tkinter is sufficient for MVP; can migrate to PyQt/PySide later if needed
- All existing tests for CLI must pass unchanged
- GUI should be intuitive for both networking professionals and beginners
