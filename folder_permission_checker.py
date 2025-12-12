import os
import stat
import argparse

def get_permissions(path):
    """
    Retrieves and evaluates folder permissions.

    Args:
        path (str): The folder path to scan.

    Returns:
        dict: Permission details and potential risk flags.
    """
    try:
        st = os.stat(path)
        mode = st.st_mode

        # Check if folder is world-writable (everyone has write access)
        world_writable = bool(mode & stat.S_IWOTH)

        return {
            "path": path,
            "world_writable": world_writable
        }

    except Exception as e:
        # Capture errors such as unauthorized access
        return {
            "path": path,
            "error": str(e)
        }


def scan_directory(base_path):
    """
    Recursively scans a directory structure and evaluates permissions.

    Args:
        base_path (str): Starting directory path

    Yields:
        dict: Permission evaluation results
    """
    for root, dirs, files in os.walk(base_path):
        yield get_permissions(root)


def main():
    """
    Main function to run the Folder Permission Checker.
    Accepts command-line input and prints results.
    """
    parser = argparse.ArgumentParser(description="Folder Permission Checker - Security Automation Tool")
    parser.add_argument("path", help="Directory path to scan for permission risks")
    args = parser.parse_args()

    # Validate the path
    if not os.path.exists(args.path):
        print("❌ Error: The directory path does not exist.")
        return

    print(f"\n🔍 Scanning directory: {args.path}\n")

    # Perform the scan
    for result in scan_directory(args.path):
        if "error" in result:
            print(f"⚠️ Error accessing {result['path']}: {result['error']}")
        elif result["world_writable"]:
            print(f"[!] INSECURE PERMISSION FOUND:\n    Path: {result['path']}\n    Risk: Folder is world-writable\n")
        else:
            print(f"[OK] {result['path']}")

    print("\n✔ Scan complete.\n")


if __name__ == "__main__":
    main()
