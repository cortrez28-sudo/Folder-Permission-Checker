# Folder Permission Checker

## 📌 Project Overview
The Folder Permission Checker is a Python-based security automation tool that scans a directory and evaluates folder permissions to identify potential misconfigurations. Misconfigured or overly permissive folder permissions can expose sensitive data, enable unauthorized modifications, or violate least-privilege principles. This tool helps security analysts and system administrators quickly spot risky folder configurations without manually checking each directory.

This project was developed for a cybersecurity automation course to demonstrate how Python scripting can support real-world security auditing tasks.

---

## 🎯 Project Objectives and Features

### Objectives
- Automate the process of reviewing folder permissions.
- Identify folders that may introduce security risks due to permissive access.
- Practice applying Python to solve practical security auditing problems.

### Key Features
- Recursively scans all folders starting from a user-provided directory path.
- Evaluates permissions using Python’s built-in `os` and `stat` modules.
- Flags folders that appear to be **world-writable** (others have write access).
- Provides clear, human-readable output identifying potentially insecure folders.
- Handles errors gracefully (for example, access denied on system folders).

---

## 🛠 Technologies and Dependencies

- **Language:** Python 3.x  
- **Standard Libraries Used:**
  - `os`
  - `stat`
  - `argparse`

No external or third-party packages are required.

---

## ⚙️ Setup Instructions

### 1. Install Python (if not already installed)
You can download Python 3 from the official website:

- https://www.python.org/downloads/

During installation, make sure to select:

> ✅ “Add Python to PATH”

### 2. Clone or Download the Repository

Using Git:

```bash
git clone https://github.com/cortrez28-sudo/Folder-Permission-Checker
cd Folder-Permission-Checker


