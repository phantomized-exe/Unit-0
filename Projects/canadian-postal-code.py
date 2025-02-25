provinces = {"A":"Newfoundland","B":"Nova Scotia","C":"Prince Edward Island","E":"New Brunswick","G":"Quebec","H":"Quebec","J":"Quebec","K":"Ontario","L":"Ontario","M":"Ontario","N":"Ontario","P":"Ontario","R":"Manitoba","S":"Saskatchewan","T":"Alberta","V":"British Columbia","X":"Nunavut or Northwest Territories","Y":"Yukon"}
postal_code = input("Enter Canadian postal code: ")
print("test")
if postal_code.upper() not in "ABCEGHJKLMNPRSTVXY" or len(postal_code) != 6:
    print("Invalid postal code")