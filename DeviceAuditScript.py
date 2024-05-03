import re

# Sample text containing user information
text = """
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

# Define a regex pattern to capture device name with both conditions met
pattern = r"(?<=DEVICE: )(?:\S+\s*\(\S+\))?(\S+).*?Username: DefaultAccount\s+Is Admin: YES"


# Find all matches in the text with a positive lookbehind
matches = re.findall(pattern, text, re.DOTALL)

# Print device names if any match is found
if matches:
  print("Devices with DefaultAccount as Admin:")
  for device_name in matches:
    print(device_name)
else:
  print("No devices found where DefaultAccount is Admin.")
