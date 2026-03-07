# Quick Start Guide - GUI Subnet Calculator

## Installation & Running (2-3 minutes)

### Step 1: Install tkinter (if needed)

Check if tkinter is installed:
```bash
python3 -m tkinter
```
A small window should open. If it does, skip to Step 2. If not, install it:

**Linux (Ubuntu/Debian)**:
```bash
sudo apt-get install python3-tk
```

**Linux (Fedora/RHEL)**:
```bash
sudo dnf install python3-tkinter
```

**macOS**:
```bash
brew install python-tk@3.x
```

**Windows**:
Re-run Python installer and select "tcl/tk and IDLE" option.

### Step 2: Navigate to the GUI directory
```bash
cd GUI_VERSION
```

### Step 3: Run the application
```bash
python3 main.py
```

The GUI window will open! No other dependencies needed.

## First Calculation (30 seconds)

1. **Enter an IP Address**: Type `192.168.1.100` in the IP field
2. **Ensure CIDR is selected**: Radio button should be on "CIDR Notation"
3. **Enter CIDR value**: Type `24`
   - You'll see the subnet mask auto-convert to `255.255.255.0`
4. **Click "Calculate Results"**
5. **View the results**:
   ```
   Network Address:      192.168.1.0
   Subnet Mask:          255.255.255.0 (/24)
   Broadcast Address:    192.168.1.255
   Number of Usable Hosts: 254
   Usable IP Range:      192.168.1.1 - 192.168.1.254
   ```

## Common Tasks

### Calculate with Subnet Mask Instead of CIDR
1. Select "Subnet Mask" radio button
2. Type `255.255.0.0` in the Subnet Mask field
   - CIDR will auto-convert to `/16`
3. Enter IP and click Calculate

### Copy Results to Clipboard
1. After calculating results
2. Click "Copy Results" button
3. Paste anywhere with Ctrl+V (or Cmd+V on Mac)

### Export Results to File
1. After calculating results
2. Click "Export as Text" button
3. Choose where to save the file
4. File will include timestamp and IP address used

### Clear All Inputs
Click the "Clear" button to reset all fields and results

## Real-World Examples

### Example 1: Home Network
- IP: `192.168.1.50`
- CIDR: `24`
- Result: 254 usable hosts (192.168.1.1 - 192.168.1.254)

### Example 2: Small Business Network
- IP: `10.0.100.5`
- CIDR: `16`
- Result: 65,534 usable hosts (10.0.0.1 - 10.0.255.254)

### Example 3: Point-to-Point Link
- IP: `203.0.113.1`
- CIDR: `30`
- Result: 2 usable hosts (RFC 3021)

### Example 4: Single Host
- IP: `192.168.1.1`
- CIDR: `32`
- Result: Single host (no network to span)

## Input Validation

The application validates inputs in real-time:

- **Valid IP**: Shows ✓ (green checkmark)
- **Invalid IP**: Shows ✗ (red X) with error message
- **Valid CIDR**: Shows auto-converted subnet mask
- **Invalid CIDR**: Shows error message (must be 0-32)
- **Valid Subnet Mask**: Shows auto-converted CIDR notation
- **Invalid Subnet Mask**: Shows error message

## Comparison: Automatic Format Conversion

### CIDR to Subnet Mask
- Enter CIDR: `25` 
- Auto-displays: `255.255.255.128`

### Subnet Mask to CIDR
- Enter Subnet Mask: `255.255.255.128`
- Auto-displays: `/25`

## Tips & Tricks

1. **Quick switching between formats**: Toggle the radio buttons to see instant conversion
2. **Example values in tooltips**: Hover over labels to see format examples
3. **Tab navigation**: Press Tab to move between fields
4. **Enter key**: Press Enter to calculate (shortcut for clicking Calculate)
5. **Error feedback**: Red text under fields shows exactly what's wrong

## Troubleshooting

### Application won't start
- Check Python version: `python3 --version` (need 3.6+)
- Test tkinter: `python3 -m tkinter` (should open a small window)

### Can't copy to clipboard
- **Linux**: Install xclip: `sudo apt-get install xclip`
- **macOS/Windows**: Should work automatically

### Results don't appear
- Check that all fields are filled
- Look for red error messages (indicates invalid input)
- Verify the IP is in correct format (e.g., 192.168.1.1)

## File Locations

The GUI version structure:
```
GUI_VERSION/
├── main.py                 ← Run this to start
├── README.md               ← Full documentation
├── gui/main_window.py      ← Main application window
├── core/calculator.py      ← Calculation functions
└── core/validators.py      ← Input validation
```

## Next Steps

Once comfortable with basic calculations:
1. Explore the tooltips and error messages
2. Try different CIDR values (0, 8, 16, 24, 32)
3. Test edge cases (/31 for point-to-point, /32 for hosts)
4. Export results to keep records

## Getting Help

- **Hover over labels** for input format examples
- **Red error messages** explain exactly what's wrong
- **README.md** has full feature documentation
- **BUILD_SUMMARY.md** has technical details

## Keyboard Shortcuts (Future Enhancement)

Currently planned for Phase 2:
- `Ctrl+B` - Calculate
- `Ctrl+C` - Clear
- `Ctrl+E` - Export
- `Ctrl+O` - Copy to clipboard

---

**Ready to calculate?** Run `python3 main.py` and get started! 🚀
