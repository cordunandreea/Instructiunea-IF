#Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
#exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. Exemplu : Date
#de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani. 
ac=int(input('anul curent:'))
lc=int(input('luna curenta:'))
zc=int(input('ziua curenta:'))
an=int(input('anul nasterii:'))
ln=int(input('luna nasterii:'))
zn=int(input('ziua nasterii:'))
if ac > 2020 or an > 2020:
    print('an invalid')
if lc > 12 or ln > 12:
    print('luna invalida')
if zc > 31 or zn > 31:
    print('zi invalida')
else:
    if lc > ln:
        print((ac-an)+1, 'ani')
    else:
        print(ac-an, 'ani')