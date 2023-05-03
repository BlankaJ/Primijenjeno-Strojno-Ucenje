def avg_reliability(): 
    
    imeDatoteke = input('Unesite ime datoteke: ') 
    substring = "X-DSPAM-Confidence: "
    substring_lenght = len(substring)
    vrijednosti = [] 

    try:
        fhand = open(imeDatoteke)
    except:
        print('nema te datoteke', imeDatoteke)
        exit()

    for line in fhand:
        if substring in line:

            try:
                vrijednost = float(line[substring_lenght: ])
                vrijednosti.append(vrijednost)
            except:
                exit()

    avg = sum(vrijednosti) / len(vrijednosti)
    print("Srednja vrijednost pouzdanosti: ", avg)

avg_reliability() 
avg_reliability()  