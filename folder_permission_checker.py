"""
Folder Permission Checker
Author: Terrence (cortrez28-sudo)
Description:
    This script recursively scans a given directory and evaluates folder permissions.
    It flags any folders that appear to be world-writable (i.e., where 'others' have
    write access), which can be a security risk in many environments.

    This tool was created for a cybersecurity automation project to demonstrate how
    Python can be used to automate basic security audits on file system permissions.
"""

import os
import stat
import argparse


def get_permissions(path: str) -> dict:
    """
    Retrieve and evaluate folder permissions for a given path.

    Args:
        path (str): The folder path to analyze.

    Returns:
        dict: A dictionary containing:
            - "path": The folder path.
            - "world_writable": Boolean indicating if the folder is world-writable.
            - "error": Error message if the path could not be accessed (optional).
    """
    try:
        # os.stat() retrieves information about the path, including permission bits
        st = os.stat(path)
        mode = st.st_mode

        # Check if the "others write" bit is set (world-writable)
        world_writable = bool(mode & stat.S_IWOTH)

        return {
            "path": path,
            "world_writable": world_writable
        }

    except Exception as e:
        # If an error occurs (e.g., access denied), return the error instead of crashing
        return {
            "path": path,
            "error": str(e)
        }


def scan_directory(base_path: str):
    """
    Recursively scan the directory structure starting at base_path.

    Args:
        base_path (str): Root directory from which to begin scanning.

    Yields:
        dict: Result from get_permissions() for each folder encountered.
    """
    # os.walk() walks the directory tree, yielding each directory in the structure
    for root, dirs, files in os.walk(base_path):
        # Evaluate permissions for the current folder (root)
        yield get_permissions(root)


def print_result(result: dict) -> None:
    """
    Print the result of a permission check in a human-readable format.

    Args:
        result (dict): A dictionary returned from get_permissions().
    """
    # If an error occurred while accessing the folder, display a warning
    if "error" in result:
        print(f"⚠️ Error accessing {result['path']}: {result['error']}")
    # If the folder is world-writable, flag it as insecure
    elif result.get("world_writable"):
        print(
            "[!] INSECURE PERMISSION FOUND:\n"
            f"    Path: {result['path']}\n"
            "    Risk: Folder is world-writable (others have write access)\n"
        )
    # Otherwise, indicate that this folder appears okay
    else:
        print(f"[OK] {result['path']}")


def main() -> None:
    """
    Main execution function.

    - Parses command-line arguments.
    - Validates the input path.
    - Iterates through the directory tree.
    - Prints security-relevant permission findings.
    """
    parser = argparse.ArgumentParser(
        description="Folder Permission Checker - Security Automation Tool"
    )
    parser.add_argument(
        "path",
        help="Directory path to scan for potentially insecure folder permissions"
    )
    args = parser.parse_args()

    # Ensure the provided path exists before scanning
    if not os.path.exists(args.path):
        print("❌ Error: The directory path does not exist. Please provide a valid path.")
        return

    print(f"\n🔍 Starting permission scan in: {args.path}\n")

    # Loop through all folders and print results based on evaluation
    for result in scan_directory(args.path):
        print_result(result)

    print("\n✔ Scan complete.\n")


if __name__ == "__main__":
    main()
