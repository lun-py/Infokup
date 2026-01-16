n=int(input())
slova=input()
def najbolja_rijec(slova,rijec):
    if len(slova)<=1:
        return rijec
    slova=slova[:-1]
    najbolja=""
    for i in range(len(slova)):
        novo_slovo=slova[i]
        ostatak=slova[:i]+slova[i+1:]
        rezultat=najbolja_rijec(ostatak, rijec + novo_slovo)
        if najbolja=="" or rezultat<najbolja:
            najbolja=rezultat
    return najbolja
print(najbolja_rijec(slova))