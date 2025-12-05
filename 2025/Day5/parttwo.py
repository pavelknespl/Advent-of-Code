def solve():
    with open('input.txt', 'r') as f:
        obsah = f.read()
    text_rozsahu = obsah.split('\n\n')[0].split()
    rozsahy = []
    for r in text_rozsahu:
        start, konec = r.split('-')
        rozsahy.append((int(start), int(konec)))
    rozsahy.sort()
    sloucene_rozsahy = []
    if not rozsahy:
        print(0)
        return
    aktualni_start, aktualni_konec = rozsahy[0]
    for i in range(1, len(rozsahy)):
        dalsi_start, dalsi_konec = rozsahy[i]
        if dalsi_start <= aktualni_konec + 1: 
            aktualni_konec = max(aktualni_konec, dalsi_konec)
        else:
            sloucene_rozsahy.append((aktualni_start, aktualni_konec))
            aktualni_start, aktualni_konec = dalsi_start, dalsi_konec
    sloucene_rozsahy.append((aktualni_start, aktualni_konec))
    celkem_cerstvych = 0
    for start, konec in sloucene_rozsahy:
        celkem_cerstvych += (konec - start + 1)
    print(celkem_cerstvych)
solve()