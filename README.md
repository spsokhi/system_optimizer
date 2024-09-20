# System Optimizer

**System Optimizer** is a Python-based utility tool designed for Windows users to optimize their system performance. It allows you to clean temporary files, optimize drives, display system information, and test internet speed all in one easy-to-use GUI.

---

## Features
- **Clean Temporary Files**: Frees up disk space by removing unnecessary files from Windows temp folders.
- **Optimize Drives**: Runs the built-in Windows drive defragmenter to optimize system drives.
- **Show System Information**: Displays detailed information about your CPU and memory usage.
- **Internet Speed Test**: Tests and displays your current internet download and upload speeds.
- **Notifications**: Shows real-time system notifications when tasks complete.

---

## Installation

### Prerequisites
- **Python 3.7+** installed on your machine.
- **pip** (Python package manager) should be installed.

### Setup

1. **Clone the repository**:
    ```
    git clone https://github.com/spsokhi/system-optimizer.git
    cd system-optimizer
    ```

2. **Create a virtual environment** (optional but recommended):
    ```
    python -m venv sys_opt
    On Windows, use: sys_opt\Scripts\activate
    On MacOS/Linux, use: source sys_opt/bin/activate   
    ```

3. **Install required dependencies**:
    ```
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```
    python main.py
    ```

---

## Usage

Once you run the application, a graphical user interface (GUI) will appear with the following options:

- **Clean Temp Files**: Click to remove unnecessary temporary files.
- **Optimize Drives**: Click to run a drive optimization process (requires admin privileges).
- **Show System Info**: Click to display CPU usage, memory usage, and available memory.
- **Test Internet Speed**: Click to check your download and upload speeds.
- **Show Notification**: Displays a system notification when tasks are completed.

Each task's result will be displayed in the text area in the GUI.

---

## Known Issues

- **Drive Optimization Privileges**: Ensure you run the app with administrative privileges to optimize drives.
- **File Deletion Errors**: Some temp files may be in use by other processes and cannot be deleted.

---

## Contributing

Contributions are welcome! If you'd like to add features or fix bugs, feel free to fork the repository and create a pull request.

---

### Explanation of the Sections:

1. **Features**: Brief overview of the functionality provided by the app.
2. **Installation**: Step-by-step guide on how to set up the project.
3. **Usage**: Instructions on how to use the app and its features.
4. **Known Issues**: A place to list any known bugs or limitations.
5. **Contributing**: Information on how others can contribute to the project.
