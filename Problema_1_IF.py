#Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj. #
#Exemplu : Date de intrare nr crt 7 punctaj 120 nr crt 3 punctaj 100 nr crt 4 punctaj 119 Date de ieşire punctaj maxim are elevul cu nr crt 7.#
ne=int(input('nr elevului:'))
ne1=int(input('nr elevului 2:'))
ne2=int(input('nr elevului 3:'))
pe=int(input('punctajul primului elev:'))
pe1=int(input('punctajul elevului al doilea:'))
pe2=int(input('punctajul elevului al treilea:'))
if pe > pe1 and pe > pe2:
 print('punctaj maxim il are elevul cu nr', ne)
if pe1 > pe and pe1 > pe2:
 print('punctaj maxim il are elevul cu nr',ne1)
if pe2 > pe and pe2 > pe1:
 print('punctaj maxim il are levul cu nr', ne2)