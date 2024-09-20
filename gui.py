import tkinter as tk
import threading
from cleaning import clean_temp_files
from optimization import optimize_drives, display_system_info
from utils import show_notification, test_internet_speed
from tkinter import ttk

class SystemOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Optimizer")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f0f0")

        # Define styles
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 10), padding=5)
        style.configure("TLabel", font=("Helvetica", 10), padding=5, background="#f0f0f0")
        
        # Create a Frame for the buttons
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.X)

        # Buttons for each feature
        clean_button = ttk.Button(button_frame, text="Clean Temp Files", command=self.run_clean_temp_files)
        clean_button.pack(side=tk.LEFT, padx=10, pady=5)

        optimize_button = ttk.Button(button_frame, text="Optimize Drives", command=self.run_optimize_drives)
        optimize_button.pack(side=tk.LEFT, padx=10, pady=5)

        info_button = ttk.Button(button_frame, text="Show System Info", command=self.run_display_system_info)
        info_button.pack(side=tk.LEFT, padx=10, pady=5)

        internet_button = ttk.Button(button_frame, text="Test Internet Speed", command=self.run_test_internet_speed)
        internet_button.pack(side=tk.LEFT, padx=10, pady=5)

        notify_button = ttk.Button(button_frame, text="Show Notification", command=self.run_show_notification)
        notify_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Frame for output text
        output_frame = ttk.Frame(self.root, padding="10")
        output_frame.pack(fill=tk.BOTH, expand=True)

        # Text widget to display the output (like a console)
        self.output_text = tk.Text(output_frame, wrap='word', height=15, width=70, bg="#e6e6e6", fg="black", font=("Consolas", 10))
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.output_text.config(state=tk.DISABLED)

        # Scrollbar for the output text widget
        scrollbar = ttk.Scrollbar(output_frame, command=self.output_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.config(yscrollcommand=scrollbar.set)

    # Methods that create threads to run tasks in the background
    def run_clean_temp_files(self):
        self.clear_output()
        self.show_processing_status()
        thread = threading.Thread(target=self.clean_temp_files)
        thread.start()

    def run_optimize_drives(self):
        self.clear_output()
        self.show_processing_status()
        thread = threading.Thread(target=self.optimize_drives)
        thread.start()

    def run_display_system_info(self):
        self.clear_output()
        self.show_processing_status()
        thread = threading.Thread(target=self.show_system_info)
        thread.start()

    def run_test_internet_speed(self):
        self.clear_output()
        self.show_processing_status()
        thread = threading.Thread(target=self.test_internet_speed)
        thread.start()

    def run_show_notification(self):
        show_notification("System check complete!", "System Optimizer")

    # The actual methods that get called by the threads
    def clean_temp_files(self):
        try:
            clean_temp_files(output_callback=self.append_output)
            self.append_output("Temporary files cleaned!")
            show_notification("Temporary files cleaned!", "System Optimizer")
        except Exception as e:
            self.append_output(f"Error cleaning temp files: {str(e)}")
        finally:
            self.hide_processing_status()

    def optimize_drives(self):
        try:
            optimize_drives(output_callback=self.append_output)
            self.append_output("Drives optimized!")
            show_notification("Drives optimized!", "System Optimizer")
        except Exception as e:
            self.append_output(f"Error optimizing drives: {str(e)}")
        finally:
            self.hide_processing_status()

    def show_system_info(self):
        try:
            display_system_info(output_callback=self.append_output)
            self.append_output("System info displayed!")
        except Exception as e:
            self.append_output(f"Error displaying system info: {str(e)}")
        finally:
            self.hide_processing_status()

    def test_internet_speed(self):
        try:
            test_internet_speed(output_callback=self.append_output)
            self.append_output("Internet speed test completed!")
        except Exception as e:
            self.append_output(f"Error testing internet speed: {str(e)}")
        finally:
            self.hide_processing_status()

    # Safe GUI updates using tkinter's after method
    def append_output(self, text):
        """Safely append output to the text widget."""
        self.root.after(0, lambda: self._insert_text(text))

    def _insert_text(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text + '\n')
        self.output_text.config(state=tk.DISABLED)
        self.output_text.see(tk.END)  # Auto-scroll to the end of the text

    def clear_output(self):
        """Clears the output text widget."""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)

    # Show the "Processing..." status
    def show_processing_status(self):
        self.append_output("Processing...")

    # Hide the processing status when the task is done
    def hide_processing_status(self):
        self.append_output("Task Completed!")
