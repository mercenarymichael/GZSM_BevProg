def tabla():
    rend = "{0:>9}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}" \
                 "{8:>4}{9:>4}{10:>4}{11:>4}"
    rend2 = "{0:>3}{1:>6}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}" \
            "{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}"
    valasz = "  :"
    print(rend.format(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    print(f"{valasz:-<53}")

    for i in range(1, 13):
        print(rend2.format(str(i) + ":", i, i*2, i*3, i*4, i*5, i*6,
                            i*7, i*8, i*9, i*10, i*11, i*12))


if __name__ == "__main__":
    tabla()