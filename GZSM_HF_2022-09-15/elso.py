

def char_freq(txt):
    chardict = {}
    for ch in txt:
        if ch in chardict:
            chardict[ch] += 1
        else:
            chardict[ch] = 1
        #
    #
    return str(chardict)


def sentence():
    #Bekeres
    print("Adjon meg egy mondatot:")
    txt = input()
    li = txt.split(" ")

    #Kiiratas
    print("Betűk gyakorisága: " + char_freq(txt))
    print("Fordítva: " + txt[::-1])
    print("Listába rendezve szavanként: " + str(li))


def main():
    sentence()


if __name__ == '__main__':
    main()
