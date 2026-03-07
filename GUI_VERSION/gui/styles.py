"""
UI styling and theme configuration for Subnet Calculator GUI.
"""

# Color palette
COLORS = {
    'bg': '#171A1F',  # primary-color
    'fg': '#000000',  # secondary-color
    'valid': '#28a745',
    'invalid': '#dc3545',
    'neutral': '#798ECD',  # accent-color
    'button_bg': '#798ECD',  # accent-color
    'button_fg': '#FFFFFF',
    'button_hover': '#1A2547',  # highlight-color
    'frame_bg': '#1E2128',  # div-color
    'entry_bg': '#1E2128',  # div-color
    'entry_fg': '#F3F4F6',  # gray-text (approximated)
    'border': '#cccccc'
}

# Fonts
FONTS = {
    'title': ('Arial', 14, 'bold'),
    'label': ('Arial', 10),
    'input': ('Arial', 10),
    'results': ('Courier New', 9),
    'button': ('Arial', 10)
}

# Padding and sizes
PADDING = {
    'frame': 15,
    'widget': 10,
    'button': 5
}

# Widget dimensions
DIMENSIONS = {
    'window_width': 800,
    'window_height': 700,
    'entry_height': 2,
    'results_height': 10
}

# Button styles
BUTTON_STYLE = {
    'bg': COLORS['button_bg'],
    'fg': COLORS['button_fg'],
    'activebackground': COLORS['button_hover'],
    'activeforeground': COLORS['button_fg'],
    'relief': 'raised',
    'bd': 1,
    'padx': 10,
    'pady': 8,
    'font': FONTS['button'],
    'cursor': 'hand2'
}

# Entry field styles
ENTRY_STYLE = {
    'bg': COLORS['entry_bg'],
    'fg': COLORS['entry_fg'],
    'relief': 'solid',
    'bd': 1,
    'font': FONTS['input']
}

# Label styles
LABEL_STYLE = {
    'bg': COLORS['bg'],
    'fg': COLORS['fg'],
    'font': FONTS['label']
}

# Status indicator styles
STATUS_VALID = {
    'fg': COLORS['valid'],
    'font': ('Arial', 12, 'bold')
}

STATUS_INVALID = {
    'fg': COLORS['invalid'],
    'font': ('Arial', 12, 'bold')
}
