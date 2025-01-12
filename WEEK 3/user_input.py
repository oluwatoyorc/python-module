QUESTION 1
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
    
    QUESTION 2
    def main():
    price = float(input("Enter the original price: $"))
    discount_percent = float(input("Enter the discount percentage (%): "))
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price is: ${final_price:.2f}")

if __name__ == "__main__":
    main()