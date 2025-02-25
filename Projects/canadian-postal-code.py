def main():
    provinces = {"A":"Newfoundland","B":"Nova Scotia","C":"Prince Edward Island",
    "E":"New Brunswick","G":"Quebec","H":"Quebec","J":"Quebec",
    "K":"Ontario","L":"Ontario","M":"Ontario","N":"Ontario",
    "P":"Ontario","R":"Manitoba","S":"Saskatchewan","T":"Alberta",
    "V":"British Columbia","X":"Nunavut or Northwest Territories","Y":"Yukon"
    }
    postal_code = input("Enter Canadian postal code: ")
    if postal_code[0].upper() not in "ABCEGHJKLMNPRSTVXY" or len(postal_code) != 6:
        print("Invalid postal code")
        main()
    is_num = False
    for i in range(6):
        if is_num:
            if postal_code[i].upper() not in "0123456789":
                print("Invalid postal code")
                main()
            is_num = False
        else:
            if postal_code[i].upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("Invalid postal code")
                main()
            is_num = True
    for i in provinces.keys():
        if postal_code[0].upper() == i:
            if postal_code[1] == 0:
                print(f"The postal code is for a rural address in {provinces[i]}")
                return
            else:
                print(f"The postal code is for an urban address in {provinces[i]}")
                return
if __name__ == "__main__":
    main()