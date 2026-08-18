# Get inputs from the user
destination = input()
price = float(input())
nights = int(input())
family_preference = bool(int(input()))     # 1 for True, 0 for False
package_family_friendly = bool(int(input()))  # 1 for True, 0 for False

# Check if the package is suitable
# Condition 1: Check destination
if (destination == "Hawaii") or (destination == "Bahamas"):
    # Condition 2: Check price and nights
    if (price <= 2000.00) and (nights >= 4):
        # Condition 3: Check family-friendliness preference
        if ((family_preference == True) and (package_family_friendly == True)) or (family_preference == False) and (package_family_friendly == False):
            print("Package is suitable")
        else:
            print("Package is not suitable")
    else:
        print("Package is not suitable")
else:
    print("Package is not suitable")