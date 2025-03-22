def divide(a, b):
    if b == 0:
        print("Error: Denominator cannot be zero.")
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Denominator cannot be zero.")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("Error: Second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("\nMathematical Operations:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting program.")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            
            if not num1.isdigit() or not num2.isdigit():
                print("Error: Please enter valid integers.")
                continue
            
            num1 = int(num1)
            num2 = int(num2)
            
            if choice == 'D':
                result = divide(num1, num2)
            elif choice == 'E':
                result = exponentiate(num1, num2)
            elif choice == 'R':
                result = remainder(num1, num2)
            elif choice == 'F':
                result = summation(num1, num2)
            
            if result is not None:
                print("Result:", result)
        else:
            print("Invalid choice. Please try again.")

main()
