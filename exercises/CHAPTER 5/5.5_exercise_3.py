def main():
    number = float(input("Enter a number: "))
    another_number = float(input("Enter another number: "))
    print(f"The difference between {number} and {another_number} is an integer? {(number-another_number).is_integer()}!")


if __name__ == "__main__":
    main()
