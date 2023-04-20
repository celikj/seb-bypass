import os
from pathlib import Path

filename = "windows 10.vmx"
onedrive_path = Path.home() / "OneDrive"

if onedrive_path.exists():
    onedrive_documents_path = onedrive_path / "Documents"
    documents_path = onedrive_documents_path if onedrive_documents_path.exists() else Path.home() / "Documents"
else:
    documents_path = Path.home() / "Documents"

file_path = next(documents_path.glob(f"**/{filename}"), None)

if file_path is not None:
    with open(file_path, "r") as file:
        file_text = file.read()

    if 'SMBIOS.reflectHost = "True"' in file_text:
        print("You have run the bypass before, you do not need to run it again.")
    else:
        with open(file_path, "a") as file:
            file.write('\nSMBIOS.reflectHost = "True"')
            print("bypass completed successfully.")
else:
    print("File not found")


input("Press any key to close the program...")
