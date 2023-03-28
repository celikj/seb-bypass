import os

user_namex = os.environ['USERNAME']
file_path = f"C:\\Users\\{user_namex}\\Documents\\Virtual Machines\\Windows 10\\windows 10.vmx"

with open(file_path, "r") as file:
    file_text = file.read()

if "SMBIOS.reflectHost = “True”" in file_text:
    print("You have run the bypass before, you do not need to run it again.")
else:
    with open(file_path, "a") as file:
        file.write("\nSMBIOS.reflectHost = “True”")
        print("SEB vm detection bypassed successfully.")

input("Press any key to close the program...")
