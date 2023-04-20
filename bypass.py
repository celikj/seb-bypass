import os
from pathlib import Path

user_namex = os.environ['USERNAME']

documents_folder = "Documents"
documents_path = Path.home() / documents_folder

file_path = f"{documents_path}\\Virtual Machines\\Windows 10\\windows 10.vmx"

with open(file_path, "r") as file:
    file_text = file.read()

if 'SMBIOS.reflectHost = "True"'  in file_text:
    print("You have run the bypass before, you do not need to run it again.")
else:
    with open(file_path, "a") as file:
        file.write('\nSMBIOS.reflectHost = "True"')
        print("bypass completed successfully.")

input("Press any key to close the program...")
