def palindrom(pali):
    jelek = ",.!-?: "
    betuk = {
        'í': 'i',
        "é": "e",
        "á": "a",
        "ő": "o",
        "ö": "o",
        "ó": "o",
        "ü": "u",
        "ú": "u",
        "ű": "u",
        "zs": "sz",
        "sz": "zs",
        "sc": "cs",
        "zd": "dz",
        "yn": "ny",
        "yg": "gy",
        "yt": "ty",
        "zdd": "ddz",
        "zss": "ssz",
        "ssz": "zss",
        "scc": "ccs",
        "ynn": "nny",
        "ygg": "ggy",
        "ytt": "tty",
    }

    #eredeti es forditott szoveg jelek nelkul
    pali = ''.join([ch for ch in pali if ch not in jelek]).lower()
    backw = pali[::-1]

    cnt = []

    for ch in betuk:                #osszetett es ekezetes betu hanyszor szerepel
        if ch in backw:
            #print(backw.count(ch))
            cnt.append(backw.count(ch))
        else:
            cnt.append(0)
        #print(ch + " " + str(cnt))

    for i, ch in enumerate(betuk):  #betuk es ekezetek csereje
        if cnt[i] != 0:
            for j in range(cnt[i]):
                if i < 9:           #9 db ekezetes van a dict elejen(pali ekezetlenites)
                    pali = pali[:pali.find(ch)] + betuk[ch] + pali[pali.find(ch)+len(ch):]
                backw = backw[:backw.find(ch)] + betuk[ch] + backw[backw.find(ch)+len(ch):]

    #print(backw)
    #print(pali)

    if pali == backw:   #kiiratas
        print("Ez egy palindrom!")
    else:
        print("Ez nem egy palindrom!")


if __name__ == "__main__":
    be = input("Kérek egy palindromot: ")
    palindrom(be)