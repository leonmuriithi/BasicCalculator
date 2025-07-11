def calculate_discount(price, discount_percent):
    # Apply discount only if it's 20% or more
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount)

if discount >= 20:
    print(f"Final price after {discount}% discount is: {final_price}")
else:
    print(f"No discount applied. Final price is: {final_price}")