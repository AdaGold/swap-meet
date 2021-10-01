import sys
from swap_meet.vendor import *
from swap_meet.item import *
from swap_meet.clothing import *
from swap_meet.decor import *
from swap_meet.electronics import *




def main(wave):
    if(wave == 1):
        print("hello")
        vendor = Vendor()
        print(f"The vendors inventory has this many items: {len(vendor.inventory)}")  

    elif (wave == "ERROR"):
        print("Try again")    
    else:
        print("Please input a wave number.  Valid wave numbers are 1.")


if __name__ == "__main__":
    print("Welcome to the Swap Meet")
    print("   Press 1 to create a vendor")
    print("   Press 2 to add items to the vendor's category")
    print("   Press 3 to swap with our internal system of vendors")

    args = input()
    if(args.isnumeric()):
        
        wave = int(args)
    else:
        wave = "ERROR"
    main(wave)



