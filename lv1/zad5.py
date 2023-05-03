fhand = open('song.txt')


rjecnik = dict()
  
for line in fhand:
    line = line.replace('.', '').replace(',', '')
    line = line.strip()
    
    line = line.lower()
    rijeci = line.split(" ")

    for rijec in rijeci:
        if rijec in rjecnik:
            rjecnik[rijec] = rjecnik[rijec] + 1
        else:
            rjecnik[rijec] = 1

    
        

for kljuc in list(rjecnik.keys()):
        print(kljuc, ":", rjecnik[kljuc])


print("Rijeci koje se pojavaljuju samo jednom:")
flag = 0
for word, count in rjecnik.items():
    if count == 1:
        flag = flag + 1
        print(word)


print("broj riječi koje se pojavljuju samo jednom", flag)