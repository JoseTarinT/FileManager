import os
from pathlib import Path
import shutil

# Let's say we have our bills downloaded from our email and we want to organize them in folders
# We create a "ElectricityBills" and a "PhoneBills" folder inside "Bills" folder.

os.mkdir("C:\\Users\\José Lws Tarín Tr\\Documents\\Bills\\PhoneBills")
os.mkdir("C:\\Users\\José Lws Tarín Tr\\Documents\\Bills\\ElectricityBills")

# Now we check that the folders were created correctly.

print(os.path.exists(r"C:\Users\José Lws Tarín Tr\Documents\Bills\PhoneBills"))
print(os.path.exists(r"C:\Users\José Lws Tarín Tr\Documents\Bills\ElectricityBills"))

# We are going to use variables to save us code.
# Parent directory:

parent_dir = r"C:\Users\José Lws Tarín Tr\Documents\Bills"
parent_dir2 = r"C:\Users\José Lws Tarín Tr\Documents\Bills\ElectricityBill"
parent_dir3 = r"C:\Users\José Lws Tarín Tr\Documents\Bills\PhoneBill"

# In this code we will send the 'Bill' files from the 'downloads' folder
# to the 'Bills' folder.

for files in os.listdir(r"C:\Users\José Lws Tarín Tr\Downloads"): # This gives us a list of all 'Folders & Files' that are in \Downloads
    if "bill" in files.lower(): # print(bill) -This step is optional, but here we can check if there are files that contain the word "bill" written
        shutil.move(os.path.join(r"C:\Users\José Lws Tarín Tr\Downloads", files), os.path.join(r"C:\Users\José Lws Tarín Tr\Documents\Bills", files))
        # Note: If we only want to copy and not move completely,
        # we just have to change 'shutil.move' to 'shutil.copy'

# In this code we send the electricity bills to 'ElectricityBills' folder but using the variables

for files in os.listdir(r"C:\Users\José Lws Tarín Tr\Documents\Bills"):
    if 'electricity' in files.lower():
        shutil.move(os.path.join(parent_dir, files), os.path.join(parent_dir2, files))

# Now we are going to move all the phone bills to the "PhoneBill" folder

for files in os.listdir(r"C:\Users\José Lws Tarín Tr\Documents\Payslips"):
    if 'phone' in files.lower():
        shutil.move(os.path.join(parent_dir, files), os.path.join(parent_dir3, files))
        
