def hanyados():
    while True:
        a = int(input("Enter 'a' value: "))
        b = int(input("Enter 'b' value: "))

        try:
            print(a / b)
        except ZeroDivisionError:
            print("Division by zero not allowed.")
        finally:
            print("Out of try except blocks")
        #


def main():
    hanyados()


if __name__ == "__main__":
    main()