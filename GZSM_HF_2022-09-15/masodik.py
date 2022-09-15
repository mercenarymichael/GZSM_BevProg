
CmtoInch = 0.39
InchtoCm = 2.54

def conversion():
    print("Adjon meg egy számot és egy mértékegységet (cm/inch)")
    unit = int(input())
    measurement = input()

    while measurement not in ['cm', 'inch']:
        print("Not correct unit! Try again! : ")
        measurement = input()
    #

    if measurement == 'cm':
        unit *= CmtoInch
        print(str(unit) + " inches")
    #
    else:
        unit *= InchtoCm
        print(str(unit) + " centimeters")
    #


def main():
    conversion()


if __name__ == "__main__":
    main()