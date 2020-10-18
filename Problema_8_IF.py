#Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator. Exemple : Date de intrare 23 45 Date de
#ieşire nu exista numar par ; Date de intrare 28 14 Date de ieşire 28 ; Date de intrare 77 4 Date de ieşire 4.
n1=int(input('primul numar este='))
n2=int(input('al doilea numar este='))
r1=n1%2
r2=n2%2
if r1==0 and r2==0 :
    if n1 > n2:
        print(n1)
    else:
        print(n2)
if r1!=0 and r2==0:
    print(n2)
if r1==0 and r2!=0:
    print(n1)
if r1!=0 and r2!=0:
    print('nu exista numar par')