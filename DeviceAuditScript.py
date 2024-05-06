import re

################################## WRITTEN BY STEVEN V. COGNATA ##################################

def parse_audit_data(data):
  """
  Parses the audit data and returns a list of devices with admin default accounts.

  Args:
    data: The audit data string.

  Returns:
    A list of devices with admin default accounts (SITE and DEVICE information).
  """
  devices = []
  sections = data.split("SITE:")
  for section in sections[1:]:
    # Extracting device information
    device_info = re.search(r"DEVICE: (.*)", section).group(1)

    # Find the "Stdout" section
    stdout_start = section.find("Stdout")
    stdout_end = section.find("Stderr")

    # Extracting user data
    user_data = section[stdout_start:stdout_end]
    admins = find_admin_default_accounts(user_data)

    # Appending device info for each admin found
    for _ in admins:
      devices.append(f"SITE: {device_info}\n")

  return devices

def find_admin_default_accounts(user_data):
  """
  Finds devices with default accounts set to admin (YES) on the following line.

  Args:
    user_data: The user data string.

  Returns:
    A list containing any empty strings (to trigger device info appending).
  """
  admins = []
  for line_index, line in enumerate(user_data.splitlines()):
    # Check for DefaultAccount on current line
    if "DefaultAccount" in line:
      # Look for "Is Admin: YES" on the next line
      next_line_index = line_index + 1
      if next_line_index < len(user_data.splitlines()) and "Is Admin:" in user_data.splitlines()[next_line_index] and user_data.splitlines()[next_line_index].endswith("YES"):
        # Found a match, add an empty string to the list
        admins.append("")
  return admins

# Replace data with audit data from datto
data = """
SITE: SGH (Allegis) (Sandy, UT) - DEVICE: DESKTOP-8A83VT1 [Chelsie Murphy | Sandy, UT]
-----------------------------------------------------------------------------------------




Component: Audit Local Users + Administrators [WIN]
---------------------------------------------------


Stdout
------
Audit Local Users + Administrators
=========================================
- Logged-in User:
- Reminder: This Component only audits local users, not users that are part
  of a domain or network. The logged-on user may not appear in this list.
=========================================
      SID: S-1-5-21-4233740057-3251218224-799995995-1002
 Username: Admin
 Is Admin: YES
 Activity: User has never logged onto device
 Disabled: False


      SID: S-1-5-21-4233740057-3251218224-799995995-500
 Username: Administrator
 Is Admin: YES
 Activity: User has never logged onto device
 Disabled: True


      SID: S-1-5-21-4233740057-3251218224-799995995-1003
 Username: Chelsie Murphy
 Is Admin: YES
 Activity: User has logged onto device at least once
 Disabled: False


      SID: S-1-5-21-4233740057-3251218224-799995995-503
 Username: DefaultAccount
 Is Admin: NO
 Activity: User has never logged onto device
 Disabled: True


      SID: S-1-5-21-4233740057-3251218224-799995995-501
 Username: Guest
 Is Admin: NO
 Activity: User has never logged onto device
 Disabled: True


      SID: S-1-5-21-4233740057-3251218224-799995995-1004
 Username: Tech
 Is Admin: YES
 Activity: User has never logged onto device
 Disabled: False


      SID: S-1-5-21-4233740057-3251218224-799995995-504
 Username: WDAGUtilityAccount
 Is Admin: NO
 Activity: User has never logged onto device
 Disabled: True


- UDF Option: Write all Users to UDF 5
- Writing results to UDF #5...
  (Admin (Administrator, Enabled) :: Tech (Administrator, Enabled) :: Chelsie Murphy (Administrator, Enabled) :: Administrator (Administrator, Disabled) :: WDAGUtilityAccount (StandardUser, Disabled) :: Guest (StandardUser, Disabled) :: DefaultAccount (StandardUser, Disabled) :: )




Stderr
------
query : The term 'query' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.


SITE: SGH (Kuonen) (Little Rock, AR) - DEVICE: SGH-AR-HKUO [Hank Kuonen | Little Rock, AR]
---------------------------------------------------------------------------------------------




Component: Audit Local Users + Administrators [WIN]
---------------------------------------------------


Stdout
------
Audit Local Users + Administrators
=========================================
- Logged-in User: hank
- Reminder: This Component only audits local users, not users that are part
  of a domain or network. The logged-on user may not appear in this list.
=========================================
      SID: S-1-5-21-313657752-2238811443-1119215659-500
 Username: Administrator
 Is Admin: YES
 Activity: User has never logged onto device
 Disabled: True


      SID: S-1-5-21-313657752-2238811443-1119215659-1004
 Username: ASPNET
 Is Admin: NO
 Activity: User has never logged onto device
 Disabled: False


      SID: S-1-5-21-313657752-2238811443-1119215659-503
 Username: DefaultAccount
 Is Admin: YES
 Activity: User has never logged onto device
 Disabled: True


      SID: S-1-5-21-313657752-2238811443-1119215659-501
 Username: Guest
 Is Admin: NO
 Activity: User has never logged onto device
 Disabled: True


      SID: S-1-5-21-313657752-2238811443-1119215659-1001
 Username: hank
 Is Admin: YES
 Activity: User has logged onto device at least once
 Disabled: False


      SID: S-1-5-21-313657752-2238811443-1119215659-1005
 Username: Tech
 Is Admin: YES
 Activity: User has logged onto device at least once
 Disabled: False


      SID: S-1-5-21-313657752-2238811443-1119215659-504
 Username: WDAGUtilityAccount
 Is Admin: NO
 Activity: User has never logged onto device
 Disabled: True


- UDF Option: Write all Users to UDF 5
- Writing results to UDF #5...
  (hank (Administrator, Enabled) :: Tech (Administrator, Enabled) :: Administrator (Administrator, Disabled) :: ASPNET (StandardUser, Enabled) :: DefaultAccount (StandardUser, Disabled) :: WDAGUtilityAccount (StandardUser, Disabled) :: Guest (StandardUser, Disabled) :: )






Stderr
------
- No stderr content -

"""

# Parse the data and print devices with admin default accounts
devices = parse_audit_data(data)
for device in devices:
  print(device)
