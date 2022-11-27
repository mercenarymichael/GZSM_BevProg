def kereses():
    li = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    n = len(li)
    also, felso = 0, n-1
    keresett = 700
    szamlalo = 0
    while also <= felso:
        szamlalo += 1
        k = (felso + also) // 2
        if keresett < li[k]:
            felso = k-1
        elif keresett > li[k]:
            also = k+1
        else:
            kimenet = felso,also,k
            print(f"A {szamlalo}. lépésben találtuk meg!")
            break

    else:
        kimenet=False

    return kimenet

if __name__ == "__main__":
    print(kereses())