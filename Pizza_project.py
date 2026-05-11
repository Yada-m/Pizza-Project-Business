# Final Group Project: Pizza Ordering System
# Course: COP1000
# Description: A basic pizza ordering system with automatic price calculation.

def main():
    # --- SECTION 1: SETTING PRICES ---
    # We use all-caps for constants. This makes it easy to change prices
    # in one place without digging through the logic later.
    SMALL_PRICE = 15
    MEDIUM_PRICE = 20
    LARGE_PRICE = 25
    PEP_SMALL_ADD = 2
    PEP_MED_LRG_ADD = 3
    CHEESE_ADD = 1

    print("Welcome to the Python Pizza Ordering System!")
    
    # --- SECTION 2: GETTING USER INPUT ---
    # We use camelCase for variables like 'pizzaSize'.
    # .upper() is used so that 's' and 'S' both work correctly.
    pizzaSize = input("What size pizza do you want? S, M, or L: ").upper()
    addPepperoni = input("Do you want pepperoni? Y or N: ").upper()
    extraCheese = input("Do you want extra cheese? Y or N: ").upper()

    # --- SECTION 3: CALCULATING THE BASE PRICE ---
    totalBill = 0

    if pizzaSize == "S":
        totalBill = SMALL_PRICE
    elif pizzaSize == "M":
        totalBill = MEDIUM_PRICE
    elif pizzaSize == "L":
        totalBill = LARGE_PRICE
    else:
        # If the user types something other than S, M, or L, we stop here.
        print("Invalid size selection. Program ending.")
        return

    # --- SECTION 4: ADDING TOPPING COSTS ---
    # First, we check for pepperoni. The price changes based on the size.
    if addPepperoni == "Y":
        if pizzaSize == "S":
            totalBill += PEP_SMALL_ADD
        else:
            totalBill += PEP_MED_LRG_ADD

    # Next, we check for extra cheese.
    if extraCheese == "Y":
        totalBill += CHEESE_ADD

    # --- SECTION 5: FINAL DISPLAY ---
    # We print the final total. 
    # The :.2f ensures the number looks like money (e.g., 20.00).
    print("\n" + "-"*20)
    print(f"Final Bill: ${totalBill:.2f}")
    print("-"*20)
    print("Thank you for your order!")

# This tells Python to start the program by running the main function.
if __name__ == "__main__":
    main()