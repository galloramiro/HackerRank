def checkMagazine(magazine, note):
    maga = magazine.split(" ")
    nota = note.split(" ")
    r = 0
    for i in nota:
        if i in maga:
            r += 1
            #maga.pop(nota[vali])
        else:
            pass
    if r == len(nota):
        return "Yes"
    else:
        return "No"



print(checkMagazine('ive got a lovely bunch of coconuts','ive got some coconuts'))      # No
print(checkMagazine('two times three is not four','two times two is four'))             # No
print(checkMagazine('give me one grand today night','give one grand today'))            # Yes