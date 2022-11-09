try:
    with open("hazi.txt", "r", encoding="UTF-8") as f:
        vowels = "qwrtzpsdfghjklyxcvbnm"
        line = f.readline()
        norm = []

        while line:
            if line.rstrip() != '':
                help = ''.join([ch for ch in line if ch not in vowels and ch not in vowels.upper() and ch.isalpha()])
                norm.append(help)

            line = f.readline()

    with open("kimenet.txt", "w", encoding="UTF-8") as f:
        i = 2
        while i < len(norm):
            f.write(norm[i]+"\n")
            i += 3

except FileNotFoundError:
    print("A fájl nem található")