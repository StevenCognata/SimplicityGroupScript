import re

########################################## WRITTEN BY STEVEN V. COGNATA ##########################################

# Datto audit data
audit_data = """

"""

# Function to extract just the device name and admin accounts
def extract_data(audit_data):
    device_name = re.search(r"DEVICE: ([^\[]+)", audit_data).group(1).strip()
    admin_accounts = re.findall(r"Username: (\w+)\n\s+Is Admin: YES", audit_data)
    return device_name, admin_accounts

# Spliting audit data into individual records
audit_records = re.split(r"SITE: ", audit_data)[1:]

# Processing each record
for record in audit_records:
    device_name, admin_accounts = extract_data(record)
    print("Device:", device_name)
    if admin_accounts:
        for account in admin_accounts:
            print("Admin Account:", account)
    else:
        print("No admin accounts found")
    print()
