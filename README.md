# Folder-Permission-Checker
# Folder Permission Checker

## 📌 Project Overview
The Folder Permission Checker is a Python-based security automation tool designed to audit folder permissions and identify misconfigurations within a directory structure. Misconfigured access control is a common vulnerability in enterprise environments, and this tool helps analysts quickly determine whether any folders have insecure or overly permissive settings.

This project was developed as part of a cybersecurity automation assignment to demonstrate how scripting can support real-world security auditing and compliance efforts.

---

## 🚀 Features
- Recursive directory scanning
- Permission extraction using Python’s built-in modules
- Detection of unsafe or world-writable folders
- Readable output for analysts
- Error-handling for inaccessible system directories
- Modular code design for scalability

---

## 🛠️ Technologies Used
- Python 3.x
- Standard libraries: `os`, `stat`, `argparse`
- Windows 10 development environment

---

## ▶️ How It Works
1. User provides a directory path.
2. The script recursively scans folders using `os.walk()`.
3. Permissions are evaluated through `os.stat()` and bitwise checks.
4. The script flags insecure or overly permissive directories.
5. Results are printed clearly for audit review.

---

## 📦 Installation

### Clone the Repo:
```bash
git clone https://github.com/<your-username>/folder-permission-checker
cd folder-permission-checker
