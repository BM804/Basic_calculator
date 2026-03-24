def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def main():
    print("🧮 BASIC CALCULATOR")

    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting calculator...")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Enter numeric values.")
            continue

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", subtract(a, b))
        elif choice == '3':
            print("Result:", multiply(a, b))
        elif choice == '4':
            print("Result:", divide(a, b))


if __name__ == "__main__":
    main()
