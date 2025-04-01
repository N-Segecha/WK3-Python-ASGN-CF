# Defining the calculate_discount function
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# User interactive interface (Main Program)
def main():
    try:
        # Prompt the user for the original price
        price = float(input("Please enter the original price of the item: "))
        # Prompt the user for the discount percentage
        discount_percent = float(input("Please enter the discount percentage (e.g., 25 for 25%): "))

        # Call the function to calculate the final price
        final_price = calculate_discount(price, discount_percent)

        # Display the appropriate message based on the discount applied
        if discount_percent >= 20:
            print(f"The final price after applying the discount is: {final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: {price:.2f}")
    except ValueError:
        # Handle invalid inputs
        print("Invalid input! Please ensure you enter numbers for the price and discount percentage.")

# Run the main program
if __name__ == "__main__":
    main()