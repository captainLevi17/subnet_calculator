"""
Main GUI window for Subnet Calculator.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys
import os
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.calculator import perform_subnet_calculation, cidr_to_subnet_mask, subnet_mask_to_cidr
from core.validators import validate_ip_with_error, validate_cidr_with_error, validate_subnet_mask_with_error
from gui.styles import COLORS, FONTS, PADDING, DIMENSIONS, BUTTON_STYLE, ENTRY_STYLE, LABEL_STYLE, STATUS_VALID, STATUS_INVALID


class SubnetCalculatorGUI(tk.Tk):
    """Main GUI application window for Subnet Calculator."""
    
    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        
        self.title("Subnet Calculator - GUI")
        self.geometry(f"{DIMENSIONS['window_width']}x{DIMENSIONS['window_height']}")
        self.configure(bg=COLORS['bg'])
        
        # Set minimum window size
        self.minsize(700, 600)
        
        # Initialize variables
        self.subnet_method = tk.StringVar(value='cidr')
        self.results = None
        
        # Build UI
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        # Main container
        main_container = tk.Frame(self, bg=COLORS['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=PADDING['frame'], pady=PADDING['frame'])
        
        # Title
        title = tk.Label(
            main_container,
            text="MLSG's Subnet Calculator",
            font=FONTS['title'],
            bg=COLORS['bg'],
            fg=COLORS['neutral']
        )
        title.pack(pady=(0, PADDING['widget']))
        
        # Separator
        separator = ttk.Separator(main_container, orient='horizontal')
        separator.pack(fill=tk.X, pady=PADDING['widget'])
        
        # Input section
        self.input_frame = tk.Frame(main_container, bg=COLORS['frame_bg'], relief=tk.SOLID, bd=1)
        self.input_frame.pack(fill=tk.X, pady=PADDING['widget'])
        self.create_input_section(self.input_frame)
        
        # Buttons section
        button_frame = tk.Frame(main_container, bg=COLORS['bg'])
        button_frame.pack(fill=tk.X, pady=PADDING['widget'])
        self.create_button_section(button_frame)
        
        # Results section
        results_frame = tk.Frame(main_container, bg=COLORS['frame_bg'], relief=tk.SOLID, bd=1)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=PADDING['widget'])
        self.create_results_section(results_frame)
    
    def create_input_section(self, parent):
        """Create the input fields section."""
        # IP Address input
        ip_label_frame = tk.Frame(parent, bg=COLORS['frame_bg'])
        ip_label_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(PADDING['widget'], 5))
        
        tk.Label(ip_label_frame, text="IPv4 Address:", bg=COLORS['frame_bg'], fg=COLORS['neutral'], 
                font=FONTS['label']).pack(side=tk.LEFT)
        tk.Label(ip_label_frame, text="(e.g., 192.168.1.100)", bg=COLORS['frame_bg'], 
                fg='#999999', font=('Arial', 8)).pack(side=tk.LEFT, padx=(5, 0))
        
        ip_input_frame = tk.Frame(parent, bg=COLORS['frame_bg'])
        ip_input_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(0, 5))
        
        self.ip_entry = tk.Entry(ip_input_frame, **ENTRY_STYLE, width=40)
        self.ip_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, PADDING['widget']))
        self.ip_entry.bind('<KeyRelease>', self.on_ip_change)
        
        self.ip_status = tk.Label(ip_input_frame, text="", bg=COLORS['frame_bg'], font=('Arial', 12))
        self.ip_status.pack(side=tk.LEFT)
        
        self.ip_error = tk.Label(parent, text="", bg=COLORS['frame_bg'], fg=COLORS['invalid'], 
                                font=('Arial', 8))
        self.ip_error.pack(fill=tk.X, padx=PADDING['widget'])
        
        # Separator
        ttk.Separator(parent, orient='horizontal').pack(fill=tk.X, padx=PADDING['widget'], pady=PADDING['widget'])
        
        # Subnet method selection
        method_frame = tk.Frame(parent, bg=COLORS['frame_bg'])
        method_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(PADDING['widget'], 5))
        
        tk.Label(method_frame, text="Subnet Mask Input Method:", bg=COLORS['frame_bg'], 
                fg=COLORS['neutral'], font=FONTS['label']).pack(anchor=tk.W)
        
        radio_frame = tk.Frame(parent, bg=COLORS['frame_bg'])
        radio_frame.pack(fill=tk.X, padx=PADDING['widget'])
        
        tk.Radiobutton(radio_frame, text="CIDR Notation (e.g., 24)", variable=self.subnet_method, 
                      value='cidr', bg=COLORS['frame_bg'], fg=COLORS['neutral'],
                      command=self.on_method_change).pack(side=tk.LEFT, padx=(0, 30))
        tk.Radiobutton(radio_frame, text="Subnet Mask (e.g., 255.255.255.0)", variable=self.subnet_method, 
                      value='mask', bg=COLORS['frame_bg'], fg=COLORS['neutral'],
                      command=self.on_method_change).pack(side=tk.LEFT)
        
        # Separator
        ttk.Separator(parent, orient='horizontal').pack(fill=tk.X, padx=PADDING['widget'], pady=PADDING['widget'])
        
        # CIDR input
        self.cidr_label_frame = tk.Frame(parent, bg=COLORS['frame_bg'])
        self.cidr_label_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(PADDING['widget'], 5))
        
        tk.Label(self.cidr_label_frame, text="CIDR Notation (0-32):", bg=COLORS['frame_bg'], 
                fg=COLORS['neutral'], font=FONTS['label']).pack(side=tk.LEFT)
        
        self.cidr_input_frame = tk.Frame(parent, bg=COLORS['frame_bg'])
        self.cidr_input_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(0, 5))
        
        self.cidr_entry = tk.Entry(self.cidr_input_frame, **ENTRY_STYLE, width=20)
        self.cidr_entry.pack(side=tk.LEFT, padx=(0, PADDING['widget']))
        self.cidr_entry.bind('<KeyRelease>', self.on_cidr_change)
        
        tk.Label(self.cidr_input_frame, text="→", bg=COLORS['frame_bg'], fg=COLORS['neutral'], 
                font=('Arial', 14)).pack(side=tk.LEFT, padx=(0, PADDING['widget']))
        
        tk.Label(self.cidr_input_frame, text="Subnet Mask:", bg=COLORS['frame_bg'], 
                fg=COLORS['neutral'], font=FONTS['label']).pack(side=tk.LEFT)
        
        self.cidr_mask_display = tk.Label(self.cidr_input_frame, text="", bg=COLORS['frame_bg'], 
                                         fg=COLORS['neutral'], font=('Arial', 10))
        self.cidr_mask_display.pack(side=tk.LEFT, padx=(PADDING['widget'], 0))
        
        self.cidr_error = tk.Label(parent, text="", bg=COLORS['frame_bg'], fg=COLORS['invalid'], 
                                  font=('Arial', 8))
        self.cidr_error.pack(fill=tk.X, padx=PADDING['widget'])
        
        # Subnet mask input
        self.mask_label_frame = tk.Frame(parent, bg=COLORS['frame_bg'])
        # self.mask_label_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(PADDING['widget'], 5))
        
        tk.Label(self.mask_label_frame, text="Subnet Mask:", bg=COLORS['frame_bg'], 
                fg=COLORS['neutral'], font=FONTS['label']).pack(side=tk.LEFT)
        
        self.mask_input_frame = tk.Frame(parent, bg=COLORS['frame_bg'])
        # self.mask_input_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(0, 5))
        
        self.mask_entry = tk.Entry(self.mask_input_frame, **ENTRY_STYLE, width=20)
        self.mask_entry.pack(side=tk.LEFT, padx=(0, PADDING['widget']))
        self.mask_entry.bind('<KeyRelease>', self.on_mask_change)
        
        tk.Label(self.mask_input_frame, text="→", bg=COLORS['frame_bg'], fg=COLORS['neutral'], 
                font=('Arial', 14)).pack(side=tk.LEFT, padx=(0, PADDING['widget']))
        
        tk.Label(self.mask_input_frame, text="CIDR:", bg=COLORS['frame_bg'], 
                fg=COLORS['neutral'], font=FONTS['label']).pack(side=tk.LEFT)
        
        self.mask_cidr_display = tk.Label(self.mask_input_frame, text="", bg=COLORS['frame_bg'], 
                                         fg=COLORS['neutral'], font=('Arial', 10))
        self.mask_cidr_display.pack(side=tk.LEFT, padx=(PADDING['widget'], 0))
        
        self.mask_error = tk.Label(parent, text="", bg=COLORS['frame_bg'], fg=COLORS['invalid'], 
                                  font=('Arial', 8))
        # self.mask_error.pack(fill=tk.X, padx=PADDING['widget'], pady=(0, PADDING['widget']))
        
        # Hide mask input initially
        self.update_input_visibility()
    
    def create_button_section(self, parent):
        """Create the button section."""
        button_inner_frame = tk.Frame(parent, bg=COLORS['bg'])
        button_inner_frame.pack(fill=tk.X)
        
        self.calculate_btn = tk.Button(button_inner_frame, text="Calculate Results", 
                                      command=self.calculate, **BUTTON_STYLE)
        self.calculate_btn.pack(side=tk.LEFT, padx=(0, PADDING['widget']))
        
        self.clear_btn = tk.Button(button_inner_frame, text="Clear", 
                                  command=self.clear_all, **BUTTON_STYLE)
        self.clear_btn.pack(side=tk.LEFT)
    
    def create_results_section(self, parent):
        """Create the results display section."""
        results_label = tk.Label(parent, text="Calculation Results:", bg=COLORS['frame_bg'], 
                                fg=COLORS['neutral'], font=FONTS['label'])
        results_label.pack(anchor=tk.W, padx=PADDING['widget'], pady=(PADDING['widget'], 5))
        
        # Results text area
        self.results_text = tk.Text(
            parent,
            bg=COLORS['entry_bg'],
            fg=COLORS['entry_fg'],
            font=FONTS['results'],
            height=DIMENSIONS['results_height'],
            relief=tk.SOLID,
            bd=1,
            state=tk.DISABLED,
            wrap=tk.WORD
        )
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=PADDING['widget'], pady=(0, PADDING['widget']))
        
        # Action buttons
        action_frame = tk.Frame(parent, bg=COLORS['frame_bg'])
        action_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(0, PADDING['widget']))
        
        self.copy_btn = tk.Button(action_frame, text="Copy Results", 
                                 command=self.copy_results, **BUTTON_STYLE)
        self.copy_btn.pack(side=tk.LEFT, padx=(0, PADDING['widget']))
        
        self.export_btn = tk.Button(action_frame, text="Export as Text", 
                                   command=self.export_results, **BUTTON_STYLE)
        self.export_btn.pack(side=tk.LEFT)
    
    def on_method_change(self):
        """Handle subnet method change."""
        self.update_input_visibility()
        self.clear_errors()
        self.clear_results()
    
    def update_input_visibility(self):
        """Show/hide input fields based on selected method."""
        if self.subnet_method.get() == 'cidr':
            # Hide mask input section
            if self.mask_label_frame.winfo_ismapped():
                self.mask_label_frame.pack_forget()
                self.mask_input_frame.pack_forget()
                self.mask_error.pack_forget()
            # Ensure CIDR input is visible
            if not self.cidr_label_frame.winfo_ismapped():
                self.cidr_label_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(PADDING['widget'], 5))
                self.cidr_input_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(0, 5))
                self.cidr_error.pack(fill=tk.X, padx=PADDING['widget'])
        else:
            # Hide CIDR input section
            if self.cidr_label_frame.winfo_ismapped():
                self.cidr_label_frame.pack_forget()
                self.cidr_input_frame.pack_forget()
                self.cidr_error.pack_forget()
            # Ensure mask input is visible
            if not self.mask_label_frame.winfo_ismapped():
                self.mask_label_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(PADDING['widget'], 5))
                self.mask_input_frame.pack(fill=tk.X, padx=PADDING['widget'], pady=(0, 5))
                self.mask_error.pack(fill=tk.X, padx=PADDING['widget'], pady=(0, PADDING['widget']))
    
    def on_ip_change(self, event=None):
        """Handle IP address input change."""
        ip = self.ip_entry.get()
        is_valid, error = validate_ip_with_error(ip)
        
        if is_valid:
            self.ip_status.config(text="✓", **STATUS_VALID)
            self.ip_error.config(text="")
        elif ip:
            self.ip_status.config(text="✗", **STATUS_INVALID)
            self.ip_error.config(text=error)
        else:
            self.ip_status.config(text="")
            self.ip_error.config(text="")
    
    def on_cidr_change(self, event=None):
        """Handle CIDR input change."""
        cidr_str = self.cidr_entry.get()
        is_valid, error, cidr = validate_cidr_with_error(cidr_str)
        
        if is_valid:
            self.cidr_error.config(text="")
            try:
                mask = cidr_to_subnet_mask(cidr)
                self.cidr_mask_display.config(text=mask)
            except Exception as e:
                self.cidr_error.config(text=str(e))
        elif cidr_str:
            self.cidr_error.config(text=error)
            self.cidr_mask_display.config(text="")
        else:
            self.cidr_error.config(text="")
            self.cidr_mask_display.config(text="")
    
    def on_mask_change(self, event=None):
        """Handle subnet mask input change."""
        mask_str = self.mask_entry.get()
        is_valid, error, cidr = validate_subnet_mask_with_error(mask_str)
        
        if is_valid:
            self.mask_error.config(text="")
            self.mask_cidr_display.config(text=f"/{cidr}")
        elif mask_str:
            self.mask_error.config(text=error)
            self.mask_cidr_display.config(text="")
        else:
            self.mask_error.config(text="")
            self.mask_cidr_display.config(text="")
    
    def calculate(self):
        """Perform subnet calculation."""
        # Get inputs
        ip = self.ip_entry.get().strip()
        method = self.subnet_method.get()
        
        if method == 'cidr':
            subnet_value = self.cidr_entry.get().strip()
        else:
            subnet_value = self.mask_entry.get().strip()
        
        # Validate
        if not ip or not subnet_value:
            messagebox.showerror("Input Error", "Please fill in all fields")
            return
        
        try:
            # Perform calculation
            self.results = perform_subnet_calculation(ip, method, subnet_value)
            self.display_results()
            self.clear_errors()
        except ValueError as e:
            messagebox.showerror("Calculation Error", str(e))
    
    def display_results(self):
        """Display calculation results."""
        if not self.results:
            return
        
        # Format results
        result_text = f"""Network Address:      {self.results['network']}
Subnet Mask:          {self.results['mask']} (/{self.results['cidr']})
Broadcast Address:    {self.results['broadcast']}
Number of Usable Hosts: {self.results['usable_hosts']}"""
        
        if self.results['first_usable'] and self.results['last_usable']:
            result_text += f"\nUsable IP Range:      {self.results['first_usable']} - {self.results['last_usable']}"
        else:
            result_text += f"\nUsable IP Range:      N/A (for /{self.results['cidr']})"
        
        # Update text widget
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, result_text)
        self.results_text.config(state=tk.DISABLED)
    
    def copy_results(self):
        """Copy results to clipboard."""
        if not self.results:
            messagebox.showwarning("No Results", "Please calculate results first")
            return
        
        result_text = self.results_text.get(1.0, tk.END).strip()
        self.clipboard_clear()
        self.clipboard_append(result_text)
        messagebox.showinfo("Success", "Results copied to clipboard!")
    
    def export_results(self):
        """Export results to text file."""
        if not self.results:
            messagebox.showwarning("No Results", "Please calculate results first")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialfile=f"subnet_calculation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        
        if not file_path:
            return
        
        try:
            result_text = f"""Subnet Calculator - Results
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Input IP Address:     {self.results['ip']}
Subnet Method:        {"CIDR" if self.subnet_method.get() == 'cidr' else "Subnet Mask"}

{self.results_text.get(1.0, tk.END).strip()}"""
            
            with open(file_path, 'w') as f:
                f.write(result_text)
            
            messagebox.showinfo("Success", f"Results exported to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export results:\n{str(e)}")
    
    def clear_all(self):
        """Clear all inputs and results."""
        self.ip_entry.delete(0, tk.END)
        self.cidr_entry.delete(0, tk.END)
        self.mask_entry.delete(0, tk.END)
        self.clear_errors()
        self.clear_results()
    
    def clear_errors(self):
        """Clear all error messages."""
        self.ip_status.config(text="")
        self.ip_error.config(text="")
        self.cidr_error.config(text="")
        self.cidr_mask_display.config(text="")
        self.mask_error.config(text="")
        self.mask_cidr_display.config(text="")
    
    def clear_results(self):
        """Clear results display."""
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)
        self.results = None


def main():
    """Entry point for the application."""
    app = SubnetCalculatorGUI()
    app.mainloop()


if __name__ == '__main__':
    main()
