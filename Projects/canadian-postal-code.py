def main():
    provinces = {"A":"Newfoundland","B":"Nova Scotia","C":"Prince Edward Island",
    "E":"New Brunswick","G":"Quebec","H":"Quebec","J":"Quebec",
    "K":"Ontario","L":"Ontario","M":"Ontario","N":"Ontario",
    "P":"Ontario","R":"Manitoba","S":"Saskatchewan","T":"Alberta",
    "V":"British Columbia","X":"Nunavut or Northwest Territories","Y":"Yukon"
    }
    postal_code = input("Enter Canadian postal code: ")
    if postal_code[0] not in "ABCEGHJKLMNPRSTVXYabcdefghijklmnopqrstuvwxyz0123456789 " or len(postal_code) != 7:
        print("Invalid postal code")
        main()
    if postal_code[3] != " ":
        print("Invalid postal code")
        main()
    is_num = False
    for i in range(7):
        if postal_code[i] == " ":
            continue
        if is_num:
            if postal_code[i] not in "0123456789":
                print("Invalid postal code")
                main()
            is_num = False
        else:
            if postal_code[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
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