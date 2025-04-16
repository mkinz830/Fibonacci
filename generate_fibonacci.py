def generate_fibonacci(n_terms):
    if n_terms <= 0:
        print("Please enter a positive integer greater than 0.")
        return

    print("Fibonacci sequence:")
    a, b = 0, 1
    for i in range(n_terms):
        print(a)
        a, b = b, a + b

def main():
    try:
        user_input = int(input("Enter the number of Fibonacci terms to generate: "))
        generate_fibonacci(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
